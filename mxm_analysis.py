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
        tnames = self.tableNames()
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
    
class xmxdb(sqldb):
    def __init__(self,xmxpath='xmxdb.db'):
        sqldb.__init__(self, xmxpath)
        self.mxm_tables = ['words', 'lyrics']
        print('building vocab...')
        self.vocab = self.getVocab()
        print('counting songs...')
        self.N = self.query('select count(distinct track_id) from lyrics', timeit=True)
        self.N = self.N[0][0]
        self.tfidf = {k:{'tf':0,'df':0,'tfidf':0} for k in self.vocab}
                 
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
    
class userdb(sqldb):
    def __init__(self, fpath='userdata.db'):
        sqldb.__init__(self, fpath)
        self.fpath = fpath
        



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
        
        

    
#useful sqlite commands
#db.c.execute("SELECT name FROM sqlite_master WHERE type='table';")
#pragma table_info('lyrics') 
def calcTFIDF(db, tf,df, norm_tf=True):
    if norm_tf: tf = 1 + np.log(tf+1)
    return tf * np.log(1 + float(db.N) / df)   