#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 00:00:30 2018

@author: babraham
"""
import sqlite3
import os
import numpy as np
from tqdm import tqdm
import time
import pickle

class sqldb():
    def __init__(self, fpath):
        self.fpath = fpath
        self.conn = sqlite3.connect(fpath)
        self.c = self.conn.cursor()
        
    def getTableNames(self):
        res = self.query("SELECT name FROM sqlite_master WHERE type='table';")
        if len(res) > 0:
            return [r[0] for r in res]
        else: print('no tables in DB!')
        
    def getSchema(self, table):
        return self.query("pragma table_info('{}')".format(table))
    
    def showTables(self):
        tnames = self.getTableNames()
        for tname in tnames:
            print('----------{}----------'.format(tname))
            schema = self.getSchema(tname)
            print('\n'.join([str(s) for s in schema]))
            
    def query(self, cmd, timeit=False):
        ti = time.time()
        res = self.c.execute(cmd)
        dt = time.time()-ti
        if timeit: print('query took {} seconds.'.format(dt))
        return res.fetchall()
    
class mxmdb(sqldb):
    def __init__(self,mxmpath='mxmdb.db'):
        sqldb.__init__(self, mxmpath)
        self.mxm_tables = ['words', 'lyrics']
        print('building vocab...')
        self.vocab = self.getVocab()
        print('counting songs...')
        self.N = self.query('select count(distinct track_id) from lyrics', timeit=True)
        self.N = self.N[0][0]
        self.tfidf = {k:{'tf':0,'df':0,'tfidf':0} for k in self.vocab}
        trackSongTups = self.query('select song_id, track_id from trackdata')
        self.songToTrack = {t[0]:t[1] for t in trackSongTups}
                 
    def getSongs(self):
        songs = self.query('SELECT distinct track_id from lyrics;')
        return [s[0] for s in songs]
    
    def getLyrics(self, songID):
        res = self.query("SELECT word, count from lyrics where track_id = '{}'".format(songID))
        return dict(res)
           
    def getVocab(self):
        res = self.query('SELECT DISTINCT word from lyrics')
        if len(res) > 0: return [r[0] for r in res]
        return None
    
    def TF(self,word):
        res = self.query("select sum(count) from lyrics where word = '{}'".format(word))
        return int(res[0][0])
    
    def getFreqStats(self):
        q = 'select word, sum(count), count(count) from lyrics group by word'
        tups = self.query(q, timeit=True)
        return tups
    
    def DF(self,word):
        res = self.query("select count(count) from lyrics where word = '{}'".format(word))
        return int(res[0][0]) 
    
    def calcTFIDF(self, tf,df, norm_tf=True):
        if norm_tf: tf = 1 + np.log(tf+1)
        return tf * np.log(1 + float(self.N) / df)   
    
    def buildTFIDFMat(self):
        print ('building tf-idf matrix...')
        ti = time.time()
        tfdf_tups = self.getFreqStats()
        for word,tf,df in tfdf_tups:
            tf_idf = self.calcTFIDF(tf,df)
            self.tfidf[word] = {'tf':tf,'df':df,'tfidf':tf_idf}
        print('total time: {} seconds'.format(time.time()-ti))
    
    def getTFs(self):
        return self.query('SELECT word, SUM(count) from lyrics group by word')
    
def buildSongMetaData(mxm):
    fname = 'unique_tracks.txt'
    with open(fname, 'r') as f:
        lines = f.readlines()
    clean_lines = []
    for l in lines:
        l = l.strip().replace("'","")
        clean_lines.append(l.split('<SEP>'))
    
    mxm.query('create table trackdata(track_id TEXT primary key, song_id TEXT, song_name TEXT, artist TEXT)')
    for i,(tid, sid, art, nm) in enumerate(tqdm(clean_lines)):
        #print('{},{},{}'.format(i,nm,art))
        mxm.query("insert into trackdata values('{}','{}','{}','{}')".format(tid,sid,nm,art))
    
class userdb(sqldb):
    def __init__(self, fpath='userdata.db'):
        sqldb.__init__(self, fpath)
        self.fpath = fpath
        print('getting users...')
        self.users = self.get_users()
        print('counting records...')
        self.N = self.query('select count(*) from userdata')
        self.N = self.N[0][0]
        self.user_dists = {}
        #self.get_songPool()
    
    def get_users(self):
        res = self.query('select distinct user_id from userdata')
        return [r[0] for r in res]
    
    def get_songPool(self):
        with open('overlapping_songs.txt', 'r') as f:
            lines = f.readlines()
        self.valid_songs = set([l.strip() for l in lines])
    
    def get_user_dists(self):
        for user in self.users:
            rows = self.query("select * from userdata where user_id = '{}'".format(user))
            uids,sids,counts = zip(*rows)
            if len(set(sids).intersection(self.valid_songs) > 10):
                del(rows)
                for uid, sid, count in zip(uids,sids,counts):
                    self.user_dists[uid][sid] = self.user_dsits[uid].get(sid,0) + count
    
def get_user_dists(db, batch_size = 128):
    num_batches = db.N / batch_size
    for n in tqdm(range(num_batches-1)):
        start, end = batch_size*n+1, batch_size*(n+1)+1
        if n == num_batches-1:
            rows = db.query('select * from userdata_sub where rowid > {}'.format(start))
        else:
            rowrange = ', '.join([str(i) for i in range(start,end)])
            rows = db.query("select * from userdata_sub where rowid in ({})".format(rowrange)) 
        for r in rows:
            uid, sid, count = r
            if uid not in db.user_dists: db.user_dists[uid] = {}
            db.user_dists[uid][sid] = db.user_dists[uid].get(sid,0) + count

    return db

def sparse_cos_sim(d1,d2):
    common_keys = set(d1.keys()).intersection(set(d2.keys()))
    num = 0
    for k in common_keys: num += d1[k]*d2[k]
    denom = np.linalg.norm(d1.values()) * np.linalg.norm(d2.values())
    return float(num) / denom
    


def filter_users(db, n, songlist=None):
    filt_tups = []
    if not songlist: songlist = db.valid_songs
    songlist = set(songlist)
    for k,v in tqdm(db.user_dists.items()):
        if len(set(v.keys()).intersection(songlist)) > n:
            filt_tups.append((k,v))
    return dict(filt_tups)

def buildSongVocabs(songdb, songlist=None):
    if not songlist: songlist = songdb.getSongs()
    vocabs = {s:{} for s in songlist}
    songlist = set(songlist)
    print('pulling data from db...')
    rows = songdb.query('select song_id, word, count from lyrics')
    for sid, word, ct in tqdm(rows):
        if sid in songlist:
            vocabs[sid][word] = vocabs[sid].get(word,0) + ct
    return vocabs
        
    
    
def buildUserVocab(userdict, songdict):
    uservocabs = {k:{} for k in userdict.keys()}
    for user, songs in tqdm(userdict.items()):
        for song in songs:
            for k,count in songdict[song].items():
                uservocabs[user][k] = uservocabs[user].get(k,0) + count
    return uservocabs
        
# =============================================================================
# Sensitivity Analysis for valid song ct. threshold
# 10,  641070
# 20,  372354
# 30,  247736
# 50, 127193
# 100 34397
# 175 8275
# 250 2690    
# 500 144
# 1000 1
# =============================================================================
    
def buildUserDB(outfilename):
    #initialize database
    conn = sqlite3.connect(outfilename)
    c = conn.cursor()
    # create user data table
    q = "CREATE TABLE userdata (user_id TEXT,"
    q += "song_id INT,"
    q += " count INT);"
    conn.execute(q)
    #read data from flat file
    print('reading data from flat file...')
    fpath = 'train_triplets.txt'
    with open(fpath, 'r') as f:
        lines = f.readlines()
    #populate table
    print('populating database...')
    for l in tqdm(lines):
        user, song, playct = l.strip().split("\t")
        q = "INSERT INTO userdata VALUES('{}','{}','{}')".format(user,song,playct)
        c.execute(q)
    conn.commit()
    conn.close()           


songstr = ', '.join(["'{}'".format(s) for s in final_songs])
udb.query("insert into userdata_sub select * from userdata where song_id in ({})".format(songstr))

trackstr = ', '.join(["'{}'".format(t) for t in final_overlap])
mxm.query("insert into lyrics_sub select * from lyrics where track_id in ({})".format(trackstr))
def calcTFIDF(db, tf,df, norm_tf=True):
    if norm_tf: tf = 1 + np.log(tf+1)
    return tf * np.log(1 + float(db.N) / df)   

def save_obj(obj, obj_name):
    with open('{}.pkl'.format(obj_name), 'w') as out:
        pickle.dump(obj, out)
        
def load_obj(obj_name):
    f = open('{}.pkl'.format(obj_name), 'r')
    return pickle.load(f)

def buildTagDB(outfilename):
    conn = sqlite3.connect(outfilename)
    c = conn.cursor()
    # create user data table
    q = "CREATE TABLE tagdata (user_id TEXT,"
    q += "song_id INT,"
    q += " count INT);"
    conn.execute(q)
    
samp = [(1, 1, 100.0), (1, 2, 100.0), (2, 3, 100.0), (2, 4, 100.0), (3, 5, 100.0)]  
print '************** DEMO 2 **************'
print 'We get all tracks with at least one tag'
sql = "SELECT tid FROM tids"
res = conn.execute(sql)
data = res.fetchall()
for k in range(10):
    print data[k]
print '...'
print '(total number of track IDs: %d)' % len(data)