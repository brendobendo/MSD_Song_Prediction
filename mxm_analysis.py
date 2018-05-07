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
import pandas as pd
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from empath import Empath
import re

#===========Global Params====================#
#taglist = load_obj('top_40k_tags_df_100k_users')

# =============================================================================
# #Steps for pre-processing
# 1. load songlist
# 2. build mxmdb
# 2. build song vocab
# 2.5 build/read in tfidf
# 3. build userdb
# 4. build user distributions
# 5. build user vocabs
# 7. build tag db
# 8. build trackTags
# 8.5 build database container - encapsulates everythign
# 9. build userTags
# 10 read in eval data
# 11 build vocab_knn
# 12 build tag knn
# =============================================================================
def getData():
    songlist = load_obj('overlapping_songs')
    mxm = mxmdb()
    mxm.tfidf = load_obj('tfidf')
    print('building song vocab...')
    mxm.sv = buildSongVocabs(mxm, songlist)
    udb = userdb()
    print('building user listening distributionser...')
    udb.users = udb.users[:100000]
    udb.get_user_dists()
    print('building user vocab...')
    udb.uv = buildUserVocabs(mxm,udb.user_dists, mxm.sv, tfidf=True)
    tdb = tagdb()
    print('making song tags...')
    tdb.buildTrackTags()
    dbc = db_container(mxm,udb,tdb)
    print('making user tags...')
    dbc = buildUserTags(dbc)
    print('getting eval data...')
    Eval = getEvalData()
    return [mxm,udb,tdb,dbc,Eval]
#============Generic DB - all databases inherit from this class==============#
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

#=======================DB Container to store all other dbs===============#
class db_container(sqldb):
    def __init__(self, songdb, userdb, tagdb):
        self.tdb = tagdb
        self.mxm = songdb
        self.udb = userdb
        self.stt = self.mxm.songToTrack
        self.tts = self.mxm.trackToSong
        self.vocab = self.mxm.vocab
        self.uhistory = self.udb.user_dists
        self.taglist = load_obj('top_40k_tags_80k_users')
        self.idToWord = load_obj('idToWord')
        self.wordToId = load_obj('wordToId')
        
    def buildUserTags(self):
        userTags = {}
        for user, history in tqdm(self.uhistory.items()):
            if user not in userTags:
                userTags[user] = {}
            for i, (song,count) in enumerate(history.items()):
                track = self.stt[song]
                try:
                    tags = self.tdb.trackTags[track]
                    for t in tags: userTags[user][t] = userTags[user].get(t, 0) + count
                except: print('error finding tags for track {}'.format(track))
        self.userTags = userTags
#====================Song Code============================================#    
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
        self.trackToSong = {v:k for k,v in self.songToTrack.items()}
        self.stopwords = set(stopwords.words('english'))
        self.vocab = set(self.vocab).difference(self.stopwords)
                 
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
    
    def getSongInfo(self, song_id, tid=None):
        if not tid: tid = self.songToTrack[song_id]
        res = self.query("select song_name, artist from trackdata where track_id = '{}'".format(tid))
        if len(res) == 0:
            print ("couldn't find any songs matching id {}".format(song_id))
            return
        else: return res[0]
             
def getSongInfo(mxm, song_id, tid=None):
    if not tid: tid = mxm.songToTrack[song_id]
    res = mxm.query("select song_name, artist from trackdata where track_id = '{}'".format(tid))
    if len(res) == 0:
        print ("couldn't find any songs matching id {}".format(song_id))
        return
    else: return res[0]
    
def buildSongVocabs(songdb, songlist=None):
    global stopwords
    if not songlist: songlist = songdb.getSongs()
    vocabs = {s:{} for s in songlist}
    songlist = set(songlist)
    print('pulling data from db...')
    rows = songdb.query('select song_id, word, count from lyrics')
    for sid, word, ct in tqdm(rows):
        if sid in songlist:
            if word not in songdb.stopwords:
                vocabs[sid][word] = vocabs[sid].get(word,0) + ct
    return vocabs
                        
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
        
#====================Code to get raw lyrics=================================#        
def get_ldf_hashes(mxm, trackstr):
    ldf = pd.read_csv('ldf_all.csv')
    sdf = mxm.query('select * from trackdata where track_id in ({})'.format(trackstr))
    sdf = pd.DataFrame(sdf, columns = ['track_id','song_id','title','artist'])
    titles, artists = sdf.title.tolist(), sdf.artist.tolist()
    titles = [t.lower() for t in titles]
    titles = [re.sub('\(.*?\)','',t) for t in titles]
    titles = [t.strip() for t in titles]
    artists = [a.lower() for a in artists]
    hash_ = [artist+'|'+title for artist,title in zip(artists,titles)]
    sdf['hash'] = hash_
    sdf['title'] = titles
    sdf['artist'] = artists
    ldf_hash = ldf['hash'].tolist()
    sdf_hash = hash_
    res = set(sdf_hash).intersection(ldf_hash)
    return res
    


#====================Artist Functions============================#

def fixSongArtistColumns(mxm):
    mxm.query('create table trackdata_tmp (track_id TEXT, song_id TEXT, artist TEXT, song_name TEXT)')
    mxm.query('insert into trackdata_tmp (track_id, song_id, artist, song_name) select track_id, song_id, artist, song_name from trackdata')
    mxm.query('drop table trackdata')
    mxm.query('alter table trackdata_tmp rename to trackdata')
    mxm.showTables()
    mxm.query('select artist from trackdata limit 5')
    mxm.conn.commit()

def getSongToArtist(mxm, udb):
    songToArtist = mxm.query('select song_id, artist from trackdata')
    user_artists = {}
    for user, songs in tqdm(udb.user_dists.items()):
        if user not in user_artists:
            user_artists[user] = {}
        for song, ct in songs.items():
            artist = songToArtist[song]
            if artist not in user_artists[user]:
                user_artists[user][artist] = ct
            else:
                user_artists[user][artist] += ct    
    return dict(songToArtist)

          
#====================User Functions============================#
class userdb(sqldb):
    def __init__(self, fpath='userdata.db'):
        sqldb.__init__(self, fpath)
        self.fpath = fpath
        print('getting users...')
        self.users = set(self.get_users())
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
    
    def get_user_dists(self, batch_size = 128, sample=False, songList = None):
        num_batches = self.N / batch_size
        if songList: songList = set(songList)
        for n in tqdm(range(num_batches-1)):
            start, end = batch_size*n+1, batch_size*(n+1)+1
            if n == num_batches-1:
                rows = self.query('select * from userdata_sub where rowid > {}'.format(start))
            else:
                rowrange = ', '.join([str(i) for i in range(start,end)])
                rows = self.query("select * from userdata_sub where rowid in ({})".format(rowrange)) 
            for r in rows:                    
                uid, sid, count = r
                if uid in self.users:
                    if not sample:
                        if uid not in self.user_dists: self.user_dists[uid] = {}
                        if songList:
                            if sid in songList:  self.user_dists[uid][sid] = self.user_dists[uid].get(sid,0) + count
                        else: self.user_dists[uid][sid] = self.user_dists[uid].get(sid,0) + count
                    else:
                        if uid in self.usamp:
                            if uid not in self.user_dists:
                                self.user_dists[uid] = {}
                            if songList:
                                if sid in songList: self.user_dists[uid][sid] = self.user_dists[uid].get(sid,0) + count
                            else: self.user_dists[uid][sid] = self.user_dists[uid].get(sid,0) + count
                        
def buildUserVocabs(mxm, userdict, songdict, tfidf = True):
    uservocabs = {k:{} for k in userdict.keys()}
    for user, songs in tqdm(userdict.items()):
        uservocabs[user] = buildUserVocab(mxm,user,songs,songdict,tfidf)
    return uservocabs

def buildUserVocab(mxm, user, usersongs, songdict, tfidf=True):
    vocab = {}
    for song, ct in usersongs.items():      
        sdict = songdict.get(song,None)
        if sdict is not None:
            #if song in songdict:
            for gram,count in sdict.items():
                if gram in mxm.vocab:
                    vocab[gram] = vocab.get(gram,0) + count
    if tfidf:
        for i,(v,tf) in enumerate(vocab.items()):
            try:
                df = mxm.tfidf[v]['df']
                tfidf = calcTFIDF(mxm,tf,df)
                vocab[v] = tfidf
            except:
                print('error finding df for word for user {} at idx {}'.format(user,i))
                pass
    return vocab

def filter_vocab(n,mxm):
    tfidf = sorted(mxm.tfidf.items(), key= lambda x: x[1]['df'], reverse=True)
    tfidf = tfidf[:n]
    mxm.vocab = set([t[0] for t in tfidf])
    return mxm

def splitStats(n, mxm, met='tfidf'):
    tfidf = sorted(mxm.tfidf.items(), key= lambda x: x[1][met], reverse=True)
    tfidf = tfidf[:n]
    v_ct = sum([v['df'] for v in dict(tfidf).values()])
    v_ct_old = sum([v['df'] for v in mxm.tfidf.values()])
    t_ct = sum([v['tf'] for v in dict(tfidf).values()])
    t_ct_old = sum([v['tf'] for v in mxm.tfidf.values()])
    return{'dprop': float(v_ct) / v_ct_old, 'tprop': float(t_ct) / t_ct_old}
       
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

def filter_users(db, n, songlist=None):
    filt_tups = []
    if not songlist: songlist = db.valid_songs
    songlist = set(songlist)
    for k,v in tqdm(db.user_dists.items()):
        if len(set(v.keys()).intersection(songlist)) > n:
            filt_tups.append((k,v))
    return dict(filt_tups)
  
#================Tag Functions=============================================#

class tagdb(sqldb):
    def __init__(self, fpath="lastfm_tags.db", trackList = None):
        self.fpath = fpath
        sqldb.__init__(self,fpath)
        tags = self.query('select * from tags')
        self.tags = {t[0]:i for i,t in enumerate(tags) if len(t[0]) > 0}
        tids = self.query('select * from tids')
        self.tracks = {t[0]:i for i,t in enumerate(tids) if len(t[0]) > 0}
        self.idToTag = [t[0] for t in sorted(self.tags.items(), key = lambda x:x[1])]
        self.idToTrack = [t[0] for t in sorted(self.tracks.items(), key = lambda x:x[1])]
        self.tracklist = set(trackList) if trackList else None

    def buildTrackTags(self):
        if self.tracklist:
            self.trackTags = {k:[] for k in list(self.tracklist)}
        else:
            self.trackTags = {k:[] for k in self.tracks.keys()}
        trips = self.query('select * from tid_tag')
        for tid, tagid, value in tqdm(trips):      
            try:
                track = self.idToTrack[tid]
                if tagid <= len(self.idToTag):
                    if self.tracklist:
                        if track in self.tracklist:
                            tag = self.idToTag[tagid]
                            self.trackTags[track].append(tag)
                    else:
                         tag = self.idToTag[tagid]
                         self.trackTags[track].append(tag)   
            except: print('error reading tagid {}'.format(tagid))               
    
    def getUserTags(self, trackHistory):
        userTags = {}
        for i, (track,count) in enumerate(trackHistory.items()):
            try:
                tags = self.trackTags[track]
                for t in tags: userTags[t] = userTags.get(t, 0) + count
            except: print('error finding tags for track {}'.format(track))
        return userTags

def getAllUserTags(mxm,udb,tdb):
    userTags = {}
    for user, history in tqdm(udb.user_dists.items()):
        history = {mxm.songToTrack[s]:v for s,v in history.items()}
        tags = tdb.getUserTags(history)
        userTags[user] = tags
    return userTags

#===================User Vector Conversion Methods========================# 
def getUserVec2(dbc, user, getY=False):
    user_vec = np.zeros(len(dbc.vocab)+len(dbc.taglist), dtype=int)
    usr_vocab = dbc.udb.uv[user]
    for v,ct in usr_vocab.items():
        user_vec[dbc.wordToId[v]] += ct
    usr_tags = dbc.userTags[user]
    for t,ct in usr_tags.items():
        if t in dbc.taglist:
            user_vec[dbc.wordToId[t]] += ct
    if getY:
        user_y = {k:0 for k in dbc.mxm.sv.keys()}
        user_lstn_cts = dbc.uhistory[user]
        for song, ct in user_lstn_cts.items():
            user_y[song] = user_y.get(song,0) + ct
        return user_vec, user_y
    else:  return user_vec
    
def getUserVec3(empty_vec, user,vocab,tags,wordToId):
    user_vec = np.zeros(len(empty_vec))
    for v,ct in vocab.items():
        user_vec[wordToId[v]] += ct
    for t,ct in tags.items():
        user_vec[wordToId[t]] += ct
    return user_vec

def getCombVecs(dbc):
    comb_vecs = {k:v for k,v in dbc.udb.uv.items()}
    for user in comb_vecs.keys():
        if user in dbc.userTags:
            #print('found match')
            tags = dbc.userTags[user]
            for tag,ct in tags.items():
                comb_vecs[user][tag] = comb_vecs[user].get(tag,0) + ct
    return comb_vecs
     
def exportUserVecs(dbc):
    xdict, ydict = {},{}
    for user, history in tqdm(dbc.uhistory.items()):
        if user in dbc.udb.uv:
            x,y = getUserVec2(dbc,user)
            xdict[user] = x
            ydict[user] = y
    xdf = pd.DataFrame.from_dict(xdict, orient="index")
    ydf = pd.DataFrame.from_dict(ydict, orient="index")
    xdf.to_csv('user_x.csv')
    ydf.to_csv('user_y.csv')
    return xdf,ydf
#==============KNN Methods================#    
class KNN():
    def __init__(self, mxm_db, userhistories, uservocab, songdict, k=5, name=None):
        self.userhistories = userhistories
        self.uservocab = uservocab
        self.k = k
        self.mxm = mxm_db
        self.songdict = songdict
        if not name: self.name = "vocab_knn"
        else:  self.name = name
        
    def find_nns(self, vocab):
        sims = [(u, self.sparse_cos_sim(vocab,v2)) for u,v2 in tqdm(self.uservocab.items())]
        sims = sorted(sims, key=lambda x:x[1], reverse=True)
        return sims[:self.k]

    def sparse_cos_sim(self,d1,d2):
        common_keys = set(d1.keys()).intersection(set(d2.keys()))
        num = 0
        for k in common_keys: num += d1[k]*d2[k]
        denom = np.linalg.norm(d1.values()) * np.linalg.norm(d2.values())
        return float(num) / denom
    
    def recommend(self, user, history):
        uv = buildUserVocab(self.mxm, user, history, self.songdict, tfidf=True)
        nns = self.find_nns(vocab=uv)
        recset = set()
        for user, sim in nns:
            usongs = self.userhistories[user]
            diff = set(usongs).difference(set(history))
            [recset.add(d) for d in list(diff)]
        return recset

import scipy.sparse as sp
d = {0: [0,1], 1: [1,2,3], 
     2: [3,4,5], 3: [4,5,6], 
     4: [5,6,7], 5: [7], 
     6: [7,8,9]}
row_ind = [k for k, v in d.items() for _ in range(len(v))]
col_ind = [i for ids in d.values() for i in ids]
X = sp.csr_matrix(([1]*len(row_ind), (row_ind, col_ind))) 
#============================Prediction=====================================#
 
def recommend(mod, user, history, typ="content"):
    if typ=="content":
        uv = buildUserVocab(mod.mxm, user, history, mod.songdict, tfidf=True)
        #tags = b
    else: uv = history
    nns = mod.find_nns(vocab=uv)
    recdict = {}
    for user, sim in nns:
        usongs = mod.userhistories[user]
        diff = set(usongs).difference(set(history))
        for d in diff:
            recdict[d] = recdict.get(d,0) + 1
    num_recs = len(history)
    recs = sorted(recdict.items(), key=lambda x:x[1], reverse=True)
    return dict(recs[:num_recs])


       
def makePreds(model, eval_data, outname = "model_preds.csv", export=False, typ="content"):
    res = {}
    for i, (user, history) in enumerate(eval_data['visible'].items()):
        print('----------------{}/{}-----------------'.format(i+1,len(eval_data['visible'])))
        recs = recommend(model,user,history, typ=typ)
        hidden = eval_data['hidden'][user]
        metrics = calcEvalMetrics(hidden, recs)
        res[user] = metrics
        if export:
            if not os.path.isfile(outname):
                out = open(outname, 'w')
                out.write('idx,user,vocabKNN,Accuracy,Recall,RBO\n')
            else: out = open(outname, 'a')
            metstr = ','.join([str(m) for m in metrics])
            out.write(','.join([str(i),user,model.name,metstr])+'\n')            
    return res

def makeRandomPreds(eval_data, songdb, udb, k=10):
    res = {}
    for user, history in tqdm(eval_data['visible'].items()):
        choices = np.random.choice(udb.user_dists.keys(), size=k, replace=False)
        recdict = {}
        for rec_user in choices:
            usongs = udb.user_dists[rec_user]
            diff = set(usongs).difference(set(history))
            for d in diff:
                recdict[d] = recdict.get(d,0) + 1
        num_recs = len(history)
        recs = sorted(recdict.items(), key=lambda x:x[1], reverse=True)
        recs = dict(recs[:num_recs])
        hidden = eval_data['hidden'][user]
        metrics = calcEvalMetrics(hidden,recs)
        res[user]=metrics
    return res
            

#==========================Sentiment Analysis===============================#
def getSongSentiments():
    sid = SentimentIntensityAnalyzer()
    ldf = pd.read_csv('ldf_all_final.csv')
    docs = [str(x) for x in ldf.lyrics]
    sentiment_scores = [sid.polarity_scores(x) for x in tqdm(docs)]
    song_ids = ldf['song_id'].tolist()
    song_sents = {k:v for k,v in zip(song_ids, sentiment_scores)}
    return song_sents

def getUserSentiments(userDict, song_sents):
    user_sents = {k:{} for k in userDict.keys()}
    for user, songs in userDict.items():
        sent_avgs = getUserSentiment(songs, song_sents)
        user_sents[user] = sent_avgs
    return user_sents

def getUserSentiment(history, song_sents):
    sent_types = song_sents.values()[0].keys()
    sent_dict = {s:[] for s in sent_types}
    for song, ct in history.items():
        sent_vals = song_sents[song]
        [sent_dict[k].append(ct*v) for k,v in sent_vals.items()]
    tot_ct = sum(history.values())
    sent_avgs = {k:(sum(sent_dict[k])/tot_ct) for k in sent_dict.keys()}
    return sent_avgs
#=====================Empath SCores========================================#
def getSongEmpaths(from_file = True):
    if from_file: return load_obj('song_empaths')
    else:
        ldf = pd.read_csv('ldf_all_final.csv')
        lexicon = Empath()
        docs = [str(x) for x in ldf.lyrics]
        cat_scores = [lexicon.analyze(x, normalize = True) for x in tqdm(docs)]
        song_ids = ldf['song_id'].tolist()
        song_scores = {k:v for k,v in zip(song_ids, cat_scores)}
    return song_scores

def getUserEmpaths(userDict, song_empaths):
    user_empaths = {k:{} for k in userDict.keys()}
    for user, songs in tqdm(userDict.items()):
        cat_avgs = getUserEmpath(songs, song_empaths)
        user_empaths[user] = cat_avgs
    return user_empaths   
            
def getUserEmpath(history, song_empaths):
    cat_types = song_empaths.values()[0].keys()
    cat_dict = {s:[] for s in cat_types}
    for song, ct in history.items():
        cat_vals = song_empaths[song]
        [cat_dict[k].append(ct*v) for k,v in cat_vals.items()]
    tot_ct = sum(history.values())
    cat_avgs = {k:(sum(cat_dict[k])/tot_ct) for k in cat_dict.keys()}
    return cat_avgs

#=============================Evaluation====================================#
def getEvalData():
    visible = open('EvalData/year1_test_triplets_visible.txt', 'r').readlines()
    visible = [v.strip().split('\t') for v in visible]
    vdict,hdict = {}, {}
    for user,song,ct in visible:
        if user not in vdict:
            vdict[user] = {}
        vdict[user][song] = vdict[user].get(song,0) + int(ct)
            
    hidden = open('EvalData/year1_test_triplets_hidden.txt', 'r').readlines()
    hidden = [h.strip().split('\t') for h in hidden]
    for user,song,ct in hidden:
        if user not in hdict:
            hdict[user] = {}
        hdict[user][song] = hdict[user].get(song,0) + int(ct)
    return {'visible':vdict,'hidden':hdict} 


def evaluate(model,eval_data,song_db,udb,outname="eval_results.csv", k=None, export=True, typ="content"):
    all_res = {k:{'model':[], 'random':[]} for k in eval_data['visible'].keys()}
    model_preds = makePreds(model,eval_data, export=False, typ=typ)
    if not k: k = model.k
    random_preds =  makeRandomPreds(eval_data,song_db,udb,k=k)
    for i,user in enumerate(model_preds.keys()):
        mres = model_preds[user]
        pres = random_preds[user]
        if export:
            if not os.path.isfile(outname):
                out = open(outname, 'w')
                out.write('idx,user,model,Accuracy,Recall,RBO\n')
            else: out = open(outname, 'a')
            mod_str =','.join([str(m) for m in mres])
            out.write(','.join([str(i),user,model.name,mod_str])+'\n') 
            rand_str =','.join([str(m) for m in pres])
            out.write(','.join([str(i),user,'random',rand_str])+'\n') 
            out.close()
        all_res[user]['model'] = mres
        all_res[user]['random'] = pres
    return all_res
    

def buildEvalSample(Eval,n=100):
    users = np.random.choice(Eval['visible'].keys(), size=n, replace=False)
    hid_sub = {u:Eval['visible'][u] for u in users.tolist()}
    vis_sub = {u:Eval['hidden'][u] for u in users.tolist()}
    return {'visible':vis_sub, 'hidden':hid_sub}

def calcEvalMetrics(d_actual,d_pred):
    acc = binaryAcc(d_actual.keys(), d_pred.keys())
    recl = recall(d_actual, d_pred)
    rbo = RBO(d_actual, d_pred)
    return (acc, recl, rbo)

def RBO(d1,d2):
    d1 = sorted(d1.items(), key=lambda x:x[1], reverse=True)
    d2 = sorted(d2.items(), key=lambda x:x[1], reverse=True)
    l1 = [tup[0] for tup in d1]
    l2 = [tup[0] for tup in d2]
    com_len = min(len(l1),len(l2))
    rbo = 0
    for i in range(1,com_len):
        common = set(l1[:i]).intersection(set(l2[:i]))
        inc = float(len(common)) / i
        rbo += inc
    rbo = float(rbo) / com_len
    return rbo

def binaryAcc(l1,l2):
    common = set(l1).intersection(set(l2))
    com_len = min(len(l1), len(l2))
    return float(len(common)) / com_len

def recall(d_actual, d_pred):
    found, total = 0,0
    for song,count in d_actual.items():
        if song in d_pred:
            pred_count = d_pred[song]
            found += min(count, pred_count)
        total += count
    return float(found) / total

    
#=======================Utilities/Data Import/Export==========================#
#trackstr = ', '.join(["'{}'".format(s) for s in final_songs])
#udb.query("insert into userdata_sub select * from userdata where song_id in ({})".format(songstr))



def calcTFIDF(db, tf,df, norm_tf=True):
    if norm_tf: tf = 1 + np.log(tf+1)
    return tf * np.log(1 + float(db.N) / df)   

def save_obj(obj, obj_name):
    with open('{}.pkl'.format(obj_name), 'w') as out:
        pickle.dump(obj, out)
        
def load_obj(obj_name):
    f = open('{}.pkl'.format(obj_name), 'r')
    return pickle.load(f)

def sparse_cos_sim(d1,d2):
    common_keys = set(d1.keys()).intersection(set(d2.keys()))
    num = 0
    for k in common_keys: num += d1[k]*d2[k]
    denom = np.linalg.norm(d1.values()) * np.linalg.norm(d2.values())
    return float(num) / denom      
        