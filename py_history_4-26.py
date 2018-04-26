# -*- coding: utf-8 -*-
# *** Spyder Python Console History Log ***

## ---(Thu Apr 26 13:53:35 2018)---
runfile('/home/brendan/TextMining/MSD_Song_Prediction/mxm_analysis.py', wdir='/home/brendan/TextMining/MSD_Song_Prediction')
buildUserDB('train_triplets.txt')
buildUserDB('userData.db')
runfile('/home/brendan/TextMining/MSD_Song_Prediction/mxm_analysis.py', wdir='/home/brendan/TextMining/MSD_Song_Prediction')
buildUserDB('userData.db')
buildUserDB('userData2.db')
runfile('/home/brendan/TextMining/MSD_Song_Prediction/mxm_analysis.py', wdir='/home/brendan/TextMining/MSD_Song_Prediction')
buildUserDB('userdata.db')
udb = userdb()
udb.query('SELECT * from userdata limit 15;')
udb.query('select count(*) from userdata')
users = udb.query('select distinct user_id from userdata')
users
len(users)
users = [u[0] for u in users]
users[:5]
u = users[0]
udb.query("select song_id, count from userdata where user_id = '{}'".format(u))
runfile('/home/brendan/TextMining/MSD_Song_Prediction/mxm_analysis.py', wdir='/home/brendan/TextMining/MSD_Song_Prediction')
mxm = mxmdb('mxmdb.db')
songs = mxm.getSongs()
len(songs)
msongs = songs
del(songs)
len(msongs)
usongs = udb.query('select distinct song_id from userdata')
len(usongs)
res = set(usongs).intersection(set(msongs))
len(res)
songs[:5]
usongs[:5]
usongs = [u[0] for u in usongs]
usongs[:5]
res = set(usongs).intersection(set(msongs))
len(res)
msongs[:5]
len(msongs[0])
len(usongs[0])
mxm.getTables()
mxm.showTables()
mxm.getSchema('lyrics')
udb.getSchema('userdata')
usongs[:5]
msongs[-5:]
for m in msongs:
    if m.startswith('SO'):
        print m
        
os.getcwd()
os.listdir('.')
f = open('unique_tracks.txt', 'r')
lines = f.readlines()
lines[:5]
l = lines[0].split('<SEP>')
l
l = lines[0].strip().split('<SEP>')
l
lines = [l.strip().split('<SEP>') for l in lines]
lines = [l.append(l[0]+l[1])]
lines[:5]
len(lines)
tracks,songs,songnames,artists = zip(*lines)
tracks[:3]
len(set(tracks))
len(set(songs))
mxm.query('create table trackdata(track_id TEXT primary key, song_id TEXT, song_name TEXT, artist TEXT)')
mxm.showTables()
runfile('/home/brendan/TextMining/MSD_Song_Prediction/mxm_analysis.py', wdir='/home/brendan/TextMining/MSD_Song_Prediction')
mxm = mxmdb()
mxm.query('create table trackdata(track_id TEXT primary key, song_id TEXT, song_name TEXT, artist TEXT)')
mxm.showTables()
mxm.getTableNames()
mxm.getSchema('trackdata')
runfile('/home/brendan/TextMining/MSD_Song_Prediction/mxm_analysis.py', wdir='/home/brendan/TextMining/MSD_Song_Prediction')
mxm = mxmdb()
mxm.showTables()
lines[:5]
for tid, sid, nm, art in tqdm(lines):
    mxm.query("insert into trackdata values('{}','{}','{}','{}')".format(tid,sid,nm,art))
tid,sid,nm,art = lines[0]
tid,sid,nm,art
mxm.query('insert into trackdata values('+tid+','+sid+','+nm+','+art+')')
mxm.query("insert into trackdata values('+tid+','+sid+','+nm+','+art+')")
mxm.query('select * from trackdata')
mxm.query('select track_id from trackdata')
for tid, sid, nm, art in tqdm(lines):
    try:mxm.query("insert into trackdata values('{}','{}','{}','{}')".format(tid,sid,nm,art))
    except: print('error adding line {}'.format(tid))
mxm.query('truncate table trackdata')
mxm.query('truncate trackdata')
mxm.query('drop table trackdata')
mxm.query('create table trackdata(track_id TEXT primary key, song_id TEXT, song_name TEXT, artist TEXT)')
for i,(tid, sid, nm, art) in tqdm(enumerate(lines)):
    print('{},{},{}'.format(i,nm,art))
    mxm.query("insert into trackdata values('{}','{}','{}','{}')".format(tid,sid,nm,art))
mxm.query('select song_name from trackdata')
l[:5]
lines[:5]
clean_lines = []
for l in lines:
    l = l.strip().replace("'","")
    clean_lines.append(l.split('<SEP>'))
with open(fname, 'r') as f:
    lines = f.readlines()

clean_lines = []
for l in lines:
    l = l.strip().replace("'","")
    clean_lines.append(l.split('<SEP>'))
fname = 'unique_tracks.txt'
with open(fname, 'r') as f:
    lines = f.readlines()

clean_lines = []
for l in lines:
    l = l.strip().replace("'","")
    clean_lines.append(l.split('<SEP>'))
clean_lines[:10]
mxm.query('drop table trackdata')
mxm.query('create table trackdata(track_id TEXT primary key, song_id TEXT, song_name TEXT, artist TEXT)')
for i,(tid, sid, art, nm) in tqdm(enumerate(lines)):
    print('{},{},{}'.format(i,nm,art))
    mxm.query("insert into trackdata values('{}','{}','{}','{}')".format(tid,sid,nm,art))
clean_tracks[0]
clean_lines[0]
for i,(tid, sid, art, nm) in tqdm(enumerate(clean_lines)):
    print('{},{},{}'.format(i,nm,art))
    mxm.query("insert into trackdata values('{}','{}','{}','{}')".format(tid,sid,nm,art))
mxm.query('drop table trackdata')
mxm.query('create table trackdata(track_id TEXT primary key, song_id TEXT, song_name TEXT, artist TEXT)')
for i,(tid, sid, art, nm) in tqdm(enumerate(clean_lines)):
    #print('{},{},{}'.format(i,nm,art))
    mxm.query("insert into trackdata values('{}','{}','{}','{}')".format(tid,sid,nm,art))
for i,(tid, sid, art, nm) in enumerate(tqdm(clean_lines)):
    #print('{},{},{}'.format(i,nm,art))
    mxm.query("insert into trackdata values('{}','{}','{}','{}')".format(tid,sid,nm,art))
mxm.query('drop table trackdata')
mxm.query('create table trackdata(track_id TEXT primary key, song_id TEXT, song_name TEXT, artist TEXT)')
for i,(tid, sid, art, nm) in enumerate(tqdm(clean_lines)):
    #print('{},{},{}'.format(i,nm,art))
    mxm.query("insert into trackdata values('{}','{}','{}','{}')".format(tid,sid,nm,art))
mxm.query('select song_id from trackdata inner join lyrics on lyrics.track_id = trackdata.track_id')
res = mxm.query('select song_id from trackdata inner join lyrics on lyrics.track_id = trackdata.track_id')
res = [r[0] for r in res]
len(res)
mxm.N
tids = mxm.query('select track_id from lyrics')
len(tids)
len(tids )==len(res)
mxm.query('alter table lyrics add song_id text')
mxm.showTables()
for r in res:
    mxm.query("insert into lyrics (song_id) values('{}')".format(r))
mxm.query('select * from lyrics limit 10')
mxm.query('insert into lyrics(song_id) select song_id from trackdata inner join lyrics on lyrics.track_id = trackdata.track_id')
mxm.showTables()
mxm.query('update lyrics set lyrics.song_id = trackdata.song_id from lyrics inner join trackdata on lyrics.track_id = trackdata.track_id')
mxm.query("SELECT lyrics.track_id, mxm_tid,word,count,is_test,trackdata.song_id into lyricsv2 from lyrics inner join trackdata")
mxm.query('alter table lyrics rename to lyrics_old')
q = "CREATE TABLE lyrics (track_id,"
   q += " mxm_tid INT,"
   q += " word TEXT,"
   q += " count INT,"
   q += " is_test INT,"
   q += " FOREIGN KEY(word) REFERENCES words(word),"
   q += "song_id TEXT)"
q = "CREATE TABLE lyrics (track_id,"
    q += " mxm_tid INT,"
    q += " word TEXT,"
    q += " count INT,"
    q += " is_test INT,"
    q += " FOREIGN KEY(word) REFERENCES words(word),"
    q += "song_id TEXT)"
q
q = "CREATE TABLE lyrics (track_id,"
q += " mxm_tid INT,"
q += " word TEXT,"
q += " count INT,"
q += " is_test INT,"
q += " FOREIGN KEY(word) REFERENCES words(word),"
q += "song_id TEXT)"
q
mxm.query(q)
q = "CREATE TABLE lyrics (track_id,"
q += " mxm_tid INT,"
q += "song_id TEXT,"
q += " word TEXT,"
q += " count INT,"
q += " is_test INT,"
q += " FOREIGN KEY(word) REFERENCES words(word))"
mxm.query(q)
mxm.showTables()
mxm.query('select * from trackdata limit 5')
mxn.query('insert into lyrics (track_id, mxm_id, song_id, word, count, is_test) select a.track_id, a.mxm_id, b.,song_id, a.word, a.count, a.is_test from lyrics as a INNER JOIN trackdata as b ON a.track_id = b.track_id')
mxm.query('insert into lyrics (track_id, mxm_id, song_id, word, count, is_test) select a.track_id, a.mxm_id, b.,song_id, a.word, a.count, a.is_test from lyrics as a INNER JOIN trackdata as b ON a.track_id = b.track_id')
mxm.query('insert into lyrics (track_id, mxm_id, song_id, word, count, is_test) select a.track_id, a.mxm_id, b.song_id, a.word, a.count, a.is_test from lyrics_old as a INNER JOIN trackdata as b ON a.track_id = b.track_id')
mxm.query('insert into lyrics (track_id, mxm_tid, song_id, word, count, is_test) select a.track_id, a.mxm_id, b.song_id, a.word, a.count, a.is_test from lyrics_old as a INNER JOIN trackdata as b ON a.track_id = b.track_id')
mxm.showTables()
mxm.query('insert into lyrics (track_id, mxm_tid, song_id, word, count, is_test) select a.track_id, a.mxm_tid, b.song_id, a.word, a.count, a.is_test from lyrics_old as a INNER JOIN trackdata as b ON a.track_id = b.track_id')
mxm.query('select * from lyrics limit 5')
mxm.getSchema('lyrics')
l_res = mxm.query('select song_id from lyrics')
u_res = udb.query('select song_id from userdata')
overlap = set(l_res).intersection(set(u_res))
len(overlap)
len(l_res)
len(u_res)
len(set(l_res))
len(set(u_res))
del(l_res)
del(u_res)
overlap[0]
overlap.at(0)
overlap = list(overlap)
overlap[0]
overlap = [l[0] for l in overlap]
overlap[0]
with open('overlapping_songs.txt', 'w') as out:
    out.write('\n'.join(overlap))
    
udb.query('select user_id, track_id, count from userdata group by user_id limit 100')
udb.showTables()
class userdb(sqldb):
    def __init__(self, fpath='userdata.db'):
        sqldb.__init__(self, fpath)
        self.fpath = fpath
udb.showTables()
udb.getSchema('userdata')
udb.query('select user_id, song_id, count from userdata group by user_id limit 100')
udb.query('select * from userdata where user_id = 0005063ece7d23dfe2ed34cbc4c79d8aaa617b78')
udb.query("select * from userdata where user_id = '0005063ece7d23dfe2ed34cbc4c79d8aaa617b78'")
res = udb.query("select * from userdata where user_id = '0005063ece7d23dfe2ed34cbc4c79d8aaa617b78'")
runfile('/home/brendan/TextMining/MSD_Song_Prediction/mxm_analysis.py', wdir='/home/brendan/TextMining/MSD_Song_Prediction')
udb = userdb()
len(udb.users)
udb.valid_songs[:5]
len(udb.valid_songs)
def get_user_dists(db):
    for user in db.users:
        rows = db.query("select * from userdata where user_id = '{}'".format(user))
        uids,sids,counts = zip(*rows)
        if len(set(sids).intersection(db.valid_songs) > 10):
            del(rows)
            for uid, sid, count in zip(uids,sids,counts):
                db.user_dists[uid][sid] = db.user_dsits[uid].get(sid,0) + count
        return db
def get_user_dists(db):
    for user in tqdm(db.users):
        rows = db.query("select * from userdata where user_id = '{}'".format(user))
        uids,sids,counts = zip(*rows)
        if len(set(sids).intersection(db.valid_songs) > 10):
            del(rows)
            for uid, sid, count in zip(uids,sids,counts):
                db.user_dists[uid][sid] = db.user_dsits[uid].get(sid,0) + count
        return db
udb = get_user_dists(udb)
def get_user_dists(db):
    for user in tqdm(db.users):
        rows = db.query("select * from userdata where user_id = '{}'".format(user))
        uids,sids,counts = zip(*rows)
        if len(set(sids).intersection(db.valid_songs)) > 10:
            del(rows)
            for uid, sid, count in zip(uids,sids,counts):
                db.user_dists[uid][sid] = db.user_dsits[uid].get(sid,0) + count
        return db
udb = get_user_dists(udb)
len(udb.users)
len(udb.user_dists)
class userdb(sqldb):
    def __init__(self, fpath='userdata.db'):
        sqldb.__init__(self, fpath)
        self.fpath = fpath
        print('getting users...')
        self.users = self.get_users()
        print('counting records...')
        self.N = self.query('select count(*) from userdata')
        self.user_dists = {}
        self.get_songPool()
    
    def get_users(self):
        res = self.query('select distinct user_id from userdata')
        return [r[0] for r in res]
    
    def get_songPool(self):
        with open('overlapping_songs.txt', 'r') as f:
            lines = f.readlines()
        self.valid_songs = set(lines)
    
    def get_user_dists(self):
        for user in self.users:
            rows = self.query("select * from userdata where user_id = '{}'".format(user))
            uids,sids,counts = zip(*rows)
            if len(set(sids).intersection(self.valid_songs) > 10):
                del(rows)
                for uid, sid, count in zip(uids,sids,counts):
                    self.user_dists[uid][sid] = self.user_dsits[uid].get(sid,0) + count
udb = userdb()
udb = get_user_dists(udb)
len(udb.user_dist)
len(udb.user_dists)
len(udb.users)
user = udb.users[0]
user
rows = db.query("select * from userdata where user_id = '{}'".format(user))
uids,sids,counts = zip(*rows)
db = udb
rows = db.query("select * from userdata where user_id = '{}'".format(user))
uids,sids,counts = zip(*rows)

rows[:5]
set(sids).intersection(db.valid_songs)
sids[:5]
len(set(sids).intersection(db.valid_songs)) > 10
list(db.valid_songs)[0]
list(db.valid_songs)[1]
db.valid_songs = [s.strip() for s in db.valid_songs]
db.valid_songs = set(db.valid_songs)
len(set(sids).intersection(db.valid_songs)) > 10
for user in tqdm(db.users):
    rows = db.query("select * from userdata where user_id = '{}'".format(user))
    uids,sids,counts = zip(*rows)
    if len(set(sids).intersection(db.valid_songs)) > 10:
        del(rows)
        for uid, sid, count in zip(uids,sids,counts):
            db.user_dists[uid][sid] = db.user_dsits[uid].get(sid,0) + count
def get_user_dists(db):
    for user in tqdm(db.users):
        rows = db.query("select * from userdata where user_id = '{}'".format(user))
        uids,sids,counts = zip(*rows)
        if len(set(sids).intersection(db.valid_songs)) > 10:
            del(rows)
            for uid, sid, count in zip(uids,sids,counts):
                db.user_dists[uid][sid] = db.user_dists[uid].get(sid,0) + count
        return db
res = get_user_dists(db)
def get_user_dists(db):
    for user in tqdm(db.users):
        rows = db.query("select * from userdata where user_id = '{}'".format(user))
        uids,sids,counts = zip(*rows)
        if len(set(sids).intersection(db.valid_songs)) > 10:
            del(rows)
            for uid, sid, count in zip(uids,sids,counts):
                if uid not in db.user_dists: db.user_dists[uid] = {}
                db.user_dists[uid][sid] = db.user_dists[uid].get(sid,0) + count
        return db
res = get_user_dists(db)
len(res.user_dists)
def get_user_dists(db):
    for user in tqdm(db.users):
        rows = db.query("select * from userdata where user_id = '{}'".format(user))
        uids,sids,counts = zip(*rows)
        if len(set(sids).intersection(db.valid_songs)) > 10:
            del(uids,sids,counts)
            for uid, sid, count in rows:
                if uid not in db.user_dists: db.user_dists[uid] = {}
                db.user_dists[uid][sid] = db.user_dists[uid].get(sid,0) + count
        return db
del(res)
db = get_user_dists(db)
len(db.users)
def get_user_dists(db):
    for user in tqdm(db.users):
        rows = db.query("select * from userdata where user_id = '{}'".format(user))
        uids,sids,counts = zip(*rows)
        if len(set(sids).intersection(db.valid_songs)) > 1:
            del(uids,sids,counts)
            for uid, sid, count in rows:
                if uid not in db.user_dists: db.user_dists[uid] = {}
                db.user_dists[uid][sid] = db.user_dists[uid].get(sid,0) + count
        return db
db = get_user_dists(db)
len(db.user_dists)
def get_user_dists(db):
    for user in tqdm(db.users):
        rows = db.query("select * from userdata where user_id = '{}'".format(user))
        uids,sids,counts = zip(*rows)
        if len(set(sids).intersection(db.valid_songs)) > 1:
            for uid, sid, count in rows:
                if uid not in db.user_dists: db.user_dists[uid] = {}
                db.user_dists[uid][sid] = db.user_dists[uid].get(sid,0) + count
        return db
db = get_user_dists(db)
def get_user_dists(db):
    for user in tqdm(db.users):
        rows = db.query("select * from userdata where user_id = '{}'".format(user))
        uids,sids,counts = zip(*rows)
        #if len(set(sids).intersection(db.valid_songs)) > 1:
        for uid, sid, count in rows:
            if uid not in db.user_dists: db.user_dists[uid] = {}
            db.user_dists[uid][sid] = db.user_dists[uid].get(sid,0) + count
        return db
db = get_user_dists(db)
db.users[:5]
len(db.users)
def get_user_dists(db):
    for user in db.users:
        rows = db.query("select * from userdata where user_id = '{}'".format(user))
        uids,sids,counts = zip(*rows)
        print('user: {}, num_matches: {}'.format(user,len(rows)))
        #if len(set(sids).intersection(db.valid_songs)) > 1:
        for uid, sid, count in rows:
            if uid not in db.user_dists: db.user_dists[uid] = {}
            db.user_dists[uid][sid] = db.user_dists[uid].get(sid,0) + count
        return db
def get_user_dists(db):
    for user in db.users:
        rows = db.query("select * from userdata where user_id = '{}'".format(user))
        uids,sids,counts = zip(*rows)
        print('user: {}, num_matches: {}'.format(user,len(rows)))
        #if len(set(sids).intersection(db.valid_songs)) > 1:
        for uid, sid, count in rows:
            if uid not in db.user_dists: db.user_dists[uid] = {}
            db.user_dists[uid][sid] = db.user_dists[uid].get(sid,0) + count
    return db
db = get_user_dists(db)
def get_user_dists(db):
    for user in tqdm(db.users):
        rows = db.query("select * from userdata where user_id = '{}'".format(user))
        uids,sids,counts = zip(*rows)
        print('user: {}, num_matches: {}'.format(user,len(rows)))
        if len(set(sids).intersection(db.valid_songs)) > 10:
            for uid, sid, count in rows:
                if uid not in db.user_dists: db.user_dists[uid] = {}
                db.user_dists[uid][sid] = db.user_dists[uid].get(sid,0) + count
    return db
db = get_user_dists(db)
def get_user_dists(db):
    for user in tqdm(db.users):
        rows = db.query("select * from userdata where user_id = '{}'".format(user))
        uids,sids,counts = zip(*rows)
        #print('user: {}, num_matches: {}'.format(user,len(rows)))
        if len(set(sids).intersection(db.valid_songs)) > 10:
            for uid, sid, count in rows:
                if uid not in db.user_dists: db.user_dists[uid] = {}
                db.user_dists[uid][sid] = db.user_dists[uid].get(sid,0) + count
    return db
db = get_user_dists(db)
all_data = udb.query('select * from userdata')
len(all_data)
del(all_data)
mxm.showTables()
mxm.query('drop table lyrics_old')
mxm.showTables()
udb.query('select * from userdata where rowid = 1')
udb.N
udb.N = udb.N[0]
udb.N
def get_user_dists(db, batch_size = 128):
    num_batches = db.N / batch_size
    for n in range(num_batches-1):
        start, end = batch_size*n, batch_size*(n+1)
        if n == num_batches-1:
            rows = db.query('select * from userdata where rowid > {}'.format(start))
        else:
            rowrange = range(start,end)
            rows = db.query('select * from userdata where rowid in {}'.format(rowrange)) 
        for r in rows:
            uid, sid, count = r
            if uid not in db.user_dists: db.user_dists[uid] = {}
            db.user_dists[uid][sid] = db.user_dists[uid].get(sid,0) + count


#    for user in tqdm(db.users):
#        rows = db.query("select * from userdata where user_id = '{}'".format(user))
#        uids,sids,counts = zip(*rows)
#        #print('user: {}, num_matches: {}'.format(user,len(rows)))
#        if len(set(sids).intersection(db.valid_songs)) > 10:
#            for uid, sid, count in rows:
#                if uid not in db.user_dists: db.user_dists[uid] = {}
#                db.user_dists[uid][sid] = db.user_dists[uid].get(sid,0) + count
    return db
db = get_user_dists(db)
def get_user_dists(db, batch_size = 128):
    num_batches = db.N / batch_size
    for n in range(num_batches-1):
        start, end = batch_size*n, batch_size*(n+1)
        if n == num_batches-1:
            rows = db.query('select * from userdata where rowid > {}'.format(start))
        else:
            rowrange = range(start,end)
            rows = db.query("select * from userdata where rowid in '{}'".format(rowrange)) 
        for r in rows:
            uid, sid, count = r
            if uid not in db.user_dists: db.user_dists[uid] = {}
            db.user_dists[uid][sid] = db.user_dists[uid].get(sid,0) + count


#    for user in tqdm(db.users):
#        rows = db.query("select * from userdata where user_id = '{}'".format(user))
#        uids,sids,counts = zip(*rows)
#        #print('user: {}, num_matches: {}'.format(user,len(rows)))
#        if len(set(sids).intersection(db.valid_songs)) > 10:
#            for uid, sid, count in rows:
#                if uid not in db.user_dists: db.user_dists[uid] = {}
#                db.user_dists[uid][sid] = db.user_dists[uid].get(sid,0) + count
    return db
db = get_user_dists(db)
db.query("select * from userdata where row_id in (1,2,3)")
db.query("select * from userdata where rowid in (1,2,3)")
db.query("select * from userdata where rowid in {}".format(range(1:20)))
db.query("select * from userdata where rowid in {}".format(range(1,20)))
db.query("select * from userdata where rowid in {}".format([str(i) for i in range(1,20)]))
db.query("select * from userdata where rowid in ({})".format([str(i) for i in range(1,20)]))
db.query("select * from userdata where rowid in ({})".format(range(1,20)))
s1 = "select * from userdata where rowid in (1,2,3)"
s2 = "select * from userdata where rowid in ({})".format(range(1,4))
s2
s2 = "select * from userdata where rowid in ({})".format(', '.join(range(1,4))))
s2 = "select * from userdata where rowid in ({})".format(', '.join(range(1,4)))
s2 = "select * from userdata where rowid in ({})".format(', '.join([str(i) for i in range(1,4)]))
s2
udb.query(s1)
udb.query(s2)
start = 100
end = 228
udb.query("select * from userdata where rowid in ({})".format(', '.join([str(i) for i in range(start,end)])))
def get_user_dists(db, batch_size = 128):
    num_batches = db.N / batch_size
    for n in range(num_batches-1):
        start, end = batch_size*n, batch_size*(n+1)
        if n == num_batches-1:
            rows = db.query('select * from userdata where rowid > {}'.format(start))
        else:
            rowrange = ', '.join([str(i) for i in range(start,end)])
            rows = db.query("select * from userdata where rowid in '{}'".format(rowrange)) 
        for r in rows:
            uid, sid, count = r
            if uid not in db.user_dists: db.user_dists[uid] = {}
            db.user_dists[uid][sid] = db.user_dists[uid].get(sid,0) + count


#    for user in tqdm(db.users):
#        rows = db.query("select * from userdata where user_id = '{}'".format(user))
#        uids,sids,counts = zip(*rows)
#        #print('user: {}, num_matches: {}'.format(user,len(rows)))
#        if len(set(sids).intersection(db.valid_songs)) > 10:
#            for uid, sid, count in rows:
#                if uid not in db.user_dists: db.user_dists[uid] = {}
#                db.user_dists[uid][sid] = db.user_dists[uid].get(sid,0) + count
    return db
db = get_user_dists(db)
udb.query('select * from userdata where rowid = 0')
def get_user_dists(db, batch_size = 128):
    num_batches = db.N / batch_size
    for n in range(num_batches-1):
        start, end = batch_size*n+1, batch_size*(n+1)+1
        if n == num_batches-1:
            rows = db.query('select * from userdata where rowid > {}'.format(start))
        else:
            rowrange = ', '.join([str(i) for i in range(start,end)])
            rows = db.query("select * from userdata where rowid in '{}'".format(rowrange)) 
        for r in rows:
            uid, sid, count = r
            if uid not in db.user_dists: db.user_dists[uid] = {}
            db.user_dists[uid][sid] = db.user_dists[uid].get(sid,0) + count


#    for user in tqdm(db.users):
#        rows = db.query("select * from userdata where user_id = '{}'".format(user))
#        uids,sids,counts = zip(*rows)
#        #print('user: {}, num_matches: {}'.format(user,len(rows)))
#        if len(set(sids).intersection(db.valid_songs)) > 10:
#            for uid, sid, count in rows:
#                if uid not in db.user_dists: db.user_dists[uid] = {}
#                db.user_dists[uid][sid] = db.user_dists[uid].get(sid,0) + count
    return db
udb.query('select * from userdata where rowid = 0')
db = get_user_dists(db)
def get_user_dists(db, batch_size = 128):
    num_batches = db.N / batch_size
    for n in tqdm(range(num_batches-1)):
        start, end = batch_size*n+1, batch_size*(n+1)+1
        if n == num_batches-1:
            rows = db.query('select * from userdata where rowid > {}'.format(start))
        else:
            rowrange = ', '.join([str(i) for i in range(start,end)])
            rows = db.query("select * from userdata where rowid in '({})'".format(rowrange)) 
        for r in rows:
            uid, sid, count = r
            if uid not in db.user_dists: db.user_dists[uid] = {}
            db.user_dists[uid][sid] = db.user_dists[uid].get(sid,0) + count


#    for user in tqdm(db.users):
#        rows = db.query("select * from userdata where user_id = '{}'".format(user))
#        uids,sids,counts = zip(*rows)
#        #print('user: {}, num_matches: {}'.format(user,len(rows)))
#        if len(set(sids).intersection(db.valid_songs)) > 10:
#            for uid, sid, count in rows:
#                if uid not in db.user_dists: db.user_dists[uid] = {}
#                db.user_dists[uid][sid] = db.user_dists[uid].get(sid,0) + count
    return db
db = get_user_dists(db)
n = 0
batch_size=128
num_batches = db.N / batch_size
start, end = batch_size*n+1, batch_size*(n+1)+1
start,end
rowrange = ', '.join([str(i) for i in range(start,end)])
rowrange
q = "select * from userdata where rowid in ({})".format(rowrange)
q
udb.query(q)
def get_user_dists(db, batch_size = 128):
    num_batches = db.N / batch_size
    for n in tqdm(range(num_batches-1)):
        start, end = batch_size*n+1, batch_size*(n+1)+1
        if n == num_batches-1:
            rows = db.query('select * from userdata where rowid > {}'.format(start))
        else:
            rowrange = ', '.join([str(i) for i in range(start,end)])
            rows = db.query("select * from userdata where rowid in ({})".format(rowrange)) 
        for r in rows:
            uid, sid, count = r
            if uid not in db.user_dists: db.user_dists[uid] = {}
            db.user_dists[uid][sid] = db.user_dists[uid].get(sid,0) + count


#    for user in tqdm(db.users):
#        rows = db.query("select * from userdata where user_id = '{}'".format(user))
#        uids,sids,counts = zip(*rows)
#        #print('user: {}, num_matches: {}'.format(user,len(rows)))
#        if len(set(sids).intersection(db.valid_songs)) > 10:
#            for uid, sid, count in rows:
#                if uid not in db.user_dists: db.user_dists[uid] = {}
#                db.user_dists[uid][sid] = db.user_dists[uid].get(sid,0) + count
    return db
db = get_user_dists(db)
db.user_dists.items()[:5]
filt_tups = []
for k,v in db.user_dists.items():
    if len(set(v).intersection(db.valid_songs)) > 10:
        filt_tups.append(k,v)
        
for k,v in db.user_dists.items():
    if len(set(v).intersection(db.valid_songs)) > 10:
        filt_tups.append((k,v))
        
len(filt_tups)
def filter_users(db, n):
    filt_tups = []
    for k,v in db.user_dists.items():
        if len(set(v).intersection(db.valid_songs)) > n:
            filt_tups.append((k,v))
    return dict(filt_tups)
res =filter_users(db, 20)
len(res)
res =filter_users(db, 50)
len(res)
res =filter_users(db, 100)
len(res)
res =filter_users(db, 1000)
len(res)
res =filter_users(db, 500)
len(res)
res =filter_users(db, 250)
len(res)
res =filter_users(db, 175)
len(res)
res =filter_users(db, 30)
len(res)
import pickle
def save_obj(obj, obj_name):
    with open('{}.pkl'.format(obj_name), 'w') as out:
        pickle.dump(obj, out)
save_obj(udb, 'user_database')
save_obj(db.user_dists, 'user_song_distributions')