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
q += "song_id TEXT,"
q += " word TEXT,"
q += " count INT,"
q += " is_test INT,"
q += " FOREIGN KEY(word) REFERENCES words(word))"
mxm.query(q)
mxm.showTables()
mxm.query('insert into lyrics (track_id, mxm_tid, song_id, word, count, is_test) select a.track_id, a.mxm_tid, b.song_id, a.word, a.count, a.is_test from lyrics_old as a INNER JOIN trackdata as b ON a.track_id = b.track_id')
mxm.query('select * from lyrics limit 5')
mxm.getSchema('lyrics')
l_res = mxm.query('select song_id from lyrics')
u_res = udb.query('select song_id from userdata')
overlap = set(l_res).intersection(set(u_res))
len(overlap)
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
#======================thursday night (mac)============================#
# -*- coding: utf-8 -*-
# *** Spyder Python Console History Log ***

## ---(Tue Oct 17 23:30:53 2017)---
import re
import mechanize

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Firefox')]
br.open("http://www.google.com")
response = br.open('http://www.google.com')
br.title()
br.forms()
for f in br.forms():
    print f
    
form['q']
br['q']
br.select_form(name="q")
for f in br.forms():
    print f
    
br.select_form('f')
br.form[0]
br.form['q']
br.form['q'] = 'Jack Abraham'
for f in br.forms():
    print f
    
br.submit()
for f in br.forms():
    print f
    
res = br.submit()
for l in br.links:
    print l
    
for l in br.links():
    print l
    
br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Firefox')]
response = br.open("http://www.ipvoid.com/ip-blacklist-check/")
for f in br.forms():
    print f
    
br.select_form('ip')
print br.forms()[0]
print br.forms()[0][0]
print br.forms()[0]['ip']
br.forms()[0]['ip'] = 103.43.202.18
br.select_form()
for f in br.forms():
    print f
    
f = br.forms()[0]
br['ip']
br.select_form('ip')
br.select_form(type='textControl')
for f in br.forms():
    print f
    
br.select_form(type='TextControl')
br.select_form(nr=0)
len(br.forms())
ct = br.select_form(nr=0)
ctl.value
ct.value
br.select_form(nr=1)
br.select_form(nr=0)
f = br.forms()[0]
f
f.value()
f.value
print f
resp2 = br.open('http://www.google.com')
for f in br.forms():
    print f
    
br.select_form('q')
br.select_control('q')
br.form.find_control('q')
for c in br.form.controls:
    print c
    
for f in br.forms():
    print f
    
br.select_form('q')
br.form['q']
response = br.open('http://www.google.com')
for f in br.forms():
    print f
    
br.form['q']
br.select_form('q')
br.select_form('f')
br.form
print br.form
br.form['q']
for f in br.forms():
    print f
    
response = br.open("http://www.ipvoid.com/ip-blacklist-check/")
for f in br.forms():
    print f
    
br.select_form(nr=0)
br.form
br.form['ip'] = 103.43.202.18
br.form['ip']
br.form['ip'] = '103.43.202.18'
search_res = br.sumbit()
for f in br.forms():
    print f
    
control = br.form.select_control(nr=1)
for c in br.form.controls:
    print c
    
c = br.form.controls[1]
c
c.readonly = False
print c
br.submit()
br.read()
br.get_data()
response = br.open("http://www.ipvoid.com/ip-blacklist-check/")
br.select_form(nr=0)
print br.form
br.form['ip'] = '103.43.202.18'
print br.form
br.form[1].readonly = False
br.form.controls[1]readonly = False
br.form.controls[1].readonly = False
print br.form
resp = br.submit()
print resp.read()
for l in br.links():
    print l
    
resp.read()
resp.get_data()
page = resp.get_data()
res = re.findall("""<span class=.*?>.*//.*?</span>""", page)
res
res = re.findall("""<span .*?>.*?</span>""", page)
res
res = re.findall("""<span .*?>[0-9]+//[0-9]+</span>""", page)
res
res = re.findall("""<span .*?>[0-9]+.[0-9]+</span>""", page)
res
res = re.findall("""<span .*?>[0-9].*?</span>""", page)
res
res = re.findall("""<span .*?>.*?[0-9].*?</span>""", page)
res
res = re.findall("""<span .*?>.*?[0-9]+//[0-9]+</span>""", page)
res
res = re.findall("""<span .*?>.*?[0-9].*?[0-9]+</span>""", page)
res
res = re.findall("""<span .*?>.*?[0-9]+.[0-9]+</span>""", page)
res
clas = re.findall("class=(.*?)", res[0])
clas
res[0]
clas = re.findall("<spsan class=(.*?)>", res[0])
clas
clas = re.findall("<span class=(.*?)>", res[0])
clas
prop = re.findall("""[0-9]+.[0-9]+</span>""", page)
prop
prop = re.findall("""([0-9]+.[0-9]+)</span>""", page)
prop
num, den = [int(t) for t in prop.split('/')]
num, den = [int(t) for t in prop[0].split('/')]
num
den
def lookup_ip(ip, browser = None):
    if browser is not None:
        br = browser
    else:
        br = mech.Browser()
        br.set_handle_robots(False)
        br.addheaders = [('User-agent', 'Firefox')]
    response = br.open("http://www.ipvoid.com/ip-blacklist-check/")
    br.select_form(nr=0)
    br.form['ip'] = ip
    br.form.controls[1].readonly = False
    resp = br.submit()
    page = resp.get_data()
    res = re.findall("""<span .*?>.*?[0-9]+.[0-9]+</span>""", page)
    label = re.findall("<spsan class=(.*?)>", res[0])[0]
    if 'danger' in label: status = "Blacklisted"
    elif 'success' in label: status = "Possibly Safe"
    else: status = "Unknown"
    prop = re.findall("""([0-9]+.[0-9]+)</span>""", page)
    num, den = [int(t) for t in prop[0].split('/')]
    decimal = float(num) / float(den)
    return status, decimal, num
lookup_ip('106.87.97.138')
import mechanize as mech
lookup_ip('106.87.97.138')
def ip_lookup(ip, browser = None):
    if browser is not None:
        br = browser
    else:
        br = mech.Browser()
        br.set_handle_robots(False)
        br.addheaders = [('User-agent', 'Firefox')]
    response = br.open("http://www.ipvoid.com/ip-blacklist-check/")
    br.select_form(nr=0)
    br.form['ip'] = ip
    br.form.controls[1].readonly = False
    resp = br.submit()
    page = resp.get_data()
    res = re.findall("""<span .*?>.*?[0-9]+.[0-9]+</span>""", page)
    label = re.findall("<span class=(.*?)>", res[0])[0]
    if 'danger' in label: status = "Blacklisted"
    elif 'success' in label: status = "Possibly Safe"
    else: status = "Unknown"
    prop = re.findall("""([0-9]+.[0-9]+)</span>""", page)
    num, den = [int(t) for t in prop[0].split('/')]
    decimal = float(num) / float(den)
    return status, decimal, num
res = ip_lookup('106.87.97.138')
res
res = ip_lookup('106.87.97.138', browser=br)
res = ip_lookup('106.87.97.138')
f = open(fname, 'r')
fname = '/Users/babraham/Desktop/pcap/hr_traffic_test.csv'
f = open(fname, 'r')
f.close()
import pandas as pd
df = pd.DataFrame.from_csv(fname)
df
df['src_host']
df[:,'src_host']
df.columns
df.ix[2]
df = pd.DataFrame.from_csv(fname)
df.columns
print df[:,0]
df.ix[1, 'dest_host']
df.columns
res = pd.DataFrame.from_csv(fname)
print res
df.columns
f = open(fname, 'r')
headers = f.readline()
headers
headers = headers.strip().split(',')
headers
data = [[] for h in headers]
fields = {headers[i]:i for i in range(len(headers))}
fields
lines = f.readlines()
for l in lines:
    lsplit = l.split(',')
    for header in headers:
        data[fields[header]].append(lsplit[fields[header]])
        
data
res = zip[d for d in data])
res = zip(d[0],d[1],d[2],d[3],d[4],d[5],d[6],d[7])
d = data
res = zip(d[0],d[1],d[2],d[3],d[4],d[5],d[6],d[7])
res
data = []
for l in lines:
    lsplit = l.strip().split(',')
    for header in headers:
        data[fields[header]].append(lsplit[fields[header]])
        
for l in lines:
    l = l.strip()
    lsplit = l.split(',')
    for header in headers:
        data[fields[header]].append(lsplit[fields[header]])
        
len(lines)
data = [[] for h in headers]
for l in lines:
    l = l.strip()
    lsplit = l.split(',')
    for header in headers:
        data[fields[header]].append(lsplit[fields[header]])
        
df = pd.DataFrame(data, columns = headers)
len(data)
len(data[0])
data[0]
lens = [len(d) for d in data]
lens
headers
df = pd.DataFrame(data)
df.columns = headers
df
df.transpose()
df = df.transpose()
df.columns = headers
df
df = pd.DataFrame(data).transpose()
f.close()
f = open(fname, 'r')
l = f.readline()
l.strip().split(',')
f.readline().strip().split(',')
f = open(fname, 'r')
headers = f.readline().strip().split(',')
data = [[] for h in headers]
fields = {headers[i]:i for i in range(len(headers))}
lines = f.readlines()
for l in lines:
    lsplit = l.strip().split(',')
    for header in headers:
        data[fields[header]].append(lsplit[fields[header]])

df = pd.DataFrame(data).transpose()
df.columns = headers
df.ix[:,'src_host']
subset = df.ix[:,['src_host', 'dest_host']]
for s in subset.iterrows():
    print s
    
for i, row in subset.iterrows():
    print row['src_host']
s = '174.226.132.5'
s.startswith('174')
for i, row in subset.iterrows:
    print row[1]
    
for i, row in subset.iterrows:
    print row['src_host']
    
for i, row in subset.iterrows():
    print row['src_host']
    
for i, row in subset.iterrows():
    print row[1]
    
for i, row in subset.iterrows():
    print row.ix[1]
    
for i, row in subset.iterrows():
    print row.at(0)
    
subset = df.ix[:10,fieldnames]
for i, row in subset.iterrows():
    for ip_type in fieldnames:
        if row[ip_type].startswith('199'):
            src_dest[fieldnames.index(ip_type)].append("Benign")
        else:
            res = ip_lookup(row['src_host'])
            src_dest[fieldnames.index(ip_type)].append(res[0])
fieldnames = ['src_host', 'dest_host']
for i, row in subset.iterrows():
    for ip_type in fieldnames:
        if row[ip_type].startswith('199'):
            src_dest[fieldnames.index(ip_type)].append("Benign")
        else:
            res = ip_lookup(row['src_host'])
            src_dest[fieldnames.index(ip_type)].append(res[0])
src_dest = [[],[]]
src_dest = [[],[]]
fieldnames = ['src_host', 'dest_host']
subset = df.ix[:10,fieldnames]
for i, row in subset.iterrows():
    for ip_type in fieldnames:
        if row[ip_type].startswith('199'):
            src_dest[fieldnames.index(ip_type)].append("Benign")
        else:
            res = ip_lookup(row['src_host'])
            src_dest[fieldnames.index(ip_type)].append(res[0])
src_dest = [[],[]]
fieldnames = ['src_host', 'dest_host']
subset = df.ix[:10,fieldnames]
for i, row in subset.iterrows():
    for ip_type in fieldnames:
        if str(row[ip_type]).startswith('199'):
            src_dest[fieldnames.index(ip_type)].append("Benign")
        else:
            res = ip_lookup(row['src_host'])
            src_dest[fieldnames.index(ip_type)].append(res[0])
src_dest
subset
df.columns
df.ix[:10, 'dest_host']
df.ix[:10, 'src_host']
df.columns
headers
for h in headers:
    h = h.strip()
    
headers
for i in range(len(headers)):
    headers[i] = headers[i].strip()
    
headers
df.columns = headers
df.ix[:10, 'dest_host']
import time
def label_hosts(fname):
    f = open(fname, 'r')
    headers = f.readline().strip().split(',')
    for i in range(len(headers)): headers[i] = headers[i].strip()
    data = [[] for h in headers]
    fields = {headers[i]:i for i in range(len(headers))}
    lines = f.readlines()
    for l in lines:
        lsplit = l.strip().split(',')
        for header in headers:
            data[fields[header]].append(lsplit[fields[header]])
    df = pd.DataFrame(data).transpose()
    df.columns = headers
    src_dest = [[],[]]
    fieldnames = ['src_host', 'dest_host']
    subset = df.ix[:10,fieldnames]
    di = time.time()
    for i, row in subset.iterrows():
        for ip_type in fieldnames:
            if str(row[ip_type]).startswith('199'):
                src_dest[fieldnames.index(ip_type)].append("Benign")
            else:
                res = ip_lookup(row['src_host'])
                src_dest[fieldnames.index(ip_type)].append(res[0])
    df = time.time()
    print "total time: " + str(df-di)
fname = '/Users/babraham/Desktop/pcap/hr_traffic_test.csv'
def label_hosts(fname):
    f = open(fname, 'r')
    headers = f.readline().strip().split(',')
    for i in range(len(headers)): headers[i] = headers[i].strip()
    data = [[] for h in headers]
    fields = {headers[i]:i for i in range(len(headers))}
    lines = f.readlines()
    for l in lines:
        lsplit = l.strip().split(',')
        for header in headers:
            data[fields[header]].append(lsplit[fields[header]])
    df = pd.DataFrame(data).transpose()
    df.columns = headers
    src_dest = [[],[]]
    fieldnames = ['src_host', 'dest_host']
    subset = df.ix[:10,fieldnames]
    di = time.time()
    for i, row in subset.iterrows():
        for ip_type in fieldnames:
            if str(row[ip_type]).startswith('199'):
                src_dest[fieldnames.index(ip_type)].append("Benign")
            else:
                res = ip_lookup(row['src_host'])
                src_dest[fieldnames.index(ip_type)].append(res[0])
    df = time.time()
    print "total time: " + str(df-di)
    return[df, src_dest]
res = label_hosts(fname)
df = res[0]
df.head()
df
def label_hosts(fname):
    f = open(fname, 'r')
    headers = f.readline().strip().split(',')
    for i in range(len(headers)): headers[i] = headers[i].strip()
    data = [[] for h in headers]
    fields = {headers[i]:i for i in range(len(headers))}
    lines = f.readlines()
    for l in lines:
        lsplit = l.strip().split(',')
        for header in headers:
            data[fields[header]].append(lsplit[fields[header]])
    df = pd.DataFrame(data).transpose()
    df.columns = headers
    src_dest = [[],[]]
    fieldnames = ['src_host', 'dest_host']
    subset = df.ix[:10,fieldnames]
    di = time.time()
    for i, row in subset.iterrows():
        for ip_type in fieldnames:
            if str(row[ip_type]).startswith('199'):
                src_dest[fieldnames.index(ip_type)].append("Benign")
            else:
                res = ip_lookup(row['src_host'])
                src_dest[fieldnames.index(ip_type)].append(res[0])
    endtime = time.time()
    print "total time: " + str(endtime-di)
    return[df, src_dest]
res = label_hosts(fname)
res[0]
df = res[0]
cols = res[1]
cols[0]
cols[1]
subset = df[:10,:]
subset = df[:10,]
subset = df.ix[:10,:]
subset['src_labels']= cols[1]
df2 = pd.DataFrame(subset)
subset['src_labels']= cols[1]
subset.columns
subset['dest_labels']= cols[0]
def label_hosts(fname):
    f = open(fname, 'r')
    headers = f.readline().strip().split(',')
    for i in range(len(headers)): headers[i] = headers[i].strip()
    data = [[] for h in headers]
    fields = {headers[i]:i for i in range(len(headers))}
    lines = f.readlines()
    for l in lines:
        lsplit = l.strip().split(',')
        for header in headers:
            data[fields[header]].append(lsplit[fields[header]])
    df = pd.DataFrame(data).transpose()
    df.columns = headers
    src_dest = [[],[]]
    fieldnames = ['src_host', 'dest_host']
    subset = df.ix[:,fieldnames]
    di = time.time()
    for i, row in subset.iterrows():
        for ip_type in fieldnames:
            if str(row[ip_type]).startswith('199'):
                src_dest[fieldnames.index(ip_type)].append("Benign")
            else:
                res = ip_lookup(row['src_host'])
                src_dest[fieldnames.index(ip_type)].append(res[0])
    endtime = time.time()
    print "total time: " + str(endtime-di)
    df['src_labels'] = src_dest[0]
    df['dest_labels'] = src_dest[1]
    return[df]
res - label_hosts(fname)

## ---(Tue Oct 24 20:50:18 2017)---
root_dir = '/Users/babraham/Google Drive/Grad_School/Fall_2017/Comp_Visual_Rec/calorie_counter_data/'
os.chdir(root_dir)
vir_folder = 'Vireo-172-test'
f101_folder = 'food-101-test'
import os

root_dir = '/Users/babraham/Google Drive/Grad_School/Fall_2017/Comp_Visual_Rec/calorie_counter_data/'
os.chdir(root_dir)
vir_folder = 'Vireo-172-test'
f101_folder = 'food-101-test'
os.chdir(vir_folder)
os.chdir(root_dir)
os.listdir(vir_folder)
vir_imgs = os.listdir(vir_folder + '/images/')
vir_imgs
v_list = open(vir_folder + vlist_path, 'r')
vlist_path = '/SplitAndIngreLabel/final_label_list.csv'
v_list = open(vir_folder + vlist_path, 'r')
lines = v_list.readlines()
len(lines)
lines[0]
lines[1]
import pandas as pd
vl_df = pd.DataFrame.from_csv(vir_folder + vlist_path)
vl_df
vl_df = pd.read_csv(vir_folder + vlist_path)
vl_df
vir_folder = 'Vireo-172-test'
vlist_path = '/SplitAndIngreLabel/final_label_list.csv'
f_folder = 'food-101-test'
flist_path = 'meta/classes.txt'
vl_df = pd.read_csv(vir_folder + vlist_path)
fl_df = pd.read_csv(f_folder + flist_path)
flist_path = '/meta/classes.txt'
vir_folder = 'Vireo-172-test'
vlist_path = '/SplitAndIngreLabel/final_label_list.csv'
f_folder = 'food-101-test'
flist_path = 'meta/classes.txt'
vl_df = pd.read_csv(vir_folder + vlist_path)
fl_df = pd.read_csv(f_folder + flist_path)

flist_path = '/meta/classes.txt'
fl_df = pd.read_csv(f_folder + flist_path)
fl_df
fl_df = pd.read_csv(f_folder + flist_path, header=False)
fl_df = open(f_folder + flist_path, 'r')
lines = fl_df.readlines()
lines = [l.strip() for l in lines]
len(lines)
lines
fl_dic = {[(i,l.strip()) for i,l in enumerate(lines)]}
fl_dic = [(i,l.strip()) for i,l in enumerate(lines)]
fl_dic
fd = dict(fl_dic)
fd
fd[100]
fl_dic = dict([(i,l.strip()) for i,l in enumerate(lines)])
vl_df[1:5,:]
vl_df.ix[1:5,:]
vl_df[vl_df['Index'] == 6]
vl_df[vl_df['Index'] == 6]['vireo_172_labels']
str(vl_df[vl_df['Index'] == 6]['vireo_172_labels'])
str(vl_df[vl_df['Index'] == 6]['vireo_172_labels']).value
vl_df[vl_df['Index'] == 6]['vireo_172_labels'].value
vl_file = open(vir_folder + vlist_path, 'r')
lines = vl_file.readlines()
vl_dic = dict([(i,l.strip()) for i,l in enumerate(lines)])
vl_dic
lines = [l.strip().split(',') for l in lines]
vl_dic = dict([(l[0],l[1]) for l in lines])
vl_dic
fl = sorted(fl_dic.values())
fl
v_imgs = os.listdir(vir_folder+'/images/').remove('DS_Store')
v_imgs = os.listdir(vir_folder+'/images/')
v_imgs
vl_dic['120']
v_imgs.remove('.DS_Store')
f_imgs = os.listdir(f_folder+'/images/')
f_imgs.remove('.DS_Store')
f_imgs
combDic = dict()

for f in f_imgs:
    fpath = f_folder + '/' + f
    if f not in combDic:
        combDic[f] = [fpath]
    else:
        combDic[f].append(fpath)
combDic.items()
s1,s2 = set(fl), set(vl_dic.values())
s1.intersection(s2)
revl = dict([(v,k) for k,v in vl_dic.items()])
revl['chicken_wings']
v_imgs = os.listdir(v_folder+'/images/')
v_imgs.remove('.DS_Store')

f_imgs = os.listdir(f_folder+'/images/')
f_imgs.remove('.DS_Store')

combDic = dict()

for f in f_imgs:
    fpath = f_folder + '/' + f
    if f not in combDic: combDic[f] = [fpath]
    else: combDic[f].append(fpath)

for v in v_imgs:
    vname = vl_dic[v]
    vpath = v_folder + '/' + v
    if vname not in combDic: combDic[vname] = [vpath]
    else: combDic[vname].append(vpath)
combDic = dict()

for f in f_imgs:
    fpath = f_folder + '/' + f
    if f not in combDic: combDic[f] = [fpath]
    else: combDic[f].append(fpath)

for v in v_imgs:
    vname = vl_dic[v]
    vpath = v_folder + '/' + v
    if vname not in combDic: combDic[vname] = [vpath]
    else: combDic[vname].append(vpath)
v_folder = 'Vireo-172-test'
combDic = dict()

for f in f_imgs:
    fpath = f_folder + '/' + f
    if f not in combDic: combDic[f] = [fpath]
    else: combDic[f].append(fpath)

for v in v_imgs:
    vname = vl_dic[v]
    vpath = v_folder + '/' + v
    if vname not in combDic: combDic[vname] = [vpath]
    else: combDic[vname].append(vpath)
    
combDic.items()
combDic = dict()

for f in f_imgs:
    fpath = f_folder + '/' + f
    if f not in combDic: combDic[f] = [fpath]
    else: combDic[f].append(fpath)

for v in v_imgs:
    vname = vl_dic[v]
    vpath = v_folder + '/' + v
    if vname not in combDic: combDic[vname] = [vpath]
    else: combDic[vname].append(vpath)
    
combDic.items()
f_imgs
f_imgs = os.listdir(f_folder+'/images/')
f_imgs.remove('.DS_Store')
f_imgs
v_imgs = os.listdir(v_folder+'/images/')
v_imgs.remove('.DS_Store')

f_imgs = os.listdir(f_folder+'/images/')
f_imgs.remove('.DS_Store')

combDic = dict()

for f in f_imgs:
    fpath = f_folder + '/' + f
    if f not in combDic: combDic[f] = [fpath]
    else: combDic[f].append(fpath)

for v in v_imgs:
    vname = vl_dic[v]
    vpath = v_folder + '/' + v
    if vname not in combDic: combDic[vname] = [vpath]
    else: combDic[vname].append(vpath)
combDic.items()
for i,k,v in enumerate(combDic.items()):
    print str(i)
    
enumerate(combDic.items())
newlist = [(i,k) in enumerate(combDic.keys())]
newList
newlist
newlist = [(i,k) for i,k in enumerate(combDic.keys())]
newlist
os.system('mkdir combinedImgs' )
new_dir = 'all_data'
for i, fldr_name in newlist:
    newfolder = new_dir + '/' + str(i)
    os.system('mkdir ' + newfolder)
    for path in combDic[fldr_name]:
        os.system('cp -r ' + path + ' ' + newfolder)
os.system('mkdir ' + new_dir )
for i, fldr_name in newlist:
    newfolder = new_dir + '/' + str(i)
    os.system('mkdir ' + newfolder)
    for path in combDic[fldr_name]:
        os.system('cp -r ' + path + ' ' + newfolder)
for i, fldr_name in newlist:
    newfolder = new_dir + '/' + str(i)
    os.system('mkdir ' + newfolder)
    for path in combDic[fldr_name]:
        cmd = ''''cp -r ' + path + ' ' + newfolder'''
        print(cmd)
        os.system(cmd)
for i, fldr_name in newlist:
    newfolder = new_dir + '/' + str(i)
    os.system('mkdir ' + newfolder)
    for path in combDic[fldr_name]:
        cmd = 'cp -r ' + path + ' ' + newfolder
        print(cmd)
        os.system(cmd)
os.system('mkdir ' + new_dir )
for i, fldr_name in newlist:
    newfolder = new_dir + '/' + str(i)
    os.system('mkdir ' + newfolder)
    for path in combDic[fldr_name]:
        cmd = 'cp -r ' + path + '/ ' + newfolder
        print(cmd)
        os.system(cmd)
combDic = dict()

for f in f_imgs:
    fpath = f_folder + '/images' + f
    if f not in combDic: combDic[f] = [fpath]
    else: combDic[f].append(fpath)

for v in v_imgs:
    vname = vl_dic[v]
    vpath = v_folder + '/images' + v
    if vname not in combDic: combDic[vname] = [vpath]
    else: combDic[vname].append(vpath)

newlist = [(i,k) for i,k in enumerate(combDic.keys())]
os.system('mkdir ' + new_dir )
for i, fldr_name in newlist:
    newfolder = new_dir + '/' + str(i)
    os.system('mkdir ' + newfolder)
    for path in combDic[fldr_name]:
        cmd = 'cp -r ' + path + '/ ' + newfolder
        print(cmd)
        os.system(cmd)
for f in f_imgs:
    fpath = f_folder + '/images/' + f
    if f not in combDic: combDic[f] = [fpath]
    else: combDic[f].append(fpath)

for v in v_imgs:
    vname = vl_dic[v]
    vpath = v_folder + '/images/' + v
    if vname not in combDic: combDic[vname] = [vpath]
    else: combDic[vname].append(vpath)

newlist = [(i,k) for i,k in enumerate(combDic.keys())]
os.system('mkdir ' + new_dir )
for i, fldr_name in newlist:
    newfolder = new_dir + '/' + str(i)
    os.system('mkdir ' + newfolder)
    for path in combDic[fldr_name]:
        cmd = 'cp -r ' + path + '/ ' + newfolder
        print(cmd)
        os.system(cmd)
newfolder='all_data/1'
for j,img in enumerate(os.listdir(newfolder)):
    print(j)
for j,img in enumerate(os.listdir(newfolder)):
    os.system('cp ' + img + ' ' + str(i) + '_' + str(j)+'.jpg')
for j,img in enumerate(os.listdir(newfolder)):
    os.system('mv ' + img + ' ' + str(i) + '_' + str(j)+'.jpg')
for i, fldr_name in newlist:
    newfolder = new_dir + '/' + str(i)
    os.system('mkdir ' + newfolder)
    for path in combDic[fldr_name]:
        cmd = 'cp -r ' + path + '/ ' + newfolder
        print(cmd)
        os.system(cmd)
for j,img in enumerate(os.listdir(newfolder)):
    os.system('mv ' + newfolder + '/' + img + ' ' + newfolder + '/' + str(i) + '_' + str(j)+'.jpg')
newfolder
for i, fldr_name in newlist:
    newfolder = new_dir + '/' + str(i)
    os.system('mkdir ' + newfolder)
    for path in combDic[fldr_name]:
        cmd = 'cp -r ' + path + '/ ' + newfolder
        #print(cmd)
        os.system(cmd)
    print 'renaming files for ' + str(i) + '...'
    for j,img in enumerate(os.listdir(newfolder)):
        os.system('mv ' + newfolder + '/' + img + ' ' + newfolder + '/' + str(i) + '_' + str(j)+'.jpg')
v_folder = 'Vireo-172'
vlist_path = '/SplitAndIngreLabel/final_label_list.csv'
f_folder = 'food-101'
flist_path = '/meta/classes.txt'
new_dir = 'all_data'
runfile('/Users/babraham/Desktop/merge_test.py', wdir='/Users/babraham/Desktop')
fl_file = open(f_folder + flist_path, 'r')
lines = fl_file.readlines()
fl_dic = dict([(i,l.strip()) for i,l in enumerate(lines)])
fl = sorted(fl_dic.values())
vl_file = open(v_folder + vlist_path, 'r')
lines = vl_file.readlines()
lines = [l.strip().split(',') for l in lines]
vl_dic = dict([int((l[0]),l[1]) for l in lines])
fl_file = open(f_folder + flist_path, 'r')
lines = fl_file.readlines()
fl_dic = dict([(i,l.strip()) for i,l in enumerate(lines)])
fl = sorted(fl_dic.values())
vl_file = open(v_folder + vlist_path, 'r')
lines = vl_file.readlines()
lines = [l.strip().split(',') for l in lines]
lines
vl_dic = dict([int((l[0]),l[1]) for l in lines[1:]])
lines[0]
lines[1:]
vl_dic = dict([int((l[0]),l[1]) for l in lines[1:]])
vl_dic = dict([int((l[0]),l[1]) for l in lines[1:3]])
for l in lines[1:3]:
    print(l[0],l[1])
    
for l in lines[1:3]:
    print(int(l[0]),l[1])
    
vl_dic = dict([(int(l[0]),l[1]) for l in lines[1:3]])
vl_dic = dict([(int(l[0]),l[1]) for l in lines[1:]])
runfile('/Users/babraham/Desktop/merge_test.py', wdir='/Users/babraham/Desktop')
vl_dic.keys()
vl_keyset = set(vl_dic.keys())
'104' in vl_keyset
'103' in vl_keyset
for v, vname in vl_dic.items():
    vpath = v_folder + '/images/' + v
    if vname not in combDic: combDic[vname] = [vpath]
    else: combDic[vname].append(vpath)
runfile('/Users/babraham/Desktop/merge_test.py', wdir='/Users/babraham/Desktop')
newlist
df = pd.DataFrame(newlist, columns=['index', 'name'])
df
df.to_csv(new_dir + '/foodList.csv')
os.chdir('all_data')
os.listdir('.')
os.chdir('images')
stats = []
for tup in newlist:
    fld = str(tup[0])
    count = len(os.listdir(fld))
    stats.append((tup[0], tup[1], count))
stats
sdf = pd.DataFrame(stats, columns=['index','category','sampleCount'])
sdf.to_csv('category_stats.csv', index=None)

## ---(Thu Oct 26 13:53:09 2017)---
2^4
import math
math.pow(2,4)
import math

def toBinary(x):
    diff = x
    powlist = []
    while diff != 0:
        power = 0
        while math.pow(2,power) < diff:
            power +=1
        diff -= math.pow(2,power)
        powlist.append((pow))  
    binlist = [[0] for i in range(len(powlist))]
    for p in powlist:
        binlist[len(binlist)-1-p] = 1
    retstr = ""
    for b in binlist: retstr += str(b)
    return retstr
toBinary(16)
def toBinary(x):
    diff = x
    powlist = []
    while diff != 0:
        power = 0
        while math.pow(2,power) < diff:
            power +=1
        diff -= math.pow(2,power)
        powlist.append((pow))  
    binlist = [[0] for i in range(len(powlist))]
    for p in powlist:
        ind = len(binlist) - int(p)
        binlist[ind] = 1
    retstr = ""
    for b in binlist: retstr += str(b)
    return retstr
toBinary(16)
def toBinary(x):
    diff = x
    powlist = []
    while diff != 0:
        power = 0
        while math.pow(2,power) < diff:
            power +=1
        diff -= math.pow(2,power)
        powlist.append((power))  
    binlist = [[0] for i in range(len(powlist))]
    for p in powlist:
        ind = len(binlist) - int(p)
        binlist[ind] = 1
    retstr = ""
    for b in binlist: retstr += str(b)
    return retstr
toBinary(16)
def toBinary(x):
    diff = x
    powlist = []
    while diff != 0:
        power = 0
        while math.pow(2,power) < diff:
            power +=1
        diff -= math.pow(2,power)
        powlist.append((power))  
    binlist = [[0] for i in range(len(powlist))]
    for p in powlist:
        ind = len(binlist) - 1 - int(p)
        binlist[ind] = 1
    retstr = ""
    for b in binlist: retstr += str(b)
    return retstr
toBinary(16)
def toBinary(x):
    diff = x
    powlist = []
    while diff != 0:
        power = 0
        while math.pow(2,power) < diff:
            power +=1
        diff -= math.pow(2,power)
        powlist.append((power))
    print str(powlist)
    binlist = [[0] for i in range(len(powlist))]
    print "binlist: " + str(binlist)
    for p in powlist:
        ind = len(binlist) - 1 - int(p)
        binlist[ind] = 1
    retstr = ""
    for b in binlist: retstr += str(b)
    return retstr
toBinary(16)
plist = [1,2,3]
max(plist)
def toBinary(x):
    diff = x
    powlist = []
    while diff != 0:
        power = 0
        while math.pow(2,power) < diff:
            power +=1
        diff -= math.pow(2,power)
        powlist.append((power))
    print str(powlist)
    binlist = [[0] for i in range(max(powlist))]
    print "binlist: " + str(binlist)
    for p in powlist:
        ind = len(binlist) - 1 - int(p)
        binlist[ind] = 1
    retstr = ""
    for b in binlist: retstr += str(b)
    return retstr
toBinary(16)
runfile('/Users/babraham/Desktop/binary.py', wdir='/Users/babraham/Desktop')
toBinary(16)
runfile('/Users/babraham/Desktop/binary.py', wdir='/Users/babraham/Desktop')
def toBinary(x):
    diff = x
    powlist = []
    while diff != 0:
        power = 0
        while math.pow(2,power) < diff:
            power +=1
        diff -= math.pow(2,power)
        powlist.append((power))
    print str(powlist)
    binlist = [[0] for i in range(max(powlist))]
    print "binlist: " + str(binlist)
    for p in powlist:
        print("p: " + str(p))
        ind = len(binlist) - int(p)
        print "ind: " + str(ind)
        binlist[ind] = [1]
    retstr = ""
    for b in binlist: retstr += str(b[0])
    return retstr
toBinary(16)
toBinary(32)
toBinary(33)
runfile('/Users/babraham/Desktop/binary.py', wdir='/Users/babraham/Desktop')
toBinary(33)
toBinary(82)
runfile('/Users/babraham/Desktop/binary.py', wdir='/Users/babraham/Desktop')
toBinary(82)
runfile('/Users/babraham/Desktop/binary.py', wdir='/Users/babraham/Desktop')
toBinary(82)
runfile('/Users/babraham/Desktop/binary.py', wdir='/Users/babraham/Desktop')
toBinary(82)
def toBinary(x):
    diff = x
    powlist = []
    power = 0
    while diff >= 0:
        while math.pow(2,power) < diff:
            power +=1
            print "pow: " + str(power)
        diff -= math.pow(2,power)
        print str("diff: " + str(diff))
        powlist.append((power))
        power = 0
    print str(powlist)
    binlist = [[0] for i in range(max(powlist))]
    print "binlist: " + str(binlist)
    for p in powlist:
        print("p: " + str(p))
        ind = len(binlist) - int(p)
        print "ind: " + str(ind)
        binlist[ind] = [1]
    retstr = ""
    for b in binlist: retstr += str(b[0])
    return retstr
toBinary(82)
runfile('/Users/babraham/Desktop/binary.py', wdir='/Users/babraham/Desktop')
toBinary(82)
runfile('/Users/babraham/Desktop/binary.py', wdir='/Users/babraham/Desktop')
toBinary(82)
runfile('/Users/babraham/Desktop/binary.py', wdir='/Users/babraham/Desktop')
toBinary(82)
runfile('/Users/babraham/Desktop/binary.py', wdir='/Users/babraham/Desktop')
toBinary(82)
runfile('/Users/babraham/Desktop/binary.py', wdir='/Users/babraham/Desktop')
toBinary(82)
runfile('/Users/babraham/Desktop/binary.py', wdir='/Users/babraham/Desktop')
toBinary(82)
runfile('/Users/babraham/Desktop/binary.py', wdir='/Users/babraham/Desktop')
toBinary(82)
runfile('/Users/babraham/Desktop/binary.py', wdir='/Users/babraham/Desktop')
toBinary(82)
runfile('/Users/babraham/Desktop/binary.py', wdir='/Users/babraham/Desktop')
toBinary(82)
toBinary(129)
runfile('/Users/babraham/Desktop/binary.py', wdir='/Users/babraham/Desktop')
toBinary(129)
runfile('/Users/babraham/Desktop/binary.py', wdir='/Users/babraham/Desktop')
toBinary(129)
res = toBinary(129)
res
len(res)
res = toBinary(72)
res
toBinary(18927)
res = toBinary(18927)
res
res == str(100100111101111)
runfile('/Users/babraham/Desktop/binary.py', wdir='/Users/babraham/Desktop')
res = toBinary(18927)
def toBinRecursive(binstr, power, diff):
    if diff <= 0:
        return binstr
    elif math.pow(2,power) < diff:
        binstr += "0"
        toBinaryRecursive(binstr,power+1,diff)
    else:
        binstr[-1] = "1"
        diff = diff - math.pow(2,power-1)
        toBinaryRecursive(binstr, 0, diff)
runfile('/Users/babraham/Desktop/binary.py', wdir='/Users/babraham/Desktop')
tbr(16)
runfile('/Users/babraham/Desktop/binary.py', wdir='/Users/babraham/Desktop')
tbr(16)
runfile('/Users/babraham/Desktop/binary.py', wdir='/Users/babraham/Desktop')
tbr(16)
runfile('/Users/babraham/Desktop/binary.py', wdir='/Users/babraham/Desktop')
tbr(16)
runfile('/Users/babraham/Desktop/binary.py', wdir='/Users/babraham/Desktop')
tbr(16)
binlist = ['1','0','0']
"".join(binlist)
runfile('/Users/babraham/Desktop/binary.py', wdir='/Users/babraham/Desktop')
tbr(24)
runfile('/Users/babraham/Desktop/binary.py', wdir='/Users/babraham/Desktop')
tbr(24)
runfile('/Users/babraham/Desktop/binary.py', wdir='/Users/babraham/Desktop')
tbr(24)
runfile('/Users/babraham/Desktop/binary.py', wdir='/Users/babraham/Desktop')
tbr(24)
runfile('/Users/babraham/Desktop/binary.py', wdir='/Users/babraham/Desktop')
tbr(24)
runfile('/Users/babraham/Desktop/binary.py', wdir='/Users/babraham/Desktop')
tbr(24)
runfile('/Users/babraham/Desktop/binary.py', wdir='/Users/babraham/Desktop')
tbr(24)
runfile('/Users/babraham/Desktop/binary.py', wdir='/Users/babraham/Desktop')
tbr(24)
l = ['a']
l[1] = 'b'
l.insert('b',1)
l.insert(1,'b')
l
l = ["0" for i in range(8)]
l
runfile('/Users/babraham/Desktop/binary.py', wdir='/Users/babraham/Desktop')
tbr(24)
runfile('/Users/babraham/Desktop/binary.py', wdir='/Users/babraham/Desktop')
tbr(24)
tbr(33)
toBinary(33)
runfile('/Users/babraham/Desktop/binary.py', wdir='/Users/babraham/Desktop')
toBinary(33)
runfile('/Users/babraham/Desktop/binary.py', wdir='/Users/babraham/Desktop')
toBinary(33)
runfile('/Users/babraham/Desktop/binary.py', wdir='/Users/babraham/Desktop')
toBinary(33)
runfile('/Users/babraham/Desktop/binary.py', wdir='/Users/babraham/Desktop')
toBinary(33)
tbr(33)

## ---(Fri Oct 27 00:46:02 2017)---
def test(a, l=[]):
    l.append(a)
    return a

test('b')
test('c')
l1 = test('b')
l2 = test('c')
print str(l1)
print str(l2)
l = [1,2,3,4,5,6]
filter(lambda x: x % 3 == 0, l)
print map(lambda x: x*x*x, l)
s = """isn't it a wonderful day? I'm dreaming."""
map(lambda x: len(x), s.split(' '))
import commands
res = commands.getoutput('cd')
res
res = commands.getoutput('python --version')
res
fdict = {"insert": lambda x,l: l.insert(x), "pop": lambda l: l.pop(-1)}
l = [1,2,3]
l.pop(-1)
fdict['insert']
def applyfn(fn, l, x=None):
    if x is not None: return fn(l,x)
def rev(l):
    ind = len(l)-1
    retlist = []
    while ind >=0:
        retlist.append(l[ind])
        ind -=1
    return retlist
rev([4,7,5])
rev([2])
rev([1,2,3,4,5,6,7,8])
"insert": lambda l,x: l.insert(x),
"pop": lambda l: l.pop(-1),
"remove": lambda l,x: l.remove(x),
"print": lambda l: print(l),
"append": lambda l,x: l.append(x),
"sort": lambda l: sorted(l),
"reverse": lambda l: rev(l)}
fdict = {
        "insert": lambda l,x: l.insert(x),
        "pop": lambda l: l.pop(-1),
        "remove": lambda l,x: l.remove(x),
        #"print": lambda l: print(l),
        "append": lambda l,x: l.append(x),
        "sort": lambda l: sorted(l),
        "reverse": lambda l: rev(l)}
def applyfn(fn, l, x=None):
    if x is not None: return fn(l,x)
    else: return fn(l)
N = int(raw_input())
def main():
    n = int(raw_input())
    counter = 1
    l = []
    fdict = {
            "insert": lambda i,x: l.insert(i,x),
            "pop": lambda : l.pop(-1),
            "remove": lambda x: l.remove(x),
            #"print": lambda : print(l),
            "append": lambda x: l.append(x),
            "sort": lambda : sorted(l),
            "reverse": lambda : rev(l)
            }
    while counter <= n:
        lin = raw_input()
        lsplit = lin.split(' ' )
        if lsplit[0] == "print":
            print(l)
        else:
            fn = fdict[lsplit[0]]
            if len(lsplit) > 2:
                applyfn(fn, int(lsplit[1]),int(lsplit[2]) )
            else: 
                applyfn(fn,int(lsplit[1]))
        counter +=1
main()
def main():
    n = int(raw_input())
    counter = 1
    l = []
    fdict = {
            "insert": lambda i,x: l.insert(i,x),
            "pop": lambda : l.pop(-1),
            "remove": lambda x: l.remove(x),
            #"print": lambda : print(l),
            "append": lambda x: l.append(x),
            "sort": lambda : sorted(l),
            "reverse": lambda : rev(l)
            }
    while counter <= n:
        lin = raw_input()
        lsplit = lin.split(' ' )
        if lsplit[0] == "print":
            print(l)
        elif len(lsplit[0]) == 1:
            applyfn(lsplit[0])
        else:
            fn = fdict[lsplit[0]]
            if len(lsplit) > 2:
                applyfn(fn, int(lsplit[1]),int(lsplit[2]) )
            else: 
                applyfn(fn,int(lsplit[1]))
        counter +=1
main()
def main():
    n = int(raw_input())
    counter = 1
    l = []
    fdict = {
            "insert": lambda i,x: l.insert(i,x),
            "pop": lambda : l.pop(-1),
            "remove": lambda x: l.remove(x),
            #"print": lambda : print(l),
            "append": lambda x: l.append(x),
            "sort": lambda : sorted(l),
            "reverse": lambda : rev(l)
            }
    while counter <= n:
        lin = raw_input()
        lsplit = lin.split(' ')
        print str(lsplit)
        if lsplit[0] == "print":
            print(l)
        elif len(lsplit[0]) == 1:
            applyfn(lsplit[0])
        else:
            fn = fdict[lsplit[0]]
            if len(lsplit) > 2:
                applyfn(fn, int(lsplit[1]),int(lsplit[2]) )
            else: 
                applyfn(fn,int(lsplit[1]))
        counter +=1
main()
def main():
    n = int(raw_input())
    counter = 1
    l = []
    fdict = {
            "insert": lambda i,x: l.insert(i,x),
            "pop": lambda : l.pop(-1),
            "remove": lambda x: l.remove(x),
            #"print": lambda : print(l),
            "append": lambda x: l.append(x),
            "sort": lambda : sorted(l),
            "reverse": lambda : rev(l)
            }
    while counter <= n:
        lin = raw_input()
        lsplit = lin.split(' ')
        print str(lsplit)
        if lsplit[0] == "print":
            print(l)
        elif len(lsplit) == 1:
            applyfn(lsplit[0])
        else:
            fn = fdict[lsplit[0]]
            if len(lsplit) > 2:
                applyfn(fn, int(lsplit[1]),int(lsplit[2]) )
            else: 
                applyfn(fn,int(lsplit[1]))
        counter +=1
main()
def applyfn(fn, x=None, i=None):
    global l
    if x is None: return fn(l)
    elif i is not None: return fn(i,x)
    else: return fn(x)
main()
def main():
    n = int(raw_input())
    counter = 1
    l = []
    fdict = {
            "insert": lambda i,x: l.insert(i,x),
            "pop": lambda : l.pop(-1),
            "remove": lambda x: l.remove(x),
            #"print": lambda : print(l),
            "append": lambda x: l.append(x),
            "sort": lambda : sorted(l),
            "reverse": lambda : rev(l)
            }
    while counter <= n:
        lin = raw_input()
        lsplit = lin.split(' ')
        print str(lsplit)
        if lsplit[0] == "print":
            print(l)
        elif len(lsplit) == 1:
            applyfn(fdict[lsplit[0]])
        else:
            fn = fdict[lsplit[0]]
            if len(lsplit) > 2:
                applyfn(fn, int(lsplit[1]),int(lsplit[2]) )
            else: 
                applyfn(fn,int(lsplit[1]))
        counter +=1
main()
def applyfn(fn, x=None, i=None):
    global l
    if x is None: return fn()
    elif i is not None: return fn(i,x)
    else: return fn(x)
main()
l
def main():
    n = int(raw_input())
    counter = 1
    l = []
    fdict = {
            "insert": lambda i,x: l.insert(i,x),
            "pop": lambda : l.pop(-1),
            "remove": lambda x: l.remove(x),
            #"print": lambda : print(l),
            "append": lambda x: l.append(x),
            "sort": lambda : sorted(l),
            "reverse": lambda : rev(l)
            }
    while counter <= n:
        lin = raw_input()
        lsplit = lin.split(' ')
        if lsplit[0] == "print":
            print(l)
        elif len(lsplit) == 1:
            applyfn(fdict[lsplit[0]])
        else:
            fn = fdict[lsplit[0]]
            if len(lsplit) > 2:
                applyfn(fn, int(lsplit[1]),int(lsplit[2]) )
            else: 
                applyfn(fn,int(lsplit[1]))
        counter +=1
main()
l = [1,5,12,2]
applyfn(fdict['sort'])
eval("sort",[1,3,1,2])

## ---(Sat Oct 28 23:10:41 2017)---
import os
os.getcwd()
data_dir = "/Users/babraham/Google Drive/Grad_School/Fall_2017/Comp_Visual_Rec/calorie_counter_data/"
os.chdir(data_dir)
data_folder = data_dir + "all_data_test"
os.listdir("all_data_test")
data_folder = data_dir + "all_data_test"
os.chdir(data_folder)
os.system("mkdir train")
os.system("mkdir test")
os.listdir("images")
classes = os.listdir("images")
c = classes[0]
os.listdir("images/" + c)
import math
math.random()
math.rand()
import random
random()
print random()
from random import *
random()
from random import random()
from random import random
os.system("mkdir images/train/" + c)
c
os.getcwd()
os.listdir('.')
os.system("mkdir train/" + c)
tr_prop = .75

classes = os.listdir("images")
for c in classes:
    os.system("mkdir train/" + c)
    os.system("mkdir test/" + c)
    files = os.listdir("images/" + c)
    for f in files:
        old = "images/" + c + "/" + f
        r = random()
        if r < tr_prop:
            new = "train/" + c + "/" + f
        else:
            new = "test/" + c + "/" + f
        os.system("mv " + old + " " + new)
classes.remove(".DS_Store")
classes = os.listdir("images")
classes.remove(".DS_Store")
for c in classes:
    os.system("mkdir train/" + c)
    os.system("mkdir test/" + c)
    files = os.listdir("images/" + c)
    files.remove(".DS_Store")
    for f in files:
        old = "images/" + c + "/" + f
        r = random()
        if r < tr_prop:
            new = "train/" + c + "/" + f
        else:
            new = "test/" + c + "/" + f
        os.system("mv " + old + " " + new)
tr_prop = .75
classes = os.listdir("images")
if ".DS_Store" in classes: classes.remove(".DS_Store")

for c in classes:
    os.system("mkdir train/" + c)
    os.system("mkdir test/" + c)
    files = os.listdir("images/" + c)
    if ".DS_Store" in files: files.remove(".DS_Store")
    for f in files:
        old = "images/" + c + "/" + f
        r = random()
        if r < tr_prop:
            new = "train/" + c + "/" + f
        else:
            new = "test/" + c + "/" + f
        os.system("mv " + old + " " + new)
train_list, test_list = [] []
train_list, test_list = [], []
import subprocess as sp
train_list, test_list = [], []
if ".DS_Store" in classes: classes.remove(".DS_Store")

for c in classes:
    os.system("mkdir train/" + c)
    os.system("mkdir test/" + c)
    files = os.listdir("images/" + c)
    if ".DS_Store" in files: files.remove(".DS_Store")
    for f in files:
        old = "images/" + c + "/" + f
        r = random()
        if r < tr_prop:
            new = "train/" + c + "/" + f
            train_list.append(new)
        else:
            new = "test/" + c + "/" + f
            test_list.append(new)
        os.system("mv " + old + " " + new)
os.path.isfile("train")
os.path.isfile("./train")
os.getcwd()
os.path.isdir("train")
if os.path.isdir("./train"): os.system("rm -R train")

if os.path.isdir("./test"): os.system("rm -R test")
os.system("mkdir train")
os.system("mkdir val")
tr_prop = .75
classes = os.listdir("images")
train_list, test_list = [], []
if ".DS_Store" in classes: classes.remove(".DS_Store")

for c in classes:
    os.system("mkdir train/" + c)
    os.system("mkdir val/" + c)
    files = os.listdir("images/" + c)
    if ".DS_Store" in files: files.remove(".DS_Store")
    for f in files:
        old = "images/" + c + "/" + f
        r = random()
        if r < tr_prop:
            new = "train/" + c + "/" + f
            train_list.append(new)
        else:
            new = "val/" + c + "/" + f
            test_list.append(new)
        os.system("mv " + old + " " + new)
train_list
os.getcwd()
os.chdir(data_folder)
os.system("mkdir train")
os.system("mkdir val")
tr_prop = .75
classes = os.listdir("images")
train_list, test_list = [], []
if ".DS_Store" in classes: classes.remove(".DS_Store")

for c in classes:
    os.system("mkdir train/" + c)
    os.system("mkdir val/" + c)
    files = os.listdir("images/" + c)
    if ".DS_Store" in files: files.remove(".DS_Store")
    for f in files:
        old = "images/" + c + "/" + f
        r = random()
        if r < tr_prop:
            new = "train/" + c + "/" + f
            train_list.append(new)
        else:
            new = "val/" + c + "/" + f
            test_list.append(new)
        os.system("mv " + old + " " + new)
        
len(train_list)
len(test_list)
270/5
990*54
3088*54
from __future__ import with_statement
for t in ['train', 'test']:
    print t
    
datalists = [("train_list", train_list), ("val_list",val_list)]
for i in range(2):
    fname, data = datalists[i]
    with open(fname, 'r') as out:
        for d in data: out.write(d + "\n")
val_list
train_list
os.system("mkdir train")
os.system("mkdir val")
tr_prop = .75
classes = os.listdir("images")
train_list, val_list = [], []
if ".DS_Store" in classes: classes.remove(".DS_Store")

for c in classes:
    os.system("mkdir train/" + c)
    os.system("mkdir val/" + c)
    files = os.listdir("images/" + c)
    if ".DS_Store" in files: files.remove(".DS_Store")
    for f in files:
        old = "images/" + c + "/" + f
        r = random()
        if r < tr_prop:
            new = "train/" + c + "/" + f
            train_list.append(new)
        else:
            new = "val/" + c + "/" + f
            val_list.append(new)
        os.system("mv " + old + " " + new)

datalists = [("train_list", train_list), ("val_list",val_list)]
for i in range(2):
    fname, data = datalists[i]
    with open(fname, 'r') as out:
        for d in data: out.write(d + "\n")
len(val_list)
len(train_list)
os.getcwd()
if ".DS_Store" in classes: classes.remove(".DS_Store")

for c in classes:
    os.system("mkdir train/" + c)
    os.system("mkdir val/" + c)
    files = os.listdir("images/" + c)
    if ".DS_Store" in files: files.remove(".DS_Store")
    for f in files:
        old = "images/" + c + "/" + f
        r = random()
        if r < tr_prop:
            new = "train/" + c + "/" + f
            train_list.append(new)
        else:
            new = "val/" + c + "/" + f
            val_list.append(new)
        os.system("mv " + old + " " + new)

datalists = [("train_list", train_list), ("val_list",val_list)]
os.listdir("images")
os.system("mkdir train")
os.system("mkdir val")
tr_prop = .75
classes = os.listdir("images")
train_list, val_list = [], []
if ".DS_Store" in classes: classes.remove(".DS_Store")

for c in classes:
    os.system("mkdir train/" + c)
    os.system("mkdir val/" + c)
    files = os.listdir("images/" + c)
    if ".DS_Store" in files: files.remove(".DS_Store")
    for f in files:
        old = "images/" + c + "/" + f
        r = random()
        if r < tr_prop:
            new = "train/" + c + "/" + f
            train_list.append(new)
        else:
            new = "val/" + c + "/" + f
            val_list.append(new)
        os.system("mv " + old + " " + new)

datalists = [("train_list", train_list), ("val_list",val_list)]
for i in range(2):
    fname, data = datalists[i]
    with open(fname + ".txt", 'r') as out:
        for d in data: out.write(d + "\n")
for i in range(2):
    fname, data = datalists[i]
    with open(fname + ".txt", 'w') as out:
        for d in data: out.write(d + "\n")
runfile('/Users/babraham/Google Drive/Grad_School/Fall_2017/Comp_Visual_Rec/calorie_counter_data/make_train_test.py', wdir='/Users/babraham/Google Drive/Grad_School/Fall_2017/Comp_Visual_Rec/calorie_counter_data')
td = {"Jordan": 23, "Bryant": 8, "Pippen": 33}
td.get("Jordan")
td.get("Jordan",0)
td.get("Jordan",1)
import torch
test = torch.LongTensor(1,1)
test
test = torch.LongTensor([1,2,3,4],[5,6,7,8])
test = torch.LongTensor([[1,2],[3,4]])
test
import torch, json, string
import torch.nn as nn
import torch.autograd
from torch.autograd import Variable
import torch.utils.data as data
import numpy as np
from nltk.tokenize import word_tokenize

embedding = nn.Embedding(10, 3)
embedding
dir(embedding)
input = Variable(torch.LongTensor([[1,2,4,5],[4,3,2,9]]))
res = embedding(input)
input
res
res.shape
res.dim
res.dim()
res[0]
len(res)
res[1]
embedding([1,2,4,5])
in2 = Variable(torch.LongTensor([1,2,4,5]))
embedding(in2)
res[0]
t1 = torch.Tensor([[1,2]])
t2 = torch.Tensor([[3,4]])
res = torch.stack(t1,t2)
imgIds = (19927, 110724, 447113, 521386, 535732, 419211, 520422, 327804, 389654, 220735, 40874, 550369, 383640, 330901, 559464, 402833, 415429, 380724, 479658, 158718, 69971, 159338, 534889, 14089, 351719, 154478, 82650, 191785, 391145, 358104, 425881, 134819, 121718, 357301, 113879, 524314, 208251, 393721, 281713, 187131, 411485, 416570, 429949, 293246, 370831, 71526, 155448, 549133, 186323, 266880, 522013, 72583, 134113, 125259, 294850, 200500, 70913, 43206, 6422, 570268, 511967, 339355, 536896, 276128, 469339, 260135, 287399, 414853, 326377, 388853, 23811, 374005, 563280, 363214, 574770, 125321, 344520, 87977, 197888, 497245, 261750, 270759, 563921, 527507, 136970, 41305, 299923, 387599, 109521, 112899, 406753, 278753, 20253, 351979, 198360, 80742, 356174, 343942, 173791, 409570, 112137, 266366, 166657, 46267, 371705, 431526, 264676, 190942, 120462, 560242, 66385, 63330, 417679, 574673, 488207, 491249, 475453, 359073, 253430, 282228, 353138, 188725, 283479, 180324, 573520, 138207, 450509, 448461)
seqLengths = (29, 26, 25, 24, 21, 20, 19, 19, 18, 18, 18, 18, 18, 17, 17, 17, 17, 17, 17, 16, 16, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 10, 10)
"""
Created on Sun Oct 29 19:26:34 2017

@author: babraham
"""

ps = """
 
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
 5001
[torch.LongTensor of size 128]
    
    
    1
    1
    1
    1
   14
    1
   14
    1
    1
    1
    1
    1
    5
    1
    1
    1
    1
   10
    5
    1
    1
    1
    1
   64
    1
    1
   13
   64
  832
   14
    1
    1
    1
    1
   14
    1
   13
   14
   64
    1
 2545
    1
    1
   14
    1
    1
    1
    1
    5
   59
   36
   14
    1
    1
    1
    5
  234
    1
    1
    1
   14
  152
 2006
    1
   13
    1
    1
    1
    1
    1
   93
   64
    5
    1
   14
    1
  214
   14
   14
    1
   14
    1
   14
    1
    1
   13
   14
    1
    1
    1
    1
    1
    1
    5
   24
    1
    1
 3876
    1
   14
    1
    1
   14
   14
   93
    1
   14
    1
    1
    1
   18
    1
    1
    1
 1814
   14
    1
    1
    1
  140
    1
  412
    1
   64
  365
  431
    1
   13
[torch.LongTensor of size 128]
  
  
  333
  152
  394
   28
   29
   29
   18
  252
   29
  178
   22
   28
 4648
   21
  238
   22
   22
   16
  663
  124
   46
   10
   23
    9
   22
   48
  190
    9
  885
  196
  100
 5002
   28
   10
  467
   73
  190
  269
    9
  537
    8
   10
  276
  196
  200
   33
   33
  116
   29
  129
  238
  600
   44
   48
   33
   78
   79
   10
  179
  340
   38
   17
  233
   50
  430
  331
   76
   33
   21
   10
  265
   19
   44
   22
 1242
   44
   17
 1481
  667
  906
   79
  417
   41
 1699
   76
  225
  266
   46
   10
   76
   33
  181
  267
  752
   58
 2681
  727
  176
  123
  430
  116
  100
   79
   41
   18
  563
 5002
   78
 2567
   33
   19
   61
   10
   42
   19
 3202
   28
  116
   76
  179
   57
  285
   36
   19
    4
    3
  352
  143
[torch.LongTensor of size 128]
    
    
    7
  260
    4
    6
  607
   33
   19
    7
   65
    7
    6
    9
    4
 2382
    4
   45
 1074
   56
   19
  287
 2532
   26
    7
    1
   16
  152
  123
    1
    8
   12
    4
  225
    3
    6
   12
    7
    8
  321
    1
    7
  657
    9
    4
   16
  346
    4
    4
   16
  678
    6
    4
  310
    9
  267
    4
    9
    8
   12
   16
    7
  330
    1
  100
    6
   10
    9
    4
    4
   50
  280
   19
   14
 1034
    6
    4
    7
    1
   19
  227
  181
   16
   44
  193
    3
    4
    4
  312
  407
    6
    4
    4
   66
    9
   19
    6
   89
   99
  113
   12
  186
   25
    4
  369
  162
   45
   12
    6
    8
   35
    4
 1299
  252
    7
  145
   35
  196
  167
   16
    4
   53
  413
    1
  996
  135
   18
  228
  157
   90
[torch.LongTensor of size 128]
  
  
  727
    1
  353
    1
   19
    4
    6
    1
  300
    1
    1
  306
   14
  333
  949
    1
   13
    1
   12
   86
    3
   39
  603
   48
   20
    9
    7
   59
 3844
    3
    1
    4
    1
    1
    3
 5002
   21
   19
  367
  256
    3
   26
  254
  106
  969
   18
   18
   49
    4
   41
  109
  176
  274
   16
   18
  538
   14
    6
    3
    1
   16
  483
    4
    1
   26
 1923
   79
   18
    6
   92
  474
   18
    1
   21
   18
  643
 4981
    6
    3
    8
   92
   17
 1909
   32
  597
    1
   19
    3
   21
   18
   18
    3
  628
 4785
   40
   45
    9
   12
    3
  535
    9
    1
    6
  451
   13
    3
   38
    1
   21
   18
   80
   53
    1
    7
    8
   16
  146
   49
   98
 1447
  414
  116
   57
  242
  142
    7
   31
  216
[torch.LongTensor of size 128]
   
   
   99
  758
 1348
  112
  528
   18
   40
 5002
    7
  112
  112
  223
  607
 1009
  109
  110
 3211
   91
  243
   11
    1
  176
    4
   10
   11
 1113
    1
   82
  451
    5
   50
    1
   72
   41
  169
 2974
   50
    6
  331
  201
   32
    1
  126
  243
   12
  310
   12
    1
  728
    8
    3
  618
   31
  806
   12
 1098
  186
   39
   32
  604
   20
  850
    1
  124
    1
   92
   26
   12
    1
   13
   81
   55
  148
   26
   56
    9
    7
    5
    1
  166
    1
   13
 1951
    4
   19
  581
   71
    1
  401
   55
   25
    5
   87
  101
    4
   39
   55
    3
   32
  193
   12
 3212
 2701
  503
  136
    1
 2758
   94
  714
  199
   13
   93
  158
 3172
  257
   20
    1
    1
  571
 3321
   15
    6
    6
   55
  493
   72
  224
    6
[torch.LongTensor of size 128]
 
 
 2702
    4
   80
  189
    3
    3
    4
    4
  210
 1929
 1605
   11
  199
 1109
   12
   20
   11
   54
    5
    1
  804
  113
  780
    3
    1
   11
 2481
    8
  503
   62
    3
   10
  114
 1125
    8
    3
  407
    1
   12
    8
    4
   36
   25
    5
    3
 1270
  106
  200
 1946
   21
 1956
  646
    5
   69
    3
  257
   12
 1184
    4
    4
   11
 1294
   29
 1116
  371
    1
  708
  153
  502
  525
  354
   31
   17
   13
  303
  561
    1
   61
  324
  119
  335
  277
   13
    1
   66
  131
   17
   46
  236
  241
   19
  753
 1516
  571
    1
  110
    3
   13
    4
  104
   37
  358
 1917
  134
  104
  102
   80
   16
    6
    3
   86
 1443
   16
 4323
  337
   11
  149
   98
    7
    3
  115
    1
 2863
    3
  184
    8
    4
    1
[torch.LongTensor of size 128]
    
    
    8
  602
  302
    9
    1
    1
    1
  192
    9
   71
  400
  309
    6
  112
    3
   11
   68
    8
  687
  216
   54
    6
   15
    5
   10
  254
    3
    1
  869
  119
    5
   16
    9
    7
   23
   27
  160
  329
   17
    1
   23
 1006
   19
  173
    1
  571
    1
  131
  649
  163
   15
   20
  202
  242
  558
  613
    3
  209
    1
 3235
  133
  150
 5002
 4084
    3
 1020
  590
   17
  134
    4
   92
    5
    5
  129
  247
  104
   36
  257
  146
    4
  310
   44
 1083
   70
   20
    7
    1
   73
   20
    1
 4139
   17
    6
   11
  526
  490
    1
  132
 4193
    1
    1
  433
  704
    6
 1760
  628
    5
   56
    1
    1
  296
    3
   20
    8
 1098
  105
  145
  184
   30
  155
   15
  395
    4
    1
    7
 1237
    1
 1809
[torch.LongTensor of size 128]
    
    
    1
   54
 1530
   16
   84
  211
 1008
 1443
  975
   31
   49
    1
    1
 1412
   32
    1
    4
  307
   25
    3
  187
    5
   65
   38
    6
   31
   27
   21
  239
    4
   68
   20
  258
    1
    7
    3
    4
  380
    5
 2283
    7
  164
    6
    8
   72
    6
   29
    6
  544
    4
    7
   11
    3
    6
 1724
    3
   14
  671
   62
    8
   69
    1
 3251
    1
   39
    4
  134
    1
    6
    1
    5
   24
   44
   17
    5
    1
  166
  101
  398
    1
  101
  229
  103
    8
   11
  213
   36
    3
   11
  559
   30
   13
   13
    5
  175
    1
  530
  107
 5002
   34
  131
   63
  193
 4149
  622
 1102
   74
   38
   29
   68
  831
   27
   11
  210
 2997
  187
    7
  119
  588
  858
    8
  506
 3970
   24
  288
  128
  262
    0
[torch.LongTensor of size 128]
 
 
 2155
    1
   19
    3
    7
  224
   15
    8
   11
   54
 5002
   74
  205
    8
    4
   10
    1
    8
   53
   32
   97
  121
    8
  151
   40
    1
    8
  115
 2350
    1
    4
   11
    6
   21
  609
    1
    1
    7
   32
  380
  715
    6
    5
    5
  134
    1
   98
    1
   11
  301
    1
    1
    1
    1
    6
   39
  192
   49
  134
   69
    3
 5002
   35
   59
  638
  652
    6
  573
 1021
  166
   51
    7
  229
  338
  217
  229
    6
 5002
  817
   29
  618
  148
  119
    1
  133
    3
  267
    5
  128
   75
  265
  284
  396
   51
   70
 1658
    2
    2
 2473
    2
    2
    2
    2
    2
    2
    2
    2
    2
   57
  342
    2
    2
  131
    2
    2
    2
  265
    2
    2
    2
   82
    0
    0
    0
    0
    0
    0
    0
[torch.LongTensor of size 128]
   
   
   25
   22
 3797
    1
    5
   81
    8
 1686
  799
    3
 1570
    7
  198
 5002
    1
    3
   46
   10
 1022
    4
    3
  233
 1082
   56
    4
 5002
    1
    6
    4
  488
    1
    1
    5
  189
  353
   98
   57
   30
    4
    7
    6
    5
  121
   83
  794
 1604
   23
  220
 1628
    4
  466
 2420
 2694
  264
  177
   85
  612
    1
   34
  357
    1
 2310
   17
   51
   68
  851
 1513
   23
    2
  853
    2
  288
    2
    2
    2
    2
  159
    2
    2
   83
    2
    2
    2
   44
   69
   27
    2
  197
    2
    2
    2
    2
    2
    2
    2
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
[torch.LongTensor of size 128]
   
   
   53
 4035
  424
  249
 1935
  265
  351
    3
  150
    1
    3
    1
    7
  820
   21
    1
  126
  227
    3
    1
    1
    1
    4
    1
  109
  228
  158
  140
  308
  396
  252
   22
  121
  146
 1348
  197
  115
 1364
    1
 2191
  139
   62
    2
    2
    2
    2
    2
   84
    2
   18
    2
    2
    2
    2
    2
    2
    2
  267
    2
    2
  151
    2
  338
  385
    2
    2
    2
    2
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
[torch.LongTensor of size 128]
  
  
  135
    5
   35
   26
   71
    6
   11
    5
    5
  131
    5
   38
   18
 1502
   42
  130
  235
  285
   27
   70
   73
  100
 2093
   91
    2
    2
    2
   57
    2
    2
    2
    2
    2
   27
    2
    2
    2
    2
  355
    2
  103
    2
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
[torch.LongTensor of size 128]
 
 
 1637
  602
    3
    1
   17
    5
  799
  852
  281
  553
  113
  207
  683
    2
    2
    2
    2
    2
    2
    2
    2
    2
    2
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
[torch.LongTensor of size 128]
   
   
   8
   3
   1
  51
 253
 149
 236
   2
   2
   2
   2
   2
   2
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
   0
[torch.LongTensor of size 128]
    
    
    1
 2128
   23
  254
    2
    2
    2
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
[torch.LongTensor of size 128]
 
 
 5002
    2
    2
    2
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
[torch.LongTensor of size 128]
 
 
 1912
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
[torch.LongTensor of size 128]
 
 
 3
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
[torch.LongTensor of size 128]
 
 
 32
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
  0
[torch.LongTensor of size 128]
 
 
 2
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
[torch.LongTensor of size 128]
 
 
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
[torch.LongTensor of size 128]

"""
imgIds = (134673, 267266, 100926, 382958, 343818, 41079, 248733, 477321, 210680, 74477, 107138, 58601, 41233, 319613, 441199, 141251, 295931, 544032, 32403, 518023, 532718, 445088, 289282, 213933, 345578, 293090, 313957, 151054, 464498, 188727, 572754, 156757, 105237, 299259, 495692, 119207, 151567, 192710, 277406, 94518, 501418, 432947, 193781, 127204, 381315, 501917, 522862, 457194, 392170, 17945, 481889, 117973, 6765, 481428, 64170, 430615, 394554, 288578, 9988, 84314, 361930, 119560, 485598, 162206, 366500, 83605, 292127, 341455, 471988, 82901, 194664, 159324, 366839, 275008, 435161, 556722, 305235, 183218, 139839, 538947, 117973, 204700, 572353, 480153, 136736, 295941, 507322, 499930, 418091, 113393, 523334, 89092, 568654, 365738, 359472, 359308, 441906, 553126, 95879, 148860, 545526, 410946, 411937, 458654, 542343, 451101, 350170, 291540, 113660, 119604, 398535, 311895, 259420, 286962, 542200, 362062, 2963, 158088, 121184, 101684, 101106, 165077, 173883, 208372, 74902, 168145, 540479, 200489)
seqLens = (22, 18, 18, 18, 17, 17, 17, 16, 16, 16, 16, 16, 16, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 10, 10, 10, 10, 10, 10, 9)
ps
import re
ps = re.sub('\\n', '', ps)
ps
paddedSeqs = re.split('[torch.LongTensor of size 128', ps)
paddedSeqs = re.split("""[torch.LongTensor of size 128""", ps)
paddedSeqs = re.split("""\[torch.LongTensor of size 128""", ps)
len(paddedSeqs)
pseqs = paddedSeqs
pseqs[0]
pseqs = [l.strip().split(' ') for l in pseqs]
pseqs[0]
pseqs = [int(l.strip().split(' ')) for l in pseqs]
pseqs = [int(l.strip().split(' ')) for l in paddedSeqs]
paddedSeqs[0]
pseqs = [[int(s) for s in seq] for seq in pseqs]
paddedSeqs = [re.sub('\]','',l) for l in paddedSeqs]
pseqs = [[int(s) for s in seq] for seq in pseqs]
paddedSeqs
paddedSeqs = paddedSeqs[:len(paddedSeqs) -1]
paddedSeqs
pseqs = [l.strip().split(' ') for l in pseqs]
pseqs = [l.strip().split(' ') for l in paddedSeqs]
pseqs
pseqs = [[int(p) for p in seq] for seq in pseqs]
pseqs = for seqs in pseqs:
for seq in pseqs:
    for p in seq:
        try:
            p = int(p)
        except:
            pass
        
pseqs
for i in range(len(pseqs)):
    for j in range(len(pseqs[i])):
        try:
            pseqs[i][j] = int(pseqs[i][j])
        except:
            pass
        
pseqs
import torch
padSeq = torch.LongTensor(pseqs)
p = pseq[0]
p = pseqs[0]
p
p = torch.LongTensor(p)
p
print p
p.view(-1,p.size(1))
p.view(-1)
p.view([128,1])
p.view([1,128])
print p.view([1,128])
len(p)
for p in pseqs:
    if len(p) > 128:
        print str(len(p)) + " at index " + str(pseqs.index(p))
        
pseqs[19]
pseqs[19][1:3]
ptest = pseqs[19][1:3].remove('')
ptest
ptest = pseqs[19].remove('')
ptest
len(ptest)
pseqs[19]
p2 = filter(lambda x:len(x) > 0, pseqs[19])
p2 = filter(lambda x:len(str(x)) > 0, pseqs[19])
p2
len(p2)
pseqs2 = [filter(lambda x:len(str(x)) > 0, seq) for seq in pseqs]
padSeq = torch.LongTensor(pseqs2)
packed = torch.pack_padded_seq(pseqs2, seqLens)
packed = torch.pack_padded_sequence(pseqs2, seqLens)
packed = torch.nn.utils.rnn.pack_padded_sequence(pseqs2, seqLens)
packed = torch.nn.utils.rnn.pack_padded_sequence(padSeq, seqLens)
packed
padSeq.select(1, 1)
p = padSeq.select(1, 1)
p.data
list(p)
def getTargets(inputTensor):
    tlist = list(inputTensor)
    tlist.insert(0,5001)
    tlist.pop()
    return torch.Tensor(tlist)
getTargets(p)
pt = getTargets(p)
p[0]
t[0]
pt[0]
p[1:5]
pt[1:5]

## ---(Tue Oct 31 00:00:55 2017)---
import re
import pandas as pd
import mechanize as mech
import time
br = browser
br = mech.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Firefox')]
br.open("http://www.myfitnesspal.com/food/search")
br.forms
for f in br.forms:
    print f
    
br.select_form(nr=0)
for f in br.forms():
    print f
    
len(br.forms())
for f in br.forms():
    print f.name
    
br.form = list(br.forms())[0]
br.form
for controls in br.form.form.controls:
    print controls
    
bform = list(br.forms())[0]
for c in bform.controls:
    print c
    
for c in bform.controls:
    print c.encode('utf-8')
    
for c in bform.controls:
    print c.name.encode('utf-8')
    
print br.select_form(name="search")
bform['search']
br.form['search']
br.form['search'] = 'cheeseburger'
resp = br.submit()
page = resp.get_data()
page
res = re.findall("""<div class="nugrition_info">(.*?)</div>""", page)
res
res = re.findall("""<div class="nugritional_info">(.*?)</div>""", page)
res
res = re.findall("""<div class="nutritional_info">(.*?)</div>""", page)
res
res = re.findall("""<div.*?class="nutritional_info">(.*?)</div>""", page)
res
res = re.findall("""class="nutritional_info">\n\t\t\t\t\t<label>.*?</div>""", page)
res
re.findall('dynamicyield', page)
re.findall('nutritional_info', page)
re.findall('nutritional_info>.*?</div>', page)
re.findall('nutritional_info.*?</div>', page)
re.findall('nutritional_info.*</div>', page)
re.findall("""<div.*?>.*?</div>""")
re.findall("""<div.*?>.*?</div>""", page)
re.findall("Calorie", page)
re.findall("Calorie.*?</label>", page)
re.findall("Calorie.*?<label>", page)
re.findall("Calorie.*?</label>.*?<label>", page)
br.div
import BeautifulSoup as bs4
from bs4 import BeautifulSoup
import bs4
import bs4
import bs4 import BeautifulSoup
from bs4 import BeautifulSoup
bs = BeautifulSoup(page)
    br = mech.Browser()
    br.set_handle_robots(False)
    br.addheaders = [('User-agent', 'Firefox')]
br.open("http://www.myfitnesspal.com/food/search")
br.select_form(nr=0)
br.form['search'] = 'cheeseburger'
resp = br.submit()
page = resp.get_data()
import mechanize as mech
import re
    br = mech.Browser()
    br.set_handle_robots(False)
    br.addheaders = [('User-agent', 'Firefox')]
br.open("http://www.myfitnesspal.com/food/search")
br.select_form(nr=0)
br.form['search'] = 'cheeseburger'
resp = br.submit()
page = resp.get_data()
bs = BeautifulSoup(page)
ul = bs.find('div')
ul
len(ul)
bs
bs.find(name="nutritional_info")
bs.find('label')
bs.find_all(attrs={"name:" "nutritional_info"})
bs.find_all(attrs={"class:" "nutritional_info"})
bs.find_all(name='div')
res = bs.find_all(name='div')
len(res)
r = res[0]
r
r.id
dir(r)
r.name
r.class
r.text
r.attrs
for r in res[1:5]:
    print r.attrs
    
for r in res[1:20]:
    print r.attrs
    
for r in res:
    print r.attrs
    
for r in res:
    if "nutrition" in r.class:
r
r[0]
r = res[1]
r
r.attrs
r.attrs['class']
for r in res:
    if 'nutrition' in r.attrs['class']:
        print r.attrs
        
for r in res:
    try:
        if 'nutrition' in r.attrs['class']:
            print r.attrs
    except:
        pass
    
r.attrs['class']
r.attrs['class'][0]
divs = bs.findall('div')
divs = bs.find_all('div')
reslist = []
for d in div:
    try:
        if 'nutrition' in d.attrs['class'][0]:
            reslist.append(d.text)
    except:
        pass
    
for d in divs:
    try:
        if 'nutrition' in d.attrs['class'][0]:
            reslist.append(d.text)
    except:
        pass
    
len(reslist)
for r in reslist:
    print r
    
for d in divs:
    try:
        if 'nutrition' in d.attrs['class'][0]:
            reslist.append(d.text)
    except:
        pass
    
len(reslist)
reslist[0]
res = re.findall(':.*?,', reslist[0])
res
r = reslist[0]
re.sub('\\n', '')
re.sub('\\n', '', r)
re.sub('\\[a-z]', '', r)
re.sub(['\\n','\\t'], '', r)
reslist = []
divs = bs.find_all('div')
for d in divs:
    try:
        if 'nutrition' in d.attrs['class'][0]:
            text = d.text
            text = re.sub('\\n', '', text)
            text = re.sub('\\t', '', text)
            reslist.append(text)
    except: pass
len(reslist)
for r in reslist:
    print r
    
r
calories = re.findall('[cC]alories: (.*?),', r)
calories
ssize = re.findall('[sS]erving [sSize]: (.*?) ', r)
ssize
ssize = re.findall('[sS]erving [sS]ize: (.*?) ', r)
ssize
calories = re.findall('[cC]alories: (.*?),', text)
ssize = re.findall('[sS]erving [sS]ize: (.*?) ', text)
fat = re.findall('[fF]at: (.*?),', text)
carbs = re.findall('[cC]arbs: (.*?),', text)
protein = re.findall('[pP]rotein: (.*?),', text)
calories, ssize, fat, carbs, protein
protein = re.findall('[pP]rotein: (.*?)', text)
protein
protein = re.findall('[pP]rotein: (.*?)', r)
protein
r
protein = re.findall('[pP]rotein:.*?(.*?)', r)
protein
protein = re.findall('[pP]rotein:  (.*?)', r)
protein
tup = zip([r[0] for r in [calories, ssize, fat, carbs]])
tup
reslist = []
divs = bs.find_all('div')
carbs, ssizes, fats, cals = [],[],[],[]
for d in divs:
    try:
        if 'nutrition' in d.attrs['class'][0]:
            text = d.text
            text = re.sub('\\n', '', text)
            text = re.sub('\\t', '', text)
            cals.append(re.findall('[cC]alories: (.*?),', text)[0])
            ssizes.append(re.findall('[sS]erving [sS]ize: (.*?) ', text)[0])
            fats.append(re.findall('[fF]at: (.*?),', text)[0])
            carbs.append(re.findall('[cC]arbs: (.*?),', text)[0])
            #protein = re.findall('[pP]rotein:  (.*?)', r)
            #tup = zip([r[0] for r in [calories, ssize, fat, carbs]])
            
            reslist.append(text)
reslist = []
divs = bs.find_all('div')
carbs, ssizes, fats, cals = [],[],[],[]
for d in divs:
    try:
        if 'nutrition' in d.attrs['class'][0]:
            text = d.text
            text = re.sub('\\n', '', text)
            text = re.sub('\\t', '', text)
            cals.append(re.findall('[cC]alories: (.*?),', text)[0])
            ssizes.append(re.findall('[sS]erving [sS]ize: (.*?) ', text)[0])
            fats.append(re.findall('[fF]at: (.*?),', text)[0])
            carbs.append(re.findall('[cC]arbs: (.*?),', text)[0])
            #protein = re.findall('[pP]rotein:  (.*?)', r)
            #tup = zip([r[0] for r in [calories, ssize, fat, carbs]])
            reslist.append(text)
reslist = []
divs = bs.find_all('div')
carbs, ssizes, fats, cals = [],[],[],[]
for d in divs:
    try:
        if 'nutrition' in d.attrs['class'][0]:
            text = d.text
            text = re.sub('\\n', '', text)
            text = re.sub('\\t', '', text)
            cals.append(re.findall('[cC]alories: (.*?),', text)[0])
            ssizes.append(re.findall('[sS]erving [sS]ize: (.*?) ', text)[0])
            fats.append(re.findall('[fF]at: (.*?),', text)[0])
            carbs.append(re.findall('[cC]arbs: (.*?),', text)[0])
            #protein = re.findall('[pP]rotein:  (.*?)', r)
            #tup = zip([r[0] for r in [calories, ssize, fat, carbs]])
    except: pass
len(carbs)
zip(ssizes, carbs, fats, cals)
cals.append(re.findall('[cC]alories: (.*?),', r)[0].decode('utf-8))
resdf = pd.DataFrame(zip(ssizes, carbs, fats, cals), columns=['ssizes', 'carbs', 'fat', 'calories'])
import pandas as pd
resdf = pd.DataFrame(zip(ssizes, carbs, fats, cals), columns=['ssizes', 'carbs', 'fat', 'calories'])
resdf
resdf['calories'].mean()
int(re.findall('[cC]arbs: (.*?),', r)[0])
carbsres = re.findall('[cC]arbs: (.*?),', r)
r
r = reslist[0]
reslist = []
divs = bs.find_all('div')
carbs, ssizes, fats, cals = [],[],[],[]
for d in divs:
    try:
        if 'nutrition' in d.attrs['class'][0]:
            text = d.text
            text = re.sub('\\n', '', text)
            text = re.sub('\\t', '', text)
            cals.append(int(re.findall('[cC]alories: (.*?),', text)[0]))
            ssizes.append(re.findall('[sS]erving [sS]ize: (.*?) ', text)[0])
            fats.append(re.findall('[fF]at: (.*?),', text)[0])
            carbsres = re.findall('[cC]arbs: (.*?),', text)
            reslist.append(text)
            #protein = re.findall('[pP]rotein:  (.*?)', r)
            #tup = zip([r[0] for r in [calories, ssize, fat, carbs]])
    except: pass

resdf = pd.DataFrame(zip(ssizes, carbs, fats, cals), columns=['ssizes', 'carbs', 'fat', 'calories'])
resdf['cals'].mean()
resdf
len(cals)
len(carbs)
len(fat)
text
rm(text)
del(text)
reslist = []
divs = bs.find_all('div')
carbs, ssizes, fats, cals = [],[],[],[]
for d in divs:
    try:
        if 'nutrition' in d.attrs['class'][0]:
            text = d.text
            text = re.sub('\\n', '', text)
            text = re.sub('\\t', '', text)
            cals.append(int(re.findall('[cC]alories: (.*?),', text)[0]))
            ssizes.append(re.findall('[sS]erving [sS]ize: (.*?) ', text)[0])
            fats.append(re.findall('[fF]at: (.*?),', text)[0])
            carbsres = re.findall('[cC]arbs: (.*?),', text)
            reslist.append(text)
            #protein = re.findall('[pP]rotein:  (.*?)', r)
            #tup = zip([r[0] for r in [calories, ssize, fat, carbs]])
    except: pass

resdf = pd.DataFrame(zip(ssizes, carbs, fats,
reslist = []
divs = bs.find_all('div')
carbs, ssizes, fats, cals = [],[],[],[]
for d in divs:
    try:
        if 'nutrition' in d.attrs['class'][0]:
            text = d.text
            text = re.sub('\\n', '', text)
            text = re.sub('\\t', '', text)
            cals.append(int(re.findall('[cC]alories: (.*?),', text)[0]))
            ssizes.append(re.findall('[sS]erving [sS]ize: (.*?) ', text)[0])
            fats.append(re.findall('[fF]at: (.*?),', text)[0])
            carbsres = re.findall('[cC]arbs: (.*?),', text)
            reslist.append(text)
            #protein = re.findall('[pP]rotein:  (.*?)', r)
            #tup = zip([r[0] for r in [calories, ssize, fat, carbs]])
    except: pass

resdf = pd.DataFrame(zip(ssizes, carbs, fats, cals), columns=['ssizes', 'carbs', 'fat', 'calories'])
resdf
len(ssizes)
len(cals)
len(fats)
reslist = []
divs = bs.find_all('div')
carbs, ssizes, fats, cals = [],[],[],[]
for d in divs:
    try:
        if 'nutrition' in d.attrs['class'][0]:
            text = d.text
            text = re.sub('\\n', '', text)
            text = re.sub('\\t', '', text)
            cals.append(int(re.findall('[cC]alories: (.*?),', text)[0]))
            ssizes.append(re.findall('[sS]erving [sS]ize: (.*?) ', text)[0])
            fats.append(re.findall('[fF]at: (.*?),', text)[0])
            carbs.append(re.findall('[cC]arbs: (.*?),', text)[0])
            reslist.append(text)
            #protein = re.findall('[pP]rotein:  (.*?)', r)
            #tup = zip([r[0] for r in [calories, ssize, fat, carbs]])
    except: pass

resdf = pd.DataFrame(zip(ssizes, carbs, fats, cals), columns=['ssizes', 'carbs', 'fat', 'calories'])
resdf
resdf['calories'].mean()
resdf['calories'].var()
resdf['calories'].stdev()
import math
resdf.shape()[0]
res.shape(0)
resdf.shape()
resdf.shape
res.shape[0]
resdf.shape[0]
bs.findall(attrs={'class':'result_count'})
bs.find_all(attrs={'class':'result_count'})
"""
def calorie_lookup(food, browser=None):
    if browser is not None:
        br = browser
    else:
        br = mech.Browser()
        br.set_handle_robots(False)
        br.addheaders = [('User-agent', 'Firefox')]
    br.open("http://www.myfitnesspal.com/food/search")
    br.select_form(nr=0)
    br.form['search'] = 'cheeseburger'
    resp = br.submit()
    page = resp.get_data()
    bs = BeautifulSoup(page)
    #bs.find_all(attrs={'class':'result_count'})
    reslist = []
    divs = bs.find_all('div')
    carbs, ssizes, fats, cals = [],[],[],[]
    for d in divs:
        try:
            if 'nutrition' in d.attrs['class'][0]:
                text = d.text
                text = re.sub('\\n', '', text)
                text = re.sub('\\t', '', text)
                cals.append(int(re.findall('[cC]alories: (.*?),', text)[0]))
                ssizes.append(re.findall('[sS]erving [sS]ize: (.*?) ', text)[0])
                fats.append(re.findall('[fF]at: (.*?),', text)[0])
                carbs.append(re.findall('[cC]arbs: (.*?),', text)[0])
                reslist.append(text)
                #protein = re.findall('[pP]rotein:  (.*?)', r)
                #tup = zip([r[0] for r in [calories, ssize, fat, carbs]])
        except: pass
    resdf = pd.DataFrame(zip(ssizes, carbs, fats, cals), columns=['ssizes', 'carbs', 'fat', 'calories'])
    cmean = resdf['calories'].mean()
    cvar = resdf['calories'].var()
    count = resdf.shape[0]
    return cmean, cvar, count
def calorie_lookup(food, browser=None):
    if browser is not None:
        br = browser
    else:
        br = mech.Browser()
        br.set_handle_robots(False)
        br.addheaders = [('User-agent', 'Firefox')]
    br.open("http://www.myfitnesspal.com/food/search")
    br.select_form(nr=0)
    br.form['search'] = 'cheeseburger'
    resp = br.submit()
    page = resp.get_data()
    bs = BeautifulSoup(page)
    #bs.find_all(attrs={'class':'result_count'})
    reslist = []
    divs = bs.find_all('div')
    carbs, ssizes, fats, cals = [],[],[],[]
    for d in divs:
        try:
            if 'nutrition' in d.attrs['class'][0]:
                text = d.text
                text = re.sub('\\n', '', text)
                text = re.sub('\\t', '', text)
                cals.append(int(re.findall('[cC]alories: (.*?),', text)[0]))
                ssizes.append(re.findall('[sS]erving [sS]ize: (.*?) ', text)[0])
                fats.append(re.findall('[fF]at: (.*?),', text)[0])
                carbs.append(re.findall('[cC]arbs: (.*?),', text)[0])
                reslist.append(text)
                #protein = re.findall('[pP]rotein:  (.*?)', r)
                #tup = zip([r[0] for r in [calories, ssize, fat, carbs]])
        except: pass
    resdf = pd.DataFrame(zip(ssizes, carbs, fats, cals), columns=['ssizes', 'carbs', 'fat', 'calories'])
    cmean = resdf['calories'].mean()
    cvar = resdf['calories'].var()
    count = resdf.shape[0]
    return (cmean, cvar, count)
calorie_lookup('cheeseburger')
calorie_lookup('spaghetti bolognese')
cmean
calorie_lookup('steak')
bs
del(bs)
calorie_lookup('steak')
def calorie_lookup(food, browser=None):
    if browser is not None:
        br = browser
    else:
        br = mech.Browser()
        br.set_handle_robots(False)
        br.addheaders = [('User-agent', 'Firefox')]
    br.open("http://www.myfitnesspal.com/food/search")
    br.select_form(nr=0)
    br.form['search'] = food
    resp = br.submit()
    page = resp.get_data()
    bs = BeautifulSoup(page)
    #bs.find_all(attrs={'class':'result_count'})
    reslist = []
    divs = bs.find_all('div')
    carbs, ssizes, fats, cals = [],[],[],[]
    for d in divs:
        
        try:
            if 'nutrition' in d.attrs['class'][0]:
                text = d.text
                text = re.sub('\\n', '', text)
                text = re.sub('\\t', '', text)
                cals.append(int(re.findall('[cC]alories: (.*?),', text)[0]))
                ssizes.append(re.findall('[sS]erving [sS]ize: (.*?) ', text)[0])
                fats.append(re.findall('[fF]at: (.*?),', text)[0])
                carbs.append(re.findall('[cC]arbs: (.*?),', text)[0])
                reslist.append(text)
                #protein = re.findall('[pP]rotein:  (.*?)', r)
                #tup = zip([r[0] for r in [calories, ssize, fat, carbs]])
        except: pass
    resdf = pd.DataFrame(zip(ssizes, carbs, fats, cals), columns=['ssizes', 'carbs', 'fat', 'calories'])
    cmean = resdf['calories'].mean()
    cvar = resdf['calories'].var()
    count = resdf.shape[0]
    return (cmean, cvar, count)
calorie_lookup('steak')
bs = BeautifulSoup(page)
bs.find_all(attrs={'class':'result_count'})
results = bs.find_all(attrs={'class':'result_count'})
re.findall('of ([0-9])+.*?</div>', results)
re.findall('of ([0-9])+.*?</div>', results[0])
results
results[0].text
re.findall('of ([0-9])+.*?', results[0].text)
re.findall('of ([0-9]+).*?', results[0].text)
range(1)
def calorie_lookup(food, browser=None, fullres = False):
    if browser is not None:
        br = browser
    else:
        br = mech.Browser()
        br.set_handle_robots(False)
        br.addheaders = [('User-agent', 'Firefox')]
    br.open("http://www.myfitnesspal.com/food/search")
    br.select_form(nr=0)
    br.form['search'] = food
    resp = br.submit()
    page = resp.get_data()
    bs = BeautifulSoup(page)
    
    reslist = []
    carbs, ssizes, fats, cals = [],[],[],[]
    results = bs.find_all(attrs={'class':'result_count'})    
    results = int(re.findall('of ([0-9]+).*?', results[0].text))
    if fullres:
        res_pages = results / 20
    else: 
        res_pages = 1
    res_pages = results / 20
    for i in res_pages:
        url = 'http://www.myfitnesspal.com/food/search?page=' + str(i)+'&search='+food
        print "opening " + str(url)
        br.open(url)
        page = resp.get_data
        divs = bs.find_all('div')
        for d in divs:
            try:
                if 'nutrition' in d.attrs['class'][0]:
                    text = d.text
                    text = re.sub('\\n', '', text)
                    text = re.sub('\\t', '', text)
                    cals.append(int(re.findall('[cC]alories: (.*?),', text)[0]))
                    ssizes.append(re.findall('[sS]erving [sS]ize: (.*?) ', text)[0])
                    fats.append(re.findall('[fF]at: (.*?),', text)[0])
                    carbs.append(re.findall('[cC]arbs: (.*?),', text)[0])
                    reslist.append(text)
                    #protein = re.findall('[pP]rotein:  (.*?)', r)
                    #tup = zip([r[0] for r in [calories, ssize, fat, carbs]])
            except: pass
    resdf = pd.DataFrame(zip(ssizes, carbs, fats, cals), columns=['ssizes', 'carbs', 'fat', 'calories'])
    cmean = resdf['calories'].mean()
    cvar = resdf['calories'].var()
    count = resdf.shape[0]
    return (cmean, cvar, count)
calorie_lookup('hamburger', fullres=True)
results
results[0].text
re.findall('of ([0-9]+).*?', results[0].text)
runfile('/Users/babraham/Google Drive/Grad_School/Fall_2017/Comp_Visual_Rec/cs6501_final_project/calorie_lookup.py', wdir='/Users/babraham/Google Drive/Grad_School/Fall_2017/Comp_Visual_Rec/cs6501_final_project')
calorie_lookup('pasta', fullres=True)
food = 'pasta'
br.open("http://www.myfitnesspal.com/food/search")
br.select_form(nr=0)
br.form['search'] = food
resp = br.submit()
page = resp.get_data()
bs = BeautifulSoup(page)
results = bs.find_all(attrs={'class':'result_count'})
print "res: " + str(results[0].text)
re.findall('of ([0-9]+).*?', results[0].text)
results = int(re.findall('of ([0-9]+).*?', results[0].text)[0])
del(food)
runfile('/Users/babraham/Google Drive/Grad_School/Fall_2017/Comp_Visual_Rec/cs6501_final_project/calorie_lookup.py', wdir='/Users/babraham/Google Drive/Grad_School/Fall_2017/Comp_Visual_Rec/cs6501_final_project')
calorie_lookup('pasta', fullres=True)
calorie_lookup('chicken caesar salad', fullres=True)
calorie_lookup('pasta', fullres=True)
calorie_lookup('ravioli', fullres=True)
runfile('/Users/babraham/Google Drive/Grad_School/Fall_2017/Comp_Visual_Rec/cs6501_final_project/calorie_lookup.py', wdir='/Users/babraham/Google Drive/Grad_School/Fall_2017/Comp_Visual_Rec/cs6501_final_project')
calorie_lookup('ravioli', fullres=True)
import os
os.getcwd()
foods = open('../calorie_counter_data/all_data_w_splits/foodList.csv', 'r')
foodlist = [l.strip().split(',')[1] for l in lines]
lines = foods.readlines()
foodlist = [l.strip().split(',')[1] for l in lines]
foodlist
foodlist = [re.sub('_',' ', l) for l in lines]
foodlist
lines = foods.readlines()
foodlist = [l.strip().split(',')[1] for l in lines]
foodlist = [re.sub('_',' ', l) for l in foodlist]
foodlist
foods = open('../calorie_counter_data/all_data_w_splits/foodList.csv', 'r')
lines = foods.readlines()
foodlist = [l.strip().split(',')[1] for l in lines]
foodlist = [re.sub('_',' ', l) for l in foodlist]
foodlist
runfile('/Users/babraham/Google Drive/Grad_School/Fall_2017/Comp_Visual_Rec/cs6501_final_project/calorie_lookup.py', wdir='/Users/babraham/Google Drive/Grad_School/Fall_2017/Comp_Visual_Rec/cs6501_final_project')
calorie_lookup(';alksdg')
runfile('/Users/babraham/Google Drive/Grad_School/Fall_2017/Comp_Visual_Rec/cs6501_final_project/calorie_lookup.py', wdir='/Users/babraham/Google Drive/Grad_School/Fall_2017/Comp_Visual_Rec/cs6501_final_project')
calorie_lookup(';alksdg')
runfile('/Users/babraham/Google Drive/Grad_School/Fall_2017/Comp_Visual_Rec/cs6501_final_project/calorie_lookup.py', wdir='/Users/babraham/Google Drive/Grad_School/Fall_2017/Comp_Visual_Rec/cs6501_final_project')
calorie_lookup(';alksdg')
foods = open('../calorie_counter_data/all_data_w_splits/foodList.csv', 'r')
lines = foods.readlines()
foodlist = [l.strip().split(',')[1] for l in lines]
foodlist = [re.sub('_',' ', l) for l in foodlist]
restups = []
for food in foodList[1:3]:
    res = calorie_lookup(food)
    restups.append(res)

df = pd.DataFrame(restups, columns=["food", "meanCals", "varCals", "Samples"])
df.to_csv('food_calorie_dataa.csv', index=False)
foods = open('../calorie_counter_data/all_data_w_splits/foodList.csv', 'r')
lines = foods.readlines()
foodlist = [l.strip().split(',')[1] for l in lines]
foodlist = [re.sub('_',' ', l) for l in foodlist]
restups = []
for food in foodlist[1:3]:
    res = calorie_lookup(food)
    restups.append(res)

df = pd.DataFrame(restups, columns=["food", "meanCals", "varCals", "Samples"])
df.to_csv('food_calorie_dataa.csv', index=False)
foods = open('../calorie_counter_data/all_data_w_splits/foodList.csv', 'r')
lines = foods.readlines()
foodlist = [l.strip().split(',')[1] for l in lines]
foodlist = [re.sub('_',' ', l) for l in foodlist]
restups = []
for food in foodlist[1:3]:
    res = calorie_lookup(food)
    print res
    restups.append(res)

df = pd.DataFrame(restups, columns=["food", "meanCals", "varCals", "Samples"])
df.to_csv('food_calorie_dataa.csv', index=False)
runfile('/Users/babraham/Google Drive/Grad_School/Fall_2017/Comp_Visual_Rec/cs6501_final_project/calorie_lookup.py', wdir='/Users/babraham/Google Drive/Grad_School/Fall_2017/Comp_Visual_Rec/cs6501_final_project')
foods = open('../calorie_counter_data/all_data_w_splits/foodList.csv', 'r')
lines = foods.readlines()
foodlist = [l.strip().split(',')[1] for l in lines]
foodlist = [re.sub('_',' ', l) for l in foodlist]
restups = []
for food in foodlist[1:3]:
    res = calorie_lookup(food)
    print res
    restups.append(res)

df = pd.DataFrame(restups, columns=["food", "meanCals", "varCals", "Samples"])
df.to_csv('food_calorie_dataa.csv', index=False)

runfile('/Users/babraham/Google Drive/Grad_School/Fall_2017/Comp_Visual_Rec/cs6501_final_project/calorie_lookup.py', wdir='/Users/babraham/Google Drive/Grad_School/Fall_2017/Comp_Visual_Rec/cs6501_final_project')
foods = open('../calorie_counter_data/all_data_w_splits/foodList.csv', 'r')
lines = foods.readlines()
foodlist = [l.strip().split(',')[1] for l in lines]
foodlist = [re.sub('_',' ', l) for l in foodlist]
restups = []
for food in foodlist[1:3]:
    res = calorie_lookup(food)
    print res
    restups.append(res)

df = pd.DataFrame(restups, columns=["food", "meanCals", "varCals", "Samples"])
df.to_csv('food_calorie_dataa.csv', index=False)

br.open('http://www.myfitnesspal.com/food/search?page=1&search=stirfry%20pork')
runfile('/Users/babraham/Google Drive/Grad_School/Fall_2017/Comp_Visual_Rec/cs6501_final_project/calorie_lookup.py', wdir='/Users/babraham/Google Drive/Grad_School/Fall_2017/Comp_Visual_Rec/cs6501_final_project')
br.open('http://www.myfitnesspal.com/food/search?page=1&search=stirfry%20pork')
res = build_database()
runfile('/Users/babraham/Google Drive/Grad_School/Fall_2017/Comp_Visual_Rec/cs6501_final_project/calorie_lookup.py', wdir='/Users/babraham/Google Drive/Grad_School/Fall_2017/Comp_Visual_Rec/cs6501_final_project')
res = build_database()
runfile('/Users/babraham/Google Drive/Grad_School/Fall_2017/Comp_Visual_Rec/cs6501_final_project/calorie_lookup.py', wdir='/Users/babraham/Google Drive/Grad_School/Fall_2017/Comp_Visual_Rec/cs6501_final_project')
res = build_database()
runfile('/Users/babraham/Google Drive/Grad_School/Fall_2017/Comp_Visual_Rec/cs6501_final_project/calorie_lookup.py', wdir='/Users/babraham/Google Drive/Grad_School/Fall_2017/Comp_Visual_Rec/cs6501_final_project')
res = build_database()
runfile('/Users/babraham/Google Drive/Grad_School/Fall_2017/Comp_Visual_Rec/cs6501_final_project/calorie_lookup.py', wdir='/Users/babraham/Google Drive/Grad_School/Fall_2017/Comp_Visual_Rec/cs6501_final_project')
res = build_database()
divs
divs[0]
divs[0].attrs
'id' in div[0].attrs
'id' in divs[0].attrs
runfile('/Users/babraham/Google Drive/Grad_School/Fall_2017/Comp_Visual_Rec/cs6501_final_project/calorie_lookup.py', wdir='/Users/babraham/Google Drive/Grad_School/Fall_2017/Comp_Visual_Rec/cs6501_final_project')
res = build_database()
text = 'Serving Size: 3 oz,Calories:  137.7,Fat:  6.1g,Carbs:  0g,Protein:  19.4g'
re.findall('[cC]alories: (.*?),', text)
int(re.findall('[cC]alories: (.*?),', text))
int(re.findall('[cC]alories: (.*?),', text)[0])
float(re.findall('[cC]alories: (.*?),', text)[0])
runfile('/Users/babraham/Google Drive/Grad_School/Fall_2017/Comp_Visual_Rec/cs6501_final_project/calorie_lookup.py', wdir='/Users/babraham/Google Drive/Grad_School/Fall_2017/Comp_Visual_Rec/cs6501_final_project')
res = build_database()
res
os.getcwd()
runfile('/Users/babraham/Google Drive/Grad_School/Fall_2017/Comp_Visual_Rec/cs6501_final_project/calorie_lookup.py', wdir='/Users/babraham/Google Drive/Grad_School/Fall_2017/Comp_Visual_Rec/cs6501_final_project')
res = build_database()
res
url = 'http://www.myfitnesspal.com/food/search?page=1&search=salmon'
br.open(url)
resp = br.open(url)
resp
resp.get_data()
runfile('/Users/babraham/Google Drive/Grad_School/Fall_2017/Comp_Visual_Rec/cs6501_final_project/calorie_lookup.py', wdir='/Users/babraham/Google Drive/Grad_School/Fall_2017/Comp_Visual_Rec/cs6501_final_project')
calorie_lookup('french fries')
foodlist[0]
foodlist[1]
calorie_lookup(foodlist[1])
res = build_database()
foodlist.index('ramen')
def makeSubsets(flist, splitlen=25):
    split = 1
    out = open("labelSplit" + str(split) + ".txt")
    for i,f in enumerate(flist):
        if i % splitlen == 0:
            split +=1
            out.close
            out = open("labelSplit" + str(split) + ".txt")
        out.write(f + '\n')
    out.close()
makeSubsets(foodlist)
runfile('/Users/babraham/Google Drive/Grad_School/Fall_2017/Comp_Visual_Rec/cs6501_final_project/calorie_lookup.py', wdir='/Users/babraham/Google Drive/Grad_School/Fall_2017/Comp_Visual_Rec/cs6501_final_project')
makeSubsets(foodlist)
os.getcwd()
def makeSubsets(flist, splitlen=25):
    split = 0
    if 'name' in flist: flist.remove('name')
    out = open("labelSplit" + str(split) + ".txt", 'w')
    for i,f in enumerate(flist):
        if i % splitlen == 0:
            split +=1
            out.close
            out = open("labelSplit" + str(split) + ".txt", 'w')
        out.write(f + '\n')
    out.close()
makeSubsets(foodlist)
def build_database(split=1):
    #foods = open('../calorie_counter_data/all_data_w_splits/foodList.csv', 'r')
    foods = open("labelSplit" + str(split) + ".txt", 'r')
    lines = foods.readlines()
    #foodlist = [l.strip().split(',')[1] for l in lines]
    foodlist = [l.strip() for l in lines]
    foodlist = [re.sub('_',' ', l) for l in foodlist]
    restups = []
    for food in foodlist:
        res = calorie_lookup(food)
        print res
        restups.append(res)
    df = pd.DataFrame(restups, columns=["food", "meanCals", "varCals", "Samples"])
    df.to_csv('food_calorie_data_' + str(split)+ '.csv', index=False)
    return df
runfile('/Users/babraham/Google Drive/Grad_School/Fall_2017/Comp_Visual_Rec/cs6501_final_project/calorie_lookup.py', wdir='/Users/babraham/Google Drive/Grad_School/Fall_2017/Comp_Visual_Rec/cs6501_final_project')
res = build_database(1)
reslist = [res]
for i in xrange(2:9):
for i in xrange(2,9):
    reslist.append(build_database(i))
    
foodlist.index('tuna tartare')
foodlist[166:168]
len(reslist)
reslist.pop(6)
for i in xrange(6,9):
    reslist.append(build_database(i))
    
reslist.append(build_database(9))
import pandas as pd
resdf = df.concat(reslist)
resdf = pd.concat(reslist)
resdf
resdf.to_csv("all_calorie_data.csv", index=False)
import matplotlib
matplotlib.pyplot.hist(reslist['meanCals',:])
import socket
socket.gethostbyaddr(128.143.25.104)
socket.gethostbyaddr([128.143.25.104])
socket.gethostbyaddr("128.143.25.104")
socket.gethostbyaddr("50.116.112.162")
socket.gethostbyname('http://magazineluizaofertasespeciais.com')
socket.gethostbyname('www.google.com')
socket.gethostbyname('http://magazineluizaofertasespeciais.com')
socket.gethostbyname('magazineluizaofertasespeciais.com')
socket.gethostbyname('zonasequrasviabcp.com')

## ---(Sun Nov  5 16:14:12 2017)---
import torch
a = torch.randn(12,100)
a
a[0]
a = torch.randn(3,3)
a
a.max(0)
a.max(1)
a.squeeze()
a.squeeze(1)
a.tolist()

## ---(Wed Nov  8 22:40:04 2017)---
import numpy as np
np.random.exponential(.5, 100)
res = np.random.exponential(2, 100)
res
import pandas as pd 
res = pd.read_csv('Users/babraham/Desktop/http_new.csv")
res = pd.read_csv('Users/babraham/Desktop/http_new.csv')
res = pd.read_csv('/Users/babraham/Desktop/http_new.csv')
res
res = pd.read_csv('/Users/babraham/Desktop/http_new.csv')
res
res.columns
res.ix['resp_filenames',:]
res.columns
res.ix[:,['resp_filenames']]
res.ix[:,1:5]
class File(object):
    def __init__(self, fsize, at, fid):
        self.id = fid
        self.fileSize = fsize
        self.arrivalTime = at
        self.serviceTime = at + fsize / 10
        self.waitingTime = 0
    def __str__(self):
        return self.__dict__()
f = File(12, 2, 1)
f.__str__()
runfile('/Users/babraham/Box Sync/2017Fall-7457/Simulation/classes.py', wdir='/Users/babraham/Box Sync/2017Fall-7457/Simulation')
f = File(12, 2, 1)
f.__str__()
runfile('/Users/babraham/Box Sync/2017Fall-7457/Simulation/classes.py', wdir='/Users/babraham/Box Sync/2017Fall-7457/Simulation')
f = File(12, 2, 1)
f.__str__()
import Queue
import Queue as q
queue = q.queue()
queue = q.Queue()
f1 = File(10,2,1)
f2 = File(3,5,2)
queue.put(f1)
queue.pop()
queue.deque()
queue
queue.items()
queue.get()
queue.size()
queue.qsize()
fqueue = list()
int1 = Interface(1)
int2 = Interface(2)
def function():
    global int1, int2, fqueue
    fqueue.append(3)
fqueue
function()
fqueue
function()
fqueue
f1 = File(12, 2, 1)
print f1
class File():
    def __init__(self, fsize, at, fid):
        self.id = fid
        self.fileSize = fsize
        self.arrivalTime = at
        self.serviceTime = at + fsize / 10
        self.waitingTime = 0
    def __str__(self):
        return str(self.__dict__)
f1 = File(12, 2, 1)
print f1
l = [1,2,3,5,7]
l.pop()
l
l.pop()
l
l.pop()
l
l.pop(0)
l
v = None
v is None
v is not None
import numpy as np
import csv

t = 0
fileID = 0
thres_count = 0

#t_int=np.random.exponential(0.5,100)

with open("trunc5M.txt") as text_file:
    lines=text_file.read().split()
    pareto=[float(i) for i in lines]
len(pareto)
pareto[1:5]
import numpy as np
np.max(pareto)
psorted = sorted(pareto)
psorted[0]
psorted = sorted(pareto, ascending=False)
psorted = sorted(pareto, reverse=True)
psorted[1:20]
min(psorted[1:100])
import matplotlib as plt
plt.hist(pareto)
import matlib.pyplot as plt
import matplotlib.pyplot as plt
plt.hist(pareto, bins=20)
plt.hist(pareto, bins=100)
plt.boxplot(pareto)
global large_thresh, thresh_count, interface_list
queue=[]
file_list = []
comp_file_list = []
#global thres_count, t, fileID
new_file = generate_file()
file_list.append(new_file)
queue.append(new_file)
#2. Remove any completed files from interfaces
def check_interface():
    for interface in interface_list:
        if not interface.busy:
            return interface.id
    return 0
def generate_file():
    global t,fileID
    t_int = np.random.exponential(1)
    f_pareto = pareto[fileID]
    t=t+t_int
    new_file=File(f_pareto,t,t_int,fileID)
    fileID=fileID+1
    print(new_file)
    return new_file
t = 0
fileID = 0
thres_count = 0
large_thresh = 200

interface1=Interface(1)
interface2=Interface(2)
interface_list=[interface1,interface2]
class Interface():
    def __init__(self, interface_id):
        self.id = interface_id
        self.busy = False
        self.fileID = None
    
    def __str__(self):
        return str(self.__dict__)
    
    def isBusy(self):
        return self.busy
    
    def addFile(self, fid):
        self.fileID = fid
        self.busy = True
    
    def clear(self):
        self.fileID = None
        self.busy = False
class File():
    def __init__(self, fsize, at, interval, fid):
        self.id = fid
        self.fileSize = fsize
        self.arrivalTime = at
        self.timeInterval = interval
        self.serviceTime = at + fsize / 1.25
        self.waitingTime = 0
        self.departureTime = 0
    
    def __str__(self):
        return str(self.__dict__)
queue
new_file = generate_file()
file_list.append(new_file)
queue.append(new_file)
for interface in interface_list:
    if interface.fileID is not None:
        #if file has been processed by now, remove it
        cur_file = file_list[interface.fileID]
        if cur_file.dep <= t:
            comp_file_list.append(file_list[interface.fileID])
            if file_list[interface.fileID].fileSize > large_thresh:
                thresh_count +=1
            interface.clear()
interface1=Interface(1)
interface2=Interface(2)
interface_list=[interface1,interface2]
for interface in interface_list:
    if interface.fileID is not None:
        #if file has been processed by now, remove it
        cur_file = file_list[interface.fileID]
        if cur_file.dep <= t:
            comp_file_list.append(file_list[interface.fileID])
            if file_list[interface.fileID].fileSize > large_thresh:
                thresh_count +=1
            interface.clear()
            
print interface_list[0]
print interface_list[1]
interfaceState = check_interface()
interfaceState
if interfaceState == 1 :
    #update departure time and add file to interface
    serving_file = queue.pop(0)
    serving_file.departureTime = t +  serving_file.serviceTime
    interface_list[interfaceState-1].addFile(serving_file.id)
elif interfaceState == 2:
    serving_file=queue.pop(0)
    serving_file.departureTime = t +  serving_file.serviceTime
    interface_list[interfaceState-1].addFile(queue[0].id)
queue
file_list
print interface_list[0]
print file_list[0]
for f in queue: f.waitingTime += new_file.t_int
new_file = generate_file()
file_list.append(new_file)
queue.append(new_file)
#2. Remove any completed files from interfaces
for interface in interface_list:
    if interface.fileID is not None:
        #if file has been processed by now, remove it
        cur_file = file_list[interface.fileID]
        if cur_file.dep <= t:
            comp_file_list.append(file_list[interface.fileID])
            if file_list[interface.fileID].fileSize > large_thresh:
                thresh_count +=1
            interface.clear()
new_file = generate_file()
file_list.append(new_file)
queue.append(new_file)
#2. Remove any completed files from interfaces
for interface in interface_list:
    if interface.fileID is not None:
        #if file has been processed by now, remove it
        cur_file = file_list[interface.fileID]
        if cur_file.departureTime <= t:
            comp_file_list.append(file_list[interface.fileID])
            if file_list[interface.fileID].fileSize > large_thresh:
                thresh_count +=1
            interface.clear()
queue
t
print interface_list[0]
interfaceState = check_interface()
if interfaceState == 1 :
    #update departure time and add file to interface
    serving_file = queue.pop(0)
    serving_file.departureTime = t +  serving_file.serviceTime
    interface_list[interfaceState-1].addFile(serving_file.id)
elif interfaceState == 2:
    serving_file=queue.pop(0)
    serving_file.departureTime = t +  serving_file.serviceTime
    interface_list[interfaceState-1].addFile(queue[0].id)

#4. Update waiting times of files in queue
for f in queue: f.waitingTime += new_file.t_int
for f in queue: f.waitingTime += new_file.timeInterval
print queue[0]
interface_list[0].isBusy()
interface_list[0].__str__()
import time
time.time()
runfile('/Users/babraham/Box Sync/2017Fall-7457/Simulation/sim.py', wdir='/Users/babraham/Box Sync/2017Fall-7457/Simulation')
runfile('/Users/babraham/Box Sync/2017Fall-7457/Simulation/sim.py', wdir='/Users/babraham/Box Sync/2017Fall-7457/Simulation')
t = 0
fileID = 0
thresh_count = 0
large_thresh = 200

interface1=Interface(1)
interface2=Interface(2)
interface_list=[interface1,interface2]
st_time = time.time()
queue=[]
file_list = []
comp_file_list = []
new_file = generate_file()
file_list.append(new_file)
queue.append(new_file)
queue
for interface in interface_list:
    if interface.fileID is not None:
        #if file has been processed by now, remove it
        cur_file = file_list[interface.fileID]
        if cur_file.departureTime <= t:
            comp_file_list.append(file_list[interface.fileID])
            if file_list[interface.fileID].fileSize > large_thresh:
                thresh_count +=1
            interface.clear()

#3. check if interfaces are available. If so, pop from queue and add to interface
interfaceState = check_interface()
print "interface_stte: " + str(interfaceState)
if interfaceState == 1 :
    #update departure time and add file to interface
    serving_file = queue.pop(0)
    serving_file.departureTime = t +  serving_file.serviceTime
    interface_list[interfaceState-1].addFile(serving_file.id)
elif interfaceState == 2:
    serving_file=queue.pop(0)
    serving_file.departureTime = t +  serving_file.serviceTime
    try:
        interface_list[interfaceState-1].addFile(queue[0].id)
    except:
        print "error. queue-len: " + str(len(queue)) + ", int_state: " + str(interfaceState)

#4. Update waiting times of files in queue
interface_list[0]
print interface_list[0]
file_list[0].serviceTime
t
for f in queue: f.waitingTime += new_file.timeInterval
queue[0].waitTime
new_file = generate_file()
file_list.append(new_file)
queue.append(new_file)
#2. Remove any completed files from interfaces
for interface in interface_list:
    if interface.fileID is not None:
        #if file has been processed by now, remove it
        cur_file = file_list[interface.fileID]
        if cur_file.departureTime <= t:
            comp_file_list.append(file_list[interface.fileID])
            if file_list[interface.fileID].fileSize > large_thresh:
                thresh_count +=1
            interface.clear()

#3. check if interfaces are available. If so, pop from queue and add to interface
interfaceState = check_interface()
print "interface_stte: " + str(interfaceState)
if interfaceState == 1 :
    #update departure time and add file to interface
    serving_file = queue.pop(0)
    serving_file.departureTime = t +  serving_file.serviceTime
    interface_list[interfaceState-1].addFile(serving_file.id)
elif interfaceState == 2:
    serving_file=queue.pop(0)
    serving_file.departureTime = t +  serving_file.serviceTime
    try:
        interface_list[interfaceState-1].addFile(queue[0].id)
    except:
        print "error. queue-len: " + str(len(queue)) + ", int_state: " + str(interfaceState)

#4. Update waiting times of files in queue
print interface_list[1]
new_file = generate_file()
file_list.append(new_file)
queue.append(new_file)
#2. Remove any completed files from interfaces
for interface in interface_list:
    if interface.fileID is not None:
        #if file has been processed by now, remove it
        cur_file = file_list[interface.fileID]
        if cur_file.departureTime <= t:
            comp_file_list.append(file_list[interface.fileID])
            if file_list[interface.fileID].fileSize > large_thresh:
                thresh_count +=1
            interface.clear()
interface_list[0].__str__()
interfaceState = check_interface()
queue
interfaceState
runfile('/Users/babraham/Box Sync/2017Fall-7457/Simulation/sim.py', wdir='/Users/babraham/Box Sync/2017Fall-7457/Simulation')
len(comp_file_list)
len(queue)
runfile('/Users/babraham/Box Sync/2017Fall-7457/Simulation/new_sim/sim.py', wdir='/Users/babraham/Box Sync/2017Fall-7457/Simulation/new_sim')
f = File(20, 2, .013, 1)
f.__str__()
f.__dict__.items()
f.__dict__.keys()
','.join(f.__dict__.keys())
def exportData():        
    simOut = open('simOutput.csv', 'w')
    simOut.write(','.join(comp_file_list[0].__dict__.keys()) + '\n')
    for fc in comp_file_list:
        outstr = ','.join(fc.__dict__.values()) + '\n'
        simOut.write(outstr)
    simOut.close()
f2 = File(22,8,2.5,2)
f3 = File(38,12,4,3)
f4 = File(11,15,3,4)
comp_file_list = [f1,f2,f3,f4]
comp_file_list = [f,f2,f3,f4]
import os
os.getcwd()
simOut = open('simOutput.csv', 'w')
simOut.write(','.join(comp_file_list[0].__dict__.keys()) + '\n')
for fc in comp_file_list:
    outstr = ','.join(fc.__dict__.values()) + '\n'
    simOut.write(outstr)

simOut.close()
','.join(f1.__dict__.values())
f1
f.values()
f.__dict__.values()
fvals = [str(v) for v in f.__dict__.values()]
fvals
','.join(fvals)
simOut = open('simOutput.csv', 'w')
simOut.write(','.join(comp_file_list[0].__dict__.keys()) + '\n')
for fc in comp_file_list:
    fvals = [str(v) for v in fc.__dict__.values()]
    outstr = ','.join(fvals) + '\n'
    simOut.write(outstr)

simOut.close()

## ---(Sun Nov 12 13:13:21 2017)---
import os
os.getcwd()
os.chdir('/Users/babraham/Box Sync/2017Fall-7457/Simulation/new_sim')
with open("trunc10M.txt") as text_file:
    lines=text_file.read().split()
    pareto=[float(i) for i in lines]
import matplotlib.pyplot as plt
plt.hist(pareto, bins = 50)
plt.hist(pareto, bins = 100)
plt.hist(pareto, bins = 100, normed=True)
max(pareto)
min(pareto)
import numpy as np
import scipy.stats as s
s.genpareto.cdf(1, scale=2)
s.genpareto.cdf(1, loc=0, scale=2)
s.genpareto.cdf(1, 2)
s.genpareto.cdf(1000, 2)
unif_numbers = np.random.uniform(qlower, qupper, 1000)
qlower = s.genpareto.cdf(lower, c)
qupper = s.genpareto.cdf(upper, c)
unif_numbers = np.random.uniform(qlower, qupper, 1000)
n = 1000
lower = 1
upper = 1000
c = 2

qlower = s.genpareto.cdf(lower, c)
qupper = s.genpareto.cdf(upper, c)
unif_numbers = np.random.uniform(qlower, qupper, 1000)
s.genpareto.ppf(qlower, c)
s.genpareto.ppf(unif_numbers, c)
paretos = s.genpareto.ppf(unif_numbers, c)
plt.hist(paretos)
max(paretos)
min(paretos)
mean(paretos)
np.mean(paretos)
n = 100000
lower = 1
upper = 1000
c = 2

qlower = s.genpareto.cdf(lower, c)
qupper = s.genpareto.cdf(upper, c)
unif_numbers = np.random.uniform(qlower, qupper, n)
paretos = s.genpareto.ppf(unif_numbers, c)
np.mean(paretos)
s.genpareto.cdf(lower, c, scale=1)
s.genpareto.cdf(lower, c)
np.random.pareto(2)
qlower = s.pareto.cdf(lower, c)
qlower
c = 2
mean, var, skew, kurt = pareto.stats(b, moments='mvsk')
mean, var, skew, kurt = s.pareto.stats(b, moments='mvsk')
mean, var, skew, kurt = s.pareto.stats(c, moments='mvsk')
mean
mean, var, skew, kurt = s.genpareto.stats(c, moments='mvsk')
mean
p2_res = s.pareto.ppf(unif_numbers, c)
p2_res
min(p2_res)
max(p2_res)
mean(p2_res)
np.mean(p2_res)
n
p2_res = s.pareto.ppf(unif_numbers, n)
np.mean(p2_res)
plt.hist(p2_res)
n = 100000
lower = 1
upper = 1000
c = 2

qlower = s.pareto.cdf(lower, c)
qupper = s.pareto.cdf(upper, c)
unif_numbers = np.random.uniform(qlower, qupper, n)
paretos = s.pareto.ppf(unif_numbers, c)
plt.hist(paretos)
np.mean(paretos)
min(paretos)
max(paretos)
def generate_sizes(n, lower=1, upper=1000, c=2):
    qlower = s.pareto.cdf(lower, c)
    qupper = s.pareto.cdf(upper, c)
    unif_numbers = np.random.uniform(qlower, qupper, n)
    paretos = s.pareto.ppf(unif_numbers, c)
    return paretos
res = generate_sizes(5000000)
plt.hist(res)
max(res)
min(res)
def generate_sizes(n, lower=1, upper=1000, c=2):
    qlower = s.pareto.pdf(lower, c)
    qupper = s.pareto.pdf(upper, c)
    unif_numbers = np.random.uniform(qlower, qupper, n)
    paretos = s.pareto.ppf(unif_numbers, c)
    return paretos
res = generate_sizes(5000000)
plt.hist(res)
res
def generate_sizes(n, lower=1, upper=1000, c=2):
    qlower = s.pareto.cdf(lower, c)
    qupper = s.pareto.cdf(upper, c)
    unif_numbers = np.random.uniform(qlower, qupper, n)
    paretos = s.pareto.ppf(unif_numbers, c)
    return paretos
inter_arrivals = np.random.exponential(1/1.178, n)
n
def generate_sizes(n, lower=1, upper=1000, c=2):
    qlower = s.pareto.cdf(lower, c)
    qupper = s.pareto.cdf(upper, c)
    unif_numbers = np.random.uniform(qlower, qupper, n)
    paretolist = s.pareto.ppf(unif_numbers, c)
    return paretolist
import scipy.stats as s
res = generate_sizes(1)
res
res[0]
n = 1
f_pareto = generate_sizes(1)[0]
f_pareto
l = [1,2,3,4,9,1]
res = map(lambda x: x > 3, l)
res
a = 1.5
b = 2.3
c = 7.8
lista = [a,b,c]
lista = [str(i) for i in lista]
lista
','.join(lista)
res = [[1,2,3],[2,2,3],[3,2,3]]
import pandas as pd
cols = ['col1', 'col2', 'col3']
df = pd.DataFrame(res, columns=cols)
df
import numpy as np
np.mean(df.ix(:,['col3']))
df.ix[:,['col3']]
np.mean(df.ix[:,['col3']])
sum(df.ix[:,['col1', 'col2', 'col3']]
)
sum(df.ix[:,['col1']])
df.types
df.dtypes
np.mean(df.ix[:,['col2']])
df
np.sum(df.ix[:,['col2']])
sum(df.ix[:,['col2']])
np.sum(df.ix[:,['col2','col']])
res = np.sum(df.ix[:,['col2','col']])
res
res[0]
res[1]
res2 = np.mean(df.ix[:,['col1','col3']])
res2
r3 = res1 + res2
r3 = res + res2
r3
res
res2
list(res2)
res3 = list(res2) + list(res)
res3

## ---(Tue Apr  3 15:45:35 2018)---
l1 = ['a','b']
l2 = ['p','q']
s =l1
a = l2
for i,s,a in enumerate(zip(l1,l2)):
    print(i,s,a)
    
for i,(s,a) in enumerate(zip(l1,l2)):
    print(i,s,a)
    
num_states, num_actions = 4
num_states, num_actions = 4,4
N_sa = np.zeros([num_states,num_actions]) #counter of (s,a)
import numpy as np
N_sa = np.zeros([num_states,num_actions]) #counter of (s,a)
N_sa[1,2]
N_sa[1,2] = 23
N_sa
N_sa[1][2] = 55
N_sa
initial_Q = np.zeros([200,2])
iq = initial_Q
iq[200]
iq[150]
np.argmax(iq[150])
iq[150,1] = .5
np.argmax(iq[150])
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4/blackjack_control.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4/MCES.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4/blackjack_control.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4/MCES.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4/blackjack_control.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4/MCES.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4/blackjack_control.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4')
states,actions,rewards = get_episode_blackjack(policy)
initial_policy = np.ones([200, 2]) / 2
states,actions,rewards = get_episode_blackjack(initial_policy)
len(states)
len(actions)
len(rewards)
states,actions,rewards
states,actions,rewards = get_episode_blackjack(initial_policy)
states,actions,rewards
stateSpace = np.zeros([200,3],dtype=int)
stateSpace[:,0] = np.tile(range(12,22),20)
stateSpace[:,1] = np.tile(np.repeat(range(1,11),10),2)
stateSpace[100:,2] = 1
stateSpace.shape
stateSpace[100:,2] = 1
stateSpace = stateSpace.tolist()
stateSpace
stateSpace[94]
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4/MCES.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4/blackjack_control.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4/MCES.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4/blackjack_control.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4/sarsa.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4/windy.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4')
np.random.random()
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4/windy.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4')
initial_Q = np.zeros([70,4])
initial_state = stateSpace.index([0,3])
gamma = 1
alpha = 0.5
epsilon = 0.01
num_episodes = 170
action_str=['left','up', 'right', 'down']
Q = np.copy(initial_Q)
num_states, num_actions = Q.shape    

steps = np.zeros(num_episodes,dtype=int) # store #steps in each episode
rewards = np.zeros(num_episodes) # store total rewards for each episode
s = np.random.choice(range(num_states))
s
x = np.random.random()
x
x > epsilon
epsilon
a = np.argmax(Q[s])
a
Q[67]
s_new, r, terminal = transition(s,a)
s_new
r
terminal
if x > epsilon:
    a_new = np.argmax(Q[s_new])
else:
    a_new = np.random.choice(range(len(Q[s_new])))
a_new
Q[s,a] = Q[s,a] + alpha*(r + gamma*Q[s_new,a_new] - Q[s,a])
Q[s,a]
s = s_new
a = a_new
s_new, r, terminal = transition(s,a)
s_new
stateSpace = np.zeros([70,2], dtype=int)
stateSpace[:,0] = np.tile(range(10),7)
stateSpace[:,1] = np.tile(np.repeat(range(7),10),1)
stateSpace = stateSpace.tolist()
terminal_state = [7,3] # state G; state S is [0,3]

wind = [0, 0, 0, 1, 1, 1, 2, 2, 1, 0]
stateSpace[65]
stateSpace[67]
x = np.random.random()
if x > epsilon:
    a_new = np.argmax(Q[s_new])
else:
    a_new = np.random.choice(range(len(Q[s_new])))
a_new
Q[s,a] = Q[s,a] + alpha*(r + gamma*Q[s_new,a_new] - Q[s,a])
s = s_new
a = a_new
Q[s,a]
r
s_new
a_new

## ---(Tue Apr  3 19:49:48 2018)---
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4/sarsa.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4/windy.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4')
initial_Q = np.zeros([70,4])
initial_state = stateSpace.index([0,3])
gamma = 1
alpha = 0.5
epsilon = 0.01
num_episodes = 170
action_str=['left','up', 'right', 'down']  

# using sarsa 
Q, steps,rewards = sarsa(initial_Q, initial_state, transition, 
                         num_episodes, gamma,alpha, epsilon)
Q
steps
rewards
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4/sarsa.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4/windy.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4/sarsa.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4/windy.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4')
stateSpace[37]
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4/sarsa.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4/windy.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4')
Q
stateSpace.index([0,3])
Q[30]
np.argmax(Q[30])
transition(30,3)
stateSpace[20]
stateSpace[0]
stateSpace[1]
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4/sarsa.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4/windy.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4/sarsa.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4/windy.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4/windy9_setup.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4/windy9.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4/sarsa_lambda.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4/windy_sarsaLambda.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4')
np.zeros([1,1])
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4/sarsa_lambda.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4/windy_sarsaLambda.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4')
lambda_ = lambdas[1]
Q,steps,rewards = sarsa_lambda(initial_Q, initial_state, transition, 
                         num_episodes, gamma,alpha, lambda_, epsilon)
Q
steps
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4/sarsa_lambda.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4/windy_sarsaLambda.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4/blackjack_control.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4')
float((diff_usableAce + diff_noUsableAce))/200
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4/windy.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4')
fig.savefig('windy.jpg')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4/windy9.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw4/hw4')

## ---(Thu Apr  5 18:00:09 2018)---
def getTopStats(proc="bro"):
    top = subprocess.Popen(('top'), stdout=subprocess.PIPE)
    output = subprocess.check_output(('grep', 'process_name'), stdin=top.stdout)
    top.wait()
def getTopStats(proc="bro"):
    top = subprocess.Popen(('top'), stdout=subprocess.PIPE)
    output = subprocess.check_output(('grep', 'process_name'), stdin=top.stdout)
    top.wait()
    print(output)
getTop
getTopStats('python')
import subprocess
getTopStats('python')
import os
os.system('timeout 3 top | grep python > temp.txt')
os.system('timeout 3 top')
os.system('ls')
os.listdir('.')
f = open('temp.txt', 'r')
f.read()
os.system('timeout 3 top | grep ctkd > temp.txt')
f = open('temp.txt', 'r')
f.read()
os.system('timeout 3 top  > temp.txt')
os.system('timeout 3 top  > temp23.txt')
os.system('top  > temp23.txt')
f = open('temp23.txt', 'r')
text = f.read()
text
tlines = text.split('\n')
tlines
len(tlines)
import re
re.findall('excel.*?\n',text)
re.findall('CVMServer.*?\n',text)
os.system('top | grep CVMServer > out.txt')
top = subprocess.Popen(('top'), stdout=subprocess.PIPE)
output = subprocess.check_output(('grep', 'process_name'), stdin=top.stdout, timeout=waitTime)
waitTime = 1
output = subprocess.check_output(('grep', 'process_name'), stdin=top.stdout, timeout=waitTime)
output = subprocess.check_output(('grep', 'process_name'), stdin=top.stdout)
top.wait()
output
from __future__ import print_function
from time import sleep
last_idle = last_total = 0
while True:
    with open('/proc/stat') as f:
        fields = [float(column) for column in f.readline().strip().split()[1:]]
    idle, total = fields[3], sum(fields)
    idle_delta, total_delta = idle - last_idle, total - last_total
    last_idle, last_total = idle, total
    utilisation = 100.0 * (1.0 - idle_delta / total_delta)
    print('%5.1f%%' % utilisation, end='\r')
    sleep(5)
test = """
cpu  721438593 12391128 87794678 31807433600 5081858 0 10279678 0 0 0
cpu0 24478817 607118 4348887 1261397893 3650964 0 8094909 0 0 0
cpu1 51701651 322793 6019246 1303138746 376937 0 98092 0 0 0
cpu2 59869892 319732 6256548 1294532386 82798 0 88321 0 0 0
cpu3 60322041 313199 5526065 1294813050 74173 0 83715 0 0 0
cpu4 57461280 326395 5317550 1297981049 60751 0 82691 0 0 0
cpu5 56633447 290500 5153691 1299130854 69713 0 82410 0 0 0
cpu6 57605769 311312 5291612 1297979710 64473 0 81561 0 0 0
cpu7 57060066 303720 5152027 1298699328 52723 0 81468 0 0 0
cpu8 61155703 303997 5346863 1294295247 51310 0 84232 0 0 0
cpu9 60470039 293826 5302396 1294920334 61727 0 83190 0 0 0
cpu10 60349928 311154 5332700 1295106733 68242 0 82930 0 0 0
cpu11 52587560 1559461 5748451 1301864731 63492 0 232270 0 0 0
cpu12 13336031 1153389 2678998 1346341826 83933 0 107121 0 0 0
cpu13 3735781 626665 2390127 1356999208 30478 0 153138 0 0 0
cpu14 3456937 514405 1994356 1357861254 24352 0 108707 0 0 0
cpu15 3440013 536187 2124562 1357721231 31710 0 106732 0 0 0
cpu16 2986820 461216 1713616 1358498087 57070 0 78595 0 0 0
cpu17 3237062 535881 1958313 1358105734 28489 0 96591 0 0 0
cpu18 3369589 514312 1803562 1358173277 19922 0 84306 0 0 0
cpu19 3549778 463745 1800787 1358042397 20280 0 84833 0 0 0
cpu20 3170317 532727 1687825 1358480002 19311 0 77741 0 0 0
cpu21 3339694 487115 1738036 1358276442 36767 0 84697 0 0 0
cpu22 3372593 438781 1698389 1358339441 31767 0 83222 0 0 0
cpu23 14747775 863486 1410063 1346734628 20466 0 38194 0 0 0
intr 42530130019 127 0 0 0 0 0 0 0 1 0 1049867384 0 0 0 0 0 0 0 69219427 0 0 0 0 0 0 0 0 0 0 0 0 0 0 13191224 1848798 0 2 0 2 2 2 2 2 2 2 1 79824619 11830297 12505557 15492801 14400800 14923175 12603242 16334930 1 47676359 16031758 15562722 11354665 11875781 12661880 13650420 16954414 3439497940 0 2280097507 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
ctxt 375732950197
btime 1508280417
processes 21544588
procs_running 1
procs_blocked 0
softirq 26895216304 11 1229516596 10726619 1480282521 15596547 0 144214145 1033786896 0 1506256489
"""
re.findall('cpu[0-9].*?\n',test)
res = re.findall('cpu[0-9].*?\n',test)
r = res[0]
r
rsplit = r.strip().split(' ')
rsplit
sum([int(i) for i in rsplit[1:6]])
float(1261397893) / 1294483679
def calcCPU(statstr):
    slist = statstr.strip().split(' ')
    idle_time = float(slist[4])
    total_time = sum([int(i) for i in slit[1:6]])
    return (1 - idle_time / total_time)*100
calcCPU(res[1])
def calcCPU(statstr):
    slist = statstr.strip().split(' ')
    idle_time = float(slist[4])
    total_time = sum([int(i) for i in slist[1:6]])
    return (1 - idle_time / total_time)*100
calcCPU(res[1])
[calcCPU(r) for r in res]
t1 = """cpu  1540499633 32799089 192564650 33342575323 5826324 0 21378605 0 0 0
cpu0 33683823 1540325 8853175 1323122533 3945495 0 13943160 0 0 0
cpu1 126402219 1032575 11140627 1326937866 397130 0 291230 0 0 0
cpu2 132481277 1047927 11643593 1320098504 97037 0 295639 0 0 0
cpu3 133243220 1044372 10840514 1320170324 80062 0 288728 0 0 0
cpu4 131566657 1011610 10294903 1322596308 64970 0 270505 0 0 0
cpu5 130558239 971473 10195155 1323848782 73779 0 272224 0 0 0
cpu6 132457236 966370 10158978 1322018635 68213 0 257577 0 0 0
cpu7 131961584 972722 10121265 1322564214 55941 0 264677 0 0 0
cpu8 134400021 1013752 10589267 1319435071 54645 0 278222 0 0 0
cpu9 136839372 941745 10122793 1317503917 64594 0 264251 0 0 0
cpu10 137281954 955674 10136714 1317148689 71205 0 259577 0 0 0
cpu11 62274138 3983862 14786772 1383862273 185633 0 817218 0 0 0
cpu12 26420312 2773968 8538824 1429786517 140592 0 385585 0 0 0
cpu13 7356126 1599000 6479754 1452995412 39645 0 521708 0 0 0
cpu14 7708134 1411334 5982807 1453392886 34246 0 424860 0 0 0
cpu15 7686806 1422848 5870290 1453579746 38459 0 376287 0 0 0
cpu16 5611981 984420 3441561 1458598443 74115 0 213214 0 0 0
cpu17 6816246 1333744 5338798 1455098586 36184 0 387578 0 0 0
cpu18 6676771 1167920 4293383 1456631430 28304 0 249453 0 0 0
cpu19 7032190 1143551 4519808 1456040874 25659 0 272524 0 0 0
cpu20 7252289 1221029 4545271 1455712777 25806 0 248047 0 0 0
cpu21 6544961 1193686 4686130 1456272277 43526 0 302884 0 0 0
cpu22 6910881 1120430 4511783 1456191045 36653 0 293103 0 0 0
cpu23 21333187 1944740 5472476 1438968203 144420 0 200347 0 0 0
intr 23652306801 127 0 0 0 0 0 0 0 1 0 1130876808 0 0 0 0 0 0 0 75619275 0 0 0 0 0 0 0 0 0 0 0 0 0 0 16210479 2343270 0 2 0 2 2 2 2 2 2 2 1 84575625 12840800 28721867 17121181 15570982 20058291 39213944 17743459 1 59073776 17178250 16746771 18410563 19301050 14271585 15022905 18397607 1291671268 0 165975289 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
ctxt 490309923525
btime 1508280417
processes 24237578
procs_running 15
procs_blocked 0
softirq 56080626451 11 2396570821 24304207 190474188 19144466 0 162878938 4086912818 0 1955700746"""
t2 = """cpu  1540527255 32799914 192570147 33342633692 5826329 0 21379298 0 0 0
cpu0 33684269 1540342 8853306 1323124766 3945498 0 13943513 0 0 0
cpu1 126404798 1032619 11140929 1326938821 397130 0 291245 0 0 0
cpu2 132483436 1047968 11643877 1320099897 97038 0 295652 0 0 0
cpu3 133245619 1044412 10840797 1320171480 80062 0 288739 0 0 0
cpu4 131568961 1011650 10295197 1322597542 64970 0 270518 0 0 0
cpu5 130560359 971514 10195435 1323850212 73779 0 272235 0 0 0
cpu6 132459363 966410 10159248 1322020057 68213 0 257590 0 0 0
cpu7 131964074 972759 10121523 1322565311 55941 0 264688 0 0 0
cpu8 134402423 1013796 10589560 1319436212 54645 0 278234 0 0 0
cpu9 136841833 941782 10123058 1317505046 64594 0 264263 0 0 0
cpu10 137284473 955718 10137007 1317149705 71205 0 259591 0 0 0
cpu11 62274379 3983880 14786903 1383865751 185633 0 817225 0 0 0
cpu12 26420366 2773969 8538849 1429790362 140592 0 385585 0 0 0
cpu13 7357769 1599000 6480003 1452997450 39645 0 521708 0 0 0
cpu14 7708168 1411342 5982926 1453396647 34246 0 424864 0 0 0
cpu15 7686884 1422869 5870405 1453583443 38461 0 376296 0 0 0
cpu16 5612000 984533 3442145 1458601577 74115 0 213291 0 0 0
cpu17 6816260 1333775 5338943 1455102304 36184 0 387595 0 0 0
cpu18 6676827 1167924 4293424 1456635234 28304 0 249454 0 0 0
cpu19 7032192 1143555 4519839 1456044764 25659 0 272526 0 0 0
cpu20 7252328 1221167 4545922 1455715796 25806 0 248119 0 0 0
cpu21 6544982 1193714 4686257 1456276016 43526 0 302897 0 0 0
cpu22 6912254 1120433 4511948 1456193418 36653 0 293104 0 0 0
cpu23 21333230 1944772 5472634 1438971868 144420 0 200358 0 0 0
intr 23656339173 127 0 0 0 0 0 0 0 1 0 1130880732 0 0 0 0 0 0 0 75619520 0 0 0 0 0 0 0 0 0 0 0 0 0 0 16210548 2343312 0 2 0 2 2 2 2 2 2 2 1 84575932 12840940 28722033 17121374 15571114 20058503 39214134 17743736 1 59074125 17178522 16747187 18410916 19301338 14271839 15023155 18398135 1292341052 0 166556992 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
ctxt 490315642798
btime 1508280417
processes 24238229
procs_running 10
procs_blocked 0
softirq 56083580410 11 2396942894 24304239 192796889 19144577 0 162879465 4087097558 0 1955774521"""
output = t2
res = re.findall('cpu[0-9].*?\n',output)
res
res = [r.strip().split(' ') for r in res]
res
res = [[float(n) for n in r[1:]] for r in recs]
res = [[float(n) for n in r[1:]] for r in res]
res
def parseStatOutput(output):
    res = re.findall('cpu[0-9].*?\n',output)
    res = [r.strip().split(' ') for r in res]
    res = [[float(n) for n in r[1:]] for r in res]
    return res
res = parseStatOutput(t2)
res
def calcCPU(statlist):
    idle_time = float(statlist[4])
    total_time = sum([int(i) for i in statlist[1:6]])
    return (1 - idle_time / total_time)*100
import gc
gc.collect()
def parseStatOutput(output):
    res = re.findall('cpu[0-9].*?\n',output)
    res = [r.strip().split(' ') for r in res]
    res = [[float(n) for n in r[1:]] for r in res]
    return res
res1,res2 = t1,t2
cmd = ['cat', '/proc/stat']
stats1 = parseStatOutput(res1)
res2 = capOutput(cmd)
stats2 = parseStatOutput(res2)
difflist = []
for i,(s1,s2) in enumerate(zip(stats1,stats2)):
    idle_diff = float(s2[4] - s1[4])
    total_diff = float(sum(s2[1:6]) - sum(s1[1:6]))
    cpu = s1[0]
    util = idle_diff / total_diff
    difflist.append((cpu,util))
difflist
s1,s2 = zip(stats1,stats2)[0]
s1
s2
idle_diff = float(s2[4] - s1[4])
idle_diff
total_diff = float(sum(s2[1:6]) - sum(s1[1:6]))
total_diff
util = 1- idle_diff / total_diff
util
def parseStatOutput(output):
    res = re.findall('cpu[0-9].*?\n',output)
    res = [r.strip().split(' ') for r in res]
    names = [r[0] for r in res]
    res = [[float(n) for n in r[1:]] for r in res]
    return names, res
names,res = parseStatOutput(t1)
names
res
zip(names,res)
def getCPUUsage(waitTime=5):
    cmd = ['cat', '/proc/stat']
    res1 = capOutput(cmd)
    names, stats1 = parseStatOutput(res1)
    time.sleep(waitTime)
    res2 = capOutput(cmd)
    names, stats2 = parseStatOutput(res2)
    difflist = []
    for i,(cpu,s1,s2) in enumerate(zip(names,stats1,stats2)):
        idle_diff = float(s2[4] - s1[4])
        total_diff = float(sum(s2[1:6]) - sum(s1[1:6]))
        util = 1- idle_diff / total_diff
        difflist.append((cpu,util))
    return difflist
def parseStatOutput(output):
    res = re.findall('cpu[0-9].*?\n',output)
    res = [r.strip().split(' ') for r in res]
    names = [r[0] for r in res]
    res = [[float(n) for n in r[1:]] for r in res]
    return names, res
names, stats1 = parseStatOutput(res1)
names, stats2 = parseStatOutput(res2)
difflist = []
for i,(cpu,s1,s2) in enumerate(zip(names,stats1,stats2)):
    idle_diff = float(s2[4] - s1[4])
    total_diff = float(sum(s2[1:6]) - sum(s1[1:6]))
    util = 1- idle_diff / total_diff
    difflist.append((cpu,util))
difflist
t1 = "cpu  1542190331 32867498 192897151 33346361802 5826876 0 21415425 0 0 0
cpu0 33715634 1542929 8865856 1323259610 3945801 0 13960224 0 0 0
cpu1 126547418 1035210 11158775 1327018402 397132 0 292047 0 0 0
cpu2 132627892 1050548 11661579 1320177917 97038 0 296436 0 0 0
cpu3 133409510 1046806 10857227 1320231701 80062 0 289524 0 0 0
cpu4 131707136 1014280 10312875 1322681670 64972 0 271279 0 0 0
cpu5 130698130 974146 10212899 1323935051 73781 0 272985 0 0 0
cpu6 132597817 968915 10176756 1322104307 68214 0 258377 0 0 0
cpu7 132106073 975282 10139091 1322646028 55941 0 265478 0 0 0
cpu8 134544053 1016360 10607117 1319517160 54647 0 279018 0 0 0
cpu9 137000539 944143 10139548 1317571243 64594 0 265025 0 0 0
cpu10 137428989 958299 10154760 1317227619 71205 0 260365 0 0 0
cpu11 62302806 3994149 14806610 1384049164 185730 0 818563 0 0 0
cpu12 26455249 2776757 8549414 1429986017 140608 0 386156 0 0 0
cpu13 7368132 1600960 6490622 1453219185 39649 0 522671 0 0 0
cpu14 7723071 1413478 5993217 1453613991 34251 0 425743 0 0 0
cpu15 7706510 1424417 5880276 1453797248 38470 0 377073 0 0 0
cpu16 5621744 986398 3449096 1458827963 74149 0 214009 0 0 0
cpu17 6820526 1336309 5349387 1455329637 36193 0 388546 0 0 0
cpu18 6683436 1170402 4304728 1456859283 28318 0 250485 0 0 0
cpu19 7045612 1147234 4530771 1456261178 25667 0 273495 0 0 0
cpu20 7257286 1222526 4552954 1455947484 25818 0 248745 0 0 0
cpu21 6552292 1195600 4696238 1456501561 43534 0 303856 0 0 0
cpu22 6923250 1124214 4526596 1456408178 36655 0 294484 0 0 0
cpu23 21347212 1948126 5480750 1439190191 144437 0 200832 0 0 0
intr 23919800163 127 0 0 0 0 0 0 0 1 0 1131068695 0 0 0 0 0 0 0 75634817 0 0 0 0 0 0 0 0 0 0 0 0 0 0 16212020 2346030 0 2 0 2 2 2 2 2 2 2 1 84586557 12842754 28724012 17124424 15573425 20061722 39219013 17748246 1 59085094 17182444 16752105 18412354 19303935 14273703 15025125 18403532 1338741853 0 207064711 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
ctxt 490681131160
btime 1508280417
processes 24248585
procs_running 11
procs_blocked 0
softirq 56272712223 11 2418566087 24306207 347633575 19148824 0 162908578 4098272820 0 1957235865"
t1 = """cpu  1542190331 32867498 192897151 33346361802 5826876 0 21415425 0 0 0
cpu0 33715634 1542929 8865856 1323259610 3945801 0 13960224 0 0 0
cpu1 126547418 1035210 11158775 1327018402 397132 0 292047 0 0 0
cpu2 132627892 1050548 11661579 1320177917 97038 0 296436 0 0 0
cpu3 133409510 1046806 10857227 1320231701 80062 0 289524 0 0 0
cpu4 131707136 1014280 10312875 1322681670 64972 0 271279 0 0 0
cpu5 130698130 974146 10212899 1323935051 73781 0 272985 0 0 0
cpu6 132597817 968915 10176756 1322104307 68214 0 258377 0 0 0
cpu7 132106073 975282 10139091 1322646028 55941 0 265478 0 0 0
cpu8 134544053 1016360 10607117 1319517160 54647 0 279018 0 0 0
cpu9 137000539 944143 10139548 1317571243 64594 0 265025 0 0 0
cpu10 137428989 958299 10154760 1317227619 71205 0 260365 0 0 0
cpu11 62302806 3994149 14806610 1384049164 185730 0 818563 0 0 0
cpu12 26455249 2776757 8549414 1429986017 140608 0 386156 0 0 0
cpu13 7368132 1600960 6490622 1453219185 39649 0 522671 0 0 0
cpu14 7723071 1413478 5993217 1453613991 34251 0 425743 0 0 0
cpu15 7706510 1424417 5880276 1453797248 38470 0 377073 0 0 0
cpu16 5621744 986398 3449096 1458827963 74149 0 214009 0 0 0
cpu17 6820526 1336309 5349387 1455329637 36193 0 388546 0 0 0
cpu18 6683436 1170402 4304728 1456859283 28318 0 250485 0 0 0
cpu19 7045612 1147234 4530771 1456261178 25667 0 273495 0 0 0
cpu20 7257286 1222526 4552954 1455947484 25818 0 248745 0 0 0
cpu21 6552292 1195600 4696238 1456501561 43534 0 303856 0 0 0
cpu22 6923250 1124214 4526596 1456408178 36655 0 294484 0 0 0
cpu23 21347212 1948126 5480750 1439190191 144437 0 200832 0 0 0
intr 23919800163 127 0 0 0 0 0 0 0 1 0 1131068695 0 0 0 0 0 0 0 75634817 0 0 0 0 0 0 0 0 0 0 0 0 0 0 16212020 2346030 0 2 0 2 2 2 2 2 2 2 1 84586557 12842754 28724012 17124424 15573425 20061722 39219013 17748246 1 59085094 17182444 16752105 18412354 19303935 14273703 15025125 18403532 1338741853 0 207064711 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
ctxt 490681131160
btime 1508280417
processes 24248585
procs_running 11
procs_blocked 0
softirq 56272712223 11 2418566087 24306207 347633575 19148824 0 162908578 4098272820 0 1957235865"""
t2 = """cpu  1542193935 32867618 192897854 33346369164 5826877 0 21415496 0 0 0
cpu0 33715729 1542929 8865867 1323259875 3945801 0 13960254 0 0 0
cpu1 126547742 1035217 11158811 1327018537 397132 0 292048 0 0 0
cpu2 132628200 1050556 11661615 1320178055 97038 0 296438 0 0 0
cpu3 133409855 1046813 10857262 1320231811 80062 0 289525 0 0 0
cpu4 131707433 1014287 10312913 1322681824 64972 0 271280 0 0 0
cpu5 130698424 974152 10212938 1323935208 73781 0 272986 0 0 0
cpu6 132598110 968920 10176794 1322104463 68214 0 258378 0 0 0
cpu7 132106418 975287 10139132 1322646132 55941 0 265480 0 0 0
cpu8 134544351 1016366 10607156 1319517313 54647 0 279020 0 0 0
cpu9 137000879 944147 10139586 1317571360 64594 0 265026 0 0 0
cpu10 137429311 958305 10154799 1317227747 71205 0 260367 0 0 0
cpu11 62302810 3994166 14806686 1384049555 185730 0 818569 0 0 0
cpu12 26455547 2776757 8549449 1429986184 140608 0 386156 0 0 0
cpu13 7368133 1600960 6490622 1453219685 39649 0 522671 0 0 0
cpu14 7723087 1413478 5993219 1453614468 34251 0 425743 0 0 0
cpu15 7706511 1424417 5880276 1453797748 38470 0 377073 0 0 0
cpu16 5621744 986398 3449096 1458828464 74149 0 214009 0 0 0
cpu17 6820527 1336309 5349387 1455330138 36193 0 388546 0 0 0
cpu18 6683436 1170402 4304728 1456859783 28319 0 250485 0 0 0
cpu19 7045613 1147270 4530940 1456261455 25667 0 273512 0 0 0
cpu20 7257305 1222526 4552958 1455947962 25818 0 248745 0 0 0
cpu21 6552295 1195600 4696238 1456502059 43534 0 303856 0 0 0
cpu22 6923250 1124214 4526596 1456408679 36655 0 294484 0 0 0
cpu23 21347214 1948132 5480777 1439190647 144437 0 200834 0 0 0
intr 23920295619 127 0 0 0 0 0 0 0 1 0 1131070041 0 0 0 0 0 0 0 75634853 0 0 0 0 0 0 0 0 0 0 0 0 0 0 16212022 2346030 0 2 0 2 2 2 2 2 2 2 1 84586577 12842762 28724016 17124428 15573428 20061731 39219016 17748251 1 59085110 17182462 16752108 18412357 19303938 14273722 15025128 18403535 1338826887 0 207148032 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
ctxt 490681817451
btime 1508280417
processes 24248587
procs_running 21
procs_blocked 0
softirq 56273112673 11 2418612221 24306211 347960759 19148826 0 162908706 4098298362 0 1957237321"""
names, stats1 = parseStatOutput(res1)
names, stats2 = parseStatOutput(res2)
difflist = []
i,cpu,s1,s1 = 0,zip(names,stats1,stats2)[0]
names
zip(stats1,stats2)
difflist = []
for i,(cpu,s1,s2) in enumerate(zip(names,stats1,stats2)):
    idle_diff = float(s2[3] - s1[3])
    total_diff = float(sum(s2[1:6]) - sum(s1[1:6]))
    util = 1- idle_diff / total_diff
    difflist.append((cpu,util))
difflist
def getCPUUsage(waitTime=5):
    cmd = ['cat', '/proc/stat']
    res1 = capOutput(cmd)
    names, stats1 = parseStatOutput(res1)
    time.sleep(waitTime)
    res2 = capOutput(cmd)
    names, stats2 = parseStatOutput(res2)
    difflist = []
    for i,(cpu,s1,s2) in enumerate(zip(names,stats1,stats2)):
        idle_diff = float(s2[3] - s1[3])
        total_diff = float(sum(s2[1:6]) - sum(s1[1:6]))
        util = 1- idle_diff / total_diff
        util2 = 100*(total_diff-idle_diff)/total_diff
        difflist.append((cpu,util,util2))
    return difflist

## ---(Thu Apr  5 21:58:38 2018)---
test = """
cpu  721438593 12391128 87794678 31807433600 5081858 0 10279678 0 0 0
cpu0 24478817 607118 4348887 1261397893 3650964 0 8094909 0 0 0
cpu1 51701651 322793 6019246 1303138746 376937 0 98092 0 0 0
cpu2 59869892 319732 6256548 1294532386 82798 0 88321 0 0 0
cpu3 60322041 313199 5526065 1294813050 74173 0 83715 0 0 0
cpu4 57461280 326395 5317550 1297981049 60751 0 82691 0 0 0
cpu5 56633447 290500 5153691 1299130854 69713 0 82410 0 0 0
cpu6 57605769 311312 5291612 1297979710 64473 0 81561 0 0 0
cpu7 57060066 303720 5152027 1298699328 52723 0 81468 0 0 0
cpu8 61155703 303997 5346863 1294295247 51310 0 84232 0 0 0
cpu9 60470039 293826 5302396 1294920334 61727 0 83190 0 0 0
cpu10 60349928 311154 5332700 1295106733 68242 0 82930 0 0 0
cpu11 52587560 1559461 5748451 1301864731 63492 0 232270 0 0 0
cpu12 13336031 1153389 2678998 1346341826 83933 0 107121 0 0 0
cpu13 3735781 626665 2390127 1356999208 30478 0 153138 0 0 0
cpu14 3456937 514405 1994356 1357861254 24352 0 108707 0 0 0
cpu15 3440013 536187 2124562 1357721231 31710 0 106732 0 0 0
cpu16 2986820 461216 1713616 1358498087 57070 0 78595 0 0 0
cpu17 3237062 535881 1958313 1358105734 28489 0 96591 0 0 0
cpu18 3369589 514312 1803562 1358173277 19922 0 84306 0 0 0
cpu19 3549778 463745 1800787 1358042397 20280 0 84833 0 0 0
cpu20 3170317 532727 1687825 1358480002 19311 0 77741 0 0 0
cpu21 3339694 487115 1738036 1358276442 36767 0 84697 0 0 0
cpu22 3372593 438781 1698389 1358339441 31767 0 83222 0 0 0
cpu23 14747775 863486 1410063 1346734628 20466 0 38194 0 0 0
intr 42530130019 127 0 0 0 0 0 0 0 1 0 1049867384 0 0 0 0 0 0 0 69219427 0 0 0 0 0 0 0 0 0 0 0 0 0 0 13191224 1848798 0 2 0 2 2 2 2 2 2 2 1 79824619 11830297 12505557 15492801 14400800 14923175 12603242 16334930 1 47676359 16031758 15562722 11354665 11875781 12661880 13650420 16954414 3439497940 0 2280097507 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
ctxt 375732950197
btime 1508280417
processes 21544588
procs_running 1
procs_blocked 0
softirq 26895216304 11 1229516596 10726619 1480282521 15596547 0 144214145 1033786896 0 1506256489
"""
output = test
re.findall('cpu[0-9].*?\n',output)
import re
res = re.findall('cpu[0-9].*?\n',output)
res
res = re.findall('cpu.*?\n',output)
res
res = [r.strip().split(' ') for r in res]
names = [r[0] for r in res]
res = [[float(n) for n in r[1:]] for r in res]
res
res[0]
re.findall('cpu.*?\n',output)
res = re.findall('cpu.*?\n',output)
res = [r.strip().split(' ') for r in res]
res[0][0]
res[0][1]
res[0].remove('')
res[0]
t1 = """              total        used        free      shared  buff/cache   available
Mem:       98718252    42606408      655704      233736    55456140    55088896
Swap:       4194300      705616     3488684"""
re.findall('[0-9]+',t1)
def get_file_from_remote_server(remote_ip, remote_uname, remote_passwd, src, dest, logfile=None):
    """ use scp to get file from remote server """
    child = pexpect.spawn('scp -r %s@%s:%s %s' % (remote_uname, remote_ip, src, dest ))
    try:
        child.logfile = open(logfile, "a")
    except Exception,e:
        child.logfile = None
    child.expect('assword:*')
    child.sendline(remote_passwd+'\r')
    try:
        child.expect(pexpect.EOF)
    except Exception,e:
        print("Import error, error : '%s'" % str(e))
        return False
    else:
        return True
get_file_from_remote_server('ivy-mv5g-bulwark.hpc.virginia.edu','bea3ch','Br#nD0$!','/home/bea3ch/shared/trafficAnalysis/trafficStats_em2.txt','./')
import pexpect
get_file_from_remote_server('ivy-mv5g-bulwark.hpc.virginia.edu','bea3ch','Br#nD0$!','/home/bea3ch/shared/trafficAnalysis/trafficStats_em2.txt','./')
import os
os.system('./copy_netstats.sh')
os.system('../copy_netstats.sh')
def get_data(local_dir="./", interface="em2"):
    subprocess.call(['./copy_netstats.sh'])
import subprocess
get_data()
os.getcwd()
os.chdir('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis')
get_data()
os.system('./copy_netstats.sh')
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis')
get_bro_perf()
interface="em2"
df = pd.DataFrame.from_csv('trafficStats_'+interface+'.txt')
df
df.columns
df['packetLoss']
df = pd.read_csv('trafficStats_'+interface+'.txt', index_col = False)
df
df['packetLoss']
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis')
get_bro_perf()
df['packetLoss'].max
df['packetLoss'].max()
df = get_data(interface='em1')
get_data(interface='em1')
res = get_data(interface='em1')
res
get_bro_perf(interface='em2')
res = get_bro_perf()
max(res['time'])
res
res['cpu']
def make_plot(df, measures=['packetLoss','throughouput']):    
    fig=plt.figure(figsize=(8,6))     
    ax1 = fig.add_subplot(111)           
    ax1.plot(df['time'], df[measures[0]], 'b-', label='Packet Drop Rate')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Packet Drop Rate', color='b')
    ax1.tick_params('y', colors='b')
    if len(measures) > 1:
        ax2 = ax1.twinx()
        ax2.plot(df['time'], df[measures[1]], 'r', label = 'Utilization (Gbps)')
        ax2.set_ylabel('Utilization (Gbps)', color='r')
        ax2.tick_params('y', colors='r')
        lgd=ax1.legend(loc='upper left',bbox_to_anchor=(1,1))
        fig.savefig('packet_drop_utilization.png',bbox_extra_artists=(lgd,), 
                    bbox_inches='tight',dpi=100)
make_plot(res, ['packetLoss', 'cpu'])
res.filter(reges='cpu*')
res.filter(regex='cpu*')
res['cpu'].max
res['cpu'].max()
res['maxCpu'] = res.filter(regex='cpu*').max()
res['maxCpu']
res['maxCpu'] = max(res.filter(regex='cpu*'))
res['maxCpu']
res['maxCpu'] = res.apply(lambda row: max(row.filter(regex='cpu*')), axis=1)
res['maxCpu']
make_plot(df,['packetLoss','maxCpu'])
make_plot(df,['maxCpu'])
make_plot(res,['maxCpu'])
make_plot(res,['packetLoss','maxCpu'])
def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client
server = 'ivy-mv5g-bulwark.hpc.virginia.edu'
port=22
user = 'bea3ch'
password='Br#nD0$!'
ssh = createSSHClient(server, port, user, password)
scp = SCPClient(ssh.get_transport())
scp.get(r'/home/bea3ch/shared/trafficAnalysis/trafficStats_em2.txt', r'./')
import paramiko
from scp import SCPClient
from scp import SCPClient
server = 'ivy-mv5g-bulwark.hpc.virginia.edu'
port=22
user = 'bea3ch'
password='Br#nD0$!'
ssh = createSSHClient(server, port, user, password)
scp = SCPClient(ssh.get_transport())
scp.get(r'/home/bea3ch/shared/trafficAnalysis/trafficStats_em2.txt', r'./')

## ---(Fri Apr  6 15:12:54 2018)---
runfile('/Users/babraham/Google Drive/Grad_School/Cyber_Research/Anomaly-based-Intrusion-Detection-System/Code/Preprocessing/parse_conn_logs.py', wdir='/Users/babraham/Google Drive/Grad_School/Cyber_Research/Anomaly-based-Intrusion-Detection-System/Code/Preprocessing')
os.getcwd()
os.chdir('/Users/babraham/Downloads')
os.chdir('em2_logs_03-25')
os.listdir('.')
res = _parse_conn('conn.20:00:00-21:00:00.log')
from tqdm import tqdm
runfile('/Users/babraham/Google Drive/Grad_School/Cyber_Research/Anomaly-based-Intrusion-Detection-System/Code/Preprocessing/parse_conn_logs.py', wdir='/Users/babraham/Google Drive/Grad_School/Cyber_Research/Anomaly-based-Intrusion-Detection-System/Code/Preprocessing')
res = _parse_conn('conn.20:00:00-21:00:00.log')
import bat
bro_df = LogToDataFrame('/dns.20:00:00-21:00:00.log')
from bat.log_to_dataframe import LogToDataFrame
bro_df = LogToDataFrame('/dns.20:00:00-21:00:00.log')
bro_df = LogToDataFrame('dns.20/00/00-21/00/00')
bro_df = LogToDataFrame('dns.20/00/00-21/00/00.log')
res = _parse_conn('splitFile/xaa.csv')
os.getcwd()
os.chdir('~/Downloads')
os.chdir('/Users/babraham/Downloads')
os.chdir('em2_logs_03_25')
os.listdir('.')
os.chdir('em2_logs_03-25')
res = _parse_conn('/splitFile/xaa.csv')
os.listdir('.')
os.listdir('splitFile')
res = _parse_conn('splitFile/xaa.csv')
res
res.columns
dns_dfd = LogToDataFrame('splitFile/ssl.test.log')
os.listdir('splitFile')
dns_dfd = LogToDataFrame('ssl.test.log')
ssl_df = dns_dfd
del(dns_dfd)
ssl_df.columns
ssl_df.columns.tolist()
base_cols = id_cols.remove('proto')
base_cols
base_cols = id_cols.pop('proto')
id_cols[:-1]
id_cols
id_cols = ['id.orig_h', 'id.resp_h', 'id.orig_p', 'id.resp_p', 'proto']
imp_fields = {}
imp_fields['conn'] = base_fields + ['orig_bytes', 'orig_pkts', 'proto', 'resp_bytes', 'resp_pkts', 'history', 'duration', 'service']
base_fields = id_cols[:-1] + ['uid']
base_fields
imp_fields['conn'] = base_fields + ['orig_bytes', 'orig_pkts', 'proto', 'resp_bytes', 'resp_pkts', 'history', 'duration', 'service']
imp_fields['conn']
del(ssl_df)
http_df = LogToDataFrame('http.test.log')
http_df.columns.tolist()
dns = LogToDataFrame('dns.test.log')
dns.columns.tolist()
del(dns)
smtp = LogToDataFrame('smtp.test.log')
smtp.columns.tolist()
smtp.head()
smtp.head(20)
smtp.describe()
smtp.columns.tolist()
smtp['tls']
smtp['rcpto']
smtp['rcptto']
smtp['reply_to']
smtp['x_originating_ip']
smtp['to']
smtp['second_received']
del(smtp)
smnp = LogToDataFrame('smnp.test.log')
smnp.shape
smnp
imp_fields = {}
imp_fields['conn'] = base_fields + ['orig_bytes', 'orig_pkts', 'proto', 'resp_bytes', 'resp_pkts', 'history', 'duration', 'service']
imp_fields['http'] = base_fields +  ['info_code','info_msg','method', 'orig_filenames','orig_mime_types','proxied','referrer','request_body_len','resp_filenames','response_body_len','status_code','status_msg','trans_depth','uri','user_agent','version']
imp_fields['dns'] = base_fields + ['AA','RA','RD','TC','TTLs','Z','answers','qclass','qclass_name','qtype','qtype_name','query','rcode','rcode_name','rejected','rtt','trans_id']
imp_fields['ssl'] = base_fields + ['cert_chain_fuids','cipher','client_cert_chain_fuids','client_issuer','client_subject','curve','established','issuer','last_alert','next_protocol','resumed','server_name','subject','validation_status','version']
imp_fields['smtp'] = base_fields + ['cc','date','first_received','from','helo','in_reply_to','is_webmail','last_reply','mailfrom','msg_id','path','rcptto','reply_to','subject','to','user_agent','x_originating_ip']
typ = "conn"
assert typ in fields.keys()
fields = {}
fieilds['conn'] = base_fields + ['orig_bytes', 'orig_pkts', 'proto', 'resp_bytes', 'resp_pkts', 'history', 'duration', 'service']
fields['http'] = base_fields +  ['info_code','info_msg','method', 'orig_filenames','orig_mime_types','proxied','referrer','request_body_len','resp_filenames','response_body_len','status_code','status_msg','trans_depth','uri','user_agent','version']
fields['dns'] = base_fields + ['AA','RA','RD','TC','TTLs','Z','answers','qclass','qclass_name','qtype','qtype_name','query','rcode','rcode_name','rejected','rtt','trans_id']
fields['ssl'] = base_fields + ['cert_chain_fuids','cipher','client_cert_chain_fuids','client_issuer','client_subject','curve','established','issuer','last_alert','next_protocol','resumed','server_name','subject','validation_status','version']
fields['smtp'] = base_fields + ['cc','date','first_received','from','helo','in_reply_to','is_webmail','last_reply','mailfrom','msg_id','path','rcptto','reply_to','subject','to','user_agent','x_originating_ip']
base_fields = id_cols[:-1] + ['uid']
fields = {}
fields['conn'] = base_fields + ['orig_bytes', 'orig_pkts', 'proto', 'resp_bytes', 'resp_pkts', 'history', 'duration', 'service']
fields['http'] = base_fields +  ['info_code','info_msg','method', 'orig_filenames','orig_mime_types','proxied','referrer','request_body_len','resp_filenames','response_body_len','status_code','status_msg','trans_depth','uri','user_agent','version']
fields['dns'] = base_fields + ['AA','RA','RD','TC','TTLs','Z','answers','qclass','qclass_name','qtype','qtype_name','query','rcode','rcode_name','rejected','rtt','trans_id']
fields['ssl'] = base_fields + ['cert_chain_fuids','cipher','client_cert_chain_fuids','client_issuer','client_subject','curve','established','issuer','last_alert','next_protocol','resumed','server_name','subject','validation_status','version']
fields['smtp'] = base_fields + ['cc','date','first_received','from','helo','in_reply_to','is_webmail','last_reply','mailfrom','msg_id','path','rcptto','reply_to','subject','to','user_agent','x_originating_ip']
assert typ in fields.keys()
typ = 'vag'
assert typ in fields.keys()
def _parse_log(logfile, outputDir="", fromStr=False, typ="conn"):
    typ = typ.strip().lower()
    assert typ in fields.keys() 
    if fromStr:
        lines = logfile.split('\n')
    else:
        with open(logfile, 'r') as f:
            lines = f.readlines()
    fieldlist = []
    for l in lines[1:10]:
        if '#fields' in l: fieldlist = l.split('\t')
    imp_fields = fields[typ]
    fields = {fieldlist[i]:i-1 for i in range(len(fieldlist))}
    imp_inds = [fields[fi] for fi in imp_fields]
    recs = []
    for l in tqdm(lines[8:len(lines)-2]):
        lsplit = l.split('\t')
        values = [lsplit[i] for i in imp_inds]
        for i in range(len(values)):
            if values[i] == '-': values[i] = '0'
        rec = dict(zip(imp_fields, values))
        if typ == 'conn':
            if rec['proto'] != 'icmp':
                rec['hash'] = ','.join([rec['id.orig_h'],rec['id.resp_h'],rec['id.resp_p'],rec['proto']])
                flags = _parse_history(rec['history'], keys=True)
                rec.update(flags)
                recs.append(rec)
    fieldNames = recs[0].keys()
    df = pd.DataFrame(recs, columns=fieldNames)
    return df
res = _parse_log('http.test.log')
def _parse_log(logfile, outputDir="", fromStr=False, typ="conn"):
    global fields
    typ = typ.strip().lower()
    assert typ in fields.keys() 
    if fromStr:
        lines = logfile.split('\n')
    else:
        with open(logfile, 'r') as f:
            lines = f.readlines()
    fieldlist = []
    for l in lines[1:10]:
        if '#fields' in l: fieldlist = l.split('\t')
    imp_fields = fields[typ]
    all_fields = {fieldlist[i]:i-1 for i in range(len(fieldlist))}
    imp_inds = [all_fields[fi] for fi in imp_fields]
    recs = []
    for l in tqdm(lines[8:len(lines)-2]):
        lsplit = l.split('\t')
        values = [lsplit[i] for i in imp_inds]
        for i in range(len(values)):
            if values[i] == '-': values[i] = '0'
        rec = dict(zip(imp_fields, values))
        if typ == 'conn':
            if rec['proto'] != 'icmp':
                rec['hash'] = ','.join([rec['id.orig_h'],rec['id.resp_h'],rec['id.resp_p'],rec['proto']])
                flags = _parse_history(rec['history'], keys=True)
                rec.update(flags)
                recs.append(rec)
    fieldNames = recs[0].keys()
    df = pd.DataFrame(recs, columns=fieldNames)
    return df
res = _parse_log('http.test.log')
imp_fields
res = _parse_log('http.test.log', typ='http')
recs
f _parse_log(logfile, outputDir="", fromStr=False, typ="conn"):
    global fields
    typ = typ.strip().lower()
    assert typ in fields.keys() 
    if fromStr:
        lines = logfile.split('\n')
    else:
        with open(logfile, 'r') as f:
            lines = f.readlines()
    fieldlist = []
    for l in lines[1:10]:
        if '#fields' in l: fieldlist = l.split('\t')
    imp_fields = fields[typ]
    all_fields = {fieldlist[i]:i-1 for i in range(len(fieldlist))}
    imp_inds = [all_fields[fi] for fi in imp_fields]
    recs = []
    for l in tqdm(lines[8:len(lines)-2]):
        lsplit = l.split('\t')
        values = [lsplit[i] for i in imp_inds]
        for i in range(len(values)):
            if values[i] == '-': values[i] = '0'
        rec = dict(zip(imp_fields, values))
        if typ == 'conn':
            if rec['proto'] != 'icmp':
                rec['hash'] = ','.join([rec['id.orig_h'],rec['id.resp_h'],rec['id.resp_p'],rec['proto']])
                flags = _parse_history(rec['history'], keys=True)
                rec.update(flags)
                recs.append(rec)
fromStr=False
outputDir=""
logfile='http.test.log'
global fields
typ = typ.strip().lower()
assert typ in fields.keys() 
if fromStr:
    lines = logfile.split('\n')
else:
    with open(logfile, 'r') as f:
        lines = f.readlines()

fieldlist = []
for l in lines[1:10]:
    if '#fields' in l: fieldlist = l.split('\t')

imp_fields = fields[typ]
all_fields = {fieldlist[i]:i-1 for i in range(len(fieldlist))}
imp_inds = [all_fields[fi] for fi in imp_fields]
recs = []
for l in tqdm(lines[8:len(lines)-2]):
    lsplit = l.split('\t')
    values = [lsplit[i] for i in imp_inds]
    for i in range(len(values)):
        if values[i] == '-': values[i] = '0'
    rec = dict(zip(imp_fields, values))
    if typ == 'conn':
        if rec['proto'] != 'icmp':
            rec['hash'] = ','.join([rec['id.orig_h'],rec['id.resp_h'],rec['id.resp_p'],rec['proto']])
            flags = _parse_history(rec['history'], keys=True)
            rec.update(flags)
            recs.append(rec)
typ
typ = 'http'
global fields
typ = typ.strip().lower()
assert typ in fields.keys() 
if fromStr:
    lines = logfile.split('\n')
else:
    with open(logfile, 'r') as f:
        lines = f.readlines()

fieldlist = []
for l in lines[1:10]:
    if '#fields' in l: fieldlist = l.split('\t')

imp_fields = fields[typ]
all_fields = {fieldlist[i]:i-1 for i in range(len(fieldlist))}
imp_inds = [all_fields[fi] for fi in imp_fields]
recs = []
for l in tqdm(lines[8:len(lines)-2]):
    lsplit = l.split('\t')
    values = [lsplit[i] for i in imp_inds]
    for i in range(len(values)):
        if values[i] == '-': values[i] = '0'
    rec = dict(zip(imp_fields, values))
    if typ == 'conn':
        if rec['proto'] != 'icmp':
            rec['hash'] = ','.join([rec['id.orig_h'],rec['id.resp_h'],rec['id.resp_p'],rec['proto']])
            flags = _parse_history(rec['history'], keys=True)
            rec.update(flags)
            recs.append(rec)
recs
for l in tqdm(lines[8:len(lines)-2]):
    lsplit = l.split('\t')
    values = [lsplit[i] for i in imp_inds]
    for i in range(len(values)):
        if values[i] == '-': values[i] = '0'
    rec = dict(zip(imp_fields, values))
    if typ == 'conn':
        if rec['proto'] != 'icmp':
            rec['hash'] = ','.join([rec['id.orig_h'],rec['id.resp_h'],rec['id.resp_p'],rec['proto']])
            flags = _parse_history(rec['history'], keys=True)
            rec.update(flags)
    recs.append(rec)
fieldNames = recs[0].keys()
df = pd.DataFrame(recs, columns=fieldNames)
del(df,recs)
res = _parse_log('http.test.log',typ='http')
runfile('/Users/babraham/Google Drive/Grad_School/Cyber_Research/Anomaly-based-Intrusion-Detection-System/Code/Preprocessing/parse_conn_logs.py', wdir='/Users/babraham/Google Drive/Grad_School/Cyber_Research/Anomaly-based-Intrusion-Detection-System/Code/Preprocessing')
res = _parse_log('http.test.log',typ='http')
os.getcwd()
os.chdir('/Users/babraham/Downloads/em2_logs_03-25')
res = _parse_log('http.test.log',typ='http')
res = _parse_log('ssl.test.log',typ='ssl')
res = _parse_log('smtp.test.log',typ='smtp')
res = _parse_log('dns.test.log',typ='dns')
logfile = 'dns.test.log'
typ='dns'
global fields
typ = typ.strip().lower()
assert typ in fields.keys() 
if fromStr:
    lines = logfile.split('\n')
else:
    with open(logfile, 'r') as f:
        lines = f.readlines()

fieldlist = []
for l in lines[1:10]:
    if '#fields' in l: fieldlist = l.split('\t')
imp_fields = fields[typ]
imp_fields
all_fields = {fieldlist[i]:i-1 for i in range(len(fieldlist))}
all_fields
[all_fields[fi] for fi in imp_fields]
for l in lines[1:10]:
    if '#fields' in l: fieldlist = l.split('\t')

imp_fields = fields[typ]
all_fields = {fieldlist[i].strip():i-1 for i in range(len(fieldlist))}
imp_inds = [all_fields[fi] for fi in imp_fields]
recs = []
res = _parse_log('dns.test.log', typ='dns')
typ = typ.strip().lower()
assert typ in fields.keys() 
if fromStr:
    lines = logfile.split('\n')
else:
    with open(logfile, 'r') as f:
        lines = f.readlines()

fieldlist = []
for l in lines[1:10]:
    if '#fields' in l: fieldlist = l.split('\t')

imp_fields = fields[typ]
all_fields = {fieldlist[i].strip():i-1 for i in range(len(fieldlist))}
all_fields
imp_inds = [all_fields[fi] for fi in imp_fields]
recs = []
for l in tqdm(lines[8:len(lines)-2]):
    lsplit = l.split('\t')
    values = [lsplit[i] for i in imp_inds]
    for i in range(len(values)):
        if values[i] == '-': values[i] = '0'
    rec = dict(zip(imp_fields, values))
    if typ == 'conn':
        if rec['proto'] != 'icmp':
            rec['hash'] = ','.join([rec['id.orig_h'],rec['id.resp_h'],rec['id.resp_p'],rec['proto']])
            flags = _parse_history(rec['history'], keys=True)
            rec.update(flags)
    recs.append(rec)
del(recs)
def _parse_log(logfile, outputDir="", fromStr=False, typ="conn"):
    global fields
    typ = typ.strip().lower()
    assert typ in fields.keys() 
    if fromStr:
        lines = logfile.split('\n')
    else:
        with open(logfile, 'r') as f:
            lines = f.readlines()
    fieldlist = []
    for l in lines[1:10]:
        if '#fields' in l: fieldlist = l.split('\t')
    imp_fields = fields[typ]
    all_fields = {fieldlist[i].strip():i-1 for i in range(len(fieldlist))}
    imp_inds = [all_fields[fi] for fi in imp_fields]
    recs = []
    for l in tqdm(lines[8:len(lines)-2]):
        lsplit = l.split('\t')
        values = [lsplit[i] for i in imp_inds]
        for i in range(len(values)):
            if values[i] == '-': values[i] = '0'
        rec = dict(zip(imp_fields, values))
        if typ == 'conn':
            if rec['proto'] != 'icmp':
                rec['hash'] = ','.join([rec['id.orig_h'],rec['id.resp_h'],rec['id.resp_p'],rec['proto']])
                flags = _parse_history(rec['history'], keys=True)
                rec.update(flags)
        recs.append(rec)
    fieldNames = recs[0].keys()
    df = pd.DataFrame(recs, columns=fieldNames)
    return df
res = _parse_log('dns.test.log',typ='dns')
res = _parse_log('ssl.test.log',typ='dns')
res = _parse_log('smtp.test.log',typ='dns')
res = _parse_log('smtp.test.log',typ='smtp')
res = _parse_log('ssl.test.log',typ='ssl')
def _parse_log(logfile, outputDir="", fromStr=False, typ=None):
    global fields
    if typ:
        typ = typ.strip().lower()
    else:
        typ = ""
        for i,t in enumerate(fields.keys()):
            if t in logfile.lower(): typ = t
    
    assert typ in fields.keys() 
    if fromStr:
        lines = logfile.split('\n')
    else:
        with open(logfile, 'r') as f:
            lines = f.readlines()
    fieldlist = []
    for l in lines[1:10]:
        if '#fields' in l: fieldlist = l.split('\t')
    imp_fields = fields[typ]
    all_fields = {fieldlist[i].strip():i-1 for i in range(len(fieldlist))}
    imp_inds = [all_fields[fi] for fi in imp_fields]
    recs = []
    for l in tqdm(lines[8:len(lines)-2]):
        lsplit = l.split('\t')
        values = [lsplit[i] for i in imp_inds]
        for i in range(len(values)):
            if values[i] == '-': values[i] = '0'
        rec = dict(zip(imp_fields, values))
        if typ == 'conn':
            if rec['proto'] != 'icmp':
                rec['hash'] = ','.join([rec['id.orig_h'],rec['id.resp_h'],rec['id.resp_p'],rec['proto']])
                flags = _parse_history(rec['history'], keys=True)
                rec.update(flags)
        recs.append(rec)
    fieldNames = recs[0].keys()
    df = pd.DataFrame(recs, columns=fieldNames)
    return df
res = _parse_log('ssl.test.log')
import os
os.stat('http.test.log')
f = open('http.test.log', 'r')
lines = f.readlines()
len(lines)
del(lines)
del(f)
def _split(logfile, l=None, n=None):
    assert l or n
    if n:
        with open(logfile, 'r') as f:
            for i,line in enumerate(f): pass
        lc = i+1
        sub_lc = lc / n
    else: sub_lc = l   
    sub_idx = 0
    subfile = re.sub('\.log', '_{}.log'.format(sub_idx), logfile)
    out = open(subfile, 'w')
    with open(logfile, 'r') as f:
        for i,line in enumerate(f):
            if i > sub_lc:
                out.close()
                sub_idx +=1
                subfile = re.sub('\.log', '_{}.log'.format(sub_idx), logfile)
                out = open(subfile, 'w')
            out.write(line)
_split('http.test.log', n=5)

## ---(Sat Apr  7 13:43:52 2018)---
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/parse_conn_logs.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work')
os.chdir('/Users/babraham/Downloads/em2_logs_03-25')
logfile = 'http.old.log'
with open(logfile, 'r') as f:
    for i,l in enumerate(f):
        pass

sub_lc = i+1
sub_lc
sub_lc = i+1 / n
n=5
sub_lc = i+1 / n
sub_lc
sub_lc = (i+1) / n
sub_lc
396842 % 79638
10 % 2
10 % 8
def _split(logfile, l=None, n=None):
    assert l or n
    if n:
        with open(logfile, 'r') as f:
            for i,l in enumerate(f):
                pass
        sub_lc = (i+1) / n
    else: sub_lc = l
    sub_idx = 0
    subname = re.sub('\.log', '_{}.log'.format(sub_idx),logfile)
    out = open(subname, 'w')
    with open(logfile, 'r') as f:
        for i,l in enumerate(f):
            if i % sub_lc == 0:
                out.close()
                sub_idx +=1
                subname = re.sub('\.log', '_{}.log'.format(sub_idx),logfile)
                out = open(subname, 'w')
            out.write(l)
res = _split('http.test.log', n=3)
files = os.listdir('.')
files
re.findall('http.test.*\.log', '#'.join(files))
re.findall('http.test.*?#', '#'.join(files))
def _split(logfile, l=None, n=None):
    assert l or n
    print('counting lines...')
    with open(logfile, 'r') as f:
        for i,l in enumerate(f): pass
        tot_lines = (i+1)
    if n:
        sub_lc = tot_lines / n      
    else:
        sub_lc = l
        n = tot_lines / sub_lc
    sub_idx = 0
    subname = re.sub('\.log', '_{}.log'.format(sub_idx),logfile)
    out = open(subname, 'w')
    with open(logfile, 'r') as f:
        for i,l in enumerate(f):
            if (i+1) % sub_lc == 0 and sub_idx < n:
                out.close()
                sub_idx +=1
                subname = re.sub('\.log', '_{}.log'.format(sub_idx),logfile)
                out = open(subname, 'w')
            out.write(l)
res = _split('http.old.test', n=5)
res = _split('http.old.log', n=5)
_split('conn.test.log', n=15)
def _split(logfile, l=None, n=None):
    assert l or n
    print('spliting file {}...'.format(logfile))
    with open(logfile, 'r') as f:
        for i,l in enumerate(f): pass
        tot_lines = (i+1)
    if n:
        sub_lc = tot_lines / n      
    else:
        sub_lc = l
        n = tot_lines / sub_lc
    sub_idx = 0
    subname = re.sub('\.log', '_{}.log'.format(sub_idx),logfile)
    out = open(subname, 'w')
    preamble = []
    with open(logfile, 'r') as f:
        for i,l in enumerate(f):
            if i < 8:
                preamble.append(l)
            if (i+1) % sub_lc == 0 and sub_idx < n:
                out.close()
                sub_idx +=1
                subname = re.sub('\.log', '_{}.log'.format(sub_idx),logfile)
                out = open(subname, 'w')
                out.write(''.join(preamble))
            out.write(l)
_split('conn.test.log')
_split('conn.test.log',n=15)
res = _parse_conn('conn.test_0.log')
res = _parse_conn('conn.test.log')
res = _parse_log('conn.test.0.log')
res = _parse_log('conn.test_0.log')
dfs = []
del(res)
for i in range(3):
    dfs.append(parse_log('conn.test_{}.log'.format(i)))
    
for i in range(3):
    dfs.append(_parse_log('conn.test_{}.log'.format(i)))
    
dfs[0].head()
del(dfs)
for i in range(3):
    dfs.append(_parse_log('conn.test_{}.log'.format(i)))
    
dfs = []
for i in range(15):
    dfs.append(_parse_log('conn.test_{}.log'.format(i)))
    
df = pd.concat(dfs)
del(df)
df = dfs[0]
for i in range(1:3):
for i in range(1,3):
    df = pd.concat(df, dfs[i])
    
for i in range(1,3):
    df = pd.concat([df, dfs[i]])
    
dire = '.'
files = os.listdir(dire)
files
re.findall('(conn.test_.*)#','#'.join(files))
re.findall('(conn.test_.*?)#','#'.join(files))
logfile = 'conn.test.log'
files = os.listdir(dire)
fpat = re.sub('\.log','',logfile)
subfiles = re.findall('({}.*?)#'.format(fpat),'#'.join(files))
subfiles
logfile in subfiles

## ---(Sat Apr  7 19:57:03 2018)---
def _split(logfile, l=None, n=None):
    assert l or n
    print('counting lines...')
    with open(logfile, 'r') as f:
        for i,l in enumerate(f): pass
        tot_lines = (i+1)
    if n: sub_lc = tot_lines / n      
    else:
        sub_lc = l
        n = tot_lines / sub_lc
    sub_idx = 0
    subname = re.sub('\.log', '_{}.log'.format(sub_idx),logfile)
    out = open(subname, 'w')
    metadata = []
    with open(logfile, 'r') as f:
        for i,l in enumerate(f):
            if i < 8:
                metadata.append(l)
            if (i+1) % sub_lc == 0 and sub_idx < n:
                out.close()
                sub_idx +=1
                subname = re.sub('\.log', '_{}.log'.format(sub_idx),logfile)
                out = open(subname, 'w')
                out.write(''.join(metadata))
            out.write(l)
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/parse_conn_logs.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work')
os.chdir('~/Downloads/em2_logs_03-25'
)
os.chdir('/Users/babraham/Downloads/em2_logs_03-25')
dire = '.'
logfile='conn.test.log'
files = os.listdir(dire)
fpat = re.sub('\.log', '', logfile)
subfiles = re.findall('{}_.*?#'.format(fpat), '#'.join(files))
subfiles
subfiles = re.findall('({}_.*?)#'.format(fpat), '#'.join(files))
subfiles
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/parse_conn_logs.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work')
os.chdir('/Users/babraham/Downloads/em2_logs_03-25')
conn_df = parse_log_by_subfile('conn.test.log')
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/parse_conn_logs.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work')
def split_and_parse(logfile, n=None, l=None, logDir=""):
    assert l or n
    _split(logfile, l,n)
    res_df = parse_log_by_subfile(logFile,logDir)
    return res_df
x = 2
def split_and_parse(logfile, n=None, l=None, logDir=""):
    assert l or n
    _split(logfile, l,n)
    res_df = parse_log_by_subfile(logFile,logDir)
    return res_df
import pickle
def save_obj(obj, name ):
    if name + '.pkl' not in os.listdir('.'):
        os.system("touch " + name + '.pkl')
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, protocol = 0)
def load_obj(name ):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)
save_obj(conn_df, 'conn_df')
jk
conn_df.columns

## ---(Sat Apr  7 22:32:14 2018)---
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis')
get_bro_perf(interface="em2")
data = get_data()
data.columns
make_plot(df)
make_plot(data)
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis')
make_plot(data)
data['time']
max(data['time'])
import datetime
datetime.datetime.fromtimestamp(int(max(data['time'])).strftime('%Y-%m-%d %H:%M:%S')
)
datetime.datetime.fromtimestamp(int(max(data['time']))).strftime('%Y-%m-%d %H:%M:%S')
res = get_data(device='em1')
res = get_data(interface='em1')
res
datetime.datetime.fromtimestamp(int(max(res['time']))).strftime('%Y-%m-%d %H:%M:%S')

## ---(Sun Apr  8 02:39:23 2018)---
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/netstats.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work')
x=2
"""
Created on Wed Mar 14 18:14:17 2018

@author: babraham
"""

import subprocess
import re
import pandas as pd
import time
import math
import os
import sys


def capOutput(cmd):
    try: output = subprocess.Popen(cmd, stdout=subprocess.PIPE ).communicate()[0]
    except: print("couldn't run command")
    return output


def getPacketLoss(waitTime=10):
    cmd = ['broctl', 'netstats']
    ti = time.time()
    startOuptut = capOutput(cmd)
    di = parseNetstatOutput(startOuptut)
    time.sleep(waitTime)
    endOutput = capOutput(cmd)
    df = parseNetstatOutput(endOutput)
    tf = time.time() - ti
    total = df.total.sum() - di.total.sum()
    lost = df.dropped.sum() - di.dropped.sum()
    ploss = float(lost) / float(total)
    pktsps = total  / float(tf)
    print('lost: {}, total: {}'.format(lost,total))
    return {'packetLoss':ploss, 'packetRateBro':pktsps}


def parseNetstatOutput(output):
    rx = re.findall('recvd=([0-9]+)', output)
    dropped = re.findall('dropped=([0-9]+)', output)
    total = re.findall('link=([0-9]+)', output)
    df = pd.DataFrame(zip(rx,dropped,total), columns=['received','dropped','total'])
    df = df.apply(pd.to_numeric, axis=0)
    return df


def parseProcOutput(output, device = "em1"):
    lines = output.split("\n")
    for i,l in enumerate(lines):
        if device.lower() in l:
            stats = re.findall(' [0-9]+', l)
            byts = int(stats[0].strip())
            pkts = int(stats[1].strip())
            return {'device':device,'bytes':byts, 'packets':pkts}
    return None


def getUtilization(waitTime = 10, device="em1", units="Gbps"):
    cmd = ['cat', '/proc/net/dev']
    startOutput = capOutput(cmd)
    startDict = parseProcOutput(startOutput, device)      
    time.sleep(waitTime)
    endOutput = capOutput(cmd)
    endDict = parseProcOutput(endOutput, device)
    totalbytes = int(endDict['bytes'] - startDict['bytes'])
    if units.lower() == "gbps": thruput = totalbytes * 8 / math.pow(10,9)
    thruput = thruput / waitTime
    totPkts = int(endDict['packets'] - startDict['packets'])
    pktSize = totalbytes / totPkts
    pktRate = totPkts / waitTime
    print('Utilization: {} Gbps'.format(thruput))
    return {'device':device,
            'throughput':thruput,
            'packetRate':pktRate,
            'packetSize':pktSize}


def calcCPU(statlist):
    try:
        idle_time = float(statlist[4])
        total_time = sum([int(i) for i in statlist[1:6]])
    except:
        print('error calculating cpu usage')
        return -1
    return (1 - idle_time / total_time)*100


def parseStatOutput(output):
    res = re.findall('cpu.*?\n',output)
    res = [r.strip().split(' ') for r in res]
    names = [r[0] for r in res]
    if 'cpu' in names:
        cpu_idx = names.index('cpu')
        res[cpu_idx].remove('')
        res[cpu_idx][0] = 'cpu_all'      
    res = [[float(n) for n in r[1:]] for r in res]
    return names, res


def getCPU(waitTime=5):
    cmd = ['cat', '/proc/stat']
    res1 = capOutput(cmd)
    names, stats1 = parseStatOutput(res1)
    time.sleep(waitTime)
    res2 = capOutput(cmd)
    names, stats2 = parseStatOutput(res2)
    difflist = []
    for i,(cpu,s1,s2) in enumerate(zip(names,stats1,stats2)):
        try:
            idle_diff = float(s2[3] - s1[3])
            total_diff = float(sum(s2[1:6]) - sum(s1[1:6]))
            util = 1- idle_diff / total_diff
            difflist.append((cpu,util))
        except:
            print('error calculating cpu usage for cpu {}'.format(cpu))
            print('idle diff: {}, total diff: {}'.rfomat(idle_diff,total_diff))
    return dict(difflist)


def getMemUsage():
    output = capOutput(['free'])
    nums = re.findall('[0-9]+',output)
    return float(nums[1])/float(nums[0])


def getAllStats(waitTime = 10, device="em1", units = "Gbps"):
    pLossDict = getPacketLoss(waitTime)
    thruputDict = getUtilization(waitTime, device, units)
    cpu_dict = getCPU(waitTime / 2)
    resDict = {k:v for k,v in thruputDict.items()}
    for k,v in pLossDict.items(): resDict[k] = v
    for k,v in cpu_dict.items(): resDict[k] = v  
    resDict['mem_usage'] = getMemUsage()     
    return resDict   


def monitor(device,fname=None,waitTime=10,maxTime=None, hasBro=True):
    ti = time.time()
    tf,dt = 0,0
    if not fname: fname = 'trafficStats_{}.txt'.format(device.lower())
    if not maxTime: maxTime = 60*60*24*21
    if device and waitTime:
        while dt < maxTime:
            if hasBro: res = getAllStats(waitTime, device)
            else: res = getUtilization(waitTime, device)
            res['time'] = time.time()
            for k in res.keys(): res[k] = str(res[k])
            res = sorted(res.items(), key=lambda x:x[0])
            if os.path.isfile(fname):
                out = open(fname, 'a')
            else:
                out = open(fname, 'w')
                out.write(','.join([r[0] for r in res])+'\n')
            out.write(','.join([r[1] for r in res])+'\n')
            out.close()
            tf = time.time()
            dt += tf - ti
            ti = tf
    else:
        print('error parsing arguments')
        sys.exit(1)


def main():
    try:
        waitTime = int(sys.argv[1])
        device = sys.argv[2]
        hasBro=True
        if device == "em1":  hasBro=False
        fname = 'trafficStats_{}.txt'.format(device)
    except:
        print("""usage: netstats.py --waitTime (secs) --device \n\nexample: netstats.py em1 10""")
        sys.exit(1)        
    monitor(device, fname,waitTime, hasBro)


if __name__ == '__main__':
    main()


test = """
cpu  721438593 12391128 87794678 31807433600 5081858 0 10279678 0 0 0
cpu0 24478817 607118 4348887 1261397893 3650964 0 8094909 0 0 0
cpu1 51701651 322793 6019246 1303138746 376937 0 98092 0 0 0
cpu2 59869892 319732 6256548 1294532386 82798 0 88321 0 0 0
cpu3 60322041 313199 5526065 1294813050 74173 0 83715 0 0 0
cpu4 57461280 326395 5317550 1297981049 60751 0 82691 0 0 0
cpu5 56633447 290500 5153691 1299130854 69713 0 82410 0 0 0
cpu6 57605769 311312 5291612 1297979710 64473 0 81561 0 0 0
cpu7 57060066 303720 5152027 1298699328 52723 0 81468 0 0 0
cpu8 61155703 303997 5346863 1294295247 51310 0 84232 0 0 0
cpu9 60470039 293826 5302396 1294920334 61727 0 83190 0 0 0
cpu10 60349928 311154 5332700 1295106733 68242 0 82930 0 0 0
cpu11 52587560 1559461 5748451 1301864731 63492 0 232270 0 0 0
cpu12 13336031 1153389 2678998 1346341826 83933 0 107121 0 0 0
cpu13 3735781 626665 2390127 1356999208 30478 0 153138 0 0 0
cpu14 3456937 514405 1994356 1357861254 24352 0 108707 0 0 0
cpu15 3440013 536187 2124562 1357721231 31710 0 106732 0 0 0
cpu16 2986820 461216 1713616 1358498087 57070 0 78595 0 0 0
cpu17 3237062 535881 1958313 1358105734 28489 0 96591 0 0 0
cpu18 3369589 514312 1803562 1358173277 19922 0 84306 0 0 0
cpu19 3549778 463745 1800787 1358042397 20280 0 84833 0 0 0
cpu20 3170317 532727 1687825 1358480002 19311 0 77741 0 0 0
cpu21 3339694 487115 1738036 1358276442 36767 0 84697 0 0 0
cpu22 3372593 438781 1698389 1358339441 31767 0 83222 0 0 0
cpu23 14747775 863486 1410063 1346734628 20466 0 38194 0 0 0
intr 42530130019 127 0 0 0 0 0 0 0 1 0 1049867384 0 0 0 0 0 0 0 69219427 0 0 0 0 0 0 0 0 0 0 0 0 0 0 13191224 1848798 0 2 0 2 2 2 2 2 2 2 1 79824619 11830297 12505557 15492801 14400800 14923175 12603242 16334930 1 47676359 16031758 15562722 11354665 11875781 12661880 13650420 16954414 3439497940 0 2280097507 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
ctxt 375732950197
btime 1508280417
processes 21544588
procs_running 1
procs_blocked 0
softirq 26895216304 11 1229516596 10726619 1480282521 15596547 0 144214145 1033786896 0 1506256489
"""
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis')
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/netstats.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work')
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis')
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/parse_conn_logs.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work')
res = split_and_parse('http.test.log')
res = split_and_parse('http.test.log',n=10)
def split_and_parse(logfile, n=None, l=None, logDir=""):
    assert l or n
    _split(logfile, l,n)
    res_df = parse_log_by_subfile(logfile,logDir)
    return res_df
res = split_and_parse('http.test.log',n=10)
logfile = 'http.test.log'
if typ: typ = typ.strip().lower()
for i,t in enumerate(fields.keys()):
    if t in logfile.lower(): typ = t
typ
with open(logfile, 'r') as f:
    lines = f.readlines()
fieldlist = []
for l in lines[1:10]:
    if '#fields' in l: fieldlist = l.split('\t')
fieldlist
imp_fields = fields[typ]
imp_fields
all_fields = {fieldlist[i].strip():i-1 for i in range(len(fieldlist))}
all_fields
fieldlist
imp_inds = [all_fields[fi] for fi in imp_fields]
recs = []
for l in tqdm(lines[8:len(lines)-2]):
    lsplit = l.split('\t')
    values = [lsplit[i] for i in imp_inds]
    for i in range(len(values)):
        if values[i] == '-': values[i] = '0'
    rec = dict(zip(imp_fields, values))
    if typ == 'conn':
        if rec['proto'] != 'icmp':
            rec['hash'] = ','.join([rec['id.orig_h'],rec['id.resp_h'],rec['id.resp_p'],rec['proto']])
            flags = _parse_history(rec['history'], keys=True)
            rec.update(flags)
    recs.append(rec)

fieldNames = recs[0].keys()
df = pd.DataFrame(recs, columns=fieldNames)
for l in tqdm(lines[8:len(lines)-2]):
    lsplit = l.split('\t')
    values = [lsplit[i] for i in imp_inds]
    for i in range(len(values)):
        if values[i] == '-': values[i] = '0'
    rec = dict(zip(imp_fields, values))
    if typ == 'conn':
        if rec['proto'] != 'icmp':
            rec['hash'] = ','.join([rec['id.orig_h'],rec['id.resp_h'],rec['id.resp_p'],rec['proto']])
            flags = _parse_history(rec['history'], keys=True)
            rec.update(flags)
    recs.append(rec)
recs
len(lines)
res = split_and_parse('http.old.log', n=10)
res
res.describe()

res.dtypes
res['response_body_len'].astype(int64)
res['response_body_len'].astype(int)
res['response_body_len'].dtypes
res.dtypes
res = parse_log('dns.test.log')
res.describe()
del(res)
res = split_and_parse('http.test.log')
res = split_and_parse('http.test.log', n=10)
logfile = 'http.test.log'
comb_df = parse_log_by_subfile('http.test.log')
dire = '.'
files = os.listdir(dire)
fpat = re.sub('\.log', '', logfile)
subfiles = re.findall('({}_.*?)#'.format(fpat), '#'.join(files))
subfiles = sorted(subfiles)
subfiles[0]
logfile = subfiles[0]
    for i,t in enumerate(fields.keys()):
        if t in logfile.lower(): typ = t                   
assert typ in fields.keys()
with open(logfile, 'r') as f:
    lines = f.readlines()
lines
res = parse_log_by_subfile('http.old.log')
if logDir: dire = logDir
else: dire = '.'

files = os.listdir(dire)
fpat = re.sub('\.log', '', logfile)
subfiles = re.findall('({}_.*?)#'.format(fpat), '#'.join(files))
subfiles = sorted(subfiles)
dire = '.'
files = os.listdir(dire)
fpat = re.sub('\.log', '', logfile)
subfiles = re.findall('({}_.*?)#'.format(fpat), '#'.join(files))
subfiles = sorted(subfiles)
subfiles
os.getcwd()
logfile
logfile = 'http.old.log'
files = os.listdir(dire)
fpat = re.sub('\.log', '', logfile)
subfiles = re.findall('({}_.*?)#'.format(fpat), '#'.join(files))
subfiles = sorted(subfiles)
subfiles
subfiles = sorted(subfiles, key=lambda x: int(re.findall('[0-9]+',x)[0]))
subfiles
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/parse_conn_logs.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work')
res = parse_log_by_subfile('http.old.log', n=10)
res = split_and_parse('http.old.log', n=10)
res.shape
res.describe()
res['uri'] = res['uri'].astype(str)
res.dtypes
res.to_string()
res['uri'].to_string()
del(res)
res = parse_log('http.old.log')
res.to_csv('http.old.csv')
del(res)
res = pd.read_csv('http.old.csv')
res.dtypes
res = pd.read_csv('http.old.csv',dtype=str)
res.dtypes
res = pd.read_csv('http.old.csv')
res.dtypes
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/parse_conn_logs.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work')
res = parse_log('ssl.test.log')
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/parse_conn_logs.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work')
res = parse_log('ssl.test.log')

## ---(Sun Apr  8 14:46:54 2018)---
import os
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/parse_conn_logs.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work')
os.chdir('/Users/babraham/Downloads/em2_logs_03-25')
os.stat('conn.test.log')
os.stat('conn.test.log').st_size
os.stat('http.old.log').st_size
res = parse_log('http.old.log')
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/parse_conn_logs.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work')
res = parse_log('http.old.log')
res = parse_log('conn.test_0.log')
res.describe()
res.head()
res.head(20)
res['orig_pkts'].describe()

logDir="."
logfile='conn.test.log'
logpat = re.sub('.log','',logfile)
filestr = "#".join(os.listdir(logDir))
subfiles = re.findall('({}_.*?)#'.format(logpat),filestr)
subfiles
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/parse_conn_logs.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work')
res = split_and_parse('http.old.log', n=10)
res.dtypes
df = res
for n in bdc.num_cols:
    df.ix[:,[n]] = df.ix[:,[n]].astype('float64')
df.columns
df.ix[:,'request_body_len'] = df.ix[:,'request_body_len'].astype('float64')
df.dtypes
logfile = 'http.old.log'
outputDir="."
export=True
typ=None
if typ: typ = typ.strip().lower()
else:
    typ = ""
    for i,t in enumerate(bdc.fields.keys()):
        if t in logfile.lower(): typ = t                   

assert typ in bdc.fields.keys()
with open(logfile, 'r') as f:
    lines = f.readlines()
fieldList, broTypes, pyTypes = [],[], []
for l in lines[1:10]:
    if '#fields' in l: fieldList = l.strip().split('\t')
    elif '#types' in l: broTypes = l.strip().split('\t')

pyTypes = [bdc.type_mapper[t] for t in broTypes]
#create a dictionary for field data types
field_types = dict(zip(fieldlist,pyTypes))
fieldList, broTypes, pyTypes = [],[], []
for l in lines[1:10]:
    if '#fields' in l: fieldList = l.strip().split('\t')[1:]
    elif '#types' in l: broTypes = l.strip().split('\t')[1:]

pyTypes = [bdc.type_mapper[t] for t in broTypes]
broTypes
bdc.type_mapper
fieldList, broTypes, pyTypes = [],[], []
for l in lines[1:10]:
    if '#fields' in l: fieldList = l.strip().split('\t')[1:]
    elif '#types' in l: broTypes = l.strip().split('\t')[1:]

pyTypes = [bdc.type_mapper.get(t,object) for t in broTypes]
field_types = dict(zip(fieldlist,pyTypes))
field_types = dict(zip(fieldList,pyTypes))
field_types
imp_fields = bdc.fields[typ]
all_fields = {fieldList[i].strip():i-1 for i in range(len(fieldlist))}
imp_inds = [all_fields[fi] for fi in imp_fields]
recs = []
for l in tqdm(lines[8:len(lines)-2]):
    lsplit = l.split('\t')
    values = [lsplit[i] for i in imp_inds]
    for i in range(len(values)):
        if values[i] == '-': values[i] = '0'
    rec = dict(zip(imp_fields, values))
    if typ == 'conn':
        if rec['proto'] != 'icmp':
            rec['hash'] = ','.join([rec['id.orig_h'],rec['id.resp_h'],rec['id.resp_p'],rec['proto']])
            flags = _parse_history(rec['history'], keys=True)
            rec.update(flags)
    recs.append(rec)

fieldNames = recs[0].keys()
imp_fields = bdc.fields[typ]
all_fields = {fieldList[i].strip():i-1 for i in range(len(fieldList))}
imp_inds = [all_fields[fi] for fi in imp_fields]
recs = []
for l in tqdm(lines[8:len(lines)-2]):
    lsplit = l.split('\t')
    values = [lsplit[i] for i in imp_inds]
    for i in range(len(values)):
        if values[i] == '-': values[i] = '0'
    rec = dict(zip(imp_fields, values))
    if typ == 'conn':
        if rec['proto'] != 'icmp':
            rec['hash'] = ','.join([rec['id.orig_h'],rec['id.resp_h'],rec['id.resp_p'],rec['proto']])
            flags = _parse_history(rec['history'], keys=True)
            rec.update(flags)
    recs.append(rec)

fieldNames = recs[0].keys()
df = pd.DataFrame(recs, columns=fieldNames, dtypes=field_types)
df = pd.DataFrame(recs, columns=fieldNames, dtype=field_types)
pyTypes
field_types
pyTypes[0]
pyTypes[0](x)
fieldList[0]
pyTypes[0]('123')
type(pyTypes[0])
type(pyTypes[0]) is function
pyTypes[0] is int
type(pyTypes[0]) == 'function'
type(pyTypes[0]) == function
res = type(pyTypes[0])
res
type(res)
type(function)
callable(pyTypes[0])
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/PreProcessing/log_parser.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/PreProcessing')
res = parse_log('http.old.log')
logfile
if typ: typ = typ.strip().lower()
else:
    typ = ""
    for i,t in enumerate(bdc.fields.keys()):
        if t in logfile.lower(): typ = t                   

assert typ in bdc.fields.keys() 
with open(logfile, 'r') as f:
    lines = f.readlines()

#capture field names, data types
fieldList, broTypes, pyTypes = [],[], []
for l in lines[1:10]:
    if '#fields' in l: fieldList = l.strip().split('\t')[1:]
    elif '#types' in l: broTypes = l.strip().split('\t')[1:]

pyTypes = [bdc.type_mapper.get(t,object) for t in broTypes]
pyTypes
field_types['id.orig.h']
field_types.keys()
field_types['id.orig_h']
field_types.items()
zip(fieldList,broTypes)
field_types = dict(zip(fieldList,pyTypes))
#get important fields for this type of log
imp_fields = bdc.fields[typ]
all_fields = {fieldList[i].strip():i-1 for i in range(len(fieldList))}
imp_inds = [all_fields[fi] for fi in imp_fields]
recs = []
l = lines[23]
lsplit = l.split('\t')
values = [lsplit[i] for i in imp_inds]
len(values)
len(field_types)
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/PreProcessing/log_parser.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/PreProcessing')
res = parse_log('http.old.log')
callable(object)
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/PreProcessing/log_parser.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/PreProcessing')
res = parse_log('http.old.log')
df = pd.DataFrame(recs, columns=fieldNames)
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/PreProcessing/log_parser.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/PreProcessing')
res = parse_log('http.old.log')
res.dtypes
zip(fieldList, broTypes)
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/PreProcessing/log_parser.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/PreProcessing')
res = parse_log('http.old.log')
res.dtypes
zip(fieldList, broTypes)
bdc.type_mapper('port')
bdc.type_mapper.get('port')
res.head()
recs[0].keys()
if typ: typ = typ.strip().lower()
else:
    typ = ""
    for i,t in enumerate(bdc.fields.keys()):
        if t in logfile.lower(): typ = t                   

assert typ in bdc.fields.keys() 
with open(logfile, 'r') as f:
    lines = f.readlines()

#capture field names, data types
fieldList, broTypes, pyTypes = [],[], []
for l in lines[1:10]:
    if '#fields' in l: fieldList = l.strip().split('\t')[1:]
    elif '#types' in l: broTypes = l.strip().split('\t')[1:]

pyTypes = [bdc.type_mapper.get(t,bdc.type_mapper['unknown']) for t in broTypes]

#create a dictionary for field data types
field_types = dict(zip(fieldList,pyTypes))
#get important fields for this type of log
imp_fields = bdc.fields[typ]
all_fields = {fieldList[i].strip():i-1 for i in range(len(fieldList))}
imp_inds = [all_fields[fi] for fi in imp_fields]
recs = []
for l in tqdm(lines[8:len(lines)-2]):
    values = l.split('\t')
    for i,(field,val) in enumerate(zip(fieldList,values)):
        if val == '-':
            broTyp = broTypes[i]
            values[i] = bdc.dash_mapper.get(broTyp, '-')
        else:
            mapping = field_types.get(field)
            if callable(mapping): values[i] = mapping(val)
            else: values[i] = mapping   
    values = [values[i] for i in imp_inds] #only include important fields
    rec = dict(zip(imp_fields, values)) 
    if typ == 'conn':
        if rec['proto'] != 'icmp':
            rec['hash'] = ','.join([rec['id.orig_h'],rec['id.resp_h'],rec['id.resp_p'],rec['proto']])
            flags = _parse_history(rec['history'], keys=True)
            rec.update(flags)
    recs.append(rec)

fieldNames = recs[0].keys()
print('creating dataframe...')
recs[0].keys()
recs[1].keys()
recs['method']
recs[0]['method']
recs[0]
l = lines[23]
values = l.split('\t')
len(values)
len(fieldList)
zip(fieldList,values)
for i,(field,val) in enumerate(zip(fieldList,values)):
    if val == '-':
        broTyp = broTypes[i]
        values[i] = bdc.dash_mapper.get(broTyp, '-')
    else:
        mapping = field_types.get(field)
        if callable(mapping): values[i] = mapping(val)
        else: values[i] = mapping
imp_fields
imp_inds
all_fields
max(all_fields.values())
all_fields = {fieldList[i].strip():i for i in range(len(fieldList))}
imp_inds
imp_inds = [all_fields[fi] for fi in imp_fields]
imp_inds
fieldList[2]
fieldList
recs = []
for l in tqdm(lines[8:len(lines)-2]):
    values = l.split('\t')
    for i,(field,val) in enumerate(zip(fieldList,values)):
        if val == '-':
            broTyp = broTypes[i]
            values[i] = bdc.dash_mapper.get(broTyp, '-')
        else:
            mapping = field_types.get(field)
            if callable(mapping): values[i] = mapping(val)
            else: values[i] = mapping   
    values = [values[i] for i in imp_inds] #only include important fields
    rec = dict(zip(imp_fields, values)) 
    if typ == 'conn':
        if rec['proto'] != 'icmp':
            rec['hash'] = ','.join([rec['id.orig_h'],rec['id.resp_h'],rec['id.resp_p'],rec['proto']])
            flags = _parse_history(rec['history'], keys=True)
            rec.update(flags)
    recs.append(rec)
recs[0]
fieldNames = recs[0].keys()
print('creating dataframe...')
df = pd.DataFrame(recs, columns=fieldNames)
df.head()
df.dtypes
1892055./(1892055+3363768509)
import gc
gc.collect()
f = open('../trafficAnalysis/stat.test.log', 'r')
f = open('../trafficAnalysis/stats.test.log', 'r')
os.getcwd()
os.getcwd('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/stats.test.log', 'r')
f = open('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/stats.test.log', 'r')
lines = f.readlines()
lines[:10]
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/PreProcessing/log_parser.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/PreProcessing')
res = parse_log('../trafficAnalysis/stats.test.log')
os.chdir('../trafficAnalysis')
os.getcwd()
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/PreProcessing/log_parser.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/PreProcessing')
os.getcwd()
res = parse_log('../trafficAnalysis/stats.test.log')
res
res.to_csv('sample_stats.csv')
res.describe()
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats')
res = get_bro_perf()
res = get_data()
res
res['date']
res['time']
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats')
res = get_data()
make_plot(res)
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats')
make_plot(res)
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats')
make_plot(res)
server = 'ivy-mv5g-bulwark.hpc.virginia.edu'
port=22
user = 'bea3ch'
password='Br#nD0$!'
ssh = createSSHClient(server, port, user, password)
dir(ssh)
dir(ssh).invoke_shell()
ssh.invoke_shell()
from ShellHandler import *
sh = ShellHandler(server, user, password)
sh.execute('pwd')
sh.execute('ls')
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats/ShellHandler.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats')
sh = ShellHandler(server, user, password)
sh.execute('ls')
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats/ShellHandler.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats')
sh = ShellHandler(server, user, password)
sh.execute('ls')
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats/ShellHandler.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats')
sh = ShellHandler(server, user, password)
sh.execute('ls')
st = 'end of stdOUT buffer. finished with exit status 0'
res = re.findall('status (.*?)', st)
res
res = re.findall('status ([0-9]+)', st)
rs
res
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats/ShellHandler.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats')
sh = ShellHandler(server, user, password)
sh.execute('ls')
res = sh.execute('ls')
res[0]
res[1]
res[1][0]
import time
time.time()
datetime.fromtimestamp(time.time())
datetime.from_timestamp(time.time())
import datetime as dt
dt.datetime.fromtimestamp(time.time())
cur_dt = dt.datetime.fromtimestamp(time.time())
dir(cur_dt)
cur_dt.year()
cur_dt.year
cdt = cur_dt
'/'.join(cdt.year,cdt.month,cdt.day)
'/'.join([cdt.year,cdt.month,cdt.day])
cdt.year
cdt.month
cdt.day
[cdt.year,cdt.month,cdt.day]
[str(cdt.year),(cdt.month),(cdt.day)]
'/'.join([str(cdt.year),str(cdt.month),str(cdt.day)])
server = 'ivy-mv5g-bulwark.hpc.virginia.edu'
user = 'bea3ch'
password='Br#nD0$!'
cdt = dt.datetime.fromtimestamp(time.time())
datestr = '/'.join([str(cdt.year),str(cdt.month),str(cdt.day)])
sh = ShellHandler(server, user, password)
sh.execute('touch --date {} /tmp/start'.format(datestr))
sh.execute('cd /home/bro/logs')
_,shout,_ = sh.execute('find -type f -newer /tmp/start -name "stats*"')
datestr
_,shout,_ = sh.execute('cat /tmp/st')
shout
import unicodedata
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats/ShellHandler.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats')
sh = ShellHandler(server,user,password)
cdt = dt.datetime.fromtimestamp(time.time())
datestr = '/'.join([str(cdt.year),str(cdt.month),str(cdt.day)])
datestr
'touch --date {} /tmp/start'.format(datestr)
sh.execute('touch --date "{}" /tmp/start'.format(datestr))
sh.execute('cd /home/bro/logs')
find_cmd = 'find -type f -newer /tmp/start -name "stats*"'
_,shout,_ = sh.execute(find_cmd)
shout
sh.execute('pwd')
find_cmd
datestr = '/'.join([str(cdt.year),str(cdt.month),str(cdt.day-1)])
sh.execute('touch --date "{}" /tmp/start'.format(datestr))
find_cmd = 'find -type f -newer /tmp/start -name "stats*"'
_,shout,_ = sh.execute(find_cmd)
shout
sh.execute('ls -alh /tmp/s*')
datestr
datestr = '-'.join([str(cdt.year),str(cdt.month),str(cdt.day-1)])
sh.execute('touch --date "{}" /tmp/start'.format(datestr))
sh.execute('cd /home/bro/logs')
find_cmd = 'find -type f -newer /tmp/start -name "stats*"'
_,shout,_ = sh.execute(find_cmd)
shout
sh.execute('touch --date "{}" /tmp/start'.format(datestr))
find_cmd = 'find -type f -newer /tmp/start -name "stats*"'sh.execute(find_cmd)
find_cmd = 'find -type f -newer /tmp/start -name "stats*"'
sh.execute(find_cmd)
res = sh.execute(find_cmd)
res[0]
res[1]
res[2]
_,_,files = sh.execute(find_cmd)
files
f = [f for f in files if 'log' in f]
f
f = [f for f in files if '.log' in f]
f
f = [f for f in files if '.log.gz' in f]
f
f = [f.strip() for f in files if '.log.gz' in f]
f
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats/ShellHandler.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats')
server = 'ivy-mv5g-bulwark.hpc.virginia.edu'
user = 'bea3ch'
password='Br#nD0$!'
cdt = dt.datetime.fromtimestamp(time.time())
datestr = '-'.join([str(cdt.year),str(cdt.month),str(cdt.day-1)])
sh = ShellHandler(server, user, password)
sh.execute('touch --date "{}" /tmp/start'.format(datestr))
sh.execute('cd /home/bro/logs')
find_cmd = 'find -type f -newer /tmp/start -name "stats*"'
_,_,files = sh.execute(find_cmd)
files = [f.strip() for f in files if '.log.gz' in f]
files
device="em2"
sh.scp.get(r'/home/bea3ch/shared/trafficAnalysis/trafficStats_{}.txt'.format(device), r'./')
files = ['/home/bro/logs'+f[1:].strip() for f in files if '.log.gz' in f]
files
for f in files:
    sh.scp.get(f, r'./')
os.getcwd()
for f in files:
    sh.execute('gunzip ' + f)
    sh.scp.get(f, r'./')
find_cmd = 'find -type f -newer /tmp/start -name "stats*"'
_,_,files = sh.execute(find_cmd)
files = ['/home/bro/logs'+f[1:].strip() for f in files if '.log.gz' in f]
files
for f in files:
    sh.execute('gunzip ' + f)
    f = re.sub('/.gz', '', f)
    sh.scp.get(f, r'./')
dir(ssh.channel)
dir(sh.channel)
dir(sh.ssh)
files = ['/home/bro/logs'+f[1:].strip() for f in files if '.log' in f]
sh.execute('tar -czf tarball - {}'.format(' '.join(files)))
files
_,_,files = sh.execute(find_cmd)
files = ['/home/bro/logs'+f[1:].strip() for f in files if '.log' in f]
sh.execute('tar -czf tarball - {}'.format(' '.join(files)))
files
' '.join(files)
files = [f[1:].strip() for f in files if '.log' in f]
files
_,_,files = sh.execute(find_cmd)
files = [f[1:].strip() for f in files if '.log' in f]
files
sh.execute('tar -czf tarball - {}'.format(' '.join(files)))
sh.execute('cd /home/bro/logs')
sh.execute('tar -czf tarball - {}'.format(' '.join(files)))
files
sh.execute('tar -czf tarball - /2018-04-08/stats.*')
sh.execute('tar -czf tarball - $(ls /2014-04-08/stats.*)')
tar_cmd = 'tar -czf tarball - {}'.format(' '.join(files))
tar_cmd
sh.execute('pwd')
tar_cmd = 'tar -czf tarball - {}'.format(' '.join(files[:-1]))
tar_cmd
fnames = ' '.join(files)
scp.get(r'{}'.rfomat(fnames), r'./')
sh.scp.get(r'{}'.rfomat(fnames), r'./')
sh.scp.get(r'{}'.format(fnames), r'./')
sh.scp.get(r'{}'.format(files[0]), r'./')
sh = ShellHandler(server, user, password)
sh.execute('touch --date "{}" /tmp/start'.format(datestr))
sh.execute('cd /home/bro/logs')
find_cmd = 'find -type f -newer /tmp/start -name "stats*"'
_,_,files = sh.execute(find_cmd)
files = [f[1:].strip() for f in files if '.log' in f]
fnames = ' '.join(files)
sh.scp.get(r'{}'.format(files[0]), r'./')
files = [re.sub('\:', '\:', f) for f in files]
files
files = [f[1:].strip() for f in files if '.log' in f]
files
_,_,files = sh.execute(find_cmd)
files = [f[1:].strip() for f in files if '.log' in f]
files
files = [re.sub('\:', 'p', f) for f in files]
files
files = [re.sub('p', '\:', f) for f in files]
files
find_cmd = 'find -type f -newer /tmp/start -name "stats*"'
_,_,files = sh.execute(find_cmd)
files = [f[1:].strip() for f in files if '.log' in f]
files = [re.sub('\:', '\\:', f) for f in files]
files
fnames = ' '.join(files)
sh.scp.get(r'{}'.format(files[0]), r'./')
sh = ShellHandler(server, user, password)
sh.execute('touch --date "{}" /tmp/start'.format(datestr))
sh.execute('cd /home/bro/logs')
find_cmd = 'find -type f -newer /tmp/start -name "stats*"'
_,_,files = sh.execute(find_cmd)
files = [f[1:].strip() for f in files if '.log' in f]
files = [re.sub('\:', '\:', f) for f in files]
fnames = ' '.join(files)
sh.scp.get(r'{}'.format(files[0]), r'./')
files = ['/home/bro/logs'+f[1:].strip() for f in files if '.log' in f]
files = [re.sub('\:', '\:', f) for f in files]
fnames = ' '.join(files)
sh.scp.get(r'{}'.format(files[0]), r'./')
sh = ShellHandler(server, user, password)
sh.execute('touch --date "{}" /tmp/start'.format(datestr))
sh.execute('cd /home/bro/logs')
find_cmd = 'find -type f -newer /tmp/start -name "stats*"'
_,_,files = sh.execute(find_cmd)
files = ['/home/bro/logs'+f[1:].strip() for f in files if '.log' in f]
files = [re.sub('\:', '\:', f) for f in files]
fnames = ' '.join(files)
sh.scp.get(r'{}'.format(files[0]), r'./')
sh.scp.open()
fnames
sh.execute('tar -cvf tarball.tar {}'.format(fnames))
sh = ShellHandler(server, user, password)
sh.execute('touch --date "{}" /tmp/start'.format(datestr))
sh.execute('cd /home/bro/logs')
find_cmd = 'find -type f -newer /tmp/start -name "stats*"'
_,_,files = sh.execute(find_cmd)
files = ['/home/bro/logs'+f[1:].strip() for f in files if '.log' in f]
files = [re.sub('\:', '\:', f) for f in files]
fnames = ' '.join(files)
#copy all relevant logs into tar file anddownload them
sh.execute('tar -cvf tarball.tar {}'.format(fnames))
sh.scp.get(r'tarball.tar', r'./')
def get_data_new(local_dir="./", device="em2"):
    server = 'ivy-mv5g-bulwark.hpc.virginia.edu'
    user = 'bea3ch'
    password='Br#nD0$!'
    cdt = dt.datetime.fromtimestamp(time.time())
    datestr = '-'.join([str(cdt.year),str(cdt.month),str(cdt.day-1)])
    sh = ShellHandler(server, user, password)
    sh.execute('touch --date "{}" /tmp/start'.format(datestr))
    sh.execute('cd /home/bro/logs')
    find_cmd = 'find -type f -newer /tmp/start -name "stats*"'
    _,_,files = sh.execute(find_cmd)
    files = ['/home/bro/logs'+f[1:].strip() for f in files if '.log' in f]
    files = [re.sub('\:', '\:', f) for f in files]
    fnames = ' '.join(files)
    #copy all relevant logs into tar file anddownload them
    sh.execute('tar -cvf tarball.tar {}'.format(fnames))
    sh.scp.get(r'/home/bro/logstarball.tar', r'./')    
    sh.scp.get(r'/home/bea3ch/shared/trafficAnalysis/trafficStats_{}.txt'.format(device), r'./')
    df = pd.read_csv('trafficStats_'+device+'.txt', index_col=False)
    return df
res = get_data_new()
def get_data_new(local_dir="./", device="em2"):
    server = 'ivy-mv5g-bulwark.hpc.virginia.edu'
    user = 'bea3ch'
    password='Br#nD0$!'
    cdt = dt.datetime.fromtimestamp(time.time())
    datestr = '-'.join([str(cdt.year),str(cdt.month),str(cdt.day-1)])
    sh = ShellHandler(server, user, password)
    sh.execute('touch --date "{}" /tmp/start'.format(datestr))
    sh.execute('cd /home/bro/logs')
    find_cmd = 'find -type f -newer /tmp/start -name "stats*"'
    _,_,files = sh.execute(find_cmd)
    files = ['/home/bro/logs'+f[1:].strip() for f in files if '.log' in f]
    files = [re.sub('\:', '\:', f) for f in files]
    fnames = ' '.join(files)
    #copy all relevant logs into tar file anddownload them
    sh.execute('tar -cvf tarball.tar {}'.format(fnames))
    sh.scp.get(r'/home/bro/logs/tarball.tar', r'./')    
    sh.scp.get(r'/home/bea3ch/shared/trafficAnalysis/trafficStats_{}.txt'.format(device), r'./')
    df = pd.read_csv('trafficStats_'+device+'.txt', index_col=False)
    return df
res = get_data_new()
def get_data_new(local_dir="./", device="em2"):
    server = 'ivy-mv5g-bulwark.hpc.virginia.edu'
    user = 'bea3ch'
    password='Br#nD0$!'
    cdt = dt.datetime.fromtimestamp(time.time())
    datestr = '-'.join([str(cdt.year),str(cdt.month),str(cdt.day-1)])
    sh = ShellHandler(server, user, password)
    sh.execute('touch --date "{}" /tmp/start'.format(datestr))
    sh.execute('cd /home/bro/logs')
    sh.execute('mkdir tmp')
    find_cmd = 'find -type f -newer /tmp/start -name "stats*"'
    _,_,files = sh.execute(find_cmd)
    files = ['/home/bro/logs'+f[1:].strip() for f in files if '.log' in f]
    files = [re.sub('\:', '\:', f) for f in files]
    fnames = ' '.join(files)
    tmp_f = '/tmp'
    sh.execute('cp ' + fnames + ' ' + tmp_f)
    sh.execute('cp /home/bea3ch/shared/trafficAnalysis/trafficStats_{}.txt {}'.format(device,tmp_f))
    #copy all relevant logs into tar file anddownload them
    sh.execute('tar -cvf tarball.tar {}'.format(fnames))
    sh.scp.get(r'/home/bro/logs/tarball.tar', r'./')    
    df = pd.read_csv('trafficStats_'+device+'.txt', index_col=False)
    return df
tmp_f = './tmp'
sh.execute('tar -zcvf tarball.tar.gz {}'.format(tmp_f))
sh.execute('rm tarball*')
sh.execute('rm -rf ./tmp')
def get_data_new(local_dir="./", device="em2"):
    server = 'ivy-mv5g-bulwark.hpc.virginia.edu'
    user = 'bea3ch'
    password='Br#nD0$!'
    cdt = dt.datetime.fromtimestamp(time.time())
    datestr = '-'.join([str(cdt.year),str(cdt.month),str(cdt.day-1)])
    sh = ShellHandler(server, user, password)
    sh.execute('touch --date "{}" /tmp/start'.format(datestr))
    sh.execute('cd /home/bro/logs')
    sh.execute('mkdir tmp')
    find_cmd = 'find -type f -newer /tmp/start -name "stats*"'
    _,_,files = sh.execute(find_cmd)
    files = ['/home/bro/logs'+f[1:].strip() for f in files if '.log' in f]
    files = [re.sub('\:', '\:', f) for f in files]
    fnames = ' '.join(files)
    tmp_f = './tmp'
    sh.execute('cp ' + fnames + ' ' + tmp_f)
    sh.execute('cp /home/bea3ch/shared/trafficAnalysis/trafficStats_{}.txt {}'.format(device,tmp_f))
    #copy all relevant logs into tar file anddownload them
    sh.execute('tar -zcvf tarball.tar.gz {}'.format(tmp_f))
    sh.scp.get(r'/home/bro/logs/tarball.tar', r'./')
    #remove tmp files
    sh.execute('rm tarball*')
    sh.execute('rm -rf ./tmp')
    df = pd.read_csv('trafficStats_'+device+'.txt', index_col=False)
    return df
res = get_data_new()
def get_data_new(local_dir="./", device="em2"):
    server = 'ivy-mv5g-bulwark.hpc.virginia.edu'
    user = 'bea3ch'
    password='Br#nD0$!'
    cdt = dt.datetime.fromtimestamp(time.time())
    datestr = '-'.join([str(cdt.year),str(cdt.month),str(cdt.day-1)])
    sh = ShellHandler(server, user, password)
    sh.execute('touch --date "{}" /tmp/start'.format(datestr))
    sh.execute('cd /home/bro/logs')
    sh.execute('mkdir tmp')
    find_cmd = 'find -type f -newer /tmp/start -name "stats*"'
    _,_,files = sh.execute(find_cmd)
    files = ['/home/bro/logs'+f[1:].strip() for f in files if '.log' in f]
    files = [re.sub('\:', '\:', f) for f in files]
    fnames = ' '.join(files)
    tmp_f = './tmp'
    sh.execute('cp ' + fnames + ' ' + tmp_f)
    sh.execute('cp /home/bea3ch/shared/trafficAnalysis/trafficStats_{}.txt {}'.format(device,tmp_f))
    #copy all relevant logs into tar file anddownload them
    sh.execute('tar -zcvf tarball.tar.gz {}'.format(tmp_f))
    sh.scp.get(r'/home/bro/logs/tarball.tar.gz', r'./')
    #remove tmp files
    sh.execute('rm tarball*')
    sh.execute('rm -rf ./tmp')
    df = pd.read_csv('trafficStats_'+device+'.txt', index_col=False)
    return df
res = get_data_new()
def get_data_new(local_dir="./", device="em2"):
    server = 'ivy-mv5g-bulwark.hpc.virginia.edu'
    user = 'bea3ch'
    password='Br#nD0$!'
    cdt = dt.datetime.fromtimestamp(time.time())
    datestr = '-'.join([str(cdt.year),str(cdt.month),str(cdt.day-1)])
    sh = ShellHandler(server, user, password)
    sh.execute('touch --date "{}" /tmp/start'.format(datestr))
    sh.execute('cd /home/bro/logs')
    sh.execute('mkdir tmp')
    find_cmd = 'find -type f -newer /tmp/start -name "stats*"'
    _,_,files = sh.execute(find_cmd)
    files = ['/home/bro/logs'+f[1:].strip() for f in files if '.log' in f]
    files = [re.sub('\:', '\:', f) for f in files]
    fnames = ' '.join(files)
    tmp_f = './tmp'
    sh.execute('cp ' + fnames + ' ' + tmp_f)
    sh.execute('cp /home/bea3ch/shared/trafficAnalysis/trafficStats_{}.txt {}'.format(device,tmp_f))
    #copy all relevant logs into tar file anddownload them
    sh.execute('tar -zcvf tarball.tar.gz {}'.format(tmp_f))
    sh.scp.get(r'/home/bro/logs/tarball.tar.gz', r'./')
    #remove tmp files
    sh.execute('rm tarball*')
    sh.execute('rm -rf ./tmp')
    #unzip local tar containing all data
    os.system('gunzip {}'.format(tmp_f))
    df = pd.read_csv('/{}/trafficStats_'+device+'.txt'.format(tmp_f), index_col=False)
    
    return df
res = get_data_new()
def get_data_new(local_dir="./", device="em2"):
    server = 'ivy-mv5g-bulwark.hpc.virginia.edu'
    user = 'bea3ch'
    password='Br#nD0$!'
    cdt = dt.datetime.fromtimestamp(time.time())
    datestr = '-'.join([str(cdt.year),str(cdt.month),str(cdt.day-1)])
    sh = ShellHandler(server, user, password)
    sh.execute('touch --date "{}" /tmp/start'.format(datestr))
    sh.execute('cd /home/bro/logs')
    sh.execute('mkdir tmp')
    find_cmd = 'find -type f -newer /tmp/start -name "stats*"'
    _,_,files = sh.execute(find_cmd)
    files = ['/home/bro/logs'+f[1:].strip() for f in files if '.log' in f]
    files = [re.sub('\:', '\:', f) for f in files]
    fnames = ' '.join(files)
    tmp_f = './tmp'
    sh.execute('cp ' + fnames + ' ' + tmp_f)
    sh.execute('cp /home/bea3ch/shared/trafficAnalysis/trafficStats_{}.txt {}'.format(device,tmp_f))
    #copy all relevant logs into tar file anddownload them
    sh.execute('tar -zcvf tarball.tar.gz {}'.format(tmp_f))
    sh.scp.get(r'/home/bro/logs/tarball.tar.gz', r'./')
    #remove tmp files
    sh.execute('rm tarball*')
    sh.execute('rm -rf ./tmp')
    #unzip local tar containing all data
    os.system('gunzip {}'.format(tmp_f))
    df = pd.read_csv('/{}/trafficStats_{}.txt'.format(device,tmp_f), index_col=False)
    
    return df
res = get_data_new()
def get_data_new(local_dir="./", device="em2"):
    server = 'ivy-mv5g-bulwark.hpc.virginia.edu'
    user = 'bea3ch'
    password='Br#nD0$!'
    cdt = dt.datetime.fromtimestamp(time.time())
    datestr = '-'.join([str(cdt.year),str(cdt.month),str(cdt.day-1)])
    sh = ShellHandler(server, user, password)
    sh.execute('touch --date "{}" /tmp/start'.format(datestr))
    sh.execute('cd /home/bro/logs')
    sh.execute('mkdir tmp')
    find_cmd = 'find -type f -newer /tmp/start -name "stats*"'
    _,_,files = sh.execute(find_cmd)
    files = ['/home/bro/logs'+f[1:].strip() for f in files if '.log' in f]
    files = [re.sub('\:', '\:', f) for f in files]
    fnames = ' '.join(files)
    tmp_f = './tmp'
    sh.execute('cp ' + fnames + ' ' + tmp_f)
    sh.execute('cp /home/bea3ch/shared/trafficAnalysis/trafficStats_{}.txt {}'.format(device,tmp_f))
    #copy all relevant logs into tar file anddownload them
    sh.execute('tar -zcvf tarball.tar.gz {}'.format(tmp_f))
    sh.scp.get(r'/home/bro/logs/tarball.tar.gz', r'./')
    #remove tmp files
    sh.execute('rm tarball*')
    sh.execute('rm -rf ./tmp')
    #unzip local tar containing all data
    os.system('gunzip {}'.format(tmp_f))
    df = pd.read_csv('./{}/trafficStats_{}.txt'.format(tmp_f,device), index_col=False)
    
    return df
res = get_data_new()
res

## ---(Mon Apr  9 00:06:03 2018)---
import numpy as np
np.zeros(5)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/HW5/hw5_code/q_learn.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/HW5/hw5_code')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/HW5/hw5_code/cliff_walking.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/HW5/hw5_code')
fig.savefig('cliff_walking.jpg')
a = np.array([1,2,3])
b = np.array([2,3,4])
a+b
np.sum(a,b)
np.add(a,b)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/HW5/hw5_code/max_bias.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/HW5/hw5_code')
fig.savefig('doubleQ_learning'+str(num_actions_B)+'.jpg')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/HW5/hw5_code/max_bias.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/HW5/hw5_code')
fig.savefig('doubleQ_learning'+str(num_actions_B)+'.jpg')

## ---(Mon Apr  9 01:45:51 2018)---
def get_data_new(local_dir="./", device="em2"):
    server = 'ivy-mv5g-bulwark.hpc.virginia.edu'
    user = 'bea3ch'
    password='Br#nD0$!'
    cdt = dt.datetime.fromtimestamp(time.time())
    datestr = '-'.join([str(cdt.year),str(cdt.month),str(cdt.day-1)])
    sh = ShellHandler(server, user, password)
    sh.execute('touch --date "{}" /tmp/start'.format(datestr))
    sh.execute('cd /home/bro/logs')
    stats_cmd = 'find -type f -newer /tmp/start -name "stats*"'
    _,_,stat_files = sh.execute(stats_cmd)
    cap_loss_cmd = 'find -type f -newer /tmp/start -name "capture_loss*"'
    _,_,cl_files = sh.execute(cap_loss_cmd)
    all_files = cl_files + stat_files
    all_files = ['/home/bro/logs'+f[1:].strip() for f in all_files if '.log' in f]
    all_files = [re.sub('\:', '\:', f) for f in all_files]
    fnames = ' '.join(all_files)
    #copy all relevant logs into tar file anddownload them
    sh.execute('tar -cvf tarball.tar {}'.format(fnames))
    sh.scp.get(r'/home/bro/logs/tarball.tar', r'./')    
    sh.scp.get(r'/home/bea3ch/shared/trafficAnalysis/trafficStats_{}.txt'.format(device), r'./')
    df = pd.read_csv('trafficStats_'+device+'.txt', index_col=False)
    #unzip all files within tmp folder
    [sh.execute('gunzip {}'.format(f)) for f in all_files if '.gz' in f]
    return df
res = get_data_new()
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats')
res = get_data_new()
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats')
res = get_data_new()
def get_data(local_dir="./", device="em2"):
    server = 'ivy-mv5g-bulwark.hpc.virginia.edu'
    user = 'bea3ch'
    password='Br#nD0$!'
    cdt = dt.datetime.fromtimestamp(time.time())
    datestr = '-'.join([str(cdt.year),str(cdt.month),str(cdt.day-1)])
    cur_date = '-'.join([str(cdt.year),str(cdt.month),str(cdt.day)])
    sh = ShellHandler(server, user, password)
    sh.execute('touch --date "{}" /tmp/start'.format(datestr))
    sh.execute('cd /home/bro/logs')
    stats_cmd = 'find -type f -newer /tmp/start -name "stats*"'
    _,_,stat_files = sh.execute(stats_cmd)
    folder = "./tmp_{}".format(cur_date)
    cap_loss_cmd = 'find -type f -newer /tmp/start -name "capture_loss*"'
    _,_,cl_files = sh.execute(cap_loss_cmd)
    all_files = cl_files + stat_files
    all_files = ['/home/bro/logs'+f[1:].strip() for f in all_files if '.log' in f]
    all_files = [re.sub('\:', '\:', f) for f in all_files]
    fnames = ' '.join(all_files)
    #copy all relevant logs into tmp folder
    sh.execute('cp {} {}'.format(fnames, folder))
    # compress tmp folder into a tarball
    sh.execute('tar -cvf tarball.tar.gz {}'.format(folder))
    sh.scp.get(r'/home/bro/logs/tarball.tar', r'./')    
    sh.scp.get(r'/home/bea3ch/shared/trafficAnalysis/trafficStats_{}.txt'.format(device), r'./')
    #unzip local tarball to get tmp folder
    os.system('gunzip ./tarball.tar.gz')
    #unzip all files within tmp folder
    local_files = os.listdir('./{}'.format(folder))
    [os.system('gunzip {}'.format(f)) for f in local_files if '.gz' in f]
    df = pd.read_csv('trafficStats_'+device+'.txt', index_col=False)
    return df
server = 'ivy-mv5g-bulwark.hpc.virginia.edu'
user = 'bea3ch'
password='Br#nD0$!'
cdt = dt.datetime.fromtimestamp(time.time())
datestr = '-'.join([str(cdt.year),str(cdt.month),str(cdt.day-1)])
cur_date = '-'.join([str(cdt.year),str(cdt.month),str(cdt.day)])
sh = ShellHandler(server, user, password)
sh.execute('touch --date "{}" /tmp/start'.format(datestr))
sh.execute('cd /home/bro/logs')
stats_cmd = 'find -type f -newer /tmp/start -name "stats*"'
_,_,stat_files = sh.execute(stats_cmd)
folder = "./tmp_{}".format(cur_date)
cap_loss_cmd = 'find -type f -newer /tmp/start -name "capture_loss*"'
_,_,cl_files = sh.execute(cap_loss_cmd)
all_files = cl_files + stat_files
all_files = ['/home/bro/logs'+f[1:].strip() for f in all_files if '.log' in f]
all_files = [re.sub('\:', '\:', f) for f in all_files]
fnames = ' '.join(all_files)
fnames
sh.execute('cp {} {}'.format(fnames, folder))
sh.execute('mkdir '.format(folder))
sh.execute('cp {} {}'.format(fnames, folder))
# compress tmp folder into a tarball
folder
sh.execute('mkdir '.format(folder))
sh.execute('mkdir {}'.format(folder))
sh.execute('cp {} {}'.format(fnames, folder))
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats')
res = get_data()
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats')
res = get_data()
sh.execute('tar -czvf tarball.tar.gz {}'.format(folder))
folder
sh.execute('tar -cvf tarball.tar.gz {}'.format(folder))
sh = ShellHandler(server, user, password)
sh.execute('touch --date "{}" /tmp/start'.format(datestr))
sh.execute('cd /home/bro/logs')
stats_cmd = 'find -type f -newer /tmp/start -name "stats*"'
_,_,stat_files = sh.execute(stats_cmd)
folder = "./tmp_{}".format(cur_date)
cap_loss_cmd = 'find -type f -newer /tmp/start -name "capture_loss*"'
_,_,cl_files = sh.execute(cap_loss_cmd)
all_files = cl_files + stat_files
all_files = ['/home/bro/logs'+f[1:].strip() for f in all_files if '.log' in f]
all_files = [re.sub('\:', '\:', f) for f in all_files]
fnames = ' '.join(all_files)
#copy all relevant logs into tmp folder
sh.execute('mkdir {}'.format(folder))
sh.execute('cp {} {}'.format(fnames, folder))
# compress tmp folder into a tarball
sh.execute('tar -cvf tarball.tar.gz {}'.format(folder)
sh = ShellHandler(server, user, password)
sh.execute('touch --date "{}" /tmp/start'.format(datestr))
sh.execute('cd /home/bro/logs')
stats_cmd = 'find -type f -newer /tmp/start -name "stats*"'
_,_,stat_files = sh.execute(stats_cmd)
folder = "./tmp_{}".format(cur_date)
cap_loss_cmd = 'find -type f -newer /tmp/start -name "capture_loss*"'
_,_,cl_files = sh.execute(cap_loss_cmd)
all_files = cl_files + stat_files
all_files = ['/home/bro/logs'+f[1:].strip() for f in all_files if '.log' in f]
all_files = [re.sub('\:', '\:', f) for f in all_files]
fnames = ' '.join(all_files)
#copy all relevant logs into tmp folder
sh.execute('mkdir {}'.format(folder))
sh.execute('cp {} {}'.format(fnames, folder))
# compress tmp folder into a tarball
sh.execute('tar -cvf tarball.tar.gz {}'.format(folder))
sh.execute('tar -cvf tarball.tar {}'.format(folder))
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats')
res = get_data()
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats')
res = get_data()
os.system('tar -xvf ./tarball.tar')
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats')
res = get_data()
dire='.'
files = os.listdir(dire)
statfiles = re.findall('(stats.*?)#','#'.join(files))
statfiles
capfiles = re.findall('(cap.*?)#','#'.join(files))
capfiles
dire = './tmp_2018-4-9'
files = os.listdir(dire)
statfiles = re.findall('(stats.*?)#','#'.join(files))
capfiles = re.findall('(cap.*?)#','#'.join(files))
statfiles
capfiles
def build_dataframes(dire='.', device="em2"):
    files = os.listdir(dire)
    statfiles = re.findall('(stats.*?)#','#'.join(files))
    capfiles = re.findall('(cap.*?)#','#'.join(files))
    #create stat dataframe
    df_stats = parse_log('/'.join([dire,statfiles[0]]))
    for s in statfiles[1:]:
        df_new = parse_log('/'.join([dire,s]))
        df_stats = pd.concat(df_stats,df_new)
        df_stats = parse_log('/'.join([dire,statfiles[0]]))
    #create stat dataframe
    df_cl = parse_log('/'.join([dire,capfiles[0]]))
    for cl in capfiles[1:]:
        df_new = parse_log('/'.join([dire,cl]))
        df_cl = pd.concat(df_cl,df_new)
    #get trafficStats
    df_dev = pd.read_csv(dire+'/trafficStats_'+device+'.txt', index_col=False)
    return df_stats,df_cl,df_dev
folder
res = build_dataframes(folder)
from log_parser import parse_log
res = build_dataframes(folder)
def build_dataframes(dire='.', device="em2"):
    files = os.listdir(dire)
    statfiles = re.findall('(stats.*?)#','#'.join(files))
    capfiles = re.findall('(cap.*?)#','#'.join(files))
    #create stat dataframe
    df_stats = parse_log('/'.join([dire,statfiles[0]]))
    for s in statfiles[1:]:
        df_new = parse_log('/'.join([dire,s]))
        df_stats = pd.concat([df_stats,df_new])
        df_stats = parse_log('/'.join([dire,statfiles[0]]))
    #create stat dataframe
    df_cl = parse_log('/'.join([dire,capfiles[0]]))
    for cl in capfiles[1:]:
        df_new = parse_log('/'.join([dire,cl]))
        df_cl = pd.concat([df_cl,df_new])
    #get trafficStats
    df_dev = pd.read_csv(dire+'/trafficStats_'+device+'.txt', index_col=False)
    return df_stats,df_cl,df_dev
res = build_dataframes(folder)
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats')
res = build_dataframes(folder)
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats')
res = get_data()
s,cl,dev = build_dataframes(folder)
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats')
pull_data()
res = build_dataframes(folder)
res[0]
res[0].describe()
res[1].describe()
res[1].shape
res[1].head()
res[1]['ts'].describe()

## ---(Mon Apr  9 12:36:11 2018)---
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats')
pull_data()
res = build_dataframes()
folder = './tmp_2018-4-9'
dire = folder
files = os.listdir(dire)
statfiles = re.findall('(stats.*?\.log)#','#'.join(files))
capfiles = re.findall('(cap.*?\.log)#','#'.join(files))
statfiles
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats')
res = pull_data('bea3ch','Br#nD0$!')
uname, passwd = 'bea3ch', 'Br#nD0$!'
local_dir = "./"
device = "em2"
server = 'ivy-mv5g-bulwark.hpc.virginia.edu'
user = uname
password= passwd
cdt = dt.datetime.fromtimestamp(time.time())
datestr = '-'.join([str(cdt.year),str(cdt.month),str(cdt.day-1)])
cur_date = '-'.join([str(cdt.year),str(cdt.month),str(cdt.day)])
sh = ShellHandler(server, user, password)
sh.execute('touch --date "{}" /tmp/start'.format(datestr))
sh.execute('cd /home/bro/logs')
stats_cmd = 'find -type f -newer /tmp/start -name "stats*"'
_,_,stat_files = sh.execute(stats_cmd)
folder = "./tmp_{}".format(cur_date)
cap_loss_cmd = 'find -type f -newer /tmp/start -name "capture_loss*"'
stats_cmd = 'find -type f -newer /tmp/start -name "stats*"'
_,_,stat_files = sh.execute(stats_cmd)
folder = "./tmp_{}".format(cur_date)
cap_loss_cmd = 'find -type f -newer /tmp/start -name "capture_loss*"'
_,_,cl_files = sh.execute(cap_loss_cmd)
all_files = cl_files + stat_files
all_files
all_files = ['/home/bro/logs'+f[1:].strip() for f in all_files if '.log' in f]
all_files = [re.sub('\:', '\:', f) for f in all_files]
fnames = ' '.join(all_files)
sh.execute('mkdir {}'.format(folder))
sh.execute('cp {} {}'.format(fnames, folder))
traffStats = '/home/bea3ch/shared/trafficAnalysis/trafficStats_{}.txt'.format(device)
sh.execute('cp {} {}'.format(traffStats,folder))
all_files
all_files = cl_files + stat_files
all_files = ['/home/bro/logs'+f[1:].strip() for f in all_files if '.log' in f]
all_files = [re.sub('\:', '\:', f) for f in all_files]
fnames = ' '.join(all_files)
all_files
sh.execute('rm -rf {} tarball.tar'.format(folder))
stats_cmd = 'find -type f -newer /tmp/start -name "stats*"'
_,_,stat_files = sh.execute(stats_cmd)
folder = "./tmp_{}".format(cur_date)
cap_loss_cmd = 'find -type f -newer /tmp/start -name "capture_loss*"'
_,_,cl_files = sh.execute(cap_loss_cmd)
all_files = cl_files + stat_files
all_files = ['/home/bro/logs'+f[1:].strip() for f in all_files if '.log' in f]
all_files = [re.sub('\:', '\:', f) for f in all_files]
fnames = ' '.join(all_files)
all_files
sh.execute('mkdir {}'.format(folder))
sh.execute('cp {} {}'.format(fnames, folder))
traffStats = '/home/bea3ch/shared/trafficAnalysis/trafficStats_{}.txt'.format(device)
sh.execute('cp {} {}'.format(traffStats,folder))
new_files = sh.execute('ls {}'.formaat(folder))
new_files = sh.execute('ls {}'.format(folder))
_,_,new_files = sh.execute('ls {}'.format(folder))
new_files
sh.execute('pwd')
res = sh.execute('ls {}'.format(folder))
res
res[1]
newfiles = res[1]
len(newfiles)
len(all_files)
all_files
res[2]
[len(r) for r in res)
[len(r) for r in res]
res[0]
res[1]
res[2]
cdt = dt.datetime.fromtimestamp(time.time())
datestr = '-'.join([str(cdt.year),str(cdt.month),str(cdt.day-1)])
cur_date = '-'.join([str(cdt.year),str(cdt.month),str(cdt.day)])
sh = ShellHandler(server, user, password)
sh.execute('touch --date "{}" /tmp/start'.format(datestr))
sh.execute('cd /home/bro/logs')
stats_cmd = 'find -type f -newer /tmp/start -name "stats*"'
_,_,stat_files = sh.execute(stats_cmd)
folder = "./tmp_{}".format(cur_date)
cap_loss_cmd = 'find -type f -newer /tmp/start -name "capture_loss*"'
_,_,cl_files = sh.execute(cap_loss_cmd)
all_files = cl_files + stat_files
all_files = ['/home/bro/logs'+f[1:].strip() for f in all_files if '.log' in f]
all_files = [re.sub('\:', '\:', f) for f in all_files]
fnames = ' '.join(all_files)
#copy all relevant logs into tmp folder
sh.execute('mkdir {}'.format(folder))
sh.execute('cp {} {}'.format(fnames, folder))
traffStats = '/home/bea3ch/shared/trafficAnalysis/trafficStats_{}.txt'.format(device)
sh.execute('cp {} {}'.format(traffStats,folder))
_,new_files,_ = sh.execute('ls {}'.format(folder))
len(all_files)
sh.execute('rm -rf {} tarball.tar'.format(folder))
cur_date = '-'.join([str(cdt.year),str(cdt.month),str(cdt.day)])
sh = ShellHandler(server, user, password)
sh.execute('touch --date "{}" /tmp/start'.format(datestr))
sh.execute('cd /home/bro/logs')
stats_cmd = 'find -type f -newer /tmp/start -name "stats*"'
_,_,stat_files = sh.execute(stats_cmd)
folder = "./tmp_{}".format(cur_date)
cap_loss_cmd = 'find -type f -newer /tmp/start -name "capture_loss*"'
_,_,cl_files = sh.execute(cap_loss_cmd)
all_files = cl_files + stat_files
all_files = ['/home/bro/logs'+f[1:].strip() for f in all_files if '.log' in f]
all_files = [re.sub('\:', '\:', f) for f in all_files]
fnames = ' '.join(all_files)
#copy all relevant logs into tmp folder
sh.execute('mkdir {}'.format(folder))
sh.execute('cp {} {}'.format(fnames, folder))
traffStats = '/home/bea3ch/shared/trafficAnalysis/trafficStats_{}.txt'.format(device)
sh.execute('cp {} {}'.format(traffStats,folder))
_,new_files,_ = sh.execute('ls {}'.format(folder))
len(all_files)
len(new_files)
new_files[:5]
all_files[:5]
all_files
dates = [l.split('/')[3] for l in all_files]
dates
dates = [l.split('/')[4] for l in all_files]
dates[:3]
zip(all_files, dates)
ad = all_files[0]
ad
re.split('[0-9]{4}-[0-9]{2}-[0-9]{2}\/',ad)
new_files = []
for date, f in zip(dates,all_files):
    fsplit = re.split('[0-9]{4}-[0-9]{2}-[0-9]{2}\/',f)
    fsplit[1] = date+'_'+fsplit[1]
    new_filename = ''.join(fsplit)
    new_files.append(new_filename)
new_files[:2]
all_files[:2]
new_files = []
for date, f in zip(dates,all_files):
    fsplit = re.split('[0-9]{4}-[0-9]{2}-[0-9]{2}\/',f)
    fsplit[0] += '/' + date + '/'
    fsplit[1] = date+'_'+fsplit[1]
    new_filename = ''.join(fsplit)
    new_files.append(new_filename)
new_files[:2]
new_files = []
for date, f in zip(dates,all_files):
    fsplit = re.split('[0-9]{4}-[0-9]{2}-[0-9]{2}\/',f)
    fsplit[0] += date + '/'
    fsplit[1] = date+'_'+fsplit[1]
    new_filename = ''.join(fsplit)
    new_files.append(new_filename)
new_files
new_files = []
for date, f in zip(dates,all_files):
    fsplit = re.split('[0-9]{4}-[0-9]{2}-[0-9]{2}\/',f)
    fsplit[0] += date + '/'
    fsplit[1] = date[2:]+'_'+fsplit[1]
    new_filename = ''.join(fsplit)
    new_files.append(new_filename)
new_files
len(new_files)
len(all_files)
mv_cmds = ['mv {} {};'.format(old,new) for old,new in zip(all_files,new_files)]
mv_cmds
mv_cmd = ''.join(['mv {} {};'.format(old,new) for old,new in zip(all_files,new_files)])
mv_cmd
mv_cmd = ';'.join(['mv {} {}'.format(old,new) for old,new in zip(all_files,new_files)])
mv_cmd
sh.execute(mv_cmd)
sh.execute('rm -rf {} tarball.tar'.format(folder))
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats')
pull_data('bea3ch', 'Br#nD0$!')
cdt = dt.datetime.fromtimestamp(time.time())
datestr = '-'.join([str(cdt.year),str(cdt.month),str(cdt.day-1)])
cur_date = '-'.join([str(cdt.year),str(cdt.month),str(cdt.day)])
sh = ShellHandler(server, user, password)
sh.execute('touch --date "{}" /tmp/start'.format(datestr))
sh.execute('cd /home/bro/logs')
stats_cmd = 'find -type f -newer /tmp/start -name "stats*"'
_,_,stat_files = sh.execute(stats_cmd)
folder = "./tmp_{}".format(cur_date)
cap_loss_cmd = 'find -type f -newer /tmp/start -name "capture_loss*"'
_,_,cl_files = sh.execute(cap_loss_cmd)
all_files = cl_files + stat_files
all_files = ['/home/bro/logs'+f[1:].strip() for f in all_files if '.log' in f]
all_files = [re.sub('\:', '\:', f) for f in all_files]
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats')
uname, passwd = 'bea3ch', 'Br#nD0$!'
server = 'ivy-mv5g-bulwark.hpc.virginia.edu'
local_dir="./"
device="em2"
server = 'ivy-mv5g-bulwark.hpc.virginia.edu'
user = uname
password= passwd
cdt = dt.datetime.fromtimestamp(time.time())
datestr = '-'.join([str(cdt.year),str(cdt.month),str(cdt.day-1)])
cur_date = '-'.join([str(cdt.year),str(cdt.month),str(cdt.day)])
sh = ShellHandler(server, user, password)
sh.execute('touch --date "{}" /tmp/start'.format(datestr))
sh.execute('cd /home/bro/logs')
stats_cmd = 'find -type f -newer /tmp/start -name "stats*"'
_,_,stat_files = sh.execute(stats_cmd)
folder = "./tmp_{}".format(cur_date)
cap_loss_cmd = 'find -type f -newer /tmp/start -name "capture_loss*"'
_,_,cl_files = sh.execute(cap_loss_cmd)
all_files = cl_files + stat_files
all_files = ['/home/bro/logs'+f[1:].strip() for f in all_files if '.log' in f]
all_files = [re.sub('\:', '\:', f) for f in all_files]
all_files
stats_cmd = 'find -type f -newer /tmp/start -name "*stats*"'
_,_,stat_files = sh.execute(stats_cmd)
folder = "./tmp_{}".format(cur_date)
cap_loss_cmd = 'find -type f -newer /tmp/start -name "*capture_loss*"'
_,_,cl_files = sh.execute(cap_loss_cmd)
all_files = cl_files + stat_files
all_files = ['/home/bro/logs'+f[1:].strip() for f in all_files if '.log' in f]
all_files = [re.sub('\:', '\:', f) for f in all_files]
all_files
dates = [re.findall('''[0-9]{4}-[0-9]{2}-[0-9]{2}\/''',l)[0] for l in all_files]
dates
date,f = zip(dates,all_files)[0]
date,f
dates = [re.findall('''([0-9]{4}-[0-9]{2}-[0-9]{2})\/''',l)[0] for l in all_files]
date,f = zip(dates,all_files)[0]
date,f
date[2:] not in f
for date, f in zip(dates,all_files):
    if date[2:] not in f:
        fsplit = re.split('[0-9]{4}-[0-9]{2}-[0-9]{2}\/',f)
        fsplit[0] += date + '/'
        fsplit[1] = date[2:]+'_'+fsplit[1]
        new_files.append(''.join(fsplit))
    else:
        new_files.append(f)
new_files = []
for date, f in zip(dates,all_files):
    if date[2:] not in f:
        fsplit = re.split('[0-9]{4}-[0-9]{2}-[0-9]{2}\/',f)
        fsplit[0] += date + '/'
        fsplit[1] = date[2:]+'_'+fsplit[1]
        new_files.append(''.join(fsplit))
    else:
        new_files.append(f)
mv_cmd = ';'.join(['mv {} {}'.format(old,new) for old,new in zip(all_files,new_files)])
sh.execute(mv_cmd)
mv_cmd = ';'.join(['mv {} {}'.format(old,new) if old != new for old,new in zip(all_files,new_files)])
mv_cmd = ';'.join(['mv {} {}'.format(old,new) for old,new in zip(all_files,new_files) if old != new ])
mv_cmd
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats')
res = get_data()
res = pull_data()
res = pull_data('bea3ch', 'Br#nD0$!')
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats')
res = pull_data('bea3ch', 'Br#nD0$!')
1366598584./(1366598584+474514392224)

## ---(Tue Apr 10 09:48:57 2018)---
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats')
res =build_dataframes('.')
df = pd.read_csv('trafficStats_em2.csv')
df
make_plot(df)
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats')
res = get_bro_perf('bea3ch', 'Br#nD0$!')
folder
os.listdir('.')
res = build_dataframes('./tmp_2018-04-09')
res = build_dataframes('./tmp_2018-4-9')
folder = './tmp_2018-4-9'
os.listdir(folder)
dire = folder
device = "em2"
files = os.listdir(dire)
files
statfiles = re.findall('(*stats.*?\.log)#','#'.join(files))
capfiles = re.findall('(*cap.*?\.log)#','#'.join(files))
statfiles = re.findall('(.*?stats.*?\.log)#','#'.join(files))
capfiles = re.findall('(.*?cap.*?\.log)#','#'.join(files))
statfiles
statfiles[0]
statfiles[1]
statfiles = re.findall('(.*?stats\..*?\.log)#','#'.join(files))
capfiles = re.findall('(.*?cap\..*?\.log)#','#'.join(files))
statfiles
capfiles
files
'#'.join(files)
re.findall('(.*?_capture.*?\.log)#','#'.join(files))
capfiles = re.findall('(.*?_capture.*?\.log)###','###'.join(files))
capfiles
capfiles = re.findall('(.*?_capture.*?\.log);',';'.join(files))
capfiles
for f in files:
    print f
    
statfiles, capfiles = [],[]
for f in files:
    if 'stats' in f: statfiles.append(f)
    elif 'cap' in f: capfiles.append(f)
statfiles
capfiles
df_stats = parse_log('/'.join([dire,statfiles[0]]))
df_stats
i,s = enumerate(statfiles[1])
i,s = enumerate(statfiles[1:])[1]
i,s, = 1, statfiles[1]
df_new = parse_log('/'.join([dire,s]))
df_stats = pd.concat([df_stats,df_new])
df_stats
df_stats = parse_log('/'.join([dire,statfiles[0]]))
for i,s in enumerate(statfiles[1:]):
    try:
        df_new = parse_log('/'.join([dire,s]))
        df_stats = pd.concat([df_stats,df_new])
    except:
        print('error merging stat df {}'.format(i))

#create stat dataframe
df_stats
df_stats.describe()
df_cl = parse_log('/'.join([dire,capfiles[0]]))
for i,cl in enumerate(capfiles[1:]):
    try:
        df_new = parse_log('/'.join([dire,cl]))
        df_cl = pd.concat([df_cl,df_new])
    except:
        print('error merging cl df {}'.format(i))

#get trafficStats
df_cl
df_cl.head()
df_cl = parse_log('/'.join([dire,capfiles[0]]))
df_cl
capfiles
df_cl = parse_log('/'.join([dire,capfiles[19]]))
df_cl.columns
df_cl.index
df_cl.describe()
df_cl = parse_log('/'.join([dire,capfiles[0]]))
for i,cl in enumerate(capfiles[1:]):
    try:
        df_new = parse_log('/'.join([dire,cl]))
        df_cl = pd.concat([df_cl,df_new])
    except:
        print('error merging cl df {}'.format(i))
df_cl['ts']
min_hash = df_cl['ts'].apply(lambda x: (x.year-1970))
min_hash
min_hash = df_cl['ts'].apply(lambda x: (x.year-1970)*24*12)
min_hash
min_hash = df_cl['ts'].apply(lambda x: (x.year-1970)*24*12 + x.month * 30 * 24 *12 + x.day * 24 * 12)
min_hash
d = df_cl['ts'][0]
d
d = df_cl.ix[0,['ts']]
d
df_cl.shape
df_cl.ix[0,:]
df_cl.to_csv('df_cl.csv')
df_cl.reset_index()
df_cl = df_cl.reset_index()
df_cl.to_csv('df_cl.csv')
df_cl.ix[0,'ts']
d = df_cl.ix[0,'ts']
dir(d)
d.minute
d.time
d.time()
d.hour
min_hash = df_cl['ts'].apply(lambda x: (x.year-1970)*24*12 + x.month * 30 * 24 *12 + x.day * 24 * 12 + x.hour * 12 + x.minute / 5)
min_hash
s = 'brendan'
s.endswith('dan')
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats')
stats,cl,dev = build_dfs(folder)
files = os.listdir(dire)
#make lists of capture loss and stat files
statfiles, capfiles = [],[]
for f in files:
    if not f.endswith('.gz'):
        if 'stats' in f: statfiles.append(f)
        elif 'cap' in f: capfiles.append(f)
res = build_df_from_list(statfiles, dire)
flist = statfiles
df_comb = parse_log('/'.join([dire,flist[0]]))
for i,s in enumerate(flist[1:]):
    try:
        df_new = parse_log('/'.join([dire,s]))
        df_comb = pd.concat([df_comb,df_new])
    except: print('error merging stat df {}'.format(i))

df_comb = df_comb.reset_index()
df_comb['day'] = df_comb['ts'].apply(lambda x: (x.year-1970)*365 +\
       x.month*30 + x.day)
df_comb.ix[0,'day']
df_comb['day']
df_comb.ix[0,['day']]
df_comb.ix[1,['day']]
row = df_comb.ix[1,:]
row
row['ts']
row['day']
row['day']*24
df_comb['hour'] = df_comb.apply(axis=1,lambda row: row['day']*24 + row['ts'].hour)
df_comb['hour'] = df_comb.apply(lambda row: row['day']*24 + row['ts'].hour, axis=1)
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats')
res = build_df_from_list(statfiles,dire)
res
res['minute']
res.ix[10:13,:]
res = parse_log(statfiles[0], export=False)
statfiles[0]
files = os.listdir(dire)
#make lists of capture loss and stat files
statfiles, capfiles = [],[]
for f in files:
    if f.endswith('.log'):
        if 'stats' in f: statfiles.append(f)
        elif 'cap' in f: capfiles.append(f)

#create stat dataframe from stat list
statfiles
stats,cl,dev = build_dfs
stats,cl,dev = build_dfs(folder)
stats['minute'].describe()
stats.to_csv('stats_test.csv')
stats.shape
stats.head()
flist
statfiles
flist = statfiles
df_comb = parse_log('/'.join([dire,flist[0]]))
i,s = 1,flist[1]
i,s
df_new = parse_log('/'.join([dire,s]))
df_new.describe()
df_comb.describe()
df_comb = pd.concat([df_comb,df_new])
df_comb.describe()
i,s = 2,flist[2]
df_new = parse_log('/'.join([dire,s]))
df_comb = pd.concat([df_comb,df_new])
df_comb.describe()
len(flist)
i = 3,flist[3]
df_new = parse_log('/'.join([dire,s]))
df_comb = pd.concat([df_comb,df_new])
df_comb.describe()
df_new.describe()
df_comb = pd.concat([df_comb,df_new])
df_comb.shape
df_comb.describe()
df_comb.nrow()
dir(df_comb)
df_comb = parse_log('/'.join([dire,flist[0]]))
for i,s in enumerate(flist[1:]):
    try:
        df_new = parse_log('/'.join([dire,s]))
        df_comb = pd.concat([df_comb,df_new])
    except: print('error merging stat df {}'.format(i))
df_comb.describe()
df_comb = df_comb.reset_index()
df_comb.describe()
df_comb.index
df_comb.shape
df_comb['day'] = df_comb['ts'].apply(lambda x: (x.year-1970)*365 +\
       x.month*30 + x.day)
df_comb['hour'] = df_comb.apply(lambda row: row['day']*24 + row['ts'].hour, axis=1)
df_comb['minute'] = df_comb.apply(lambda row: row['hour']*60 +\
       row['ts'].minute, axis=1)
df_comb.describe()
df_comb.head(10)
df_comb.idx[1:20,'tcp_conns']
df_comb.ix[1:20,'tcp_conns']
tcp_conns = df_comb.ix[1:20,'tcp_conns']
tcp_conns.describe()
tcp_conns.mean()
sub = df_comb.ix[:50,:]
sub.describe()
df_comb = df_comb.reset_index(drop=True)
df_comb.describe()
df.index
df_comb.index
df_comb = parse_log('/'.join([dire,flist[0]]))
for i,s in enumerate(flist[1:]):
    try:
        df_new = parse_log('/'.join([dire,s]))
        df_comb = pd.concat([df_comb,df_new])
    except: print('error merging stat df {}'.format(i))

df_comb = df_comb.reset_index(drop=True)
df_comb.describe()
df_comb.to_csv('stat_test_2.csv')
df_comb.dtypes
df_comb['pkt_lag'] = df_comb['pkt_lag'].astype(int64)
df_comb['pkt_lag'] = df_comb['pkt_lag'].astype('int64')
df_comb.dtypes
stats, cl, dev = build_dfs(dire)
stats.describe()
df_comb = build_df_from_list(statfiles,dire)
df_comb.describe()
statfiles, capfiles = [],[]
for f in files:
    if f.endswith('.log'):
        if 'stats' in f: statfiles.append(f)
        elif 'cap' in f: capfiles.append(f)
statfiles
df_stats = build_df_from_list(statfiles, dire)
df_stats.describe()
df_cl = build_df_from_list(capfiles, dire)
df_cl.describe()
df_dev = pd.read_csv(dire+'/trafficStats_'+device+'.txt', index_col=False)
def build_dfs(dire='.', device="em2"):
    files = os.listdir(dire)
    #make lists of capture loss and stat files
    statfiles, capfiles = [],[]
    for f in files:
        if f.endswith('.log'):
            if 'stats' in f: statfiles.append(f)
            elif 'cap' in f: capfiles.append(f)
    #create stat dataframe from stat list
    df_stats = build_df_from_list(statfiles, dire)
    #create stat dataframe from capture loss list
    df_cl = build_df_from_list(capfiles, dire)
    #get trafficStats
    df_dev = pd.read_csv(dire+'/trafficStats_'+device+'.txt', index_col=False)
    return df_stats,df_cl,df_dev
res = build_dfs(folder)
res[0].head(20)
res[0].describe()
res[1].describe()
res[2].describe()
df_cl = build_df_from_list(capfiles, dire)
capfiles[19]
res = parse_log(capfiles[19])
res = parse_log('/'.join(dire,capfiles[19]))
res = parse_log('/'.join([dire,capfiles[19])])
'/'.join([dire,capfiles[19]])
res = parse_log('/'.join([dire,capfiles[19]]))
res.describe()
res2 = parse_log('/'.join([dire,capfiles[18]]))
res3 = pd.concat(res,res2)
res3 = pd.concat([res,res2])
def build_df_from_list(flist,dire='.'):
    df_comb = parse_log('/'.join([dire,flist[0]]))
    for i,s in enumerate(flist[1:]):
        #try:
        df_new = parse_log('/'.join([dire,s]))
        df_comb = pd.concat([df_comb,df_new])
        #except: print('error merging stat df {}'.format(i))
    df_comb = df_comb.reset_index(drop=True)
    df_comb['day'] = df_comb['ts'].apply(lambda x: (x.year-1970)*365 +\
           x.month*30 + x.day)
    df_comb['hour'] = df_comb.apply(lambda row: row['day']*24 + row['ts'].hour, axis=1)
    df_comb['minute'] = df_comb.apply(lambda row: row['hour']*60 +\
           row['ts'].minute, axis=1)
    return df_comb
res = build_df_from_list(capfiles,dire)
capfiles[19]
f = open('/'.join([dire,capfiles[19]]),'r')
f.read()
res = parse_log('/'.join([dire,capfiles[19]]))
def build_df_from_list(flist,dire='.'):
    df_comb = parse_log('/'.join([dire,flist[0]]))
    for i,s in enumerate(flist[1:]):
        #try:
        print(i,s)
        df_new = parse_log('/'.join([dire,s]))
        df_comb = pd.concat([df_comb,df_new])
        #except: print('error merging stat df {}'.format(i))
    df_comb = df_comb.reset_index(drop=True)
    df_comb['day'] = df_comb['ts'].apply(lambda x: (x.year-1970)*365 +\
           x.month*30 + x.day)
    df_comb['hour'] = df_comb.apply(lambda row: row['day']*24 + row['ts'].hour, axis=1)
    df_comb['minute'] = df_comb.apply(lambda row: row['hour']*60 +\
           row['ts'].minute, axis=1)
    return df_comb
res = build_df_from_list(capfiles,dire)
res = parse_log(capfiles[20])
res = parse_log('/'.join([dire,capfiles[20]]))
res = parse_log('/'.join([dire,capfiles[21]]))
res = parse_log('/'.join([dire,capfiles[22]]))
capfiles[20:22]
res = parse_log('/'.join([dire,capfiles[23]]))
capfiles[20:23]
comb = stats.join([cl,dev] on="minute", how="inner")
comb = stats.join([cl,dev], on="minute", how="inner")
stats.set_index(['day','hour','minute'],append=True)
stats = stats.set_index(['day','hour','minute'])
stats
stats = build_df_from_list(statfiles, dire)
stats.describe()
stats.head()
stats.describe()
comb = stats.join(cl, on="minute", how="inner")
res = stats.join(cl,on="minutes",how="inner",lsuffix="_stat")
res = stats.join(cl,on="minute",how="inner",lsuffix="_stat")
res
stats['ts'].range
stats['ts'].range()
stats['ts'].min()
stats['ts'].max()
cl.ts.min()
cl.ts.max()
stats.minute.min()
stats.minute.max()
cl.minute.min(), cl.minute.max()
s1 = set(stats.minutes.tolist())
s1 = set(stats.ix[:,'minute'].tolist())
s2 = set(cl.ix[:,'minute'].tolist())
s1.intersection(s2)
len(s1.intersection(s2))
len(s1)
len(s2)
res = stats.join(cl, on="minute", lsuffix="_stats")
res
res = stats.join(cl, on="minute", lsuffix="_stats")
res.describe()
cl.describe()
cl = build_df_from_list(capfiles,dire)
def build_df_from_list(flist,dire='.'):
    df_comb = parse_log('/'.join([dire,flist[0]]))
    for i,s in enumerate(flist[1:]):
        try:
            df_new = parse_log('/'.join([dire,s]))
            df_comb = pd.concat([df_comb,df_new])
        except: print('error merging stat df {}'.format(i))
    df_comb = df_comb.reset_index(drop=True)
    df_comb['day'] = df_comb['ts'].apply(lambda x: (x.year-1970)*365 +\
           x.month*30 + x.day)
    df_comb['hour'] = df_comb.apply(lambda row: row['day']*24 + row['ts'].hour, axis=1)
    df_comb['minute'] = df_comb.apply(lambda row: row['hour']*60 +\
           row['ts'].minute, axis=1)
    return df_comb
res = build_df_from_list(capfiles,dire)
res.describe()
join_res = stats.join(res, on="minute", lsuffix="_stats")
join_res.describe()
cities = ['chicago', 'detroit']
teams = ['bulls', 'pistons']
champs = [6,3]
d1 = pd.DataFrame(data=zip(cities,teams),columns=['city','team'])
d1
d2 = pd.DataFrame(data=zip(teams,champs),columns=['team','num_champs'])
d2
d1.join(d2, on="team", lsuffix="_d1")
d1.join(d2, lsuffix="_d1",rsuffix="_d2")
d1.join(d2, on=["team"], lsuffix="_d1")
stats.set_index('minute')
stats.set_index('minute').join(cl.set_index('minute'),l_suffix="_stats",rsuffix="_cl")
stats.set_index('minute').join(cl.set_index('minute'),lsuffix="_stats",rsuffix="_cl")
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats')
def build_dfs(dire='.', device="em2", join_key="minute"):
    assert(join_by in ['minute','hour','day'])
    files = os.listdir(dire)
    #make lists of capture loss and stat files
    statfiles, capfiles = [],[]
    for f in files:
        if f.endswith('.log'):
            if 'stats' in f: statfiles.append(f)
            elif 'cap' in f: capfiles.append(f)
    #create stat dataframe from stat list
    df_stats = build_df_from_list(statfiles, dire)
    #create stat dataframe from capture loss list
    df_cl = build_df_from_list(capfiles, dire)
    #get trafficStats
    df_dev = pd.read_csv(dire+'/trafficStats_'+device+'.txt', index_col=False)
    
    df_comb = df_stats.set_index(join_key).join(df_cl.set_index(join_key), lsuffix="_stats",rsuffix="cl")
    df_comb = df_comb.set_index(join_key).join(df_dev.set_index(join_key),rsuffix="_dev")
    return df_stats,df_cl,df_dev
def build_dfs(dire='.', device="em2", join_key="minute"):
    assert(join_key in ['minute','hour','day'])
    files = os.listdir(dire)
    #make lists of capture loss and stat files
    statfiles, capfiles = [],[]
    for f in files:
        if f.endswith('.log'):
            if 'stats' in f: statfiles.append(f)
            elif 'cap' in f: capfiles.append(f)
    #create stat dataframe from stat list
    df_stats = build_df_from_list(statfiles, dire)
    #create stat dataframe from capture loss list
    df_cl = build_df_from_list(capfiles, dire)
    #get trafficStats
    df_dev = pd.read_csv(dire+'/trafficStats_'+device+'.txt', index_col=False)
    
    df_comb = df_stats.set_index(join_key).join(df_cl.set_index(join_key), lsuffix="_stats",rsuffix="cl")
    df_comb = df_comb.set_index(join_key).join(df_dev.set_index(join_key),rsuffix="_dev")
    return df_stats,df_cl,df_dev
res = build_dfs(dire)
def build_dfs(dire='.', device="em2", join_key="minute"):
    assert(join_key in ['minute','hour','day'])
    files = os.listdir(dire)
    #make lists of capture loss and stat files
    statfiles, capfiles = [],[]
    for f in files:
        if f.endswith('.log'):
            if 'stats' in f: statfiles.append(f)
            elif 'cap' in f: capfiles.append(f)
    #create stat dataframe from stat list
    df_stats = build_df_from_list(statfiles, dire)
    #create stat dataframe from capture loss list
    df_cl = build_df_from_list(capfiles, dire)
    #get trafficStats
    df_dev = pd.read_csv(dire+'/trafficStats_'+device+'.txt', index_col=False)
    
    df_comb = df_stats.set_index(join_key).join(df_cl.set_index(join_key),rsuffix="cl")
    df_comb = df_comb.set_index(join_key).join(df_dev.set_index(join_key),rsuffix="_dev")
    return df_stats,df_cl,df_dev
res = build_dfs(dire)
join_key="minute"
assert(join_key in ['minute','hour','day'])
files = os.listdir(dire)
#make lists of capture loss and stat files
statfiles, capfiles = [],[]
for f in files:
    if f.endswith('.log'):
        if 'stats' in f: statfiles.append(f)
        elif 'cap' in f: capfiles.append(f)

#create stat dataframe from stat list
df_stats = build_df_from_list(statfiles, dire)
#create stat dataframe from capture loss list
df_cl = build_df_from_list(capfiles, dire)
#get trafficStats
df_dev = pd.read_csv(dire+'/trafficStats_'+device+'.txt', index_col=False)
df_comb = df_stats.set_index(join_key).join(df_cl.set_index(join_key),rsuffix="cl")
df_comb.columns
df_comb.index
df_comb = df_comb.join(df_dev.set_index(join_key),rsuffix="_dev")
df_dev['minute']
df_dev = build_df_from_list([dire+'/trafficStats_'+device+'.txt'])
d3
d1
d2
d2.append({'team':'lakers','num_champs':11})
d2.append({'team':'lakers','num_champs':11},ignore_index=True)
d2
d2 = d2.append({'team':'lakers','num_champs':11},ignore_index=True)
d1.set_index('team').join(d2.set_index('team'),rsuffix="_d2")
d2.rename({'num_champs':'champions'})
d2.rename(index=str,{'num_champs':'champions'})
d2.rename(columns={'num_champs':'champions'})
'champions' in d2.columns
'num_champs' in d2.columns
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats/log_parser.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats')
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats')
df_dev = build_df_from_list([dire+'/trafficStats_'+device+'.txt'])
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats')
res = build_dfs(dire)
df_dev = pd.read_csv(dire+'/trafficStats_'+device+'.txt', index_col=False)
df_dev.columns
if 'time' in df_dev.columns: df_dev.rename(columns={'time':'ts'})
if 'time' in df_dev.columns: df_dev = df_dev.rename(columns={'time':'ts'})
df_dev.columns
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats')
res = build_dfs(dire)
d3
d2
d3 = d1.set_index('team').join(d2.set_index('team'),rsuffix="_d2"))
d3 = d1.set_index('team').join(d2.set_index('team'),rsuffix="_d2")
d3
d3['num_champs'].apply(lambda x: x+1)
def fix_time_col(df):
    if 'time' in df.columns:
        df = df.rename(columns={'time':'ts'})
        df['ts'] = df['ts'].apply(lambda x: dt.datetime.fromtimestamp(x))
    return df
df_dev.columns
df_dev = pd.read_csv(dire+'/trafficStats_'+device+'.txt', index_col=False)
df_dev.columns
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats')
'time' in df_dev.columns
df_dev = fix_time_col(df_dev)
df_dev['ts']
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats')
res = build_dfs(dire)
res
assert(join_key in ['minute','hour','day'])
files = os.listdir(dire)
#make lists of capture loss and stat files
statfiles, capfiles = [],[]
for f in files:
    if f.endswith('.log'):
        if 'stats' in f: statfiles.append(f)
        elif 'cap' in f: capfiles.append(f)

#create stat dataframe from stat list
df_stats = build_df_from_list(statfiles, dire)
#create stat dataframe from capture loss list
df_cl = build_df_from_list(capfiles, dire)
#get trafficStats
df_dev = pd.read_csv(dire+'/trafficStats_'+device+'.txt', index_col=False)
if 'time' in df_dev.columns: df_dev = add_datetime(df_dev)

df_dev = add_hashes(df_dev)
df_comb = df_stats.set_index(join_key).join(df_cl.set_index(join_key),rsuffix="cl")
df_comb
df_comb.index
df_dev.index
df_dev = df_dev.set_index('minute')
df_dev.index
df_comb.describe()
df_comb.index.min()
df_comb.index.mas()
df_comb.index.max()
df_dev.index.min()
df_dev.index.max()
assert(join_key in ['minute','hour','day'])
files = os.listdir(dire)
#make lists of capture loss and stat files
statfiles, capfiles = [],[]
for f in files:
    if f.endswith('.log'):
        if 'stats' in f: statfiles.append(f)
        elif 'cap' in f: capfiles.append(f)

#create stat dataframe from stat list
df_stats = build_df_from_list(statfiles, dire)
#create stat dataframe from capture loss list
df_cl = build_df_from_list(capfiles, dire)
#get trafficStats
df_dev = pd.read_csv(dire+'/trafficStats_'+device+'.txt', index_col=False)
if 'time' in df_dev.columns: df_dev = add_datetime(df_dev)

df_dev = add_hashes(df_dev)
df_comb = df_stats.set_index(join_key).join(df_cl.set_index(join_key),rsuffix="cl")

df_dev.minute.min()
df_dev.minute.max()
df_comb.index.min()
df_dev.minute = df_dev.minute.apply(lambda x:x+300,axis=1)
df_dev.minute = df_dev.minute.apply(axis=1,lambda x:x+300)
df_dev.minute = df_dev.minute.apply(lambda x:x+300)
df_comb = df_comb.join(df_dev.set_index(join_key),rsuffix="_dev")
df_comb
df_comb['cpu0'].describe()
df_dev.minute = df_dev.minute.apply(lambda x:x+200)
df_comb = df_comb.join(df_dev.set_index(join_key),rsuffix="_dev")
df_comb['cpu0'].describe()
df_comb.describe()
df_comb.to_csv('df_comb_test.csv')
df_stats.to_csv('stats_test2.csv')
df_cl.to_csv('cap_loss.csv')
df_dev.to_csv('trafficStatsAll.csv')
df_dev.minute.min(), df_dev.minute.max()
df_dev.minute = df_dev.minute.apply(lambda x: x+500)
df_dev.minute.min(), df_dev.minute.max()
df_cl.minute.min(), df_cl.minute.max()
df_dev.to_csv('trafficStatsAll.csv')

## ---(Wed Apr 11 13:12:10 2018)---
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/monitoringScripts/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/monitoringScripts')
res = pull_data('bea3ch', 'Br#nD0$!')
res = pull_data('bea3ch', 'Br#nD0$@')

## ---(Wed Apr 11 16:26:44 2018)---
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats')
uname, passwd = 'bea3ch', 'Br#nD0$@'
clear
clar()
clear()
server = 'ivy-mv5g-bulwark.hpc.virginia.edu'
user = uname
password= passwd
cdt = dt.datetime.fromtimestamp(time.time())
datestr = '-'.join([str(cdt.year),str(cdt.month),str(cdt.day-1)])
cur_date = '-'.join([str(cdt.year),str(cdt.month),str(cdt.day)])
sh = ShellHandler(server, user, password)
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats')
res = pull_data(uname, passwd)
server = 'ivy-mv5g-bulwark.hpc.virginia.edu'
user = uname
password= passwd
bro_dir = '/mnt/localraid/bro/logs'
cdt = dt.datetime.fromtimestamp(time.time())
datestr = '-'.join([str(cdt.year),str(cdt.month),str(cdt.day-1)])
cur_date = '-'.join([str(cdt.year),str(cdt.month),str(cdt.day)])
sh = ShellHandler(server, user, password)
sh.execute('touch --date "{}" /tmp/start'.format(datestr))
sh.execute('cd {}'.format(bro_dir))
stats_cmd = 'find -type f -newer /tmp/start -name "*stats*"'
_,_,stat_files = sh.execute(stats_cmd)
stat_files
res = sh.execute(stats_cmd)
res
_,stat_files,_ = sh.execute(stats_cmd)
stat_files
folder = "./tmp_{}".format(cur_date)
cap_loss_cmd = 'find -type f -newer /tmp/start -name "*capture_loss*"'
_,cl_files,_ = sh.execute(cap_loss_cmd)
cl_files
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats')
pull_data(uname, passwd)
sh = ShellHandler(server, user, password)
sh.execute('touch --date "{}" /tmp/start'.format(datestr))
sh.execute('cd {}'.format(bro_dir))
stats_cmd = 'find -type f -newer /tmp/start -name "*stats*"'
_,stat_files,_ = sh.execute(stats_cmd)
folder = "./tmp_{}".format(cur_date)
cap_loss_cmd = 'find -type f -newer /tmp/start -name "*capture_loss*"'
_,cl_files,_ = sh.execute(cap_loss_cmd)
all_files = cl_files + stat_files
all_files = [bro_dir +f[1:].strip() for f in all_files if '.log' in f]
all_files = [re.sub('\:', '\:', f) for f in all_files]
all_files
dates = [re.findall('''([0-9]{4}-[0-9]{2}-[0-9]{2})\/''',l)[0] for l in all_files]
new_files = []
for date, f in zip(dates,all_files):
    if date[2:] not in f:
        fsplit = re.split('[0-9]{4}-[0-9]{2}-[0-9]{2}\/',f)
        fsplit[0] += date + '/'
        fsplit[1] = date[2:]+'_'+fsplit[1]
        new_files.append(''.join(fsplit))
    else:
        new_files.append(f)
new_files
mv_cmd = ';'.join(['mv {} {}'.format(old,new) for old,new in zip(all_files,new_files) if old != new ])
mv_cmd
fnames = ' '.join(new_files)
sh.execute('mkdir {}'.format(folder))
sh.execute('cp {} {}'.format(fnames, folder))
traffStats = '/home/bea3ch/shared/trafficAnalysis/trafficStats_{}.txt'.format(device)
device="em2"
traffStats = '/home/bea3ch/shared/trafficAnalysis/trafficStats_{}.txt'.format(device)
sh.execute('ls {}'.format(folder))
sh.execute('tar -cvf tarball.tar {}'.format(folder))
sh.scp.get(r'{}/tarball.tar'.format(bro_dir), r'./')
sh.execute('rm -rf {} tarball.tar'.format(folder))
os.system('tar -xvf ./tarball.tar')
local_files = os.listdir('{}'.format(folder))
local_files
os.system('rm ./tarball.tar')
[os.system('gunzip {}'.format(f)) for f in local_files if '.gz' in f]
os.listdir(folder)
[os.system('gunzip {}'.format('/'.join([folder,f]))) for f in local_files if '.gz' in f]
os.system('rm {}/*.gz'.format(folder))
statfiles
stat_files
server = 'ivy-mv5g-bulwark.hpc.virginia.edu'
user = uname
password= passwd
bro_dir = '/mnt/localraid/bro/logs'
cdt = dt.datetime.fromtimestamp(time.time())
datestr = '-'.join([str(cdt.year),str(cdt.month),str(cdt.day-1)])
cur_date = '-'.join([str(cdt.year),str(cdt.month),str(cdt.day)])
sh = ShellHandler(server, user, password)
sh.execute('touch --date "{}" /tmp/start'.format(datestr))
sh.execute('cd {}'.format(bro_dir))
stats_cmd = 'find -type f -newer /tmp/start -name "*stats*"'
_,stat_files,_ = sh.execute(stats_cmd)
stat_files
os.getcwd()
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/trafficStats')
res = pull_data(uname, passwd)
pull_data(uname,passwd)
stats, cl, dev = build_dfs(folder)
dire = folder
join_key="minute"
files = os.listdir(dire)
#make lists of capture loss and stat files
statfiles, capfiles = [],[]
for f in files:
    if f.endswith('.log'):
        if 'stats' in f: statfiles.append(f)
        elif 'cap' in f: capfiles.append(f)
statfiles
capfiles
df_stats = build_df_from_list(statfiles, dire)
df_cl = build_df_from_list(capfiles, dire)
df_dev = pd.read_csv(dire+'/trafficStats_'+device+'.txt', index_col=False)
df_dev['time']
df_dev.columns
df_dev['time'].describe()
time.time()
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW1/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW1')
da = DocAnalyzer(N=1)
da = loadDir(da, './yelp/train')

## ---(Fri Apr 13 12:16:58 2018)---
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW1/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW1')

## ---(Sun Apr 15 18:26:41 2018)---
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw5/hw5_code/q_learn.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw5/hw5_code')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw5/hw5_code/cliff_walking.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw5/hw5_code')
fig.savefig('cliff_walking.jpg')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw5/hw5_code/doubleQ.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw5/hw5_code')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw5/hw5_code/max_bias.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/hw5/hw5_code')

## ---(Tue Apr 17 17:33:58 2018)---
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW1/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW1')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/LanguageModel.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da_train = load_obj('da_train_new')
dir(da_train)
da.m_reviews[0]
da_train.m_reviews[0]
print(da_train.m_reviews[0])
dir(da_train.m_reviews[0])
printReview(da_train.m_reviews[0])
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/post.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
p = createPost(da_train)
def createPost(da, dire='yelp/test'):
    num_files = len(os.listdir(dire))
    choice = np.random.choice(range(num_files))
    json_data = da.loadJson('/'.join([dire,test_files[choice]]))
    revChoice = np.random.choice(range(len(json_data['Reviews'])))
    rev = post(json_data['Reviews'][revChoice])
    rev.tokens = textToGrams(da,rev.content)
    return rev
p1 = createPost(da_train)
os.getcwd()
p1 = createPost(da_train)
def createPost(da, dire='yelp/test'):
    files = os.listdir(dire)
    choice = np.random.choice(range(len(files)))
    json_data = da.loadJson('/'.join([dire,files[choice]]))
    revChoice = np.random.choice(range(len(json_data['Reviews'])))
    rev = post(json_data['Reviews'][revChoice])
    rev.tokens = textToGrams(da,rev.content)
    return rev
p1 = createPost(da_train)
dire='yelp/test'
da = da_train
files = os.listdir(dire)
choice = np.random.choice(range(len(files)))
files
choice
files[10]
da.loadJson('/'.join([dire,files[choice]]))
'/'.join([dire,files[choice]])
f = open('/'.join([dire,files[choice]]), 'r')
f.read()
clear
f = open('/'.join([dire,files[choice]]), 'r')
res = json.load(f)
dir(da_train)
fname = '/'.join([dire,files[choice]])
res = da_train.loadJson(fname)
def loadJson(da, fname):
        with open(fname, 'r') as f:
            return json.load(f)
res = loadJson(da_train, fname)
res
def loadJson(fname):
        with open(fname, 'r') as f:
            return json.load(f)
import gc
gc.collect()
def createPost(da, dire='yelp/test'):
    files = os.listdir(dire)
    choice = np.random.choice(range(len(files)))
    json_data = loadJson('/'.join([dire,files[choice]]))
    revChoice = np.random.choice(range(len(json_data['Reviews'])))
    rev = post(json_data['Reviews'][revChoice])
    rev.tokens = textToGrams(da,rev.content)
    return rev
def createPost(dire='yelp/test'):
    files = os.listdir(dire)
    choice = np.random.choice(range(len(files)))
    json_data = loadJson('/'.join([dire,files[choice]]))
    revChoice = np.random.choice(range(len(json_data['Reviews'])))
    rev = post(json_data['Reviews'][revChoice])
    rev.tokens = textToGrams(da,rev.content)
    return rev
p1 = createPost()
def createPost(da,dire='yelp/test'):
    files = os.listdir(dire)
    choice = np.random.choice(range(len(files)))
    json_data = loadJson('/'.join([dire,files[choice]]))
    revChoice = np.random.choice(range(len(json_data['Reviews'])))
    rev = post(json_data['Reviews'][revChoice])
    rev.tokens = textToGrams(da,rev.content)
    return rev
p1 = createPost(da_train)
nltk.sent_tokenize('youre a cunt')
files = os.listdir(dire)
choice = np.random.choice(range(len(files)))
json_data = loadJson('/'.join([dire,files[choice]]))
revChoice = np.random.choice(range(len(json_data['Reviews'])))
rev = post(json_data['Reviews'][revChoice])
rev.tokens = textToGrams(da,rev.content)
rev.content
raw_tokens = da.tokenize(text)
text = rev.content
raw_tokens = da.tokenize(text)
da
da.tokenize('this is a test')
da2 = DocAnalyzer()
da2.tokenize(rev.content)
p1 = createPost(da2)
print(p1)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/post.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
p1 = createPost(da2)
print(p1)
p1 = createPost(da2)
print(p1)
p1.content
p1.review
dir(p1)
p1.rating
int(p1.rating)
int(float(p1.rating))
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/post.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
p1 = createPost(da2)
print(p1)
p1.sent
da2.m_reviews = [d for d in da_train.m_reviews]
da_test = load_obj('da_test')
da_test = load_obj('da_test_new')
da_comb = da2.merge(da_test)
da_comb = da2.mergeDA(da_test)
del(da2,da_test)
del(da_train)
da_comb.p = 'hello'
da_comb
da_test = load_obj('da_test_new')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da_test_new = da_test.copy()
da_train = load_obj('da_train_new')
da_sub = DocAnalyzer()
sub = l2 = ['CvmAN25laBbwZTqmlEAR1Q.json',
 'd5YWKrP-zG74nqOYzHn7Zg.json',
 'dCw8uBtwnJFKwMnASlZLzg.json']
l2
sub
a=b=1
a
a,b
da_sub = loadDir(da_sub, 'yelp/train', sublist=sub)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer()
l2 = ['CvmAN25laBbwZTqmlEAR1Q.json',
 'd5YWKrP-zG74nqOYzHn7Zg.json',
 'dCw8uBtwnJFKwMnASlZLzg.json']
da = loadDir(da, 'yelp/train', sublist=l2)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer(N=2)
da = loadDir(da, sublist=sub)
l2 = ['CvmAN25laBbwZTqmlEAR1Q.json',
 'd5YWKrP-zG74nqOYzHn7Zg.json',
 'dCw8uBtwnJFKwMnASlZLzg.json']
da = loadDir(da, sublist=l2)
da = loadDir(da, 'yelp/train', sublist=l2)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer()
da = loadDir(da, 'yelp/train', sublist=l2)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer()
da = loadDir(da, 'yelp/train', sublist=l2)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer()
da = loadDir(da, 'yelp/train', sublist=l2)
import time
da = loadDir(da, 'yelp/train', sublist=l2)
del(da)
da = DocAnalyzer(N=1)
da = loadDir(da, 'yelp/train', sublist=l2)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da2 = DocAnalyzer(N=2)
da2 = loadDir(da2, 'yelp/train', sublist=l2)
da1 = DocAnalyzer(N=1)
da1 = loadDir(da1, 'yelp/train', sublist=l2)
l = ['a','n']
l3 = ['b','d']
l1.extend(l3)
l.extend(l3)
l
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer(N=1)
da = loadDir(da, 'yelp/train', sublist = l3)
da.m_reviews
da = loadDir(da, 'yelp/train', sublist = l2)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer(N=1)
da = loadDir(da, 'yelp/train', sublist = l2)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer(N=1)
da = loadDir(da, 'yelp/train', sublist = l2)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer(N=1)
da = loadDir(da, 'yelp/train', sublist = l2)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer(N=1)
gc.collect()
import gc
gc.collect()
da = DocAnalyzer(N=1)
da = loadDir(da, 'yelp/train', sublist = l2)
d = {'a':23,'b':40}
d[a] = d.get('b',0)+20
d['a'] = d.get('b',0)+20
d['a']
d['c'] = d.get('c',0) + 15
d['c']
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer(N=1)
da = loadDir(da, 'yelp/train', sublist=l2)

## ---(Tue Apr 17 21:22:21 2018)---
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
l2 = ['CvmAN25laBbwZTqmlEAR1Q.json',
 'd5YWKrP-zG74nqOYzHn7Zg.json',
 'dCw8uBtwnJFKwMnASlZLzg.json']
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer()
da = loadDir(da, 'yelp/train', sublist=l2)
def loadDir(da, directory, sublist=None, suffix=".json", debug=False, old=False):
    files = os.listdir(directory)
    if sublist: files = sublist
    for f in files:
        filename = "/".join([directory,f])
        #try:                   
        print("-------file {} ({} / {})----".format(filename, files.index(f)+1, len(files)))
        if os.path.isfile(filename) and f.endswith(suffix):
            if old:
                da.ad_old(da.loadJson("/".join([directory,f])))
            else:
                da.analyzeDoc(da.loadJson("/".join([directory,f])), debug=debug)                   
        
        elif os.path.isdir(filename):
            new_dir = filename
            da = loadDir(da, new_dir, suffix)
        #except:
            #print("error reading file {}".format(f))
    return da
da = loadDir(da, 'yelp/train', sublist=l2[0], old=True)
da = loadDir(da, 'yelp/train', sublist=l2[0:2], old=True)
da = loadDir(da, 'yelp/train', sublist=l2[0:2], old=False)
da1 = loadDir(da, 'yelp/train', sublist=l2[0:2], old=True)
def loadDir(da, directory, sublist=None, suffix=".json", debug=False, old=False):
    files = os.listdir(directory)
    if sublist: files = sublist
    for f in files:
        filename = "/".join([directory,f])
        #try:                   
        print("-------file {} ({} / {})----".format(filename, files.index(f)+1, len(files)))
        if os.path.isfile(filename) and f.endswith(suffix):
            if old:
                da.ad_old(da.loadJson("/".join([directory,f])), debug=debug)
            else:
                da.analyzeDoc(da.loadJson("/".join([directory,f])), debug=debug)                   
        
        elif os.path.isdir(filename):
            new_dir = filename
            da = loadDir(da, new_dir, suffix)
        #except:
            #print("error reading file {}".format(f))
    return da
da1 = loadDir(da, 'yelp/train', sublist=l2[0:2], old=True, debug=True)
da1.tf
da1.df
da2 = loadDir(da, 'yelp/train', sublist=l2[0:2], old=False, debug=True)
da2.df['goodw']
len(da2.df)
len(da1.df)
ct = 0
for k,v in da1.df.values():
    if v == da2.df[k]:
        counter +=1
        
for k,v in da1.df.values():
    if v == da2.df[k]:
        counter +=1
        
da1.df.values()[:3]
for k,v in da1.df.items():
    if v == da2.df[k]:
        counter +=1
        
counter = 0
for k,v in da1.df.items():
    if v == da2.df[k]:
        counter +=1
        
counter
counter = 0
for k,v in da1.tf.items():
    if v == da2.tf[k]:
        counter +=1
        
counter
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer(N=1)
da.loadDir('yelp/train', sublist=l2, debug=True)
p1 = da.m_reviews[0]
p1.sfent
p1.sent
p1.review
p1.rating
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer(N=2)
da.loadDir('yelp/train', sublist=l3, debug=True)
da.loadDir('yelp/train', sublist=l2, debug=True)
da.lls[0]
da.__dict__.keys()
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer(N=2)
da.__dict__.keys()
da.lls
da.df
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer()
da.loadDir('yelp/train', sublist=l2, debug=True)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer()
da.loadDir('yelp/train', sublist=l2, debug=True)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer()
da.loadDir('yelp/train', sublist=l2, debug=True)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer()
da.loadDir('yelp/train', sublist=l2, debug=True)
da.lls[0]
print([k,v,da.lls[1][k] for k,v in da.lls[0].items()])
print([(k,v,da.lls[1][k]) for k,v in da.lls[0].items()])
print([(k,v,da.lls[1].get(k,0)) for k,v in da.lls[0].items()])
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer(N=1)
da.loadDir('yelp/train', sublist=l2,debug=True)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer(N=1)
da.loadDir('yelp/train', sublist=l2,debug=True)
da.mgnls['tf'][0]
da.mgnls['tf'][0]['flavor']
da.mgnls['tf'][1]['flavor']
da.mgnls['df'][0]['flavor']
da.mgnls['df'][1]['flavor']
da.prior
da.set_prior()
da.prior
int(da.prior * len(da.m_reviews))
pos_revs = [r for r in da.m_reviews if r.sent == 1]
len(pos_revs)
x = 5
-x
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer()
da.loadDir('yelp/train', sublist=l3, debug=True)
da.loadDir('yelp/train', sublist=l2, debug=True)
da.calcIG('food')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer()
da.loadDir('yelp/train', sublist=l2, debug=True)
da.calcIG('food')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer()
da.loadDir('yelp/train', sublist=l2, debug=True)
da.calcIG('food')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer()
da.loadDir('yelp/train', sublist=l2, debug=True)
da.calcIG('food')
def calcIG(da, t):
    if da.prior == 0: da.set_prior()
    tot_pos = int(da.prior * len(da.m_reviews))
    for t in da.tf.keys():
        p_P = da.prior #prob of Positive(P)
        p_t = float(da.tf[t]) / sum(da.tf.values())
        p_Pt = float(da.mgnls['df'][1][t]) / tot_pos
        # prior: -1 * [p(y=0)log(y=0) + p(y=1)log(p(y=1))]
        prior_ent = -(p_P * np.log(p_P) + (1-p_P)*np.log(1-p_P))
        # pos: p(t) * [p(y=0|t)log(y=0|t) + p(y=1|t)+log(p(y=1|t))]
        pos_ent = p_t * (p_Pt * np.log(p_Pt) + (1-p_Pt)*np.log(1-p_Pt))
        # neg: p(!t) * [p(y=0|!t)log(y=0|!t) + p(y=1|!t)+log(p(y=1|!t))]
        neg_ent = (1-p_t) * ((1-p_Pt) * np.log(1-p_Pt) + (p_Pt)*np.log(p_Pt))
    return prior_ent + pos_ent + neg_ent
res = calcIG(da,'food')
t = 'food'
if da.prior == 0: da.set_prior()

tot_pos = int(da.prior * len(da.m_reviews))
tot_pos
p_P = da.prior #prob of Positive(P)
p_t = float(da.tf[t]) / sum(da.tf.values())
p_Pt = float(da.mgnls['df'][1][t]) / tot_pos
prior_ent = -(p_P * np.log(p_P) + (1-p_P)*np.log(1-p_P))
# pos: p(t) * [p(y=0|t)log(y=0|t) + p(y=1|t)+log(p(y=1|t))]
pos_ent = p_t * (p_Pt * np.log(p_Pt) + (1-p_Pt)*np.log(1-p_Pt))
# neg: p(!t) * [p(y=0|!t)log(y=0|!t) + p(y=1|!t)+log(p(y=1|!t))]
neg_ent = (1-p_t) * ((1-p_Pt) * np.log(1-p_Pt) + (p_Pt)*np.log(p_Pt))
prior_ent + pos_ent + neg_ent
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer()
da.loadDir('yelp/train', sublist=l2, debug=True)
da.calcIG('food')
da.calcIG('good')
da.calcIG('bad')
da.calcIG('gross')
da.calcIG('excellent')
da.calcIG('delicious')
da.calcIG('very')
len(da.mgnls['df])
len(da.mgnls['df'])
len(da.mgnls['df'][0])
da.mgnls['df'][0].keys()
da.calcIG('discourag')
set(da.mgnls['df'][0].keys()).intersection(set(da.mgnls['df'][1].keys()))
da.calcIG('weird')
da.calcIG('wish')
da.calcIG('week')
da.calcIGs()
np.log(1)
np.log(100)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer(N=1)
da.loadDir('yelp/train', sublist=l2)
da.calcIGs()
sorted(da.metrics['ig'].items(), key=lambda x: x[1], reverse=True)
sorted(da.ig.items(), key=lambda x: x[1], reverse=True)
sorted(da.metric['ig'].items(), key=lambda x: x[1], reverse=True)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer(N=1)
da.loadDir('yelp/train', sublist=l2)
da.calcIGs()
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer(N=1)
da.loadDir('yelp/train', sublist=l2)
da.calcIGs()
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer(N=1)
da.loadDir('yelp/train', sublist=l2)
da.tf.keys()[:100]
da.calcIGs()
da.tf['migrat']
da.mgnls['tf'][0]['migrat']
da.prior
def calcIG(da, t):
    if da.prior == 0: da.set_prior()
    p_P = da.prior #prob of Positive(P)
    tot_pos = int(p_P * len(da.m_reviews))
    p_t = float(da.tf[t]) / sum(da.tf.values())
    p_Pt = float(da.mgnls['df'][1].get(t,0)) / tot_pos
    if p_Pt == 0: prior_ent = 0
    else:
        # prior: -1 * [p(y=0)log(y=0) + p(y=1)log(p(y=1))]
        prior_ent = -(p_P * np.log(p_P) + (1-p_P)*np.log(1-p_P))
    # pos: p(t) * [p(y=0|t)log(y=0|t) + p(y=1|t)+log(p(y=1|t))]
    pos_ent = p_t * (p_Pt * np.log(p_Pt) + (1-p_Pt)*np.log(1-p_Pt))
    # neg: p(!t) * [p(y=0|!t)log(y=0|!t) + p(y=1|!t)+log(p(y=1|!t))]
    neg_ent = (1-p_t) * ((1-p_Pt) * np.log(1-p_Pt) + (p_Pt)*np.log(p_Pt))
    return prior_ent + pos_ent + neg_ent
calacIG(da,'migrat']
calacIG(da,'migrat')
calcIG(da,'migrat')
t = 'migrat'
if da.prior == 0: da.set_prior()

p_P = da.prior #prob of Positive(P)
tot_pos = int(p_P * len(da.m_reviews))
p_t = float(da.tf[t]) / sum(da.tf.values())
p_Pt = float(da.mgnls['df'][1].get(t,0)) / tot_pos
p_p
p_P
tot_pos
p_t
da.tf[t]
sum(da.tf.values())
p_Pt
def calcIG(da, t):
    if da.prior == 0: da.set_prior()
    p_P = da.prior #prob of Positive(P)
    tot_pos = int(p_P * len(da.m_reviews))
    p_t = float(da.tf[t]) / sum(da.tf.values())
    p_Pt = float(da.mgnls['df'][1].get(t,0)) / da.tf[t]
    if p_Pt == 0: prior_ent = 0
    else:
        # prior: -1 * [p(y=0)log(y=0) + p(y=1)log(p(y=1))]
        prior_ent = -(p_P * np.log(p_P) + (1-p_P)*np.log(1-p_P))
    # pos: p(t) * [p(y=0|t)log(y=0|t) + p(y=1|t)+log(p(y=1|t))]
    pos_ent = p_t * (p_Pt * np.log(p_Pt) + (1-p_Pt)*np.log(1-p_Pt))
    # neg: p(!t) * [p(y=0|!t)log(y=0|!t) + p(y=1|!t)+log(p(y=1|!t))]
    neg_ent = (1-p_t) * ((1-p_Pt) * np.log(1-p_Pt) + (p_Pt)*np.log(p_Pt))
    return prior_ent + pos_ent + neg_ent
calcIG(da,t)
calcIG(da,'good')
calcIG(da,'bad')
def calcIG(da, t):
    if da.prior == 0: da.set_prior()
    p_P = da.prior #prob of Positive(P)
    tot_pos = int(p_P * len(da.m_reviews))
    p_t = float(da.tf[t]) / sum(da.tf.values())
    p_Pt = float(da.mgnls['df'][1].get(t,0)) / da.df[t]
    if p_Pt == 0: prior_ent = 0
    else:
        # prior: -1 * [p(y=0)log(y=0) + p(y=1)log(p(y=1))]
        prior_ent = -(p_P * np.log(p_P) + (1-p_P)*np.log(1-p_P))
    # pos: p(t) * [p(y=0|t)log(y=0|t) + p(y=1|t)+log(p(y=1|t))]
    pos_ent = p_t * (p_Pt * np.log(p_Pt) + (1-p_Pt)*np.log(1-p_Pt))
    # neg: p(!t) * [p(y=0|!t)log(y=0|!t) + p(y=1|!t)+log(p(y=1|!t))]
    neg_ent = (1-p_t) * ((1-p_Pt) * np.log(1-p_Pt) + (p_Pt)*np.log(p_Pt))
    return prior_ent + pos_ent + neg_ent
calcIG(da,'bad')
calcIG(da,'good')
calcIG(da,'delicious')
def calcIG(da, t):
    if da.prior == 0: da.set_prior()
    p_P = da.prior #prob of Positive(P)
    tot_pos = int(p_P * len(da.m_reviews))
    p_t = float(da.tf[t]) / sum(da.tf.values())
    try:
        p_Pt = float(da.mgnls['df'][1].get(t,0)) / da.df.get(t,0)
    except:  p_Pt = 0
    if p_Pt == 0: prior_ent = 0
    else:
        # prior: -1 * [p(y=0)log(y=0) + p(y=1)log(p(y=1))]
        prior_ent = -(p_P * np.log(p_P) + (1-p_P)*np.log(1-p_P))
    # pos: p(t) * [p(y=0|t)log(y=0|t) + p(y=1|t)+log(p(y=1|t))]
    pos_ent = p_t * (p_Pt * np.log(p_Pt) + (1-p_Pt)*np.log(1-p_Pt))
    # neg: p(!t) * [p(y=0|!t)log(y=0|!t) + p(y=1|!t)+log(p(y=1|!t))]
    neg_ent = (1-p_t) * ((1-p_Pt) * np.log(1-p_Pt) + (p_Pt)*np.log(p_Pt))
    return prior_ent + pos_ent + neg_ent
calcIG(da,'awesome')
calcIG(da,'amazing')
calcIG(da,'great')
calcIG(da,'perfect')
da.calcIGs()
da.tf['gooooooddd']
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer(N=1)
da.loadDir('/yelp/train',sublist=l2)
da.loadDir('/yelp/train/',sublist=l2)
os.listdir('/yelp/train')
os.listdir('yelp/train')
da.loadDir('yelp/train/',sublist=l2)
da.filter_vocab(10)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da.loadDir('yelp/train/',sublist=l2)
da = DocAnalyzer(N=1)
da.loadDir('yelp/train/',sublist=l2, debug=True)
da.filter_vocab
da.filter_vocab(10)
def filter_vocab(da, k):
    #remove old stopwords
    da.removeStopwords()
    tdf = sorted(da.df.items(), key= lambda x:x[1], reverse=True)
    stat_df = pd.DataFrame(tdf, columns=['gram', 'DF'])
    tot_reviews = len(da.m_reviews)
    
    #filter out top 100 grams
    stat_df = stat_df.ix[100:,:]
    #filter out grams w DF less than k
    stat_df = stat_df[stat_df['DF'] >= k]
    #get information gain and chi square
    stat_df['IDF'] = 1 + np.log(float(tot_reviews)/stat_df['DF'])
    stat_df['IG'] = [da.metric['ig'].get(t,0) for t in stat_df['gram'].tolist()]
    for typ in ['tf','df']:
        for (lbl, name) in [(0,'neg'),(1,'pos')]:
            stat_df['_'.join([name,typ])] = [da.mgnls[typ][lbl].get(t,0) for t in stat_df['gram'].tolist()]
    
    stat_df['posTF'] = [da.mgnls['tf'][1].get(t,0) for t in stat_df['gram'].tolist()]
    #stat_df['chi_sq'] = [da.metric['chisq'][t] for t in stat_df['gram'].tolist()]
    
    da.stats = stat_df
    grams = set(stat_df['gram'].tolist())
    #create template for review vector 
    da.empty_vec = {g:0 for g in grams}
    return da
da = filter_vocab(da,10)
da.stats
def filter_vocab(da, k):
    #remove old stopwords
    da.removeStopwords()
    tdf = sorted(da.df.items(), key= lambda x:x[1], reverse=True)
    stat_df = pd.DataFrame(tdf, columns=['gram', 'DF'])
    tot_reviews = len(da.m_reviews)
    
    #filter out top 100 grams
    #stat_df = stat_df.ix[100:,:]
    #filter out grams w DF less than k
    stat_df = stat_df[stat_df['DF'] >= k]
    #get information gain and chi square
    stat_df['IDF'] = 1 + np.log(float(tot_reviews)/stat_df['DF'])
    stat_df['IG'] = [da.metric['ig'].get(t,0) for t in stat_df['gram'].tolist()]
    for typ in ['tf','df']:
        for (lbl, name) in [(0,'neg'),(1,'pos')]:
            stat_df['_'.join([name,typ])] = [da.mgnls[typ][lbl].get(t,0) for t in stat_df['gram'].tolist()]
    
    stat_df['posTF'] = [da.mgnls['tf'][1].get(t,0) for t in stat_df['gram'].tolist()]
    #stat_df['chi_sq'] = [da.metric['chisq'][t] for t in stat_df['gram'].tolist()]
    
    da.stats = stat_df
    grams = set(stat_df['gram'].tolist())
    #create template for review vector 
    da.empty_vec = {g:0 for g in grams}
    return da
da = DocAnalyzer(N=1)
da.loadDir('yelp/train/',sublist=l2, debug=True)
da.filter_vocab(10)
da = filter_vocab(da,10)
da.stats['ig']
da.stats['IG']
da.setIGs()
da.calcIGs()
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer(N=1)
da.loadDir('yelp/train', sublist=l3, debug=True)
da.loadDir('yelp/train', sublist=l2, debug=True)
da.filter_vocab(10)
da.calcIGs()
da.calcIG('goif')
da.calcIG('rule')
da.tf['rule']
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer(N=1)
da.loadDir('yelp/train', sublist=l2,debug=True)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer(N=1)
da.loadDir('yelp/train', sublist=l2,debug=True)
da.filter_vocab()
da.filter_vocab(10)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer(N=1)
da.loadDir('yelp/train', sublist=l2,debug=True)
da.filter_vocab()
da.filter_vocab(10)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer(N=1)
da.loadDir('yelp/train', sublist=l2,debug=True)
da.filter_vocab(10)
da.stats
da.calcIGs()
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer(N=1)
da.loadDir('yelp/train', sublist=l2,debug=True)
da.filter_vocab(10)
da.calcIGs()
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer(N=1)
da.loadDir('yelp/train', sublist=l2,debug=True)
da.filter_vocab(10)
da.calcIGs()
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer(N=1)
da.loadDir('yelp/train', sublist=l2,debug=True)
da.filter_vocab(10)
da.calcIGs()
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer(N=1)
da.loadDir('yelp/train', sublist=l2,debug=True)
da.filter_vocab(10)
da.calcIGs()
da.stats
da.stats['IG'].range()
da.stats['IG'].plot()
da.metric.keys()
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer(N=1)
da.loadDir('yelp/train', sublist=l2, debug=True)
da.calcChiSq('food')
def calcChiSq(da, t):
    A = da.mgnls['df'][1].get(t,0)
    B = len(da.mgnls['df'][1]) - A
    C = da.mgnls['df'][0].get(t,0)
    D = len(da.mgnls['df'][0]) - C
    num = (A + B + C + D) (A*D-B*C)**2
    denom = (A+C)*(B+D)*(A+B)*(C+D)
    return float(num) / float(denom)
t = 'food'
A = da.mgnls['df'][1].get(t,0)
B = len(da.mgnls['df'][1]) - A
C = da.mgnls['df'][0].get(t,0)
D = len(da.mgnls['df'][0]) - C
A,B,C,D
(A + B + C + D)
(A*D-B*C)**2
num = (A + B + C + D) (A*D-B*C)**2
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer(N=1)
da.loadDir('yelp/train', sublist=l2, debug=True)
da.calcChiSq('food')
da.calcChiSq('good')
da.calcChiSq('bad')
da.calcChiSqs()
da.filter_vocab(k=10)
da.calcChiSqs()
max(da.stats['chisq'])
max(da.stats['chi_sq'])
da.stats.columns
max(da.stats['chiSq'])
max(da.stats['ChiSq'])
len(da.mgnls['df'][0]
)
len(da.tf)
A,B,C,D
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/monitoringScripts/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/monitoringScripts')
pull_data('bea3ch','Br#nD0$@')
os.getcwd()
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/monitoringScripts/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/monitoringScripts')
pull_data('bea3ch','Br#nD0$@')
stats, cl, dev = build_dfs()
stats, cl, dev = build_dfs('tmp_2018_4_18')
stats, cl, dev = build_dfs(dire='tmp_2018_4_18')
stats, cl, dev = build_dfs(dire='tmp_2018-4-18')
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/monitoringScripts/log_parser.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/monitoringScripts')
stats, cl, dev = build_dfs(dire='tmp_2018-4-18')
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/monitoringScripts/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/monitoringScripts')
stats, cl, dev = build_dfs('tmp_2018-4-18')
dire = 'tmp_2018-4-18'
device = 'em2'
df_dev = pd.read_csv(dire+'/trafficStats_'+device+'.txt', index_col=False)
df = df_dev
df['ts']
df['ts'].describe()
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/monitoringScripts/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/monitoringScripts')
stats, cl = build_dfs('tmp_2018_4_18')
stats, cl = build_dfs('tmp_2018-4-18')
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/monitoringScripts/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/monitoringScripts')
stats, cl = build_dfs('tmp_2018-4-18')
cl.describe()
stats.describe(include=['mean'])
stats.describe()
stats.columns
stats.columns['pkts_dropped'].describe()
stats.columns['pkts_dropped']
stats['pkts_dropped'].describe()
1375039350. / (1375039350 + 576895622112)
os.getcwd()
f = open('tmp_2018-4-18/trafficStats_em2.txt', 'r')
ftext = f.readlines()
fsplits = [f.strip().split(',') for f in fsplits]
fsplits = [f.strip().split(',') for f in ftext]
fsplits[:5]
lens= [len(r) for r in fsplits]
lens
np.var(lens)
np.mean(lens)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW1/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW1')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW1/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW1')
da = DocAnalyzer()
os.getcwd()
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer()
os.listdir('.')
lists = open('train_test_sublists.txt', 'r').readlines()
lists
lists = open('train_test_sublists.txt', 'r').read()
import re
lists
re.findall('.*?\= \[.*\]\n',lists)
re.findall('.*? \= \[.*\]\n',lists)
re.findall('\[.*\]\n',lists)
re.findall('\[.*?',lists)
re.findall("\['.*?'",lists)
re.findall("\['.*'",lists)
re.findall("\['.*",lists)
res = re.findall("\['.*",lists)
len(res)
res = re.findall("\['.*'\n",lists)
res
res = re.findall("\['.*'",lists)
res
lists
lists = re.sub('\\n', '', lists)
lists
train_test = re.split('\] ', lists)
train_test
l1 = ['0qnMSq3gYhGDesZKxNgAkQ.json', '4lgk5AJvmoXPrfSlCyjiQg.json', '9IRdWhDNo2T6vyMLwrQdMw.json', 'A9xPHLcWtRgK6Mf4-ksBrw.json', 'AZrLjmV0A2TzOCkZ6CU-Fg.json']
l2 = ['CvmAN25laBbwZTqmlEAR1Q.json', 'd5YWKrP-zG74nqOYzHn7Zg.json', 'dCw8uBtwnJFKwMnASlZLzg.json', 'dlDEuDIvZI6I0cGZy4jIYg.json', 'e1grgYnCxbue-tU5Gf6IlQ.json']
test1 = [ '3OLZOlqgOXdqY0uwxcOTfw.json', '3VCZ21-DIw7voVexDMXDSA.json', 'CvmAN25laBbwZTqmlEAR1Q.json']
test2 = ['gQCn4Gv-4_UUUFwpo-zHvA.json', 'rzHGofdCbaskvo2SzC6Vpg.json', 'sWXT0sNodEnxZjziB3saZQ.json']
da.loadDir('yelp/train', sublist=l2)
da.calcChiSq('tasty')
da.calcChiSq('good')
da.calcChiSq('bad')
da.calcChiSq('excellent')
def calcChiSq(da, t):
   A = da.mgnls['df'][1].get(t,0) # # of pos docs with t
   B = len(da.mgnls['df'][1]) - A # # of pos docs without t
   C = da.mgnls['df'][0].get(t,0) # # of neg docs with t
   D = len(da.mgnls['df'][0]) - C# # of neg docs without t
   num = (A + B + C + D)+(A*D-B*C)**2
   denom = (A+C)*(B+D)*(A+B)*(C+D)
   return float(num) / float(denom)
A = da.mgnls['df'][1].get(t,0) # # of pos docs with t
B = len(da.mgnls['df'][1]) - A # # of pos docs without t
C = da.mgnls['df'][0].get(t,0) # # of neg docs with t
D = len(da.mgnls['df'][0]) - C# # of neg docs without t
t = 'great'
A = da.mgnls['df'][1].get(t,0) # # of pos docs with t
B = len(da.mgnls['df'][1]) - A # # of pos docs without t
C = da.mgnls['df'][0].get(t,0) # # of neg docs with t
D = len(da.mgnls['df'][0]) - C# # of neg docs without
A,B,C,D
len(da.m_reviews)
da.mgnls['df'][1]['great']
num_pos = int(da.prior*len(da.m_reviews))
num_neg = len(da.m_reviews) - num_pos
A = da.mgnls['df'][1].get(t,0) # # of pos docs with t
B = num_pos - A # # of pos docs without t
C = da.mgnls['df'][0].get(t,0) # # of neg docs with t
D = num_neg - C# # of neg docs without t
A,B,C,D
num_pos
da.prior
da.set_prior()
num_pos = int(da.prior*len(da.m_reviews))
num_neg = len(da.m_reviews) - num_pos
A = da.mgnls['df'][1].get(t,0) # # of pos docs with t
B = num_pos - A # # of pos docs without t
C = da.mgnls['df'][0].get(t,0) # # of neg docs with t
D = num_neg - C# # of neg docs without t

num_pos
num_neg
A,B,C,D
num = (A + B + C + D)+(A*D-B*C)**2
denom = (A+C)*(B+D)*(A+B)*(C+D)
float(num) / float(denom)
print(da.m_reviews[0])
print(da.m_reviews[1])
print(da.m_reviews[2])
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer()
da.loadDir('yelp/train', sublist=l1[0], debug=True)
da.loadDir('yelp/train', sublist=[l1[0]], debug=True)
len(da.m_reviews)
da.tf
da = DocAnalyzer(N=1)
da.loadDir('yelp/train', sublist=[l1[0]], debug=True)
da.tf
da2 = DocAnalyzer(N=1)
da2.loadDir('yelp/train', sublist=l1[:3])
counter = 0
for i, rev in enumerate(da2.m_reviews):
    if rev.sent == 0:
        if counter < 5:
            print(i)
            counter +=1
            
da.m_reviews[1].sent
da.mgnls['df'][0]
da.analyzeDoc(da2.m_reviews[16].getJSON())
da.m_reviews[1].content
da.m_reviews[1].content.getJSON()
da.m_reviews[1].getJSON()
l1[0]
da_test = DocAnalyzer(N=1)
da.m_reviews[1].content
neg1 = """"In short: this place was just alright. \xa0It definitely does not warrant itself a 4 or 5. \xa0I tried the wood-fired oyster roast, fried alligator, smoked pork ribs, the cochon (main entree), pork cheeks, gumbo, and fried livers.Oyster: \xa0Really good flavorFried alligator: it is fried food with their red sauce that is pretty tasty and better with the mint. \xa0Smoked pork ribs: I don't like smoked stuff but this one actually grew on me. \xa0I actually enjoyed it. It doesn't have a bitter after taste and the smoked flavor and smell is not strong at all. \xa0It's the right balance. \xa0Surprisingly, it was my favorite out of everything.Cochon ($28) - it's like eating pork with a crapload of salt. \xa0Seriously, I don't know if it's only that evening, but the chef was heavy handed on the salt. :/ \xa0Sheesh. \xa0It was NOT worth the $28 even if you are a pork lover...and I AM a pork eater. \xa0You aint' missing much. Save your money for the smaller plates. \xa0Pork cheeks - let's just say this...I remember it being sweet and unimpressive. Enough said. \xa0Gumbo - it was alright. Had better 'nuff said.Fried livers - TOO MUCH batter. I mean it was like eating batter with a hint of liver. LOL...yeah no.So folks, let's just say this. Their main entrees like like around $20 and up. \xa0We sat next to a group of adults and we looked over and they did NOT even finish their food. \xa0I mean, I don't care if people get full or they don't want to gain weight or whatever, but if you have really good food in front of you and you love food, you WILL finish 99% of your food. \xa0Yeah...one guy ate only half. I think he brought it to go, but I can't be too sure. We left before they did. \xa0So for all the 5 ratings...yikes. \xa0I'm surprised this place got 4 stars. \xa0I should've tried their deli side instead. \xa0Darn!"""
neg2 = da2.m_reviews[16].content
neg2
pos1 = da.m_reviews[0].content
pos1
pos2 = da.m_reviews[2].content
pos2
docs = [pos1,pos2,neg1,neg2]
for i,d in enumerate(docs):
    docs[i] = re.sub('\\xa0','',d)
    
docs[0]
docs[1]
docs[2]
da.tokenize(docs[2])
tokens = [da.tokenize(rs) for rs in docs]
for i,toklist in enumerate(tokens):
    for j, token in toklist:
        toklist[i][j] = da.normalize(token)
        
for i,toklist in enumerate(tokens):
    for j, token in toklist:
        tokens[i][j] = da.normalize(token)
        
for i,toklist in enumerate(tokens):
    for j, token in enumerate(toklist):
        tokens[i][j] = da.normalize(token)
        
tokens[0]
mgnls = {'tf':[{},{}], 'df':[{},{}]}
for d in docs[:2]:
    print d
    
for toklist in tokens[:2]:
    seen_toksn = set()
    for t in toklist:
        if t not in seen_tokens:
            mgnls['df'][1][t] = mgnls['df'][1].get(t,0) + 1
            seen_tokens.add(t)
        mgnls['tf'][1][t] = mgnls['tf'][1].get(t,0) + 1      
        
for toklist in tokens[:2]:
    seen_tokens = set()
    for t in toklist:
        if t not in seen_tokens:
            mgnls['df'][1][t] = mgnls['df'][1].get(t,0) + 1
            seen_tokens.add(t)
        mgnls['tf'][1][t] = mgnls['tf'][1].get(t,0) + 1
        
mgnls['df'][1]
for toklist in tokens[2:]:
    seen_tokens = set()
    for t in toklist:
        if t not in seen_tokens:
            mgnls['df'][0][t] = mgnls['df'][1].get(t,0) + 1
            seen_tokens.add(t)
        mgnls['tf'][0][t] = mgnls['tf'][1].get(t,0) + 1
        
len(mgnls['tf'][0])
len(mgnls['tf'][1])
section = set(mgnls['tf'][0].keys()).intersection(set(mgnls['tf'][1].keys()))
len(section)
list(section)[:5]
list(section)[:10]
da_test.mgnls = mgnls
def calcChiSq(da_t, t):
    num_pos = int(da_t.prior*len(da_t.m_reviews))
    num_neg = len(da_t.m_reviews) - num_pos
    A = da_t.mgnls['df'][1].get(t,0) # # of pos docs with t
    B = num_pos - A # # of pos docs without t
    C = da_t.mgnls['df'][0].get(t,0) # # of neg docs with t
    D = num_neg - C# # of neg docs without t
    num = (A + B + C + D)+(A*D-B*C)**2
    denom = (A+C)*(B+D)*(A+B)*(C+D)
    return float(num) / float(denom)
res = calcChiSq(da_test, 'order')
da_t = da_test
num_pos = int(da_t.prior*len(da_t.m_reviews))
num_neg = len(da_t.m_reviews) - num_pos
num_pos, num_neg
da_t.set_prior()
da.m_reviews = docs
da_t.set_prior()
da_t.prior = .5
num_pos = int(da_t.prior*len(da_t.m_reviews))
num_neg = len(da_t.m_reviews) - num_pos

num_pos
da_t.prior
len(da_t.m_reviews)
da_t.m_reviews = docs
len(da_t.m_reviews)
num_pos = int(da_t.prior*len(da_t.m_reviews))
num_neg = len(da_t.m_reviews) - num_pos

num_pos, num_neg
A = da_t.mgnls['df'][1].get(t,0) # # of pos docs with t
B = num_pos - A # # of pos docs without t
C = da_t.mgnls['df'][0].get(t,0) # # of neg docs with t
D = num_neg - C# # of neg docs without t
A,B,C,D
da_t.mgnls['df'][0].get('order', 0)
t
t = 'order'
A = da_t.mgnls['df'][1].get(t,0) # # of pos docs with t
B = num_pos - A # # of pos docs without t
C = da_t.mgnls['df'][0].get(t,0) # # of neg docs with t
D = num_neg - C# # of neg docs without t
A,B,C,D
mgnls = {'tf':[{},{}], 'df':[{},{}]}
for toklist in tokens[:2]:
    seen_tokens = set()
    for t in toklist:
        if t not in seen_tokens:
            mgnls['df'][1][t] = mgnls['df'][1].get(t,0) + 1
            seen_tokens.add(t)
        mgnls['tf'][1][t] = mgnls['tf'][1].get(t,0) + 1
for toklist in tokens[2:]:
    seen_tokens = set()
    for t in toklist:
        if t not in seen_tokens:
            mgnls['df'][0][t] = mgnls['df'][0].get(t,0) + 1
            seen_tokens.add(t)
        mgnls['tf'][0][t] = mgnls['tf'][0].get(t,0) + 1
da_t.mgnls = mgnls
A = da_t.mgnls['df'][1].get(t,0) # # of pos docs with t
B = num_pos - A # # of pos docs without t
C = da_t.mgnls['df'][0].get(t,0) # # of neg docs with t
D = num_neg - C# # of neg docs without t
A,B,C,D
t
t = 'order'
A = da_t.mgnls['df'][1].get(t,0) # # of pos docs with t
B = num_pos - A # # of pos docs without t
C = da_t.mgnls['df'][0].get(t,0) # # of neg docs with t
D = num_neg - C# # of neg docs without
A,B,C,D
A+B+C+D
(A*D-B*C)**2
num = (A + B + C + D)+(A*D-B*C)**2
num
denom = (A+C)*(B+D)*(A+B)*(C+D)
denom
float(num) / float(denom)
set(selection)
select
len(section)
type(section)
set(da_t.mgnls['df'][1].keys()).difference(section)
only_pos = set(da_t.mgnls['df'][1].keys()).difference(section)
tups = [(k,da_t.mgnls['df'][0][k]) for k in only_pos]
tups = [(k,da_t.mgnls['df'][1][k]) for k in only_pos]
tups
sorted(tups, key=lambda x:x[1], reverse=True)[:5]
t = 'wonderful'
num_pos = int(da_t.prior*len(da_t.m_reviews))
num_neg = len(da_t.m_reviews) - num_pos
A = da_t.mgnls['df'][1].get(t,0) # # of pos docs with t
B = num_pos - A # # of pos docs without t
C = da_t.mgnls['df'][0].get(t,0) # # of neg docs with t
D = num_neg - C# # of neg docs without t
num = (A + B + C + D)+(A*D-B*C)**2
denom = (A+C)*(B+D)*(A+B)*(C+D)
num
denom
A = 15
num = (A + B + C + D)+(A*D-B*C)**2
denom = (A+C)*(B+D)*(A+B)*(C+D)
num,denom
da.calcIG(t)
def calcIG(da, t):
    if da.prior == 0: da.set_prior()
    p_P = da.prior #prob of Positive(P)
    p_t = float(da.tf[t]) / sum(da.tf.values())
    try:
        p_Pt = float(da.mgnls['df'][1].get(t,0)) / da.df.get(t,0)
    except:  p_Pt = 0
    if p_Pt == 0: prior_ent = 0
    else:
        # prior: -1 * [p(y=0)log(y=0) + p(y=1)log(p(y=1))]
        prior_ent = -(p_P * np.log(p_P) + (1-p_P)*np.log(1-p_P))
    # pos: p(t) * [p(y=0|t)log(y=0|t) + p(y=1|t)+log(p(y=1|t))]
    pos_ent = p_t * (p_Pt * np.log(p_Pt) + (1-p_Pt)*np.log(1-p_Pt))
    # neg: p(!t) * [p(y=0|!t)log(y=0|!t) + p(y=1|!t)+log(p(y=1|!t))]
    neg_ent = (1-p_t) * ((1-p_Pt) * np.log(1-p_Pt) + (p_Pt)*np.log(p_Pt))
    return prior_ent + pos_ent + neg_ent
calcIG(da_t, t)
da_t.prior
def calcIG(da_t, t):
    if da_t.prior == 0: da_t.set_prior()
    p_P = da_t.prior #prob of Positive(P)
    p_t = float(da_t.tf[t]) / sum(da_t.tf.values())
    try:
        p_Pt = float(da_t.mgnls['df'][1].get(t,0)) / da_t.df.get(t,0)
    except:  p_Pt = 0
    if p_Pt == 0: prior_ent = 0
    else:
        # prior: -1 * [p(y=0)log(y=0) + p(y=1)log(p(y=1))]
        prior_ent = -(p_P * np.log(p_P) + (1-p_P)*np.log(1-p_P))
    # pos: p(t) * [p(y=0|t)log(y=0|t) + p(y=1|t)+log(p(y=1|t))]
    pos_ent = p_t * (p_Pt * np.log(p_Pt) + (1-p_Pt)*np.log(1-p_Pt))
    # neg: p(!t) * [p(y=0|!t)log(y=0|!t) + p(y=1|!t)+log(p(y=1|!t))]
    neg_ent = (1-p_t) * ((1-p_Pt) * np.log(1-p_Pt) + (p_Pt)*np.log(p_Pt))
    return prior_ent + pos_ent + neg_ent
calcIG(da_t, t)
p_P = da_t.prior #prob of Positive(P)
p_t = float(da_t.tf[t]) / sum(da_t.tf.values())
for toklist in tokens:
    seen_tokens = set()
    for t in toklist:
        if t not in seen_tokens:
            da_t.df[t] = da_t.df.get(t,0) + 1
            seen_tokens.add(t)
        da_t.tf[t] = da_tf.get(t,0) + 1
for toklist in tokens:
    seen_tokens = set()
    for t in toklist:
        if t not in seen_tokens:
            da_t.df[t] = da_t.df.get(t,0) + 1
            seen_tokens.add(t)
        da_t.tf[t] = da_t.tf.get(t,0) + 1
p_P = da_t.prior #prob of Positive(P)
p_t = float(da_t.tf[t]) / sum(da_t.tf.values())
p_t
da_t.tf[t]
t
t = 'wonderful'
p_P = da_t.prior #prob of Positive(P)
p_t = float(da_t.tf[t]) / sum(da_t.tf.values())

p_t
p_Pt = float(da_t.mgnls['df'][1].get(t,0)) / da_t.df.get(t,0)
prior_ent = -(p_P * np.log(p_P) + (1-p_P)*np.log(1-p_P))
pos_ent = p_t * (p_Pt * np.log(p_Pt) + (1-p_Pt)*np.log(1-p_Pt))
neg_ent = (1-p_t) * ((1-p_Pt) * np.log(1-p_Pt) + (p_Pt)*np.log(p_Pt))
prior_ent + pos_ent + neg_ent
prior_ent
pos_ent
neg_ent
p_Pt
def Log(x):
    retval = 0 if x == 0 else np.log(x)
    return retval
Log(0)
Log(4)
    prior_ent = -(p_P * np.log(p_P) + (1-p_P)*np.log(1-p_P))
# pos: p(t) * [p(y=0|t)log(y=0|t) + p(y=1|t)+log(p(y=1|t))]
pos_ent = p_t * ((1-p_Pt)*Log(1-p_Pt) + p_Pt * Log(p_Pt))
# neg: p(!t) * [p(y=0|!t)log(y=0|!t) + p(y=1|!t)+log(p(y=1|!t))]
neg_ent = (1-p_t) * ((1-p_Pt) * Log(1-p_Pt) + (p_Pt)*Log(p_Pt))
pos_ent
neg_ent
p_Pt
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/entropy.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
playTennis = [9, 5] # Yes, No

# attribute, number of members (feature)
outlook = [
    [4, 0],  # overcase
    [2, 3],  # sunny
    [3, 2]   # rain
]
temperature = [
    [2, 2],  # hot
    [3, 1],  # cool
    [4, 2]   # mild
]
humidity = [
    [3, 4],  # high
    [6, 1]   # normal
]
wind = [
    [6, 2],  # weak
    [3, 3]   # strong
]
num_pos = da_t.prior * len(da_t.m_reviews)
num_pos
num_pos = int(num_pos)
num_neg = len(da_t.m_reviews) - num_pos
num_neg
tot = [2,2]
A,B,C,D
t
da_t.mgnls['df'][0][t]
da_t.mgnls['df'][1][t]
gain(tot, [2,0])
print(gain(playTennis, outlook))
print(gain(playTennis, temperature))
print(gain(playTennis, humidity))
print(gain(playTennis, wind))
gain(tot, [[2,0]])
da_t.mgnls['tf'][0]['order']
da_t.mgnls['tf'][1]['order']
da_t.tf['order']

## ---(Wed Apr 18 22:11:54 2018)---
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da_t = DocAnalyzer(N=1)
os.listdir('.')
lists = open('train_test_sublists.txt','r').read()
lists
lists = re.sub('\\n','',lists)
lists
l1 = ['0qnMSq3gYhGDesZKxNgAkQ.json', '4lgk5AJvmoXPrfSlCyjiQg.json', '9IRdWhDNo2T6vyMLwrQdMw.json', 'A9xPHLcWtRgK6Mf4-ksBrw.json', 'AZrLjmV0A2TzOCkZ6CU-Fg.json']
l2 = ['CvmAN25laBbwZTqmlEAR1Q.json', 'd5YWKrP-zG74nqOYzHn7Zg.json', 'dCw8uBtwnJFKwMnASlZLzg.json', 'dlDEuDIvZI6I0cGZy4jIYg.json', 'e1grgYnCxbue-tU5Gf6IlQ.json']
test1 = [ '3OLZOlqgOXdqY0uwxcOTfw.json', '3VCZ21-DIw7voVexDMXDSA.json', 'CvmAN25laBbwZTqmlEAR1Q.json']
test2 = ['gQCn4Gv-4_UUUFwpo-zHvA.json', 'rzHGofdCbaskvo2SzC6Vpg.json', 'sWXT0sNodEnxZjziB3saZQ.json']
da_t.loadDir('yelp/train', sublist = [l1[0]], debug=True)
da_t.mgnls['df'].items()[:5]
da_t.mgnls['df'][0].items()
da_t.loadDir('yelp/train', debug=True)
da_t.vocab
da_t.tf.keys()[:5]
da_t.tf.keys()[:10]
da_t.mgnls['df'][0]['hate']
da_t.mgnls['df'][1]['hate']
sorted(da_t.tf.items(), key=lambda x:x[1], reverse=True)[:10]
sorted(da_t.tf.items(), key=lambda x:x[1], reverse=True)[:50]
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
calcIG(da_t, 'order')
da_t.set_prior()
calcIG(da_t, 'order')
t = 'order'
da_t.mgnls['df'][0]['order']
da_t.mgnls['df'][1]['order']
da_t.df['order']
p_P = da_t.prior #prob of Positive(P)
#number of postiive and neg ddocs
num_pos = int(p_P) * len(da_t.m_reviews)
num_neg = len(da_t.m_reviews) - num_pos
p_t = float(da_t.tf[t]) / sum(da_t.tf.values())
num_pos, num_neg
da_t.prior
num_pos
int(p_P) * len(da_t.m_reviews)
int(p_P * len(da_t.m_reviews))
num_neg = len(da_t.m_reviews) - num_pos
num_neg
len(da_t.m_reviews)
num_neg = len(da_t.m_reviews) - num_pos
num_pos
num_pos = int(p_P * len(da_t.m_reviews))
num_neg = len(da_t.m_reviews) - num_pos
num_pos, num_neg
p_t = float(da_t.tf[t]) / sum(da_t.tf.values())
p_t
p_Pt = float(da_t.mgnls['df'][1].get(t,0)) / da_t.df.get(t,0)
p_Pt
da_t.mgnls['df'][1].get(t,0)
da_t.mgnls['df'][0].get(t,0)
p_Nt = float(da_t.mgnls['df'][0].get(t,0)) / da_t.df.get(t,0)
p_Nt
p_Pt_not = float(num_pos - da_t.mgnls['df'][1][t]) / num_pos
p_Nt_not = float(num_neg - da_t.mgnls['df'][0][t]) / num_neg
p_Pt_not
def calcIG(da_t, t):
    if da_t.prior == 0: da_t.set_prior()
    p_P = da_t.prior #prob of Positive(P)
    #number of postiive and neg ddocs
    num_pos = int(p_P * len(da_t.m_reviews))
    num_neg = len(da_t.m_reviews) - num_pos
    p_t = float(da_t.tf[t]) / sum(da_t.tf.values())
    try: p_Pt = float(da_t.mgnls['df'][1].get(t,0)) / da_t.df.get(t,0)
    except:  p_Pt = 0
    if p_Pt == 0: prior_ent = 0
     # prior: -1 * [p(y=0)log(y=0) + p(y=1)log(p(y=1))]
    else: prior_ent = -(p_P * np.log(p_P) + (1-p_P)*np.log(1-p_P))
    
    try: p_Nt = float(da_t.mgnls['df'][0].get(t,0)) / da_t.df.get(t,0)
    except:  p_Nt = 0
    
    p_Pt_not = float(num_pos - da_t.mgnls['df'][1][t]) / num_pos
    p_Nt_not = float(num_neg - da_t.mgnls['df'][0][t]) / num_neg
    
    # pos: p(t) * [p(y=0|t)log(y=0|t) + p(y=1|t)+log(p(y=1|t))]
    pos_ent = p_t * (p_Nt*Log(p_Nt) + p_Pt*Log(p_Pt))
    # neg: p(!t) * [p(y=0|!t)log(y=0|!t) + p(y=1|!t)+log(p(y=1|!t))]
    neg_ent = (1-p_t) * (p_Nt_not * Log(p_Nt_not) + (p_Pt_not)*Log(p_Pt_not))
    return prior_ent + pos_ent + neg_ent
calcIG(da_t, t)
p_P = da_t.prior #prob of Positive(P)
#number of postiive and neg ddocs
num_pos = int(p_P * len(da_t.m_reviews))
num_neg = len(da_t.m_reviews) - num_pos
p_t = float(da_t.tf[t]) / sum(da_t.tf.values())
try: p_Pt = float(da_t.mgnls['df'][1].get(t,0)) / da_t.df.get(t,0)
except:  p_Pt = 0

if p_Pt == 0: prior_ent = 0
 # prior: -1 * [p(y=0)log(y=0) + p(y=1)log(p(y=1))]
else: prior_ent = -(p_P * np.log(p_P) + (1-p_P)*np.log(1-p_P))


try: p_Nt = float(da_t.mgnls['df'][0].get(t,0)) / da_t.df.get(t,0)
except:  p_Nt = 0


p_Pt_not = float(num_pos - da_t.mgnls['df'][1][t]) / num_pos
p_Nt_not = float(num_neg - da_t.mgnls['df'][0][t]) / num_neg

# pos: p(t) * [p(y=0|t)log(y=0|t) + p(y=1|t)+log(p(y=1|t))]
pos_ent = p_t * (p_Nt*Log(p_Nt) + p_Pt*Log(p_Pt))
# neg: p(!t) * [p(y=0|!t)log(y=0|!t) + p(y=1|!t)+log(p(y=1|!t))]
neg_ent = (1-p_t) * (p_Nt_not * Log(p_Nt_not) + (p_Pt_not)*Log(p_Pt_not))
prior_ent
pos_ent
neg_ent
p_Nt*Log(p_Nt)
def calcIG(da_t, t):
    if da_t.prior == 0: da_t.set_prior()
    p_P = da_t.prior #prob of Positive(P)
    #number of postiive and neg ddocs
    num_pos = int(p_P * len(da_t.m_reviews))
    num_neg = len(da_t.m_reviews) - num_pos
    p_t = float(da_t.tf[t]) / sum(da_t.tf.values())
    try: p_Pt = float(da_t.mgnls['df'][1].get(t,0)) / da_t.df.get(t,0)
    except:  p_Pt = 0
    if p_Pt == 0: prior_ent = 0
     # prior: -1 * [p(y=0)log(y=0) + p(y=1)log(p(y=1))]
    else: prior_ent = -(p_P * np.log(p_P) + (1-p_P)*Log(1-p_P))
    
    try: p_Nt = float(da_t.mgnls['df'][0].get(t,0)) / da_t.df.get(t,0)
    except:  p_Nt = 0
    
    p_Pt_not = float(num_pos - da_t.mgnls['df'][1][t]) / num_pos
    p_Nt_not = float(num_neg - da_t.mgnls['df'][0][t]) / num_neg
    
    # pos: p(t) * [p(y=0|t)log(y=0|t) + p(y=1|t)+log(p(y=1|t))]
    pos_ent = -(p_t * (p_Nt*Log(p_Nt) + p_Pt*Log(p_Pt)))
    # neg: p(!t) * [p(y=0|!t)log(y=0|!t) + p(y=1|!t)+log(p(y=1|!t))]
    neg_ent = -(1-p_t) * (p_Nt_not * Log(p_Nt_not) + (p_Pt_not)*Log(p_Pt_not))
    return pos_ent + neg_ent - prior_ent
calcIG(da_t, t)
res = []
for t in da_t.tf.keys():
    res.append((t,calcIG(da_t,t)))
    
def calcIG(da_t, t):
    if da_t.prior == 0: da_t.set_prior()
    p_P = da_t.prior #prob of Positive(P)
    #number of postiive and neg ddocs
    num_pos = int(p_P * len(da_t.m_reviews))
    num_neg = len(da_t.m_reviews) - num_pos
    p_t = float(da_t.tf[t]) / sum(da_t.tf.values())
    try: p_Pt = float(da_t.mgnls['df'][1].get(t,0)) / da_t.df.get(t,0)
    except:  p_Pt = 0
    if p_Pt == 0: prior_ent = 0
     # prior: -1 * [p(y=0)log(y=0) + p(y=1)log(p(y=1))]
    else: prior_ent = -(p_P * np.log(p_P) + (1-p_P)*Log(1-p_P))
    
    try: p_Nt = float(da_t.mgnls['df'][0].get(t,0)) / da_t.df.get(t,0)
    except:  p_Nt = 0
    
    p_Pt_not = float(num_pos - da_t.mgnls['df'][1].get(t,0)) / num_pos
    p_Nt_not = float(num_neg - da_t.mgnls['df'][0].get(t,0)) / num_neg
    
    # pos: p(t) * [p(y=0|t)log(y=0|t) + p(y=1|t)+log(p(y=1|t))]
    pos_ent = -(p_t * (p_Nt*Log(p_Nt) + p_Pt*Log(p_Pt)))
    # neg: p(!t) * [p(y=0|!t)log(y=0|!t) + p(y=1|!t)+log(p(y=1|!t))]
    neg_ent = -(1-p_t) * (p_Nt_not * Log(p_Nt_not) + (p_Pt_not)*Log(p_Pt_not))
    return pos_ent + neg_ent - prior_ent
for t in da_t.tf.keys():
    res.append((t,calcIG(da_t,t)))
    
res
da_t.prior*len(da_t.m_reviews)
priors = [62, len(da_t.m_reviews)-62]
priors
da_t.mgnls['df'][0]['quality']
def get_counts(da, t):
    num_pos = int(da.prior * len(da.m_reviews))
    num_neg = len(da.m_reviews) - num_pos
    t_pos = da.mgnls['df'][1].get(t,0)
    t_neg = da.mgnls['df'][0].get(t,0)
    return [num_pos, num_neg], [t_pos, t_neg]
get_counts(da_t, 'order')
priors, counts = get_counts(da_t, 'order')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/entropy.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
gain(priors, [counts])
calcIG(da_t, 'order')
calcIG(da_t, 'gross')
priors, gross = get_counts(da_t, 'gross')
gain(priors, gross)
gain(priors, [gross])
d,a = priors,[gross]
v = a[0]
v
a
entropy(a)
entropy(v)
log(p, 2)
p = v[0]
pi = v
p * log(p, 2)
def get_entropy(countlist):
    total = 0
    for count in countlist:
        p = float(count) / sum(countlist)
        total += p*Log(p)
    return total*-1
get_entropy([1,1])
entropy([1,1])
def entropy(pi):
    '''
    return the Entropy of a probability distribution:
    entropy(p) = − SUM (Pi * log(Pi) )
    defintion:
            entropy is a metric to measure the uncertainty of a probability distribution.
    entropy ranges between 0 to 1
    Low entropy means the distribution varies (peaks and valleys).
    High entropy means the distribution is uniform.
    See:
            http://www.cs.csi.cuny.edu/~imberman/ai/Entropy%20and%20Information%20Gain.htm
    '''
    
    total = 0
    for p in pi:
        p = p / sum(pi)
        if p != 0:
            total += p * np.log(p)
        else:
            total += 0
    total *= -1
    return total
entropy([1,1])
get_entropy([1,1])
pi = [1,1]
p = pi[0]
p = p / sum(pi)
p
def entropy(pi):
    '''
    return the Entropy of a probability distribution:
    entropy(p) = − SUM (Pi * log(Pi) )
    defintion:
            entropy is a metric to measure the uncertainty of a probability distribution.
    entropy ranges between 0 to 1
    Low entropy means the distribution varies (peaks and valleys).
    High entropy means the distribution is uniform.
    See:
            http://www.cs.csi.cuny.edu/~imberman/ai/Entropy%20and%20Information%20Gain.htm
    '''
    
    total = 0
    for p in pi:
        p = float(p) / sum(pi)
        if p != 0:
            total += p * np.log(p)
        else:
            total += 0
    total *= -1
    return total
entropy([1,1])
def IG(da_t, t):
    if da_t.prior == 0: da_t.set_prior()
    tot_pos = int(da_t.prior * len(da_t.m_reviews))
    tot_neg = len(da_t.m_reviews) - tot_pos
    t_pos = da_t.mgnls['df'][1].get(t,0)
    t_neg = da_t.mgnls['df'][0].get(t,0)
    priors, counts = [tot_pos,tot_neg], [t_pos,t_neg]
    prior_entropy = get_entropy(priors)
    term_entropy = get_entropy(counts)
    return prior_entropy - term_entropy
IG(da_t, 'order')
priors, counts = get_counts(da_t, 'order')
counts
gain(da_t, 'order')
gain(priors, counts)
gain(priors, [counts])
t = 'order'
if da_t.prior == 0: da_t.set_prior()

tot_pos = int(da_t.prior * len(da_t.m_reviews))
tot_neg = len(da_t.m_reviews) - tot_pos
t_pos = da_t.mgnls['df'][1].get(t,0)
t_neg = da_t.mgnls['df'][0].get(t,0)
priors, counts = [tot_pos,tot_neg], [t_pos,t_neg]
priors
counts
prior_entropy = get_entropy(priors)
sum([1,2,3])
sum([1,2,3]) / sum([2,4,9])
def IG(da_t, t):
    if da_t.prior == 0: da_t.set_prior()
    tot_pos = int(da_t.prior * len(da_t.m_reviews))
    tot_neg = len(da_t.m_reviews) - tot_pos
    t_pos = da_t.mgnls['df'][1].get(t,0)
    t_neg = da_t.mgnls['df'][0].get(t,0)
    priors, counts = [tot_pos,tot_neg], [t_pos,t_neg]
    prior_entropy = get_entropy(priors)
    term_entropy = float(sum(counts)) / sum(priors) *  get_entropy(counts)
    return prior_entropy - term_entropy
IG(da_t, 'order')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer(N=1)
da.loadDir('yelp/train', debug=True)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer(N=1)
da.loadDir('yelp/train', debug=True)
da.prior
da.IG('good')
da.IG('great')
da.IG('vagine')
def ChiSq(da_t, t):
    num_pos = int(da_t.prior*len(da_t.m_reviews))
    num_neg = len(da_t.m_reviews) - num_pos
    A = da_t.mgnls['df'][1].get(t,0) # # of pos docs with t
    B = num_pos - A # # of pos docs without t
    C = da_t.mgnls['df'][0].get(t,0) # # of neg docs with t
    D = num_neg - C# # of neg docs without t
    num = (A + B + C + D)+(A*D-B*C)**2
    denom = (A+C)*(B+D)*(A+B)*(C+D)
    return float(num) / float(denom)
def chiSq(da_t, t):
    num_pos = int(da_t.prior*len(da_t.m_reviews))
    num_neg = len(da_t.m_reviews) - num_pos
    A = da_t.mgnls['df'][1].get(t,0) # # of pos docs with t
    B = num_pos - A # # of pos docs without t
    C = da_t.mgnls['df'][0].get(t,0) # # of neg docs with t
    D = num_neg - C# # of neg docs without t
    num = (A + B + C + D)+(A*D-B*C)**2
    denom = (A+C)*(B+D)*(A+B)*(C+D)
    return float(num) / float(denom)
chiSq(da_t, 'order')
chs = [chSq(da_t, t) for t in da_t.tf.keys()]
chs = [chiSq(da_t, t) for t in da_t.tf.keys()]
def chiSq(da_t, t):
    num_pos = int(da_t.prior*len(da_t.m_reviews))
    num_neg = len(da_t.m_reviews) - num_pos
    A = da_t.mgnls['df'][1].get(t,0) # # of pos docs with t
    B = num_pos - A # # of pos docs without t
    C = da_t.mgnls['df'][0].get(t,0) # # of neg docs with t
    D = num_neg - C# # of neg docs without t
    num = (A + B + C + D)+(A*D-B*C)**2
    denom = (A+C)*(B+D)*(A+B)*(C+D)
    value =  float(num) / float(denom) if denom !=0 else 0
    return value
chs = [chiSq(da_t, t) for t in da_t.tf.keys()]
max(chs)
min(chs)
t
t = 'order'
num_pos = int(da_t.prior*len(da_t.m_reviews))
num_neg = len(da_t.m_reviews) - num_pos
A = da_t.mgnls['df'][1].get(t,0) # # of pos docs with t
B = num_pos - A # # of pos docs without t
C = da_t.mgnls['df'][0].get(t,0) # # of neg docs with t
D = num_neg - C# # of neg docs without t
num_pos, num_neg
A,B,C,D
chiSq(da_t, 'order')
num = (A + B + C + D)+(A*D-B*C)**2
num
(A+C)*(B+D)*(A+B)*(C+D)
num_pos = int(da_t.prior*len(da_t.m_reviews))
num_neg = len(da_t.m_reviews) - num_pos
A = da_t.mgnls['df'][1].get(t,0) # # of pos docs with t
B = num_pos - A # # of pos docs without t
C = da_t.mgnls['df'][0].get(t,0) # # of neg docs with t
D = num_neg - C# # of neg docs without t
A,B,C,D
num = (A + B + C + D)+(A*D-B*C)**2
num
num = (A + B + C + D)+pow((A*D - B*C),2)
num
num = (A + B + C + D)*pow((A*D - B*C),2)
num
denom
denom = (A+C)*(B+D)*(A+B)*(C+D)
denom
def chiSq(da_t, t):
    num_pos = int(da_t.prior*len(da_t.m_reviews))
    num_neg = len(da_t.m_reviews) - num_pos
    A = da_t.mgnls['df'][1].get(t,0) # # of pos docs with t
    B = num_pos - A # # of pos docs without t
    C = da_t.mgnls['df'][0].get(t,0) # # of neg docs with t
    D = num_neg - C# # of neg docs without t
    num = (A + B + C + D)*pow((A*D - B*C),2)
    denom = (A+C)*(B+D)*(A+B)*(C+D)
    value =  float(num) / float(denom) if denom !=0 else 0
    return value
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer(N=1)
da.loadDir('yelp/train', debug=True)
da.chiSq('order')
get_counts(da,  'order')
sorted(da.tf, key=lambda x:x[1], reverse=True)[:50]
sorted(da.tf.items(), key=lambda x:x[1], reverse=True)[:50]
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer(N=1)
da.loadDir('yelp/train', debug=True)
sorted(da.tf.items(), key=lambda x:x[1], reverse=True)[:50]
'it' in da.stopwords
'it' in da.m_stopwords
da.normalize('I')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer(N=1)
da.loadDir('yelp/train', debug=True)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer(N=1)
da.loadDir('yelp/train', debug=True)
'i' in da.m_stopwords
da.m_stopwords
'my' in self.m_stopwords
'my' in da.m_stopwords
'it' in da.m_stopwords
sorted(da.tf.items(), key=lambda x:x[1], reverse = True)[:50]
keys = [k for k in da.tf.keys()]
for k in keys:
    if k in da.m_stopwords:
        da.tf.pop(k)
        da.df.pop(k)
        da.mgnls['df'][0].pop(k)
        da.mgnls['df'][1].pop(k)
        da.mgnls['tf'][0].pop(k)
        da.mgnls['tf'][1].pop(k)
        
for k in keys:
    if k in da.m_stopwords:
        da.tf.pop(k,0)
        da.df.pop(k,0)
        da.mgnls['df'][0].pop(k,0)
        da.mgnls['df'][1].pop(k,0)
        da.mgnls['tf'][0].pop(k,0)
        da.mgnls['tf'][1].pop(k,0)
        
sorted(da.tf.items(), key=lambda x:x[1], reverse = True)[:50]
itup = sorted(da.tf.items(), key=lambda x:x[1], reverse = True)[0]
itup
itup[0] == 'i'
itup[0] in da.m_stopwords
'i' in da.m_stopwords
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer(N=1)
da.loadDir('yelp/train', debug=True)
sorted(da.tf.items(), key=lambda x:x[1], reverse = True)[:50]
def filter_vocab(da, k):
    tdf = sorted(da.df.items(), key= lambda x:x[1], reverse=True)
    stat_df = pd.DataFrame(tdf, columns=['gram', 'DF'])
    tot_reviews = len(da.m_reviews)
    
    #filter out grams w DF less than k
    stat_df = stat_df[stat_df['DF'] >= k]
    #calculate information gain and chi square
    stat_df['IDF'] = 1 + np.log(float(tot_reviews)/stat_df['DF'])
    stat_df['IG'] = [da.metric['ig'].get(t,0) for t in stat_df['gram'].tolist()]
    for typ in ['tf','df']:
        for (lbl, name) in [(0,'neg'),(1,'pos')]:
            stat_df['_'.join([name,typ])] = [da.mgnls[typ][lbl].get(t,0) for t in stat_df['gram'].tolist()]
    
    stat_df['posTF'] = [da.mgnls['tf'][1].get(t,0) for t in stat_df['gram'].tolist()]
    stat_df['chi_sq'] = [da.metric['chisq'][t] for t in stat_df['gram'].tolist()]
    
    da.stats = stat_df
    grams = set(stat_df['gram'].tolist())
    #create template for review vector 
    da.empty_vec = {g:0 for g in grams}
    return da
da = filter_vocab(da,10)
k=10
tdf = sorted(da.df.items(), key= lambda x:x[1], reverse=True)
stat_df = pd.DataFrame(tdf, columns=['gram', 'DF'])
tot_reviews = len(da.m_reviews)

#filter out grams w DF less than k
stat_df = stat_df[stat_df['DF'] >= k]
#calculate information gain and chi square
stat_df['IDF'] = 1 + np.log(float(tot_reviews)/stat_df['DF'])
stat_df['IG'] = [da.metric['ig'].get(t,0) for t in stat_df['gram'].tolist()]
for typ in ['tf','df']:
    for (lbl, name) in [(0,'neg'),(1,'pos')]:
        stat_df['_'.join([name,typ])] = [da.mgnls[typ][lbl].get(t,0) for t in stat_df['gram'].tolist()]
stat_df['posTF'] = [da.mgnls['tf'][1].get(t,0) for t in stat_df['gram'].tolist()]
stat_df['chi_sq'] = [da.metric['chisq'][t] for t in stat_df['gram'].tolist()]
stat_df['posTF'] = [da.mgnls['tf'][1].get(t,0) for t in stat_df['gram'].tolist()]
calcChiSqs()
da.calcChiSqs()
def filter_vocab(da, k):
    tdf = sorted(da.df.items(), key= lambda x:x[1], reverse=True)
    da.stat_df = pd.DataFrame(tdf, columns=['gram', 'DF'])
    tot_reviews = len(da.m_reviews)
    da.stat_df['IDF'] = 1 + np.log(float(tot_reviews)/da.stat_df['DF'])
    
    #filter out grams w DF less than k
    da.stat_df = da.stat_df[da.stat_df['DF'] >= k]
    #calculate information gains
    da.calcIGs()
    #calculate chiSqs
    for typ in ['tf','df']:
        for (lbl, name) in [(0,'neg'),(1,'pos')]:
            da.stat_df['_'.join([name,typ])] = [da.mgnls[typ][lbl].get(t,0) for t in da.stat_df['gram'].tolist()]
    
    da.stat_df['posTF'] = [da.mgnls['tf'][1].get(t,0) for t in da.stat_df['gram'].tolist()]
    if len(da.metric['chisq']) == 0: da.calcChiSqs()
    da.stat_df['chi_sq'] = [da.metric['chisq'][t] for t in da.stat_df['gram'].tolist()]
    return da
da = filter_vocab(da, 10)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer(N=1)
da.loadDir('yelp/train', debug=True)
da.calcChiSqs()
da.calcIGs()
max(da.metric['chisq'])
da.metric['chisq'][:5]
da.metric['chisq']
da.metric['chisq'].values()
max(da.metric['chisq'].values())
def filter_vocab(da, k):
    tdf = sorted(da.df.items(), key= lambda x:x[1], reverse=True)
    da.stat_df = pd.DataFrame(tdf, columns=['gram', 'DF'])
    tot_reviews = len(da.m_reviews)
    da.stat_df['IDF'] = 1 + np.log(float(tot_reviews)/da.stat_df['DF'])
    
    #filter out grams w DF less than k
    da.stat_df = da.stat_df[da.stat_df['DF'] >= k]
    #calculate information gains
    if len(da.metric['igs']) == 0: da.calcIGs()
    da.stat_df['IG'] = [da.IG(t) for t in da.stat_df['gram'].tolist()]
    #calculate chiSqs
    if len(da.metric['igs']) == 0: da.calcChiSqs()    
    da.stat_df['chi_sq'] = [da.metric['chisq'][t] for t in da.stat_df['gram'].tolist()]
    for typ in ['tf','df']:
        for (lbl, name) in [(0,'neg'),(1,'pos')]:
            da.stat_df['_'.join([name,typ])] = [da.mgnls[typ][lbl].get(t,0) for t in da.stat_df['gram'].tolist()]
    
    da.stat_df['posTF'] = [da.mgnls['tf'][1].get(t,0) for t in da.stat_df['gram'].tolist()]
    if len(da.metric['chisq']) == 0: da.calcChiSqs()
    return da
da = filter_vocab(da,10)
def filter_vocab(da, k):
    tdf = sorted(da.df.items(), key= lambda x:x[1], reverse=True)
    da.stat_df = pd.DataFrame(tdf, columns=['gram', 'DF'])
    tot_reviews = len(da.m_reviews)
    da.stat_df['IDF'] = 1 + np.log(float(tot_reviews)/da.stat_df['DF'])
    
    #filter out grams w DF less than k
    da.stat_df = da.stat_df[da.stat_df['DF'] >= k]
    #calculate information gains
    if len(da.metric['ig']) == 0: da.calcIGs()
    da.stat_df['IG'] = [da.IG(t) for t in da.stat_df['gram'].tolist()]
    #calculate chiSqs
    if len(da.metric['igs']) == 0: da.calcChiSqs()    
    da.stat_df['chi_sq'] = [da.metric['chisq'][t] for t in da.stat_df['gram'].tolist()]
    for typ in ['tf','df']:
        for (lbl, name) in [(0,'neg'),(1,'pos')]:
            da.stat_df['_'.join([name,typ])] = [da.mgnls[typ][lbl].get(t,0) for t in da.stat_df['gram'].tolist()]
    
    da.stat_df['posTF'] = [da.mgnls['tf'][1].get(t,0) for t in da.stat_df['gram'].tolist()]
    if len(da.metric['chisq']) == 0: da.calcChiSqs()
    return da
da = filter_vocab(da,10)
def filter_vocab(da, k):
    tdf = sorted(da.df.items(), key= lambda x:x[1], reverse=True)
    da.stat_df = pd.DataFrame(tdf, columns=['gram', 'DF'])
    tot_reviews = len(da.m_reviews)
    da.stat_df['IDF'] = 1 + np.log(float(tot_reviews)/da.stat_df['DF'])
    
    #filter out grams w DF less than k
    da.stat_df = da.stat_df[da.stat_df['DF'] >= k]
    #calculate information gains
    if len(da.metric['ig']) == 0: da.calcIGs()
    da.stat_df['IG'] = [da.IG(t) for t in da.stat_df['gram'].tolist()]
    #calculate chiSqs
    if len(da.metric['chisq']) == 0: da.calcChiSqs()    
    da.stat_df['chi_sq'] = [da.metric['chisq'][t] for t in da.stat_df['gram'].tolist()]
    for typ in ['tf','df']:
        for (lbl, name) in [(0,'neg'),(1,'pos')]:
            da.stat_df['_'.join([name,typ])] = [da.mgnls[typ][lbl].get(t,0) for t in da.stat_df['gram'].tolist()]
    
    da.stat_df['posTF'] = [da.mgnls['tf'][1].get(t,0) for t in da.stat_df['gram'].tolist()]
    if len(da.metric['chisq']) == 0: da.calcChiSqs()
    return da
da = filter_vocab(da,10)
da.stat_df
len(da.tf)
da.tf.items()[:5]
da = DocAnalyzer()
import gc
gc.collect()
da = DocAnalyzer(N=1)
da.loadDir('yelp/train')
da = filter_vocab(da, k=10)
cs_df = da.stat_df.copy()
cs_df
cs_df = cs_df[cs_df['chisq'] > 3.841]
cs_df.columns
cs_df = cs_df[cs_df['chi_sq'] > 3.841]
cs_df
da.loadDir('yelp/test')
da = filter_vocab(da, k=10)
da.calcChiSqs()
da.calcIGs()
da = filter_vocab(da, k=10)
da.stat_df
cs_df = da.stat_df.copy()
cs_df = cs_df[cs_df['chi_sq'] > 3.841]
cs_df
ig_df = da.stat_df.copy()
ig_df = da.stat_df.sort_values(by='IG',ascending=False)
ig_df['IG']
max(da.stat_df['IG'])
stat_df['IG'].shape
da.stat_df['IG'].shape
ig_df = ig_df[:5000,]
ig_df = ig_df.ix[:5000,:]
ig_df.to_csv('top_5k_IG.csv', index=False)
ig_df.columns
ig_words = ig_df['gram'].tolist()
ig_words
chi_words = cs_df['gram'].tolist()
combined_vocab = set(chi_words).union(set(ig_words))
len(combined_vocab)
da.final_vocab = combined_vocab
save_obj(da, 'da_hw3')
cs_df = cs_df.sort_values(by='chi_sq',ascending=False)
cs_df.head()
cs_df.ix[:20,:].to_csv('top_20_chisq.csv', index=False)
ig_df.ix[:20,:].to_csv('top_20_ig.csv', index=False)
ig_df.head()
ig_df.ix[:5,:]
ig_df = da.stat_df.sort_values(by='IG',ascending=False)
ig_df.ix[:5,:]
ig_df.ix[:20,:]
cs_df.ix[:5,:]
cs_df.ix[1,1]
cs_df.ix[:1,1]
ig_df.ix[:20,:]
ig_df.ix[20,:]
ig_df.ix[[4,20],:]
ig_df.ix[[range(20)],:]
ig_df.ix[[4,8,12],:]
ig_df.ix[[1,2,3],:]
ig_df.ix[range(3),:]
ig_df.ix[range(20),:]
ig_df.ix[range(20),:].to_csv('top_20_ig.csv', index=False)
ig_df.head()
ig_df.ix[range(5),:]
ig_df.reset_index()
ig_df = ig_df.reset_index()
ig_df.ix[:20,:]
ig_df.ix[:20,:].to_csv('top_20_ig.csv', index=False)
cs_df.reset_index()
cs_df = cs_df.reset_index()
cs_df.ix[:20,:]
cs_df.ix[:20,:].to_csv('top_20_chisq.csv', index=False)
len(da.final_vocab)
dir(da.m_reviews[0])
da.empty_vec
da.empty_vec = {k:0 for k in da.final_vocab}
da.empty_vec
r = da.m_reviews[0]
r.setVec(da)
da.stats = da.stat_df
r.setVec(da)
def setVecs(revlist, da):
    if len(da.stat_df) > 0:
        for r in tqdm(revlist): r.setVec(da)
        da.m_reviews = revlist
    return da
def setVecs(revlist, da):
    if len(da.stat_df) > 0:
        for r in tqdm(revlist): r.setVec(da)
    return da
def setVecs(revlist, da):
    if len(da.stat_df) > 0:
        for r in tqdm(revlist): r.setVec(da)
    return revlist
revs = setVecs(da.m_reviews, da)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/post.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')

## ---(Thu Apr 19 02:16:40 2018)---
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = load_obj('da_hw3')
da.stat_df
del(da)
da = DocAnalyzer()
da.loadDir('yelp/train')
da.loadDir('yelp/test')
da = setVecs(da.m_reviews, da)
da.filter_vocab(10)
da = filter_vocab(da, 10)
da = setVecs(da.m_reviews, da)
da.empty_vec
da[0]
da[0].vec
del(da)
import gc
gc.collect()
da = DocAnalyzer()
da.loadDir('yelp/train')
da.loadDir('yelp/test')
da.stat_df.shape
da.filter_vocab(10)
da = filter_vocab(da, 10)
da.empty_vec = {k:0 for k in da.stat_df['gram'].tolist()}
len(da.empty_vec)
ig_words = da.stat_df.sort_values(by="ig", ascending=False)
ig_words = da.stat_df.sort_values(by="IG", ascending=False)
ig_words.reset_index()
ig_words = ig_words.reset_index()
ig_words.head()
ig_words = ig_words.ix[:5000,:]
ig_words = set(ig_words['gram'].tolist())
da.stat_df.shape
cs_df = da.stat_df.sort_values(by="chi_sq", ascending=False)
cs_df.head()
cs_df = cs_df[cs_df['chi_sq'] > 3.841]
cs_df.shape
da.final_vocab = set(cs_df['gram'].tolist()).union(set(ig_df['gram'].tolist()))
da.final_vocab = set(cs_df['gram'].tolist()).union(ig_words)
len(da.final_words)
len(da.final_vocab)
da = setVecs(da.m_reviews, da)
da.m_reviews[0].vec
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer()
da.loadDir('yelp/train')
da.loadDir('yelp/test')
da.setFinalVocab()
da.filter_vocab(10)
da = filter_vocab(da, 10)
da.setFinalVocab()
da.final_vocab
da.empty_vec
da.empty_vec = {k:0 for k in da.final_vocab}
da.setVecs()
revlist = setVecs(da)
da.m_reviews = revlist
revlist[0].vec
lens = [len(r.vec) for r in da.m_reviews]
np.mean(lens)
len(da.m_reviews)
da.m_reviews = [r for r in da.m_reviews if len(r.vec) > 5]
len(da.m_reviews)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/nb.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
nb = NB(da)
nb.pos_da.m_reviews [r for r in da if r.sent == 1]
nb.pos_da.m_reviews = [r for r in da.m_reviews if r.sent == 1]
len(nb.pos_da.m_reviews)
nb.pos_uni.buildModel(nb.pos_da)
np.pos_uni.m_model['good']
nb.pos_uni
nb.pos_uni.m_model['good']
da.mgnls['tf'][1]['good']
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/nb.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
nb = NB(da)
nm.pos_uni.m_model['good']
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/nb.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
nb= NB(da)
nb.p_mod.m_model['good']
nb.n_mod.m_model['good']
nb.p_mod.calcMLProb('good')
nb.n_mod.calcMLProb('good')
np.p_mod.calcMLProb('wonderful')
nb.p_mod.calcMLProb('wonderful')
nb.n_mod.calcMLProb('wonderful')
nb.p_mod.calcLinearSmoothedProb('good')
nb.n_mod.calcLinearSmoothedProb('good')
nb.n_mod.calcLinearSmoothedProb('bad')
nb.p_mod.calcLinearSmoothedProb('bad')
nb.p_mod.calcLinearSmoothedProb('nasty')
nb.p_mod.calcLinearSmoothedProb('terrible')
nb.n_mod.calcLinearSmoothedProb('terrible')
nb.n_mod.calcLinearSmoothedProb('terribl')
nb.p_mod.calcLinearSmoothedProb('terribl')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/LanguageModel.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
nb = NB(da)
nb.p_mod.calcLinearSmoothedProb('Good')
nb.p_mod.calcLinearSmoothedProb('terrible')
class NB:
    def __init__(self, da, delta = .1,):
        self.pos_da = DocAnalyzer()
        self.neg_da = DocAnalyzer()
        self.pos_da.m_reviews = [r for r in da.m_reviews if r.sent == 1]
        self.neg_da.m_reviews = [r for r in da.m_reviews if r.sent == 0]
        self.da_all = da
        self.delta = delta
        self.p_mod = LanguageModel(delta=delta,da_ref=da,smoothType="ad")
        self.p_mod.m_model = self.da_all.mgnls['tf'][1]
        self.n_mod = LanguageModel(delta=delta,da_ref=da,smoothType="ad")
        self.n_mod.m_model = self.da_all.mgnls['tf'][0]
    
    def logRatio(self,t):
        pos_prob = self.p_mod.calcLinearSmoothedProb(t)
        neg_prob = self.n_mod.calcLinearSmoothedProb(t)
        return Log(pos_prob / neg_prob)
    
    def calcLogRatios(self):
        self.logRatios = {k:self.logRatio(k) for k in self.da_all.final_vocab}
nb=NB(da)
nb.logRatio('good')
class NB:
    def __init__(self, da, delta = .1,):
        self.pos_da = DocAnalyzer()
        self.neg_da = DocAnalyzer()
        self.pos_da.m_reviews = [r for r in da.m_reviews if r.sent == 1]
        self.neg_da.m_reviews = [r for r in da.m_reviews if r.sent == 0]
        self.da_all = da
        self.delta = delta
        self.p_mod = LanguageModel(delta=delta,da_ref=da,smoothType="ad")
        self.p_mod.m_model = self.da_all.mgnls['tf'][1]
        self.n_mod = LanguageModel(delta=delta,da_ref=da,smoothType="ad")
        self.n_mod.m_model = self.da_all.mgnls['tf'][0]
    
    def logRatio(self,t):
        pos_prob = self.p_mod.calcLinearSmoothedProb(t)
        neg_prob = self.n_mod.calcLinearSmoothedProb(t)
        return self.da_all.Log(pos_prob / neg_prob)
    
    def calcLogRatios(self):
        self.logRatios = {k:self.logRatio(k) for k in self.da_all.final_vocab}
nb=NB(da)
nb.logRatio('good')
nb.logRatio('great')
nb.logRatio('terrible')
nb.calcLogRatios()
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/nb.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
nb = NB(da)
nb.calcLogRatios()
res = sorted(nb.logRatios, key=lambda x:x[1], reverse=True)
res = sorted(nb.logRatios.items(), key=lambda x:x[1], reverse=True)
res[:20]
res = sorted(nb.logRatios.items(), key=lambda x:x[1], reverse=False)
res[:20]
nb.da_all.tf['lovee']
nb.p_mod.m_model['lovee']
nb.n_mod.m_model['lovee']
nb.logRatio('lovee')
t = 'lovee'
self.p_mod.calcLinearSmoothedProb(t)
nb.p_mod.calcLinearSmoothedProb(t)
nb.n_mod.calcLinearSmoothedProb(t)
nb.p_mod.calcLinearSmoothedProb('loveeee')
nb.p_mod.calcLinearSmoothedProb('loveeeee')
nb.p_mod.calcLinearSmoothedProb('lovveeeee')
nb.p_mod.calcLinearSmoothedProb('looooooooooovveeeee')
nb.n_mod.calcLinearSmoothedProb('looooooooooovveeeee')
nb.n_mod.calcLinearSmoothedProb('habbak')
t
nb.n_mod.m_model['lovee']
nb.n_mod.m_model['vagina']
nb.n_mod.calcLinearSmoothedProb('vagina')
nb.n_mod.calcLinearSmoothedProb('lovee')
nb.n_mod.da_ref.stem('lovee')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/LanguageModel.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
nb = NB(da)
nb.logRatio('lovee')
nb.calcLogRatios()
sorted(nb.logRatios.items(), key=lambda x:x[1], reverse=True)[:20]
sorted(nb.logRatios.items(), key=lambda x:x[1], reverse=False)[:20]
Log(2)
np.log(2)*np.log(3)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/nb.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
nb = NB(da)
nb.classify(da.m_reviews[0])
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/nb.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
nb = NB(da)
nb.classify(da.m_reviews[0])
nb.classify(da.m_reviews[1])
nb.classify(da.m_reviews[2])
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/nb.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
nb = NB(da)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/nb.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
nb = NB(da)
nb.classify(da.m_reviews[2])
scores = {}
for r in tqdm(da.m_reviews):
    scores[r] = nb.classify(r)
    
samp_size = 200
res = np.random.choice(da.m_reviews,, size=samp_size, replace=False)
res = np.random.choice(da.m_reviews, size=samp_size, replace=False)
scores = {}
for r in tqdm(res):
    scores[r] = nb.classify(r)
    
pred_pairs = [(score, res[i].sent) for i,score in enumerate(scores)]
pred_pairs
scores[0]
scores
for i,r in tqdm(enumerate(res)):
    scores[i] = nb.classify(r)
    
scores
pred_pairs = [(v, res[k].sent) for k,v in scores.items()]
res[0]
for k,v in scores.items()[:5]:
    print k,v
    
for k,v in scores.items()[:5]:
    print res[k].sent
    
sents = [res[k].sent for k in scores.keys()]
scores.keys()
scores = {}
for i,r in tqdm(enumerate(res)):
    scores[i] = nb.classify(r)
    
scores.keys()
pred_pairs = [(v,res[k].sent) for k,v in scores.items()]
pred_pairs
save_obj(da, 'da_hw3')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/nb.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
nb = NB(da)
nb.classify(da.m_reviews[0])
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/LanguageModel.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
nb = NB(da)
nb.classify(da.m_reviews[0])
sum(nb.p_mod.m_model.keys())
nb.p_mod.m_model['good']
sum(nb.p_mod.m_model.values())
nb.p_mod.d
nb.p_mod.V
nb.n_mod.d
nb.n_mod.V
sum(nb.n_mod.m_model.values())
len(nb.p_mod.m_model.keys())
len(nb.n_mod.m_model.keys())
review = da.m_reviews[0]
total += nb.da_all.prior / (1-nb.da_all.prior)
total = nb.da_all.prior / (1-nb.da_all.prior)
total
for t in review.tokens:
    pos_log = nb.da_all.Log(self.p_mod.calcLinearSmoothedProb(t))
    neg_log = nb.da_all.Log(self.n_mod.calcLinearSmoothedProb(t))
    total += (pos_log - neg_log)
    
for t in review.tokens:
    pos_log = nb.da_all.Log(nb.p_mod.calcLinearSmoothedProb(t))
    neg_log = nb.da_all.Log(nb.n_mod.calcLinearSmoothedProb(t))
    total += (pos_log - neg_log)
    
total
tot2 = nb.da_all.prior / (1-nb.da_all.prior)
for t in review.tokens:
    tot2 += nb.logRatio(t)
    
tot2
preds = [nb.classify(r) for r in da.m_reviews]
preds = [nb.classify(r) for r in tqdm(da.m_reviews)]
preds[:5]
pairs = zip(preds, [r.sent for r in da.m_reviews])
pairs[:5]
pairs = sorted(pairs, key=lambda x:x[0])
pairs[:5]
i = 2
pred_labels = []
pred, y = pairs[i]
neg_preds = [0 for idx in range(i)]
neg_preds
pos_preds = [1 for idx in range(i,len(pairs))]
tot_preds = neg_preds.extend(pos_preds)
len(tot_preds)
neg_preds = [0 for idx in range(i)]
tot_preds = list(neg_preds, pos_preds)
tot_preds = neg_preds + pos_preds
tot_preds[:5]
labels[:5]
labels = [t[1] for t in pairs]
labels[:5]
pairs[:5]
lbl_pairs = zip(tot_preds,labels)
lbl_pairs[:5]
cm = np.ndarray([2,2], dtype=int)
cm[0,1] +=1
cm
cm = np.zeros([2,2], dtype=int)
cm
cm[0,1] +=1
cm
def evaluate(pred_lbls, true_lbls, mets = ['P','R']):
    metrics = ['PR','RE','F','AUC', 'ACC', 'P']
    res = {}
    for m in mets: assert m in metrics
    #build confusion matrix
    cm = np.zeros([2,2])
    for p,l in zip(pred_labels,true_labels):
        cm[p,l] +=1
    precs, recs = {},{}
    TN, FN = cm[0,0],cm[0,1]
    FP, TN = cm[1,0],cm[1,1]
    if 'PR' in mets:
        precs[0] = float(TN) / (TN + FN)
        precs[1] = float(TP) / (TP + FP)
        res['Precision'] = np.mean(precs)
    if 'RE' in mets:
        recs[0] = float(TN) / (TN + FP)       
        precs[1] = float(TP) / (TP + FN)
        res['Recall'] = np.mean(recs)
    if 'F' in mets:
        results['F'] = float(2) / (1.0 / res['Precision'] + 1.0 / res['Recall'])
    #TODo: Add statistical significant test (P) - chi sq?
     return res
def evaluate(pred_lbls, true_lbls, mets = ['P','R']):
    metrics = ['PR','RE','F','AUC', 'ACC', 'P']
    res = {}
    for m in mets: assert m in metrics
    #build confusion matrix
    cm = np.zeros([2,2])
    for p,l in zip(pred_labels,true_labels):
        cm[p,l] +=1
    precs, recs = {},{}
    TN, FN = cm[0,0],cm[0,1]
    FP, TN = cm[1,0],cm[1,1]
    if 'PR' in mets:
        precs[0] = float(TN) / (TN + FN)
        precs[1] = float(TP) / (TP + FP)
        res['Precision'] = np.mean(precs)
    if 'RE' in mets:
        recs[0] = float(TN) / (TN + FP)       
        precs[1] = float(TP) / (TP + FN)
        res['Recall'] = np.mean(recs)
    if 'F' in mets:
        results['F'] = float(2) / (1.0 / res['Precision'] + 1.0 / res['Recall'])
    #TODo: Add statistical significant test (P) - chi sq?
    return res
tot_preds[:5]
labels[:5]
evaluate(tot_preds, labels)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/nb.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
evaluate(tot_preds, labels)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/nb.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
evaluate(tot_preds, labels)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/nb.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
evaluate(tot_preds, labels)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/nb.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
evaluate(tot_preds, labels)
pred_lbls, true_lbls = tot_preds, labels
res = {}
for m in mets: assert m in metrics

#build confusion matrix
cm = np.zeros([2,2])
for p,l in zip(pred_lbls,true_lbls):
    cm[p,l] +=1

precs, recs = {},{}
TN, FN = cm[0,0],cm[0,1]
FP, TP = cm[1,0],cm[1,1]
res = {}
mets = ['PR', 'RE']
cm = np.zeros([2,2])
for p,l in zip(pred_lbls,true_lbls):
    cm[p,l] +=1

precs, recs = {},{}
TN, FN = cm[0,0],cm[0,1]
FP, TP = cm[1,0],cm[1,1]
cm
cm = np.zeros([2,2], type=int)
for p,l in zip(pred_lbls,true_lbls):
    cm[p,l] +=1

precs, recs = {},{}
TN, FN = cm[0,0],cm[0,1]
FP, TP = cm[1,0],cm[1,1]
cm = np.zeros([2,2], dtype=int)
for p,l in zip(pred_lbls,true_lbls):
    cm[p,l] +=1

precs, recs = {},{}
TN, FN = cm[0,0],cm[0,1]
FP, TP = cm[1,0],cm[1,1]
if 'PR' in mets:
    precs[0] = float(TN) / (TN + FN)
    precs[1] = float(TP) / (TP + FP)
cm
TN,TP
TP
FP
FN
float(TN) / (TN + FP)
float(TP) / (TP + FN)
recs[0] = float(TN) / (TN + FP)       
precs[1] = float(TP) / (TP + FN)
res['Recall'] = np.mean(recs.values())
res['Recall']
if 'RE' in mets:
    recs[0] = float(TN) / (TN + FP)       
    recs[1] = float(TP) / (TP + FN)
    res['Recall'] = np.mean(recs.values())
res['Recall']
if 'PR' in mets:
    precs[0] = float(TN) / (TN + FN)
    precs[1] = float(TP) / (TP + FP)
res['Precision'] = np.mean(precs.values())
res['Precision']
precs
cm
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/nb.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
evaluate(pred_lbls, true_lbls)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/nb.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
import matplotlib.pyplot as plt
prlist = evaluate(pred_lbls,true_lbls)
prlist
def gen_PRC(preds, true_labels):
    if len(preds) != len(true_labels):
        print("different numbers of predictions and labels")
        return
    else:
        prlist = []
        for idx, (pred,y) in enumerate(zip(preds,true_labels)):
            pred_labels = []
            pred_labels += [0 for i in range(idx)] #negative pred labels
            pred_labels += [1 for i in range(idx,len(preds))] #positive pred labels
            assert len(pred_labels) == len(true_labels)
            res = evaluate(pred_labels,true_labels, metrics=['PR','RE'])
            p,r = res['precision'],res['recall']
            prlist.append((p,r))
    return prlist
preds[:5]
labels[:5]
res = gen_PRC(preds, labels)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/nb.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
res = gen_PRC(preds, labels)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/nb.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
res = gen_PRC(preds, labels)
def div(num,denom):
    if denom == 0: return 0
    else: return float(num)/denom
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/nb.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
res = gen_PRC(preds, labels)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/nb.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
res = gen_PRC(preds, labels)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/nb.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
res = gen_PRC(preds, labels)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/nb.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
res = gen_PRC(preds, labels)
def gen_PRC(preds, true_labels):
    if len(preds) != len(true_labels):
        print("different numbers of predictions and labels")
        return
    else:
        prlist = []
        pl_tups = zip(preds, true_labels)
        for idx, (pred,y) in tqdm(enumerate(pl_tups)):
            pred_labels = []
            pred_labels += [0 for i in range(idx)] #negative pred labels
            pred_labels += [1 for i in range(idx,len(preds))] #positive pred labels
            assert len(pred_labels) == len(true_labels)
            res = evaluate(pred_labels,true_labels, mets=['PR','RE'])
            p,r = res['precision'],res['recall']
            prlist.append((p,r))
    return prlist
res = gen_PRC(preds, labels)
def gen_PRC(preds, true_labels):
    if len(preds) != len(true_labels):
        print("different numbers of predictions and labels")
        return
    else:
        prlist = []
        pl_tups = zip(preds, true_labels)
        for idx, (pred,y) in enumerate(tqdm(pl_tups)):
            pred_labels = []
            pred_labels += [0 for i in range(idx)] #negative pred labels
            pred_labels += [1 for i in range(idx,len(preds))] #positive pred labels
            assert len(pred_labels) == len(true_labels)
            res = evaluate(pred_labels,true_labels, mets=['PR','RE'])
            p,r = res['precision'],res['recall']
            prlist.append((p,r))
    return prlist
res = gen_PRC(preds, labels)

## ---(Thu Apr 19 16:07:43 2018)---
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/nb.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
def PRC(preds, true_labels, iterlist = None):
    if not iterlist: iterlist = range(len(preds))
    prlist = []
    for i in iterlist:
        pred_labels = []
        pred_labels += [0 for i in range(i)] #negative pred labels
        pred_labels += [1 for i in range(i,len(preds))] #positive pred labels
        assert len(pred_labels) == len(true_labels)
        res = evaluate(pred_labels,true_labels, mets=['PR','RE'])
        p,r = res['precision'],res['recall']
        prlist.append((i,(p,r)))
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/nb.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/nb.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = load_obj('da_hw3')
nb = NB(da)
predtext = open('predlist.txt', 'r').read()
os.listdir('.')
predtext = open('preds.txt', 'r').read()
preds = predtext.split(',')
preds = [float(p) for p in preds]
preds[:5]
labels = [r.sent for r in da.m_reviews]
labels[:5]
PRC(preds, labels)
len(preds)
len(labels)
true_labels = labels
iterlist = None
if not iterlist: iterlist = range(len(preds))
len(iterlist)
i = iterlist[0]
i
prlist = []
pred_labels = []
pred_labels += [0 for i in range(i)] #negative pred labels
pred_labels += [1 for i in range(i,len(preds))]
len(pred_labels)
assert len(pred_labels) == len(true_labels)
res = evaluate(pred_labels,true_labels, mets=['PR','RE'])
p,r = res['precision'],res['recall']
p,r
if not iterlist: iterlist = range(len(preds))

prlist = []
for i in iterlist:
    print(i)
    pred_labels = []
    pred_labels += [0 for i in range(i)] #negative pred labels
    pred_labels += [1 for i in range(i,len(preds))] #positive pred labels
    assert len(pred_labels) == len(true_labels)
    res = evaluate(pred_labels,true_labels, mets=['PR','RE'])
    p,r = res['precision'],res['recall']
    prlist.append((i,(p,r)))
i
iterlist[:5]
if not iterlist: iterlist = range(len(preds))

prlist = []
for idx in iterlist:
    print(idx)
    pred_labels = []
    pred_labels += [0 for i in range(idx)] #negative pred labels
    pred_labels += [1 for i in range(idx,len(preds))] #positive pred labels
    assert len(pred_labels) == len(true_labels)
    res = evaluate(pred_labels,true_labels, mets=['PR','RE'])
    p,r = res['precision'],res['recall']
    prlist.append((i,(p,r)))
def PRC(preds, true_labels, iterlist = None):
    if not iterlist: iterlist = range(len(preds))
    prlist = []
    for idx in tqdm(iterlist):
        print(idx)
        pred_labels = []
        pred_labels += [0 for i in range(idx)] #negative pred labels
        pred_labels += [1 for i in range(idx,len(preds))] #positive pred labels
        assert len(pred_labels) == len(true_labels)
        res = evaluate(pred_labels,true_labels, mets=['PR','RE'])
        p,r = res['precision'],res['recall']
        prlist.append((i,(p,r)))
res = PRC(preds, labels, iterlist[0,1,2,3])
res = PRC(preds, labels, iterlist=[0,1,2,3])
def PRC(preds, true_labels, iterlist = None):
    if not iterlist: iterlist = range(len(preds))
    prlist = []
    for idx in tqdm(iterlist):
        print(idx)
        pred_labels = []
        pred_labels += [0 for i in range(idx)] #negative pred labels
        pred_labels += [1 for i in range(idx,len(preds))] #positive pred labels
        assert len(pred_labels) == len(true_labels)
        res = evaluate(pred_labels,true_labels, mets=['PR','RE'])
        p,r = res['precision'],res['recall']
        prlist.append((i,(p,r)))
    return prlist
res = PRC(preds, labels, iterlist=[0,1,2,3])
res
def PRC(preds, true_labels, iterlist = None):
    if not iterlist: iterlist = range(len(preds))
    prlist = []
    for idx in tqdm(iterlist):
        print(idx)
        pred_labels = []
        pred_labels += [0 for i in range(idx)] #negative pred labels
        pred_labels += [1 for i in range(idx,len(preds))] #positive pred labels
        assert len(pred_labels) == len(true_labels)
        res = evaluate(pred_labels,true_labels, mets=['PR','RE'])
        p,r = res['precision'],res['recall']
        prlist.append((idx,(p,r)))
    return prlist
res = PRC(preds, labels, iterlist=[0,1,2,3])
res
num_cores = 20
nc=20
rev_lists = make_core_lists(range(len(preds)), nc)
rev_lists
len(rev_lists)
len(rev_lists[0])
nc = 3
rev_lists = make_core_lists(range(len(preds)), nc)
prlist = []
pl_tups = zip(preds, true_labels)
pl_tups = sorted(pl_tups, key=lambda x:x[0], reverse=False)
p2, l2 = zip(*pl_tups)
p2[:5]
l2[:5]
def gen_PRC(preds, true_labels, parallel=False, nc=num_cores):
    if len(preds) != len(true_labels):
        print("different numbers of predictions and labels")
        return
    else:
        prlist = []
        pl_tups = zip(preds, true_labels)
        pl_tups = sorted(pl_tups, key=lambda x:x[0], reverse=False)
        sorted_p, sorted_l = zip(*pl_tups)
        if parallel:           
            rev_lists = make_core_lists(range(len(preds)), nc)
            pool = mp.Pool(processes=nc)
            recs = [pool.apply_async(PRC, args=(sorted_p,sorted_l,rev_lists[i])) for i in range(nc)]
            recs = [r.get() for r in recs]    
            recs_coll = []
            for r in recs: recs_coll +=r
            recs_coll = sorted(recs_coll, key= lambda x:x[0], reverse=False)
            idxs, prlist = zip(*recs_coll)
        else:
            recs_coll = PRC(sorted_p, sorted_l)
            idxs, prlist = zip(*recs_coll)
    return prlist
res = gen_PRC(preds, labels, parallel=True, nc=3)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/nb.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = load_obj('da_hw3')
pr_df = pd.DataFrame.from_csv('precs_and_recs.csv')
pr_df.plot()
plt.plot(x=df['prec'],y=df['rec'])
pr_df.columns
plt.plot(x=pr_df['prec'],y=pr_df['rec'])
fig = plt.figure(figsize = (8,6))
ax1 = fog.add_subplot(111)
ax1 = fig.add_subplot(111)
ax1.plot(pr_df['prec'],pr_df['rec'], 'r')
ax1.show()
plt.plot(pr_df['rec'],pr_df['prec'])
r_samp = np.random.choice(da.m_reviews, size=500,replace=False)
preds = [nb.classify(r_samp) for r in r_samp]
nb = NB(da)
preds = [nb.classify(r_samp) for r in r_samp]
rsamp[0]
r_samp[0]
r_samp[:5]
res = nb.classify(r_samp[0])
res
res = [nb.classify(r) for r in r_samp]
preds = res
del(res)
labels = [r.sent for r in r_samp]
zip(preds, labels)[:20]
sgns = [1 if r > 0 else 0 for r in preds]
res = evaluate(sgns, labels)
res
res = gen_PRC(preds, labels)
def PRC(preds, true_labels, iterlist = None):
    if not iterlist: iterlist = range(len(preds))
    prlist = []
    for idx in tqdm(iterlist):
        pred_labels = []
        pred_labels += [0 for i in range(idx)] #negative pred labels
        pred_labels += [1 for i in range(idx,len(preds))] #positive pred labels
        assert len(pred_labels) == len(true_labels)
        res = evaluate(pred_labels,true_labels, mets=['PR','RE'])
        p,r = res['precision'],res['recall']
        prlist.append((idx,(p,r)))
    return prlist
res = gen_PRC(preds, labels)
res
psub, lsub = preds[:10], labels[:10]
res = evaluate(psub,lsub)
ssub, lsub = sgns[:10], labels[:10]
res = evaluate(ssub,lsub)
res
res = gen_PRC(psub, lsub)
res
zip(psub,lsub)
tups = zip(psub,lsub)
tups = sorted(tups, key=lambda x:x[0], reverse=False)
psub,lsub = zip(*tups)
zip(psub,lsub)
res = gen_PRC(psub,lsub)
res
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/nb.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
res = gen_PRC(psub,lsub)
res
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/nb.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
res = gen_PRC(psub,lsub)
res
from sklearn.metrics import precision_recall_curve
precision, recall, thresholds = precision_recall_curve(lsub,psub)
precision
recall
plt.plot(recall, precision)
plt.plot(precision, recall)
zip(precision, recall)
preds = [nb.classify(r_samp) for r in r_samp]
preds = [nb.classify(r) for r in r_samp]
r_samp[:5]
nb.classify(r_samp[0])
nb
import numpy as np
nb.classify(r_samp[0])
da
del(np)
nb.classify(r_samp[0])
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/nb.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = load_obj('da_hw3')
nb = NB(da)
r_samp = np.random.choice(da.m_reviews, size=500, replace=False)
preds = [nb.classify(r) for r in r_samp]
labels = [r.sent for r in r_samp]
from sklearn.metrics import precision_recall_curve
prec, rec, thresh = precision_recall_curve(preds,labels)
labels[:10]
prec, rec, thresh = precision_recall_curve(labels,preds)
plt.plot(prec, rec)
precision, recall, thresh = precision_recall_curve(labels, preds)
fig = plt.figure()
precision, recall, thresh = precision_recall_curve(labels, preds)
fig = plt.figure()
ax = fig.add(subplot(111))
ax.plot(recall,precision)
precision, recall, thresh = precision_recall_curve(labels, preds)
fig = plt.figure()
ax = fig.add_subplot(subplot(111))
ax.plot(recall,precision)
precision, recall, thresh = precision_recall_curve(labels, preds)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(recall,precision)
precision, recall, thresh = precision_recall_curve(labels, preds)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(recall,precision)
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('PR Curve for NB Classifier')
fig.savefig('PR_Curve_NB_2_2.png')
plt.show()
prs = {k:{'prec':[],'rec':[]} for k in deltas}
for d in deltas:
    nb = NB(da, delta=d)
    preds = [nb.classify(r) for r in r_samp]
    labels = [r.sent for r in r_samp]
    precision, recall, thresh = precision_recall_curve(labels, preds)
    prs[d]['prec'] = precision
    prs[d]['rec'] = recall
deltas = [.01,.1,.5,1]
prs = {k:{'prec':[],'rec':[]} for k in deltas}
for d in deltas:
    nb = NB(da, delta=d)
    preds = [nb.classify(r) for r in r_samp]
    labels = [r.sent for r in r_samp]
    precision, recall, thresh = precision_recall_curve(labels, preds)
    prs[d]['prec'] = precision
    prs[d]['rec'] = recall
prs[0.1]
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(prs[0.1]['rec'],prs[0.1]['prec'])
ax.plot(prs[0.01]['rec'],prs[0.01]['prec'])
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(prs[0.1]['rec'],prs[0.1]['prec'], 'r', prs[1]['rec'],prs[1]['prec'], 'b',\
        prs[.5]['rec'],prs[.5]['prec'], 'g',prs[.01]['rec'],prs[.01]['prec'], 'y')
plt.plot(prs[1]['rec'],prs[1]['prec'], 'b')
plt.plot(prs[1]['rec'],prs[1]['prec'], 'b', label="d=1")
plt.plot(prs[.5]['rec'],prs[.5]['prec'], 'g', label="d=.5")
plt.plot(prs[.1]['rec'],prs[.1]['prec'], 'y', label="d=.1")
plt.plot(prs[1]['rec'],prs[1]['prec'], 'r', label="d=1")
plt.legend()
deltas = [.01,.1,.5,.8]
prs = {k:{'prec':[],'rec':[]} for k in deltas}
for d in deltas:
    nb = NB(da, delta=d)
    preds = [nb.classify(r) for r in r_samp]
    labels = [r.sent for r in r_samp]
    precision, recall, thresh = precision_recall_curve(labels, preds)
    prs[d]['prec'] = precision
    prs[d]['rec'] = recall
styles = ['-.r', '..b', '^g', '.y', '*p']
for i,d in enumerate(prs.keys()):
    plt.plot(prs[d]['rec'], prs[d]['prec'], styles[i], label = "d={}".format(d))


plt.legend()
styles = ['-.r', '_b', '^g', '.y', '*p']
for i,d in enumerate(prs.keys()):
    plt.plot(prs[d]['rec'], prs[d]['prec'], styles[i], label = "d={}".format(d))


plt.legend()
styles = ['r', 'b', 'g', 'y', 'p']
for i,d in enumerate(prs.keys()):
    plt.plot(prs[d]['rec'], prs[d]['prec'], styles[i], label = "d={}".format(d))


plt.legend()
styles = ['r', 'b', 'g', 'y', 'p']
for i,d in enumerate(prs.keys()):
    plt.plot(prs[d]['rec'], prs[d]['prec'], styles[i], label = "d={}".format(d))

plt.title('PR Curves for different values of Delta')   
plt.xlabel('Recall') 
plt.ylabel('Precision')
plt.legend()
styles = ['r', 'b', 'g', 'y', 'p']
for i,d in enumerate(prs.keys()):
    plt.plot(prs[d]['rec'], prs[d]['prec'], styles[i], label = "d={}".format(d))

plt.title('PR Curves for different values of Delta')   
plt.xlabel('Recall') 
plt.ylabel('Precision')
plt.axis([0,1,0,1])
plt.legend()
plt.savefig('PR_plot_different_deltas')
styles = ['r', 'b', 'g', 'y', 'p']
for i,d in enumerate(prs.keys()):
    plt.plot(prs[d]['rec'], prs[d]['prec'], styles[i], label = "d={}".format(d))

plt.title('PR Curves for different values of Delta')   
plt.xlabel('Recall') 
plt.ylabel('Precision')
plt.axis([0,1,.8,1])
plt.legend()
plt.savefig('PR_plot_different_deltas')
for i,d in enumerate(prs.keys()):
    plt.plot(prs[d]['rec'], prs[d]['prec'], styles[i], label = "d={}".format(d))

plt.title('PR Curves for different values of Delta')   
plt.xlabel('Recall') 
plt.ylabel('Precision')
plt.axis([0,1,.8,1.02])
plt.legend()
plt.savefig('PR_plot_different_deltas')

## ---(Thu Apr 19 22:07:02 2018)---
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/nb.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
np.random.uniform(-1,1)
da = load_obj('da_hw3')
da.m_reviews[0].vec
hashfn = [{} for i in range(5)]
for i in range(5):
    hashfn[i] = {k:np.random.uniform(-1,1) for k in da.empty_vec.keys()}
    
hashfn
hashfn[0]
hashfn[1]
r = da.m_reviews[0]
dp = sum([r.vec[k]*hashfn[0][k] for k in r.vec.keys()])
dp
r.vec.keys()
r.vec.values()
[hashfn[0][k] for k in r.vec.keys()]
dp = sum([r.vec[k]*hashfn[0][k] for k in r.vec.keys()])
dp
str(-1)
def sgn(x):
    if x > 0: return 1
    elif x < 0: return -1
    else: return 0
sgin(-13)
sgn(-13)
sgn(13)
sgn(0)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/knn.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
knn = KNN(da)
knn.setHashes()
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/knn.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
knn = KNN(da)
knn.setHashes()
knn.hashfn[0]
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/knn.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
knn = KNN(da)
knn.setHashes()
knn.train()
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/knn.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
knn = KNN(da)
knn.setHashes()
knn.train()
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/knn.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
knn = KNN(da)
knn.setHashes()
knn.train()

[len(knn.buckets)]
[len(k) for k in knn.buckets]
len(da.m_reviews)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/knn.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
knn = KNN(da)
knn.setHashes()
knn.train()
da_test = da.copy()
da_test = DocAnalyzer()
test_revs = np.random.choice(da.m_reviews, size=.7*len(da.m_reviews), replace=False)
train_size = int(.7*len(da.m_reviews))
train_size
test_size = len(da.m_reviews) - train_size
train_docs = np.random.choice(da.m_reviews, size=train_size, replace=False)
diff = set(da.m_reviews).difference(set(train_docs))
len(diff)
test_docs = list(diff)
da_train = DocAnalyzer()
da_train.m_reviews = train_docs
da_test = DocAnalyzer()
da_test.m_reviews = test_docs
knn = KNN(da_train)
knn.train()
knn.setHashes()
knn.train()
da_train = DocAnalyzer()
da_train.loadDir('yelp/train')
len(da_train.empty_vec)
da_train.empty_vec = {k:0 for k in da_train.tf.keys()}
len(da_train.empty_vec)
da_train.filter_vocab(10)
len(da_train.empty_vec)
knn = KNN(da_train)
knn.setHashes()
knn.train()
da_train.setVecs()
da_train = setVecs(da_train)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da_train = DocAnalyzer()
dt = da_train
del(da_train)
dt.loadDir('yelp/train')
dt.setVecs()
dt.filter_vocab()
dt.filter_vocab(10)
dt.setFinalVocab()
dt.setVecs()
revlist = setVecs_parallel(da.m_reviews,da,nc=3)
revlist = setVecs_parallel(dt.m_reviews,dt,nc=3)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
revlist = setVecs_parallel(dt.m_reviews,dt,nc=3)
def setVecs_parallel(revlist, da_t, nc=num_cores):
    if len(da_t.tf) > 0:
        rev_lists = make_core_lists(revlist, nc)
        pool = mp.Pool(processes=nc)
        revs = [pool.apply_async(setVecs, args=(da_t,rev_lists[i])) for i in range(nc)]
        revs = [rev.get() for rev in revs]
        revs_coll = []
        for r in revs:
            revs_coll += r
        return revs_coll
    else:
        print("analyzer has no vocabulary")
        return revlist
da_t = dt
revlist = dt.m_reviews
nc = 3
rev_lists = make_core_lists(revlist, nc)
pool = mp.Pool(processes=nc)
revs = [pool.apply_async(setVecs, args=(da_t,rev_lists[i])) for i in range(nc)]
revs = [rev.get() for rev in revs]
revs_coll = []
pool = mp.Pool(processes=nc)
revs = [pool.apply_async(setVecs, args=(da_t,rev_lists[i])) for i in range(nc)]
revs = [rev.get() for rev in revs]
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
setVecs_parallel(revlist, dt, nc=3)
tfiles = os.listdir('yelp/train')
tfiles = np.random.choice(tfiles, size= 8, replace=False)
da_t = DocAnalyzer()
del(dt)
import gc
gc.collect()
da_t.loadDir('yelp/train', sublist=tfiles)
res = readQueries('query.json')
res = readQueries()
res
res[0]
queries = [post(q) for q in res]
knn = KNN(da)
knn.setHashes()
knn.train()
knn.classify(queries[0])
for q in queries:
    q.setVec(da)
    
for q in queries:
    q.tokens = textToGrams(da,q.content)
    
da2 = DocAnalyzer()
da2.__dict__ = {k:v for k,v in da.__dict__.items()}
del(da)
da = da2
del(da2)
for q in queries:
    q.tokens = textToGrams(da,q.content)
    
len(queries[0].vec)
len(queries[0].tokens)
for q in queries:
    q.setVec(da)
    
knn.classify(queries[0])
def find_nns(da,bucket, rev):
    sims = []
    assert bucket in da.buckets
    neighbors = da.buckets[bucket]
    for idx,n in tqdm(enumerate(neighbors)):
        sims.append((idx, sparse_cos_sim(n, rev)))
    sims = sorted(sims, key=lambda x:x[0], reverse=True)
    return [(neighbors[idx],sim) for idx,sim in enumerate(sims)[:da.k]]
bucket = knn.hashRev(queries[0], addToBucket=False)
bucket
rev = queries[0]
sims = []
assert bucket in da.buckets
neighbors = da.buckets[bucket]
def find_nns(knn,bucket, rev):
    sims = []
    assert bucket in knn.buckets
    neighbors = knn.buckets[bucket]
    for idx,n in tqdm(enumerate(neighbors)):
        sims.append((idx, sparse_cos_sim(n, rev)))
    sims = sorted(sims, key=lambda x:x[0], reverse=True)
    return [(neighbors[idx],sim) for idx,sim in enumerate(sims)[:knn.k]]
sims = []
assert bucket in knn.buckets
neighbors = knn.buckets[bucket]
len(neighbors)
len(knn.buckets)
for idx,n in tqdm(enumerate(neighbors)):
    sims.append((idx, sparse_cos_sim(n, rev)))
sims[:5]
sims = sorted(sims, key=lambda x:x[1], reverse=True)
def find_nns(knn,bucket, rev):
    sims = []
    assert bucket in knn.buckets
    neighbors = knn.buckets[bucket]
    for idx,n in enumerate(tqdm(neighbors)):
        sims.append((idx, sparse_cos_sim(n, rev)))
    sims = sorted(sims, key=lambda x:x[1], reverse=True)
    return [(neighbors[idx],sim) for idx,sim in enumerate(sims)[:knn.k]]
res = find_nns(knn, bucket, rev)
def find_nns(knn,bucket, rev):
    sims = []
    assert bucket in knn.buckets
    neighbors = knn.buckets[bucket]
    for idx,n in enumerate(tqdm(neighbors)):
        sims.append((idx, sparse_cos_sim(n, rev)))
    sims = sorted(sims, key=lambda x:x[1], reverse=True)
    return [(neighbors[idx],sim) for idx,sim in enumerate(sims[:knn.k])]
res = find_nns(knn, bucket, rev)
for r in res:
    print(r)
    
for r in res:
    print(r[0])
    
res[0].content
res[0][0].content
res[0][1].content
res[1][0].content
s = """"It's been more than four years and nothing but love continues to emanates from the wood burning stove. \xa0Even as a single I had to wait more than 45 minutes last night in the windy night. \xa0Hey Jack and Envie beer helped ease the passage of time as I headed back to a seat in the chef's section. \xa0The mushroom salad was epic - a righteous mix of Kentucky mint, Italian parsley, bacon, and thinly sliced button mushrooms. \xa0I matched it with the pork shoulder and fried livers on toast because I couldn't choose between the entrees.The staff is fantastic and the space, as always, has a great warm vibe.""""
s = "It's been more than four years and nothing but love continues to emanates from the wood burning stove. \xa0Even as a single I had to wait more than 45 minutes last night in the windy night. \xa0Hey Jack and Envie beer helped ease the passage of time as I headed back to a seat in the chef's section. \xa0The mushroom salad was epic - a righteous mix of Kentucky mint, Italian parsley, bacon, and thinly sliced button mushrooms. \xa0I matched it with the pork shoulder and fried livers on toast because I couldn't choose between the entrees.The staff is fantastic and the space, as always, has a great warm vibe."
re.sub('\\xa0','',s)
printReview(res[1][0])
for r in res:
    printReview(r[0])
    
def find_nns(self, rev, typ="hash", bucket=None):
    assert typ.lower() in ['hash', 'bf'] 
    sims = []
    if typ=="hash":
        assert bucket in self.buckets
        neighbors = self.buckets[bucket]
    else: neighbors = self.da_all.m_reviews
    for idx,n in tqdm(enumerate(neighbors)):
            sims.append((idx, sparse_cos_sim(n, rev)))
    sims = sorted(sims, key=lambda x:x[0], reverse=True)
    return [(neighbors[idx],sim) for idx,sim in enumerate(sims)[:self.k]]
def find_nns(self, rev, typ="hash", bucket=None):
    ti = time.time()
    assert typ.lower() in ['hash', 'bf'] 
    sims = []
    if typ=="hash":
        assert bucket in self.buckets
        neighbors = self.buckets[bucket]
    else: neighbors = self.da_all.m_reviews
    for idx,n in tqdm(enumerate(neighbors)):
            sims.append((idx, sparse_cos_sim(n, rev)))
    sims = sorted(sims, key=lambda x:x[0], reverse=True)
    retlist = [(neighbors[idx],sim) for idx,sim in enumerate(sims)[:self.k]]
    dt = time.time()-ti
    return retlist
def find_nns(da, rev, typ="hash", bucket=None):
    ti = time.time()
    assert typ.lower() in ['hash', 'bf'] 
    sims = []
    if typ=="hash":
        assert bucket in da.buckets
        neighbors = da.buckets[bucket]
    else: neighbors = da.da_all.m_reviews
    for idx,n in tqdm(enumerate(neighbors)):
            sims.append((idx, sparse_cos_sim(n, rev)))
    sims = sorted(sims, key=lambda x:x[0], reverse=True)
    retlist = [(neighbors[idx],sim) for idx,sim in enumerate(sims)[:da.k]]
    dt = time.time()-ti
    return retlist
def find_nns(knn, rev, typ="hash", bucket=None):
    ti = time.time()
    assert typ.lower() in ['hash', 'bf'] 
    sims = []
    if typ=="hash":
        if not bucket:
            bucket = knn.hashRev(rev, addToBucket=False)
        neighbors = knn.buckets[bucket]
    else: neighbors = knn.da_all.m_reviews
    for idx,n in tqdm(enumerate(neighbors)):
            sims.append((idx, sparse_cos_sim(n, rev)))
    sims = sorted(sims, key=lambda x:x[0], reverse=True)
    retlist = [(neighbors[idx],sim) for idx,sim in enumerate(sims)[:knn.k]]
    dt = time.time()-ti
    return retlist
res = find_nns(knn, queries[0])
def find_nns(knn, rev, typ="hash", bucket=None):
    ti = time.time()
    assert typ.lower() in ['hash', 'bf'] 
    sims = []
    if typ=="hash":
        if not bucket:
            bucket = knn.hashRev(rev, addToBucket=False)
        neighbors = knn.buckets[bucket]
    else: neighbors = knn.da_all.m_reviews
    for idx,n in enumerate(tqdm(neighbors)):
            sims.append((idx, sparse_cos_sim(n, rev)))
    sims = sorted(sims, key=lambda x:x[0], reverse=True)
    retlist = [(neighbors[idx],sim) for idx,sim in enumerate(sims[:knn.k])]
    dt = time.time()-ti
    return retlist
res = find_nns(knn, queries[0])
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/knn.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
def find_nns(knn, rev, typ="hash", bucket=None):
    ti = time.time()
    assert typ.lower() in ['hash', 'bf'] 
    sims = []
    if typ=="hash":
        if not bucket:
            bucket = knn.hashRev(rev, addToBucket=False)
        neighbors = knn.buckets[bucket]
    else: neighbors = knn.da_all.m_reviews
    for idx,n in enumerate(tqdm(neighbors)):
            sims.append((idx, sparse_cos_sim(n, rev)))
    sims = sorted(sims, key=lambda x:x[0], reverse=True)
    retlist = [(neighbors[idx],sim) for idx,sim in enumerate(sims[:knn.k])]
    dt = time.time()-ti
    return retlist, dt
res, dt= find_nns(knn, queries[0])
dt
dts = []
for q in queries:
    res, dt = find_nns(knn, q)
    dts.append(dt)
    
np.mean(dts)
for q in queries:
    res, dt = find_nns(knn, q)
    dts.append(dt)
    
np.mean(dts)
for q in queries:
    res, dt = find_nns(knn, q)
    dts.append(dt)
    
for q in queries:
    res, dt = find_nns(knn, q, typ='bf')
    dts.append(dt)
    
np.mean(dts)
np.mean(dts[-5:])
dts = []
del(dts)
dts = []
bf_idx = [[] for i in range(5)]
approx_idx = [[] for i in range(5)]
bf_dts = []
for i,q in enumerate(queries):
    res_bf, dt = find_nns(knn, q, typ='bf')
    bf_dts.append(dt)
    bf_idx[i] = [r[0] for r in res]
    
bf_idx
bf_dts
np.mean(bf_dts)
for i,q in enumerate(queries):
    res_bf, dt = find_nns(knn, q)
    dts.append(dt)
    approx_idx[i] = [r[0] for r in res]
    
np.mean(dts)
approx_ids = [[rev.id for rev in res] for res in approx_idx]
approx_ids
bf_ids = [[rev.id for rev in res] for res in bf_idx]
comp = zip(approx_ids, bf_ids)
comp[0]
for app, bf in comp:
    sim = set(app).intersection(set(bf))
    print('matches: {}'.format(len(sim)))
    
approx_idx
approx_ids = []
for res in approx_idx:
    res_ids = []
    for r in res:
        res_ids.append(r.id)
    approx_ids.append(res_ids)
    
approx_ids
dts = []
bf_idx = [[] for i in range(5)]
approx_idx = [[] for i in range(5)]
bf_dts = []
for i,q in enumerate(queries):
    res_bf, dt = find_nns(knn, q, typ='bf')
    bf_dts.append(dt)
    bf_idx[i] = [r[0] for r in res_bf]
    
bf_ids = [[rev.id for rev in res] for res in bf_idx]
bf_ids[0]
bf_ids[1]
res = find_nns(knn, queries[3])
res[0]
res = find_nns(knn, queries[2])
res[0]
ap_idx = []
ap_dts = []
for i,q in enumerate(queries):
    res = find_nns(knn,q)
    res_ids = [r[0].id for r in res[0]]
    app_idx.append(res_ids)
    ap_dts.append(res[1])
    
for i,q in enumerate(queries):
    res = find_nns(knn,q)
    res_ids = [r[0].id for r in res[0]]
    ap_idx.append(res_ids)
    ap_dts.append(res[1])
    
ap_idx
bf_idx, bf_dts = [],[]
np.mean(ap_dts)
for i,q in enumerate(queries):
    res = find_nns(knn,q, type="bf")
    res_ids = [r[0].id for r in res[0]]
    bf_idx.append(res_ids)
    bf_dts.append(res[1])
    
for i,q in enumerate(queries):
    res = find_nns(knn,q, typ="bf")
    res_ids = [r[0].id for r in res[0]]
    bf_idx.append(res_ids)
    bf_dts.append(res[1])
    
bf_idx
for i,q in enumerate(queries):
    res = find_nns(knn,q, type="bf")
    res_ids = [r[0].id for r in res[0]]
    bf_idx.append(res_ids)
    bf_dts.append(res[1])
    
res = find_nns(knn,queries[3], typ="bf")
res[0]
res3 = res
del(res)
res2 = find_nns(knn,queries[2], typ="bf")
res2[0]
printReview(queries[2])
for r in res2[0]:
    printReview(r[0])
    
res2_ap = find_nns(knn, queries[2])
for r in res2_ap:
    printReview(r[0])
    
for r in res2_ap[0]:
    printReview(r[0])
    
queries[2]
printReview(queries[2])
res2_ap = find_nns(knn, queries[2])
m1 = res2_ap[0][0]
m1
m1 = res2_ap[0][0][0]
m1
m2 = res2_ap[0][1][0]
sparse_cos_sim(m1,queries[2])
res = searchReviews(da, ['tacos'],['pico'])
res = searchReviews(da, ['tacos','pico'])
term_matches = [1378, 1379, 1384, 1389, 1400, 1407, 1408, 1420, 1427, 1429, 1431, 1437, 1446, 1466, 1500, 1501, 1502, 1518, 1531, 1534, 1550, 1571, 1593, 1601, 1612, 1614, 1615, 1618, 1620, 1622]
sims = [sparse_cos_sim(da.m_reviews[t],queries[2]) for t in term_matches]
sims
res2
sims = [r[1][1] for r in res2]
posts, stast = zip(*res2)
res2[0]
res2[1]
posts, stast = zip(*res2[0])
posts
stats
stats = stast
stats
max(sims)
rev = queries[2]
typ="hash"
bucket = None
sims = []
if typ=="hash":
    if not bucket:
        bucket = knn.hashRev(rev, addToBucket=False)
    neighbors = knn.buckets[bucket]
else: neighbors = knn.da_all.m_reviews

for idx,n in enumerate(tqdm(neighbors)):
        sims.append((idx, sparse_cos_sim(n, rev)))
typ="bf"
sims = []
if typ=="hash":
    if not bucket:
        bucket = knn.hashRev(rev, addToBucket=False)
    neighbors = knn.buckets[bucket]
else: neighbors = knn.da_all.m_reviews

for idx,n in enumerate(tqdm(neighbors)):
        sims.append((idx, sparse_cos_sim(n, rev)))
sims = sorted(sims, key=lambda x:x[1], reverse=True)
sims[:5]
printReview(da.m_reviews[1429])
def find_nns(knn, rev, typ="hash", bucket=None):
    ti = time.time()
    assert typ.lower() in ['hash', 'bf'] 
    sims = []
    if typ=="hash":
        if not bucket:
            bucket = knn.hashRev(rev, addToBucket=False)
        neighbors = knn.buckets[bucket]
    else: neighbors = knn.da_all.m_reviews
    for idx,n in enumerate(tqdm(neighbors)):
            sims.append((idx, sparse_cos_sim(n, rev)))
    sims = sorted(sims, key=lambda x:x[1], reverse=True)
    retlist = [(neighbors[idx],sim) for idx,sim in enumerate(sims[:knn.k])]
    dt = time.time()-ti
    return retlist, dt
q = queries[0]
ap_res = find_nns(knn,q)
res_ids = [r[1][0].id for r in ap_res[1]]
ap_res[1]
res_ids = [r[1][0].id for r in ap_res[0]]
res[0]
res[1]
res
ap_res[0]
ap_res[0][0]
ap_res[0][0][0]
ap_res[0][0][1]
def find_nns(knn, rev, typ="hash", bucket=None):
    ti = time.time()
    assert typ.lower() in ['hash', 'bf'] 
    sims = []
    if typ=="hash":
        if not bucket:
            bucket = knn.hashRev(rev, addToBucket=False)
        neighbors = knn.buckets[bucket]
    else: neighbors = knn.da_all.m_reviews
    for idx,n in enumerate(tqdm(neighbors)):
            sims.append((idx, sparse_cos_sim(n, rev)))
    sims = sorted(sims, key=lambda x:x[1], reverse=True)
    retlist = sims[:knn.k]
    dt = time.time()-ti
    return retlist, dt
ap_res = find_nns(knn,q)
ap_res
bf_res = find_nns(knn,q,typ="bf")
bf_res
bf_results = []
ap_results = []
for q in queries:
    bf_res = find_nns(knn,q,typ="bf")
    bf_results.append(bf_res[0])
    ap_res = find_nns(knn,q)
    ap_results.append(ap_res[0])
    
comb = zip(bf_results,ap_results)
comb
for c in comb:
    print c
    
for c in comb:
    print c + '\n'
    
for c in comb:
    print str(c) + '\n'
    
printRev = printReview
for bf, ap in comb:
    b_mean = np.mean([r[1] for r in bf])
    ap_mean = np.mean([r[1] for r in ap])
    print('bf_mean: {} | ap_mean: {}
for bf, ap in comb:
    b_mean = np.mean([r[1] for r in bf])
    ap_mean = np.mean([r[1] for r in ap])
    print('bf_mean: {} | ap_mean: {}'.format(bf_mean,ap_mean))
    
for bf, ap in comb:
    bf_mean = np.mean([r[1] for r in bf])
    ap_mean = np.mean([r[1] for r in ap])
    print('bf_mean: {} | ap_mean: {}'.format(bf_mean,ap_mean))
    
printRev(da.m_reviews[32332])
queries[0]
printRev(queries[0])
da.m_reviews[18724]
printRev(18724)
printRev(da.m_reviews[18724])
printRev(da.m_reviews[1367])
def find_nns(knn, rev, typ="hash", bucket=None):
    assert typ.lower() in ['hash', 'bf'] 
    sims = []
    if typ=="hash":
        if not bucket:
            bucket = knn.hashRev(rev, addToBucket=False)
        neighbors = knn.buckets[bucket]
    else: neighbors = knn.da_all.m_reviews
    for idx,n in enumerate(tqdm(neighbors)):
            sims.append(n, sparse_cos_sim(n, rev))
    top_matches = sorted(sims, key=lambda x:x[1][1], reverse=True)
    reviews, sims = zip(*top_matches)[:5]
    return reviews, sims
revs, sims = find_nns(knn, queries[0])
assert typ.lower() in ['hash', 'bf'] 
sims = []
if typ=="hash":
    if not bucket:
        bucket = knn.hashRev(rev, addToBucket=False)
    neighbors = knn.buckets[bucket]
else: neighbors = knn.da_all.m_reviews

for idx,n in enumerate(tqdm(neighbors)):
        sims.append((n, sparse_cos_sim(n, rev))

top_matches = sorted(sims, key=lambda x:x[1][1], reverse=True)
reviews, sims = zip(*top_matches)[:5]
return reviews, sims
def find_nns(knn, rev, typ="hash", bucket=None):
    assert typ.lower() in ['hash', 'bf'] 
    sims = []
    if typ=="hash":
        if not bucket:
            bucket = knn.hashRev(rev, addToBucket=False)
        neighbors = knn.buckets[bucket]
    else: neighbors = knn.da_all.m_reviews
    for idx,n in enumerate(tqdm(neighbors)):
            sims.append((n, sparse_cos_sim(n, rev)))
    top_matches = sorted(sims, key=lambda x:x[1][1], reverse=True)
    reviews, sims = zip(*top_matches)[:5]
    return reviews, sims
revs, sims = find_nns(knn, queries[0])
rev = queries[0]
if typ=="hash":
    if not bucket:
        bucket = knn.hashRev(rev, addToBucket=False)
    neighbors = knn.buckets[bucket]
else: neighbors = knn.da_all.m_reviews

for idx,n in enumerate(tqdm(neighbors)):
        sims.append((n, sparse_cos_sim(n, rev)))

top_matches = sorted(sims, key=lambda x:x[1], reverse=True)
reviews, sims = zip(*top_matches)[:5]
printRev(reviews[0])
reviews
typ
typ = 'hash'
sims = []
if typ=="hash":
    if not bucket:
        bucket = knn.hashRev(rev, addToBucket=False)
    neighbors = knn.buckets[bucket]
else: neighbors = knn.da_all.m_reviews

for idx,n in enumerate(tqdm(neighbors)):
        sims.append((n, sparse_cos_sim(n, rev)))

top_matches = sorted(sims, key=lambda x:x[1], reverse=True)
top_matches[:5]
reviews, sims = zip(*top_matches)[:5]
reviews
top_matches = sorted(sims, key=lambda x:x[1], reverse=True)
top_matches = top_matches[:5]
reviews, sims = zip(*top_matches)
sims = []
if typ=="hash":
    if not bucket:
        bucket = knn.hashRev(rev, addToBucket=False)
    neighbors = knn.buckets[bucket]
else: neighbors = knn.da_all.m_reviews

for idx,n in enumerate(tqdm(neighbors)):
        sims.append((n, sparse_cos_sim(n, rev)))
sims[0]
top_matches = sorted(sims, key=lambda x:x[1], reverse=True)
top_matches = top_matches[:5]
reviews, sims = zip(*top_matches)
reviews
sims
del(reviews, sims, top_matches)
import gc
gc.collect()
def find_nns(knn, rev, typ="hash", bucket=None):
    assert typ.lower() in ['hash', 'bf'] 
    sims = []
    if typ=="hash":
        if not bucket:
            bucket = knn.hashRev(rev, addToBucket=False)
        neighbors = knn.buckets[bucket]
    else: neighbors = knn.da_all.m_reviews
    for idx,n in enumerate(tqdm(neighbors)):
            sims.append((n, sparse_cos_sim(n, rev)))
    top_matches = sorted(sims, key=lambda x:x[1], reverse=True)
    top_matches = top_matches[:5]
    reviews, sims = zip(*top_matches)
    return reviews, sims
res = find_nns(knn, queries[0])
revs, sims = res
for r in revs:
    printReview(r)
    
printRev(queries[0])
res = find_nns(knn, queries[0], typ="bf")
revs, sims = res
for r in revs:
    printRev(r)
    
revs[0].vec
queries[0].vec
del(da)
gc.collect()
da = DocAnalyzer()
da.loadDir('yelp/test', debug=True)
da.loadDir('yelp/test')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/knn.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = DocAnalyzer()
tr_f = os.listdir('yelp/train')
sub = tr_f[:5]
da.loadDir('yelp/train', sublist=sub)
da.filter_vocab(10)
da.setFinalVocab()
da.setVecs()
res = setVecs_parallel(da.m_reviews[:100], da, nc=3)
res[0].vec
knn.classify(queries[0])
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/knn.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
knn = KNN(da)
knn.setHashes()
knn.train()
da.filter_vocab()
da.filter_vocab(10)
da = filter_vocab(da,10)
del(da)
da = load_obj('da_hw3')
knn = KNN(da)
knn.setHashes()
knn.train()
queries[0].vec
queries = readQueries()
queries = [post(q) for q in queries]
for q in queries:
    q.tokens = textToGrams(da,q.content)
    q.setVec(da)
    
def classify(knn,rev):
    bucket = knn.hashRev(rev, addToBucket=False)
    closest = knn.find_nns(rev,bucket=bucket)
    neighbors, sims = zip(*closest)
    votes = [0,0]
    for n in neighbors:
        votes[n.sent] +=1
    return np.argmax(votes)
res = classify(knn,queries[0])
bucket = knn.hashRev(rev, addToBucket=False)
closest = knn.find_nns(rev,bucket=bucket)
rev = queries[0]
bucket = knn.hashRev(rev, addToBucket=False)
closest = knn.find_nns(rev,bucket=bucket)

closest
neighbors, sims = zip(*closest)
neighbors, sims = closest[0],closest[1]
neighbors
neighbors, sims = closest
def classify(knn,rev):
    bucket = knn.hashRev(rev, addToBucket=False)
    closest = knn.find_nns(rev,bucket=bucket)
    neighbors, sims = closest
    votes = [0,0]
    for n in neighbors:
        votes[n.sent] +=1
    return np.argmax(votes)
classify(knn, queries[0])
from sklearn.metrics import *
preds = [knn.classify(r) for r in da.m_reviews[:100]]
preds = [classify(knn,r) for r in da.m_reviews[:100]]
labels = [r.sent for r in da.m_reviews[:100]]
pred_labels = [1 if p > 0 else 0 for p in preds]
pred_labels[:5]
labels[:5]
cm = confusion_matrix(labels,pred_labels)
cm
prec = precision_score(labels,pred_labels)
prec
recall = recall_score(labels,pred_labels)
recall
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/knn.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
knn = KNN(da)
knn.setHashes()
knn.train()
knn.classify(queries[0])
def getFoldData(da,k=10, l=5, knn_k=5, val=False): 
    if "folds" not in da.__dict__.keys():
        da.makeFolds(k)
    fData = {'folds':{i:{'trainDA':None,'testDA':None,'preds':None} for i in range(k)}}
    if val:
        da_validation = da.copy()
        vsize = int(.05 * len(da.m_articles))
        da_validation.m_articles = np.random.choice(da.m_articles, size=(vsize), replace=False)
        remaining_articles = set(da.m_articles).difference(set(da_validation.m_articles))
        da.m_articles = list(remaining_articles)
        fData['da_val'] = da_validation
    
    for f_idx,fold in enumerate(da.folds):
        tr_folds = range(k)
        if k > 1: tr_folds.pop(f_idx)
        tr_inds = []
        for ind in tr_folds: tr_inds += da.folds[ind]
        tst_inds = fold
        #build training sets (DocAnalyzers)
        da_train = da.copy()
        da_train.m_articles = [da.m_articles[i] for i in tr_inds]
        #build test sets (DocAnalyzers)
        da_test = da.copy()
        da_test.m_articles = [da.m_articles[j] for j in tst_inds]
        fData['folds'][f_idx] = {'trainDA':da_train,'testDA':da_test,'preds':[]}
    return fData
fData = getFoldData(da)
def makeFolds(da, k=5):
    inds = range(len(da.m_reviews))
    #np.random.shuffle(inds)
    da.folds = [[] for i in range(k)]
    for ind in inds:
        f = np.random.choice(range(k))
        da.folds[f].append(ind)
    return da
da = makeFolds(da, k=10)
da.folds[0]
da.mgnls['df'][0]
k=10
debug=False
delta = .1
l=5
knn_k=5
val = False
fdata = None
if debug: da.m_articles = da.m_articles[:20]

if fdata: fData = fdata
else: fData = getFoldData(da,k, val=False)

toIdx = da.getTagToIdx()
n = len(toIdx)
if debug: da.m_articles = da.m_articles[:20]
if fdata: fData = fdata
if fdata: fData = fdata
else: fData = getFoldData(da,k, val=False)
da2 = DocAnalyzer()
da2.__dict__ = {k:v for k,v in da.__dict__.items()}
da3 = da2.copy()
del(da3)
del(da)
da = da2
del(da2)
if debug: da.m_articles = da.m_articles[:20]

if fdata: fData = fdata
else: fData = getFoldData(da,k, val=False)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/eval.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
if debug: da.m_reviews = da.m_reviews[:20]

if fdata: fData = fdata
else: fData = getFoldData(da,k, val=False)

toIdx = da.getTagToIdx()
n = len(toIdx)
fData = getFoldData(da,k, val=False)
da.copy()
da_2 = DocAnalyzer()
da2.__dict__ = {k:v for k,v in da.__dict__.items()}
da_2.__dict__ = {k:v for k,v in da.__dict__.items()}
del(da)
da3 = da_2.copy()
da = da3
da = da_2.copy()
del(da_2)
del(da_3)
del(da3)
da2 = da.copy()
del(da2)
fData = getFoldData(da,k, val=False)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/nb.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
fdata[0]
fData[0]
fData.__dict__.keys()
fData.keys()
fData['folds'].keys()
fData['folds'][0].keys()
def kfoldCV(da,k=10, debug=False,delta=.1,l=5, knn_k=5, val=False, fdata=None):
    if debug: da.m_reviews = da.m_reviews[:20]
    if fdata: fData = fdata
    else: fData = getFoldData(da,k, val=False)
    k_preds, nb_preds, true_lbls = [],[], []
    for f_idx, fold in tqdm(fData['folds'].items()):
        #create models based only on fold data
        knn = KNN(fold['trainDA'],k=knn_k,l=l)
        knn.setHashes()
        knn.train()       
        nb = NB(fold['trainDA'], delta=delta)
        if fold['testDA']: da_test = fold['testDA']
        else: da_test = da['da_val']       
        for rev in da_test.m_reviews:
            k_preds.append(knn.classify(rev))
            nb_preds.append(nb.classify(rev))
            true_lbls.append(rev.sent)              
    return k_preds, nb_preds, true_lbls
kp,np,tl = kfoldCV(da,debug=True)
kp,np,tl = kfoldCV(da,debug=True,fdata=fData)
import numpy as np
kp,np,tl = kfoldCV(da,debug=True,fdata=fData)
del(np)
kp,np,tl = kfoldCV(da,debug=True,fdata=fData)
debug=True
fdata=fData
if debug: da.m_reviews = da.m_reviews[:20]

if fdata: fData = fdata
else: fData = getFoldData(da,k, val=False)

k_preds, nb_preds, true_lbls = [],[], []
f_idx, fold = fData['folds'].items()[0]
knn = KNN(fold['trainDA'],k=knn_k,l=l)
knn.setHashes()
fold['trainDA']
da = DocAnalyzer()
da = load_obj('da_hw3_knn')
da = load_obj('da_hw3')
def setHashes(knn):
    for i in range(knn.l):
        knn.hashfn[i] = {k:np.random.uniform(-1,1) for k in knn.da_all.empty_vec.keys()}
    return knn
knn = setHashes(knn)
import numpy as np
knn = setHashes(knn)
knn.train()
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/eval.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = load_obj('da_hw3')
if debug: da.m_reviews = da.m_reviews[:20]

if fdata: fData = fdata
else: fData = getFoldData(da,k, val=False)
da_2 = da.copy()
k=10
delta=.1
l=5
knn_k=5
val=False
fdata=None
if debug: da.m_reviews = da.m_reviews[:20]

if fdata: fData = fdata
else: fData = getFoldData(da,k, val=False)

k_preds, nb_preds, true_lbls = [],[], []
debug=True
if debug: da.m_reviews = da.m_reviews[:20]

if fdata: fData = fdata
else: fData = getFoldData(da,k, val=False)

k_preds, nb_preds, true_lbls = [],[], []
f_idx, fold = fData['folds'].items()[0]
knn = KNN(fold['trainDA'],k=knn_k,l=l)
knn = setHashes(knn)
knn.train()
nb = NB(fold['trainDA'], delta=delta)
if fold['testDA']: da_test = fold['testDA']
for rev in da_test.m_reviews:
    k_preds.append(knn.classify(rev))
    nb_preds.append(nb.classify(rev))
    true_lbls.append(rev.sent)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/nb.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
nb = NB(fold['trainDA'], delta=delta)
for rev in da_test.m_reviews:
    k_preds.append(knn.classify(rev))
    nb_preds.append(nb.classify(rev))
    true_lbls.append(rev.sent)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/eval.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
if debug: da.m_reviews = da.m_reviews[:20]

if fdata: fData = fdata
else: fData = getFoldData(da,k, val=False)

k_preds, nb_preds, true_lbls = [],[], []
for f_idx, fold in tqdm(fData['folds'].items()):
    #create models based only on fold data
    knn = KNN(fold['trainDA'],k=knn_k,l=l)
    knn = setHashes(knn)
    knn.train()       
    nb = NB(fold['trainDA'], delta=delta)
    if fold['testDA']: da_test = fold['testDA']
    else: da_test = da['da_val']
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/eval.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = load_obj('da_hw3')
k=10
debug=False
delta=.1
l=5
knn_k=5
val=False
fdata=None
if debug: da.m_reviews = da.m_reviews[:20]

if fdata: fData = fdata
else: fData = getFoldData(da,k, val=False)

k_preds, nb_preds, true_lbls = [],[], []
f_idx, fold = fData['folds'].items()[0]
knn = KNN(fold['trainDA'],k=knn_k,l=l)
knn = setHashes(knn)
knn.train()
nb = NB(fold['trainDA'], delta=delta)
if fold['testDA']: da_test = fold['testDA']
for rev in da_test.m_reviews:
    k_preds.append(knn.classify(rev))
    nb_preds.append(nb.classify(rev))
    true_lbls.append(rev.sent)
da_test.m_reviews = da_test.m_reviews[:200]
for rev in da_test.m_reviews:
    k_preds.append(knn.classify(rev))
    nb_preds.append(nb.classify(rev))
    true_lbls.append(rev.sent)
from sklearn.metrics import *
nb_prec = precision_score(true_lbls,nb_preds)
nb_prec
def evalPreds(true_labels, pred_labels):
    prec = precision_score(true_labels, pred_labels)
    recall = recall_score(true_labels, pred_labels)
    f1 = f1_score(true_labels, pred_labels)
    return prec,recall,f1
p,r,f = evalPreds(true_lbls, nb_preds)
p,r,f
p,r,f = evalPreds(true_lbls, knn_preds)
p,r,f = evalPreds(true_lbls, k_preds)
p,r,f
def kfoldCV(da,k=10, debug=False,delta=.1,l=5, knn_k=5, val=False, fdata=None):
    if debug: da.m_reviews = da.m_reviews[:20]
    if fdata: fData = fdata
    else: fData = getFoldData(da,k, val=False)
    k_preds, nb_preds, true_lbls = [],[], []
    for f_idx, fold in tqdm(fData['folds'].items()):
        #create models based only on fold data
        knn = KNN(fold['trainDA'],k=knn_k,l=l)
        knn = setHashes(knn)
        knn.train()       
        nb = NB(fold['trainDA'], delta=delta)
        if fold['testDA']: da_test = fold['testDA']
        else: da_test = da['da_val'] 
        if debug: da_test.m_reviews = da_test.m_reviews[:50]
        for rev in da_test.m_reviews:
            k_preds.append(knn.classify(rev))
            nb_preds.append(nb.classify(rev))
            true_lbls.append(rev.sent)              
    return k_preds, nb_preds, true_lbls
kp,np,tl = kfoldCV(da, debug=True)
da = load_obj('da_hw3')
da2 = da.copy()
def kfoldCV(da,k=10, debug=False,delta=.1,l=5, knn_k=5, val=False, fdata=None):
    if fdata: fData = fdata
    else: fData = getFoldData(da,k, val=False)
    k_preds, nb_preds, true_lbls = [],[], []
    for f_idx, fold in tqdm(fData['folds'].items()):
        #create models based only on fold data
        knn = KNN(fold['trainDA'],k=knn_k,l=l)
        knn = setHashes(knn)
        knn.train()       
        nb = NB(fold['trainDA'], delta=delta)
        if fold['testDA']: da_test = fold['testDA']
        else: da_test = da['da_val'] 
        if debug: da_test.m_reviews = da_test.m_reviews[:50]
        for rev in da_test.m_reviews:
            k_preds.append(knn.classify(rev))
            nb_preds.append(nb.classify(rev))
            true_lbls.append(rev.sent)              
    return k_preds, nb_preds, true_lbls
res = kfoldCV(da, debug=True)
res
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/eval.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
def kfoldCV(da,k=10, debug=False,delta=.1,l=5, knn_k=5, val=False, fdata=None):
    if fdata: fData = fdata
    else: fData = getFoldData(da,k, val=False)
    k_preds, nb_preds, true_lbls = [],[], []
    for f_idx, fold in tqdm(fData['folds'].items()):
        #create models based only on fold data
        knn = KNN(fold['trainDA'],k=knn_k,l=l)
        knn = setHashes(knn)
        knn.train()       
        nb = NB(fold['trainDA'], delta=delta)
        if fold['testDA']: da_test = fold['testDA']
        else: da_test = da['da_val'] 
        if debug: da_test.m_reviews = da_test.m_reviews[:10]
        for rev in da_test.m_reviews:
            k_preds.append(knn.classify(rev))
            nb_preds.append(nb.classify(rev))
            true_lbls.append(rev.sent)              
    return k_preds, nb_preds, true_lbls
res = kfoldCV(da, debug=True)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/eval.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = load_obj('da_hw3')
res = kfoldCV(da, debug=True)
k_preds, nb_preds, true_lbls = res
prec,recall,f1 = evalPreds(true_lbls,nb_preds)
nb_res = evalPreds(true_lbls,nb_preds)
nb_res
knn_res = evalPreds(true_lbls,k_preds)
knn_res
def kfoldCV2(da,k=10, debug=False,delta=.1,l=5, knn_k=5, val=False, fdata=None, par=False):
    if fdata: fData = fdata
    else: fData = getFoldData(da,k, val=False)
    k_preds, nb_preds, true_lbls = [],[], []
    if parallel:
        pool = mp.Pool(processes=k)
        recs = [pool.apply_async(getFoldPreds, args=(f_idx,fold,knn_k,l))\
                for f_idx,fold in enumerate(fData['folds'].items())]
        recs = [r.get() for r in recs]    
        recs_coll = []
        for r in recs: recs_coll +=r
        k_preds, nb_preds, true_lbls = zip(*recs_coll)
    else:
        for f_idx, fold in tqdm(fData['folds'].items()):
            #create models based only on fold data
            kp,np,tl = getFoldPreds(f_idx,fold,knn_k,l)
            k_preds += kp
            nb_preds += np
            true_lbls += tl 
    return k_preds, nb_preds, true_lbls
def getFoldPreds(f_idx,fold,knn_k=5,l=5, debug=False):
    knn = KNN(fold['trainDA'],k=knn_k,l=l)
    knn = setHashes(knn)
    knn.train()       
    nb = NB(fold['trainDA'], delta=delta)
    if fold['testDA']: da_test = fold['testDA']
    if debug: da_test.m_reviews = da_test.m_reviews[:10]
    k_preds,nb_preds,true_lbls = [],[],[]
    for rev in da_test.m_reviews:
        k_preds.append(knn.classify(rev))
        nb_preds.append(nb.classify(rev))
        true_lbls.append(rev.sent)
    return k_preds, nb_preds, true_lbls
def kfoldCV2(da,k=10, debug=False,delta=.1,l=5, knn_k=5, val=False, fdata=None, par=False):
    if fdata: fData = fdata
    else: fData = getFoldData(da,k, val=False)
    k_preds, nb_preds, true_lbls = [],[], []
    if parallel:
        pool = mp.Pool(processes=k)
        recs = [pool.apply_async(getFoldPreds, args=(f_idx,fold,knn_k,l))\
                for f_idx,fold in enumerate(fData['folds'].items())]
        recs = [r.get() for r in recs]    
        recs_coll = []
        for r in recs: recs_coll +=r
        k_preds, nb_preds, true_lbls = zip(*recs_coll)
    else:
        for f_idx, fold in tqdm(fData['folds'].items()):
            #create models based only on fold data
            kp,np,tl = getFoldPreds(f_idx,fold,knn_k,l)
            k_preds += kp
            nb_preds += np
            true_lbls += tl 
    return k_preds, nb_preds, true_lbls
res = kfoldCV2(da,par=True)
def kfoldCV2(da,k=10, debug=False,delta=.1,l=5, knn_k=5, val=False, fdata=None, par=False):
    if fdata: fData = fdata
    else: fData = getFoldData(da,k, val=False)
    k_preds, nb_preds, true_lbls = [],[], []
    if par:
        pool = mp.Pool(processes=k)
        recs = [pool.apply_async(getFoldPreds, args=(f_idx,fold,knn_k,l))\
                for f_idx,fold in enumerate(fData['folds'].items())]
        recs = [r.get() for r in recs]    
        recs_coll = []
        for r in recs: recs_coll +=r
        k_preds, nb_preds, true_lbls = zip(*recs_coll)
    else:
        for f_idx, fold in tqdm(fData['folds'].items()):
            #create models based only on fold data
            kp,np,tl = getFoldPreds(f_idx,fold,knn_k,l)
            k_preds += kp
            nb_preds += np
            true_lbls += tl 
    return k_preds, nb_preds, true_lbls
res = kfoldCV2(da,par=True)
def getFoldPreds(f_idx,fold,knn_k=5,l=5, debug=False):
    knn = KNN(fold['trainDA'],k=knn_k,l=l)
    knn = setHashes(knn)
    knn.train()       
    nb = NB(fold['trainDA'], delta=delta)
    if fold['testDA']: da_test = fold['testDA']
    if debug: da_test.m_reviews = da_test.m_reviews[:10]
    k_preds,nb_preds,true_lbls = [],[],[]
    for rev in da_test.m_reviews:
        k_preds.append(knn.classify(rev))
        nb_preds.append(nb.classify(rev))
        true_lbls.append(rev.sent)
    return zip(k_preds, nb_preds, true_lbls)
res = kfoldCV2(da,par=True)
if fdata: fData = fdata
else: fData = getFoldData(da,k, val=False)

k_preds, nb_preds, true_lbls = [],[], []
if par:
    pool = mp.Pool(processes=k)
    recs = [pool.apply_async(getFoldPreds, args=(f_idx,fold,knn_k,l))\
            for f_idx,fold in enumerate(fData['folds'].items())]
fdata=None
par=True
val=False
if fdata: fData = fdata
else: fData = getFoldData(da,k, val=False)

k_preds, nb_preds, true_lbls = [],[], []
if par:
    pool = mp.Pool(processes=k)
    recs = [pool.apply_async(getFoldPreds, args=(f_idx,fold,knn_k,l))\
            for f_idx,fold in enumerate(fData['folds'].items())]
k=10
debug=True
delta=.1
l=5
knn_k=5
val=False
def kfoldCV(da,k=10, debug=False,delta=.1,l=5, knn_k=5, val=False, fdata=None):
    if fdata: fData = fdata
    else: fData = getFoldData(da,k, val=False)
    k_preds, nb_preds, true_lbls = [],[], []
    for f_idx, fold in tqdm(fData['folds'].items()):
        #create models based only on fold data
        knn = KNN(fold['trainDA'],k=knn_k,l=l)
        knn = setHashes(knn)
        knn.train()       
        nb = NB(fold['trainDA'], delta=delta)
        if fold['testDA']: da_test = fold['testDA']
        else: da_test = da['da_val'] 
        if debug: da_test.m_reviews = np.random.choice(da_test.m_reviews, size=75, replace=False)
        for rev in da_test.m_reviews:
            k_preds.append(knn.classify(rev))
            nb_preds.append(nb.classify(rev))
            true_lbls.append(rev.sent)              
    return k_preds, nb_preds, true_lbls
res = kfoldCV(da, debug=True)
res[:5]
metrics = evalPreds(res[1],res[0])
nb_mets = metrics
knn_mets = nb_mets
knn_preds = evalPreds(res[0],res[2])
nb_mets = evalPreds(res[1],res[2])
knn_mets = knn_preds
knn_mets
nb_mets
l = ['a','b']
l[4] = 23
def kfoldCV(da,k=10, debug=False,delta=.1,l=5, knn_k=5, val=False, fdata=None):
    if fdata: fData = fdata
    else: fData = getFoldData(da,k, val=False)
    fold_results = {'knn':[],'nb':[]}
    for f_idx, fold in tqdm(fData['folds'].items()):
        #create models based only on fold data
        knn = KNN(fold['trainDA'],k=knn_k,l=l)
        knn = setHashes(knn)
        knn.train()       
        nb = NB(fold['trainDA'], delta=delta)
        if fold['testDA']: da_test = fold['testDA']
        else: da_test = da['da_val'] 
        if debug: da_test.m_reviews = np.random.choice(da_test.m_reviews, size=75, replace=False)
        knn_preds, nb_preds, true_lbls = [],[], []
        for rev in da_test.m_reviews:
            knn_preds.append(knn.classify(rev))
            nb_preds.append(nb.classify(rev))
            true_lbls.append(rev.sent)
        knn_perf = evalPreds(true_lbls,knn_preds)
        nb_perf = evalPreds(true_lbls,nb_preds)
        fold_results['knn'].append(knn_perf)
        fold_results['nb'].append(nb_perf)
    return fold_results
res = kfoldCV(da, debug=True)
res
diffs = [nb - knn for nb,knn in zip(res['nb'].values(),res['knn'].values())]
diffs = [nb - knn for nb,knn in zip(res['nb'],res['knn'])]
res['nb'][0]
nb_p = [r[0] for r in res['nb']]
nb_p[:2]
nb_r = [r[1] for r in res['nb']]
nb_f = [r[2] for r in res['nb']]
[np.mean(m) for m in (nb_p,nb_r,nb_f)]
knn_p = [r[0] for r in res['knn']]
knn_r = [r[1] for r in res['knn']]
knn_f = [r[2] for r in res['knn']]
[np.mean(m) for m in (knn_p,knn_r,knn_f)]
p_diffs = [k-p for (k,p) in zip(knn_p,nb_p)]
r_diffs = [k-p for (k,p) in zip(knn_r,nb_r)]
f_diffs = [k-p for (k,p) in zip(knn_f,nb_f)]
scipy.stats.ttest_1samp(f_diffs,0)
import scipy
scipy.stats.ttest_1samp(f_diffs,0)
scipy.stats.ttest_1samp(r_diffs,0)
scipy.stats.ttest_1samp(p_diffs,0)
res = {'f':[-9.49,5.5e-6],'r':[-4.17,.00239],'p':[-10.277],2.85e-6}
res = {'f':[-9.49,5.5e-6],'r':[-4.17,.00239],'p':[-10.277,2.85e-6]}
res
for k in res.items():
    print k
    
import math
math.log(len(da.m_reviews),2)
if fdata: fData = fdata
else: fData = getFoldData(da,k, val=False)

k_preds, nb_preds, true_lbls = [],[], []
if par:
    pool = mp.Pool(processes=k)
    recs = [pool.apply_async(getFoldPreds, args=(f_idx,fold,knn_k,l))\
            for f_idx,fold in enumerate(fData['folds'].items())]
k
del(k)
if fdata: fData = fdata
else: fData = getFoldData(da,k, val=False)

k_preds, nb_preds, true_lbls = [],[], []
if par:
    pool = mp.Pool(processes=k)
    recs = [pool.apply_async(getFoldPreds, args=(f_idx,fold,knn_k,l))\
            for f_idx,fold in enumerate(fData['folds'].items())]
    
k=10
if fdata: fData = fdata
else: fData = getFoldData(da,k, val=False)

k_preds, nb_preds, true_lbls = [],[], []
if par:
    pool = mp.Pool(processes=k)
    recs = [pool.apply_async(getFoldPreds, args=(f_idx,fold,knn_k,l))\
            for f_idx,fold in enumerate(fData['folds'].items())]
    
recs = [r.get() for r in recs]
def getFoldPreds(f_idx,fold,knn_k=5,l=5, debug=False):
    knn = KNN(fold['trainDA'],k=knn_k,l=l)
    knn = setHashes(knn)
    knn.train()       
    nb = NB(fold['trainDA'], delta=delta)
    predlist = []
    if fold['testDA']: da_test = fold['testDA']
    if debug: da_test.m_reviews = da_test.m_reviews[:10]
    #k_preds,nb_preds,true_lbls = [],[],[]
    for rev in da_test.m_reviews:
        kp = knn.classify(rev)
        nbp = nb.classify(rev)
        tl = rev.sent
        predlist.append((kp,nbp,tl))
    return 2
res = kfoldCV2(da,par=True,debug=True)

## ---(Fri Apr 20 09:13:58 2018)---
def getFoldPreds(f_idx,fold,knn_k=5,l=5, debug=False):
    knn = KNN(fold['trainDA'],k=knn_k,l=l)
    knn = setHashes(knn)
    knn.train()       
    nb = NB(fold['trainDA'], delta=delta)
    predlist = []
    if fold['testDA']: da_test = fold['testDA']
    if debug: da_test.m_reviews = da_test.m_reviews[:10]
    #k_preds,nb_preds,true_lbls = [],[],[]
    for rev in da_test.m_reviews:
        kp = knn.classify(rev)
        nbp = nb.classify(rev)
        tl = rev.sent
        predlist.append((kp,nbp,tl))
    return predlist
fData.keys()
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/eval.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = load_obj('da_hw3')
fData = getFoldData(da)
f_idx, fold = 0,fData['folds'][0]
res = getFoldPreds(f_idx,fold)
from nb import NB
res = getFoldPreds(f_idx,fold)
def getFoldPreds(f_idx,fold,knn_k=5,l=5, debug=False):
    knn = KNN(fold['trainDA'],k=knn_k,l=l)
    knn = setHashes(knn)
    knn.train()       
    nb = NB(fold['trainDA'])
    predlist = []
    if fold['testDA']: da_test = fold['testDA']
    if debug: da_test.m_reviews = da_test.m_reviews[:10]
    #k_preds,nb_preds,true_lbls = [],[],[]
    for rev in da_test.m_reviews:
        kp = knn.classify(rev)
        nbp = nb.classify(rev)
        tl = rev.sent
        predlist.append((kp,nbp,tl))
    return predlist
res = getFoldPreds(f_idx,fold)
def getFoldPreds(f_idx,fold,knn_k=5,l=5, debug=False):
    knn = KNN(fold['trainDA'],k=knn_k,l=l)
    knn = setHashes(knn)
    knn.train()       
    nb = NB(fold['trainDA'])
    predlist = []
    if fold['testDA']: da_test = fold['testDA']
    if debug: da_test.m_reviews = da_test.m_reviews[:10]
    #k_preds,nb_preds,true_lbls = [],[],[]
    for rev in tqdm(da_test.m_reviews):
        kp = knn.classify(rev)
        nbp = nb.classify(rev)
        tl = rev.sent
        predlist.append((kp,nbp,tl))
    return predlist
res = getFoldPreds(f_idx,fold,debug=True)
predlist
res
res = kfoldCV2(da,k=3,debug=True,par=True)
res = kfoldCV2(da,k=4,debug=True,par=True)
res = kfoldCV2(da,k=8,debug=True,par=True)
res = kfoldCV2(da,k=10,debug=True,par=True)

## ---(Fri Apr 20 13:03:36 2018)---
17000./60
283.33/60
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/eval.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
combos = pd.read_csv('combos.csv', index_col=None)
combos
l,k = combos.ix[:,'l'].tlist(), combox.ix[:,'k'].tolist()
l,k = combos.ix[:,['l']]].tlist(), combox.ix[:,'k'].tolist()
l,k = combos.ix[:,['l']].tlist(), combox.ix[:,'k'].tolist()
l,k = combos.ix[:,['l']].tolist(), combox.ix[:,'k'].tolist()
combos.ix[:,'l']
combos.ix[:,['l']]
combos.columns
combos.index
ftext = open('combox.csv', 'r').read()
ftext = open('combos.csv', 'r').read()
lines = ftext.split('\n')
lines
lsplits = lines.split('\r')
lsplits = ftext.split('\r')
lsplits
combos.ix[:,0]
combos.ix[:,0].tolist()
l = combos.ix[:,0].tolist()
k = combos.ix[:,1].tolist()
combos = zip(l,k)
combos
save_obj(combos, 'combos')
def kfoldCV(da,k=10, debug=False,delta=.1,l=5, knn_k=5, val=False, fdata=None,includeNB=True):
    if fdata: fData = fdata
    else: fData = getFoldData(da,k, val=False)
    fold_results = {'knn':[],'nb':[]}
    for f_idx, fold in fData['folds'].items():
        #create models based only on fold data
        knn = KNN(fold['trainDA'],k=knn_k,l=l)
        knn = setHashes(knn)
        knn.train()
        if includeNB: nb = NB(fold['trainDA'], delta=delta)
        if fold['testDA']: da_test = fold['testDA']
        else: da_test = da['da_val'] 
        if debug: da_test.m_reviews = np.random.choice(da_test.m_reviews, size=75, replace=False)
        knn_preds, nb_preds, true_lbls = [],[], []
        for rev in tqdm(da_test.m_reviews):
            knn_preds.append(knn.classify(rev))
            if includeNB: nb_preds.append(nb.classify(rev))
            true_lbls.append(rev.sent)
        knn_perf = evalPreds(true_lbls,knn_preds)
        if includeNB: nb_perf = evalPreds(true_lbls,nb_preds)
        fold_results['knn'] = (knn_perf)
        if includeNB: fold_results['nb'] = (nb_perf)
    return fold_results
cv_res = load_obj('kfold_all_l5_k5')
cv_res
def kfoldCV(da,k=10, debug=False,delta=.1,l=5, knn_k=5, val=False, fdata=None,includeNB=True):
    if fdata: fData = fdata
    else: fData = getFoldData(da,k, val=False)
    fold_results = {'knn':[],'nb':[]}
    for f_idx, fold in fData['folds'].items():
        #create models based only on fold data
        knn = KNN(fold['trainDA'],k=knn_k,l=l)
        knn = setHashes(knn)
        knn.train()
        if includeNB: nb = NB(fold['trainDA'], delta=delta)
        if fold['testDA']: da_test = fold['testDA']
        else: da_test = da['da_val'] 
        if debug: da_test.m_reviews = np.random.choice(da_test.m_reviews, size=75, replace=False)
        knn_preds, nb_preds, true_lbls = [],[], []
        for rev in tqdm(da_test.m_reviews):
            knn_preds.append(knn.classify(rev))
            if includeNB: nb_preds.append(nb.classify(rev))
            true_lbls.append(rev.sent)
        knn_perf = evalPreds(true_lbls,knn_preds)
        if includeNB: nb_perf = evalPreds(true_lbls,nb_preds)
        fold_results['knn'].append(knn_perf)
        if includeNB: fold_results['nb'].append(nb_perf)
    return fold_results
cv_res
def tune_params(da,kcv=10, debug=False):
    combos = load_obj('combos')
    runs = []
    for k,l in combos:
        cv_res = kfold_CV(da,l=l,k=kcv,knn_k=k, includeNB=False, debug=debug)
        precs, recs, fs = zip(*cv_res['knn'])
        runs.append((k,l,np.mean(precs),np.mean(recs),np.mean(fs)))
    res = sorted(runs, key=lambda x:x[4], reverse=True)
    return res
da
da = load_obj('da_hw3')
gc.collect()
import gf
res = tune_params(da,debug=True)
def tune_params(da,kcv=10, debug=False):
    combos = load_obj('combos')
    runs = []
    for k,l in combos:
        cv_res = kfoldCV(da,l=l,k=kcv,knn_k=k, includeNB=False, debug=debug)
        precs, recs, fs = zip(*cv_res['knn'])
        runs.append((k,l,np.mean(precs),np.mean(recs),np.mean(fs)))
    res = sorted(runs, key=lambda x:x[4], reverse=True)
    return res
res = tune_params(da,debug=True)
def kfoldCV(da,k=10, debug=False,delta=.1,l=5, knn_k=5, val=False, fdata=None,includeNB=True):
    if fdata: fData = fdata
    else: fData = getFoldData(da,k, val=False)
    fold_results = {'knn':[],'nb':[]}
    for f_idx, fold in fData['folds'].items():
        #create models based only on fold data
        knn = KNN(fold['trainDA'],k=knn_k,l=l)
        knn = setHashes(knn)
        knn.train()
        if includeNB: nb = NB(fold['trainDA'], delta=delta)
        if fold['testDA']: da_test = fold['testDA']
        else: da_test = da['da_val'] 
        if debug: da_test.m_reviews = np.random.choice(da_test.m_reviews, size=5, replace=False)
        knn_preds, nb_preds, true_lbls = [],[], []
        for rev in tqdm(da_test.m_reviews):
            knn_preds.append(knn.classify(rev))
            if includeNB: nb_preds.append(nb.classify(rev))
            true_lbls.append(rev.sent)
        knn_perf = evalPreds(true_lbls,knn_preds)
        if includeNB: nb_perf = evalPreds(true_lbls,nb_preds)
        fold_results['knn'].append(knn_perf)
        if includeNB: fold_results['nb'].append(nb_perf)
    return fold_results
res = tune_params(da,debug=True)
def kfoldCV(da,k=10, debug=False,delta=.1,l=5, knn_k=5, val=False, fdata=None,includeNB=True):
    if fdata: fData = fdata
    else: fData = getFoldData(da,k, val=False)
    fold_results = {'knn':[],'nb':[]}
    for f_idx, fold in fData['folds'].items():
        #create models based only on fold data
        knn = KNN(fold['trainDA'],k=knn_k,l=l)
        knn = setHashes(knn)
        knn.train()
        if includeNB: nb = NB(fold['trainDA'], delta=delta)
        if fold['testDA']: da_test = fold['testDA']
        else: da_test = da['da_val'] 
        if debug: da_test.m_reviews = np.random.choice(da_test.m_reviews, size=1, replace=False)
        knn_preds, nb_preds, true_lbls = [],[], []
        for rev in tqdm(da_test.m_reviews):
            knn_preds.append(knn.classify(rev))
            if includeNB: nb_preds.append(nb.classify(rev))
            true_lbls.append(rev.sent)
        knn_perf = evalPreds(true_lbls,knn_preds)
        if includeNB: nb_perf = evalPreds(true_lbls,nb_preds)
        fold_results['knn'].append(knn_perf)
        if includeNB: fold_results['nb'].append(nb_perf)
    return fold_results
kcv=10
debug=True
combos = load_obj('combos')
runs = []
for i,(k,l) in enumerate(combos):
    print('-----------------{}: k:{}, l:{}-----------------'.format(i,k,l))
    cv_res = kfoldCV(da,l=l,k=kcv,knn_k=k, includeNB=False, debug=debug)
    precs, recs, fs = zip(*cv_res['knn'])
    runs.append((k,l,np.mean(precs),np.mean(recs),np.mean(fs)))
def tune_params(da,kcv=10, debug=False):
    combos = load_obj('combos')
    runs = []
    for i,(k,l) in enumerate(combos):
        print('-----------------{}: k:{}, l:{}-----------------'.format(i,k,l))
        cv_res = kfoldCV(da,l=l,k=kcv,knn_k=2, includeNB=False, debug=debug)
        precs, recs, fs = zip(*cv_res['knn'])
        runs.append((k,l,np.mean(precs),np.mean(recs),np.mean(fs)))
    res = sorted(runs, key=lambda x:x[4], reverse=True)
    return res
def tune_params(da,kcv=10, debug=False):
    combos = load_obj('combos')
    runs = []
    for i,(k,l) in enumerate(combos[:3]):
        print('-----------------{}: k:{}, l:{}-----------------'.format(i,k,l))
        cv_res = kfoldCV(da,l=l,k=kcv,knn_k=2, includeNB=False, debug=debug)
        precs, recs, fs = zip(*cv_res['knn'])
        runs.append((k,l,np.mean(precs),np.mean(recs),np.mean(fs)))
    res = sorted(runs, key=lambda x:x[4], reverse=True)
    return res
res = tune_params(da,debug=True)
def tune_params(da,kcv=10, debug=False):
    combos = load_obj('combos')
    runs = []
    for i,(k,l) in enumerate(combos[:3]):
        print('-----------------{}: k:{}, l:{}-----------------'.format(i,k,l))
        cv_res = kfoldCV(da,l=l,k=2,knn_k=k, includeNB=False, debug=debug)
        precs, recs, fs = zip(*cv_res['knn'])
        runs.append((k,l,np.mean(precs),np.mean(recs),np.mean(fs)))
    res = sorted(runs, key=lambda x:x[4], reverse=True)
    return res
res = tune_params(da,debug=True)
def tune_params(da,kcv=10, debug=False):
    combos = load_obj('combos')
    runs = []
    for i,(k,l) in enumerate(combos[:2]):
        print('-----------------{}: k:{}, l:{}-----------------'.format(i,k,l))
        cv_res = kfoldCV(da,l=l,k=kcv,knn_k=k, includeNB=False, debug=debug)
        precs, recs, fs = zip(*cv_res['knn'])
        runs.append((k,l,np.mean(precs),np.mean(recs),np.mean(fs)))
    res = sorted(runs, key=lambda x:x[4], reverse=True)
    return res
res = tune_params(da,debug=True)
res
def getFoldData(da,k=10, val=False): 
    #if "folds" not in da.__dict__.keys():
    da.makeFolds(k)
    fData = {'folds':{i:{'trainDA':None,'testDA':None,'preds':None} for i in range(k)}}
    if val:
        da_validation = da.copy()
        vsize = int(.05 * len(da.m_reviews))
        da_validation.m_reviews = np.random.choice(da.m_reviews, size=(vsize), replace=False)
        remaining_articles = set(da.m_reviews).difference(set(da_validation.m_reviews))
        da.m_reviews = list(remaining_articles)
        fData['da_val'] = da_validation
    
    for f_idx,fold in enumerate(da.folds):
        tr_folds = range(k)
        if k > 1: tr_folds.pop(f_idx)
        tr_inds = []
        for ind in tr_folds: tr_inds += da.folds[ind]
        tst_inds = fold
        #build training sets (DocAnalyzers)
        da_train = da.copy()
        da_train.m_reviews = [da.m_reviews[i] for i in tr_inds]
        #build test sets (DocAnalyzers)
        da_test = da.copy()
        da_test.m_reviews = [da.m_reviews[j] for j in tst_inds]
        fData['folds'][f_idx] = {'trainDA':da_train,'testDA':da_test,'preds':[]}
    return fData
fd = getFoldData(da,k=2)
def tune_params(da,kcv=2, debug=False):
    combos = load_obj('combos')
    runs = []
    for i,(k,l) in enumerate(combos[:2]):
        print('-----------------{}: k:{}, l:{}-----------------'.format(i,k,l))
        cv_res = kfoldCV(da,l=l,k=kcv,knn_k=k, includeNB=False, debug=debug)
        precs, recs, fs = zip(*cv_res['knn'])
        runs.append((k,l,np.mean(precs),np.mean(recs),np.mean(fs)))
    res = sorted(runs, key=lambda x:x[4], reverse=True)
    return res
res = tune_params(da,debug=True)
def kfoldCV(da,k=10, debug=False,delta=.1,l=5, knn_k=5, val=False, fdata=None,includeNB=True):
    if fdata: fData = fdata
    else: fData = getFoldData(da,k, val=False)
    fold_results = {'knn':[],'nb':[]}
    for f_idx, fold in fData['folds'].items():
        #create models based only on fold data
        knn = KNN(fold['trainDA'],k=knn_k,l=l)
        knn = setHashes(knn)
        knn.train()
        if includeNB: nb = NB(fold['trainDA'], delta=delta)
        if fold['testDA']: da_test = fold['testDA']
        else: da_test = da['da_val'] 
        if debug: da_test.m_reviews = np.random.choice(da_test.m_reviews, size=5, replace=False)
        knn_preds, nb_preds, true_lbls = [],[], []
        for rev in tqdm(da_test.m_reviews):
            knn_preds.append(knn.classify(rev))
            if includeNB: nb_preds.append(nb.classify(rev))
            true_lbls.append(rev.sent)
        knn_perf = evalPreds(true_lbls,knn_preds)
        if includeNB: nb_perf = evalPreds(true_lbls,nb_preds)
        fold_results['knn'].append(knn_perf)
        if includeNB: fold_results['nb'].append(nb_perf)
    return fold_results
res = tune_params(da,debug=True)
def tune_params(da,kcv=2, debug=False):
    combos = load_obj('combos')
    runs = []
    for i,(k,l) in enumerate(combos):
        print('-----------------{}: k:{}, l:{}-----------------'.format(i,k,l))
        cv_res = kfoldCV(da,l=l,k=kcv,knn_k=k, includeNB=False, debug=debug)
        precs, recs, fs = zip(*cv_res['knn'])
        runs.append((k,l,np.mean(precs),np.mean(recs),np.mean(fs)))
    res = sorted(runs, key=lambda x:x[4], reverse=True)
    return res
res = tune_params(da,debug=True)
combs = pd.read_csv('combos.csv')
combs.columns
l,k = combs.ix[:,0].tolist(), combs.ix[:,1].tolist()
combos = zip(l,k)
combos
save_obj(combos, 'combos')
res = tune_params(da, debug=True)
combos
def tune_params(da,kcv=2, debug=False):
    combos = load_obj('combos')
    runs = []
    for i,(l,k) in enumerate(combos):
        print('-----------------{}: k:{}, l:{}-----------------'.format(i,k,l))
        cv_res = kfoldCV(da,l=l,k=kcv,knn_k=k, includeNB=False, debug=debug)
        precs, recs, fs = zip(*cv_res['knn'])
        runs.append((k,l,np.mean(precs),np.mean(recs),np.mean(fs)))
    res = sorted(runs, key=lambda x:x[4], reverse=True)
    return res
res = tune_params(da,debug=True)
knn = KNN(da, l=15,k=1)
knn.setHashes()
knn.train()
[len(b) for b in knn.bucket]
[len(b) for b in knn.buckets]
lens = [len(b) for b in knn.bucket]
lens = [len(b) for b in knn.buckets]
min(lens)
max(lens)
knn.l
knn.k
math.pow(2,15)
math.pow(2,15.4)
math.pow(2,15.5)
len(da.m_reviews)
sum(lens)
knn.buckets[0]
knn.buckets.values()[0]
knn.buckets.values()[0:5]
lens = [len(b) for b in knn.buckets]
min(lens)
len(knn.buckets[1])
len(knn.buckets.values()[1])
lens = [len(b) for b in knn.buckets.values()]
lens
np.mean(lens)

## ---(Fri Apr 20 15:41:59 2018)---
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/eval.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = load_obj('da_hw3')
combos = load_obj('combos')
combos
combos.remove((15,1))
combos.append((13,1))
save_obj(combos)
save_obj(combos, 'combos')
s = 'b_a'
b,a = s.split('_')
b,a
b
kcv=2
debug=False
par=True
if par:
    pool = mp.Pool(processes=len(combos))
    recs = {}
    for i,(l,k) in enumerate(combos):
        key= str(l)+'-'+str(k)
        rec[key] = spool.apply_async(kfoldCV, args=(da,l,k))
import multiprocessing as mp
if par:
    pool = mp.Pool(processes=len(combos))
    recs = {}
    for i,(l,k) in enumerate(combos):
        key= str(l)+'-'+str(k)
        rec[key] = spool.apply_async(kfoldCV, args=(da,l,k))
        
runs = []
if par:
    pool = mp.Pool(processes=len(combos))
    recs = {}
    for i,(l,k) in enumerate(combos):
        key= str(l)+'-'+str(k)
        rec[key] = mp.spool.apply_async(kfoldCV, args=(da,l,k))
pool = mp.Pool(processes=len(combos))
recs = {}
for i,(l,k) in enumerate(combos):
    key= str(l)+'-'+str(k)
    rec[key] = pool.apply_async(kfoldCV, args=(da,l,k))
pool = mp.Pool(processes=len(combos))
recs = {}
for i,(l,k) in enumerate(combos):
    key= str(l)+'-'+str(k)
    recs[key] = pool.apply_async(kfoldCV, args=(da,l,k))
keys, recs_raw = recs.items()
recs_new = [r.get() for r in recs_raw]

## ---(Fri Apr 20 16:07:32 2018)---
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/eval.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
da = load_obj('da_hw3')
kdv = 2
debug = True
par = True
combos = load_obj('combos')
combos = combos[:3]
runs = []
len(combos)
if par:
    pool = mp.Pool(processes=len(combos))
    recs = {}
    for i,(l,k) in enumerate(combos):
        key= str(l)+'-'+str(k)
        recs[key] = pool.apply_async(kfoldCV, args=(da,l,k))
    keys, recs_raw = recs.items()
    recs_new = [r.get() for r in recs_raw]
pool = mp.Pool(processes=len(combos))
recs = {}
for i,(l,k) in enumerate(combos):
    key= str(l)+'-'+str(k)
    recs[key] = pool.apply_async(kfoldCV, args=(da,l,k, debug))
debug
def tune_params(da,kcv=2, debug=False, par=False):
    combos = load_obj('combos')
    combos = combos[:3]
    runs = []
    if par:
        pool = mp.Pool(processes=len(combos))
        recs = {}
        for i,(l,k) in enumerate(combos):
            key= str(l)+'-'+str(k)
            recs[key] = pool.apply_async(kfoldCV, args=(da,l,k, debug))
        keys, recs_raw = recs.items()
        recs_new = [r.get() for r in recs_raw]    
        for key,rec in zip(keys,recs_new):
            l,k = key.split('-')
            precs, recalls, fs = zip(*rec)
            runs.append((str(k),str(l),np.mean(precs),np.mean(recalls),np.mean(fs)))
    else:
        for i,(l,k) in enumerate(combos):
            print('-----------------{}: k:{}, l:{}-----------------'.format(i,k,l))
            cv_res = kfoldCV(da,l=l,k=kcv,knn_k=k, includeNB=False, debug=debug)
            precs, recs, fs = zip(*cv_res['knn'])
            runs.append((k,l,np.mean(precs),np.mean(recs),np.mean(fs)))
    res = sorted(runs, key=lambda x:x[4], reverse=True)
    with open('tune_param_results.txt', 'w') as out:
        out.write(res)   
    return res
def kfoldCV(da,l, knn_k, debug, k=10, delta=.1, val=False, fdata=None,includeNB=True):
    if fdata: fData = fdata
    else: fData = getFoldData(da,k, val=False)
    fold_results = {'knn':[],'nb':[]}
    for f_idx, fold in fData['folds'].items():
        #create models based only on fold data
        knn = KNN(fold['trainDA'],k=knn_k,l=l)
        knn = setHashes(knn)
        knn.train()
        if includeNB: nb = NB(fold['trainDA'], delta=delta)
        if fold['testDA']: da_test = fold['testDA']
        else: da_test = da['da_val'] 
        if debug: da_test.m_reviews = np.random.choice(da_test.m_reviews, size=5, replace=False)
        knn_preds, nb_preds, true_lbls = [],[], []
        for rev in tqdm(da_test.m_reviews):
            knn_preds.append(knn.classify(rev))
            if includeNB: nb_preds.append(nb.classify(rev))
            true_lbls.append(rev.sent)
        knn_perf = evalPreds(true_lbls,knn_preds)
        if includeNB: nb_perf = evalPreds(true_lbls,nb_preds)
        fold_results['knn'].append(knn_perf)
        if includeNB: fold_results['nb'].append(nb_perf)
    return fold_results
combos = load_obj('combos')
combos = combos[:3]
runs = []
if par:
    pool = mp.Pool(processes=len(combos))
    recs = {}
    for i,(l,k) in enumerate(combos):
        key= str(l)+'-'+str(k)
        recs[key] = pool.apply_async(kfoldCV, args=(da,l,k, debug))
recs.items()[0]
keys, recs_raw = zip(*recs.items())
recs_new = [r.get() for r in recs_raw]
for key,rec in zip(keys,recs_new):
    l,k = key.split('-')
    precs, recalls, fs = zip(*rec)
    runs.append((str(k),str(l),np.mean(precs),np.mean(recalls),np.mean(fs)))
recs_new[:5]
recs_new[0]
for key,rec in zip(keys,recs_new):
    l,k = key.split('-')
    precs, recalls, fs = zip(*rec['knn'])
    runs.append((str(k),str(l),np.mean(precs),np.mean(recalls),np.mean(fs)))
runs
res = sorted(runs, key=lambda x:x[4], reverse=True)
res
revs = readReviews()
queries = readQueries()
queries = [post(q) for q in queries]
knn = KNN(da)
knn.setHashes()
knn.train()
for q in queries:
    q.tokens = textToGrams(da,q.content)
    q.setVec(da)
    
res = knn.find_nns(queries[0])
res
revs, probs = zip(*res)
revs, probs = res
printReview(revs[0])
printReview(revs[1])
printReview(revs[2])
printReview(revs[3])
printReview(revs[4])
brute_res = knn.find_nns(queries[0],typ="bf")
b_revs, probs = brute_res
for b in b_revs:
    printReview(b)
    

## ---(Fri Apr 20 20:45:46 2018)---
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3/eval.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW3')
5500./1.5
55000/1.5/3600
def tune_params(da,kcv=10, debug=False, par=False):
    combos = load_obj('combos')
    runs = []
    outname = 'temp_results.txt'
    if par:
        pool = mp.Pool(processes=len(combos))
        recs = {}
        for i,(l,k) in enumerate(combos):
            key= str(l)+'-'+str(k)
            recs[key] = pool.apply_async(kfoldCV, args=(da,l,k, debug))
        keys, recs_raw = zip(*recs.items())
        recs_new = [r.get() for r in recs_raw]    
        for key,rec in zip(keys,recs_new):
            l,k = key.split('-')
            precs, recalls, fs = zip(*rec['knn'])
            runs.append((str(k),str(l),np.mean(precs),np.mean(recalls),np.mean(fs)))
            if os.path.isfile(outname):
                out = open(outname, 'a')
            else:
                out = open(outname, 'w')
                out.write('k,l,precision,recall,f_score\n')
            out.write(runs[-1]+'\n')
            out.close()
    else:
        for i,(l,k) in enumerate(combos):
            print('-----------------{}: k:{}, l:{}-----------------'.format(i,k,l))
            cv_res = kfoldCV(da,l=l,k=kcv,knn_k=k, includeNB=False, debug=debug)
            precs, recs, fs = zip(*cv_res['knn'])
            runs.append((k,l,np.mean(precs),np.mean(recs),np.mean(fs)))
    res = sorted(runs, key=lambda x:x[4], reverse=True)
    with open('tune_param_results.txt', 'w') as out:
        out.write(res)   
    return res
len(combos)
combos = load_obj('combos')
len(combos)
combos
l = [2,5,10]
k = [1,5,10]
combos = [(2,1),(2,5),(2,10),(5,1),(5,5),(5,10),(10,1),(10,5),(10,10)]
def tune_params(da,kcv=10, debug=False, par=False):
    #combos = load_obj('combos')
    combos = [(2,1),(2,5),(2,10),(5,1),(5,5),(5,10),(10,1),(10,5),(10,10)]    
    runs = []
    outname = 'temp_results.txt'
    if par:
        pool = mp.Pool(processes=len(combos))
        recs = {}
        for i,(l,k) in enumerate(combos):
            key= str(l)+'-'+str(k)
            recs[key] = pool.apply_async(kfoldCV, args=(da,l,k, debug))
        keys, recs_raw = zip(*recs.items())
        recs_new = [r.get() for r in recs_raw]    
        for key,rec in zip(keys,recs_new):
            l,k = key.split('-')
            precs, recalls, fs = zip(*rec['knn'])
            runs.append((str(k),str(l),np.mean(precs),np.mean(recalls),np.mean(fs)))
            if os.path.isfile(outname):
                out = open(outname, 'a')
            else:
                out = open(outname, 'w')
                out.write('k,l,precision,recall,f_score\n')
            out.write(runs[-1]+'\n')
            out.close()
    else:
        for i,(l,k) in enumerate(combos):
            print('-----------------{}: k:{}, l:{}-----------------'.format(i,k,l))
            cv_res = kfoldCV(da,l=l,k=kcv,knn_k=k, includeNB=False, debug=debug)
            precs, recs, fs = zip(*cv_res['knn'])
            runs.append((k,l,np.mean(precs),np.mean(recs),np.mean(fs)))
    res = sorted(runs, key=lambda x:x[4], reverse=True)
    with open('tune_param_results.txt', 'w') as out:
        out.write(res)   
    return res
da
da = load_obj('da_hw3')
def appendResults(data, outname='temp_results.txt'):
    if os.path.isfile(outname):  out = open(outname, 'a')
    else:
        out = open(outname, 'w')
        out.write('k,l,precision,recall,f_score\n')
    out.write(data+'\n')
    out.close()
def tune_params(da,kcv=10, debug=False, par=False):
    #combos = load_obj('combos')
    combos = [(2,1),(2,5),(2,10),(5,1),(5,5),(5,10),(10,1),(10,5),(10,10)]    
    runs = []
    outname = 'temp_results.txt'
    if par:
        pool = mp.Pool(processes=len(combos))
        recs = {}
        for i,(l,k) in enumerate(combos):
            key= str(l)+'-'+str(k)
            recs[key] = pool.apply_async(kfoldCV, args=(da,l,k, debug))
        keys, recs_raw = zip(*recs.items())
        recs_new = [r.get() for r in recs_raw]    
        for key,rec in zip(keys,recs_new):
            l,k = key.split('-')
            precs, recalls, fs = zip(*rec['knn'])
            runs.append((str(k),str(l),np.mean(precs),np.mean(recalls),np.mean(fs)))    
            appendResults(runs[-1])
    else:
        for i,(l,k) in enumerate(combos):
            print('-----------------{}: k:{}, l:{}-----------------'.format(i,k,l))
            cv_res = kfoldCV(da,l=l,k=kcv,knn_k=k, includeNB=False, debug=debug)
            precs, recs, fs = zip(*cv_res['knn'])
            runs.append((k,l,np.mean(precs),np.mean(recs),np.mean(fs)))
            appendResults(runs[-1])
    res = sorted(runs, key=lambda x:x[4], reverse=True)
    with open('tune_param_results.txt', 'w') as out:
        out.write(res)   
    return res
def kfoldCV(da,l, knn_k, debug, k=10, delta=.1, val=False, fdata=None,includeNB=True):
    if fdata: fData = fdata
    else: fData = getFoldData(da,k, val=False)
    fold_results = {'knn':[],'nb':[]}
    for f_idx, fold in fData['folds'].items():
        #create models based only on fold data
        knn = KNN(fold['trainDA'],k=knn_k,l=l)
        knn = setHashes(knn)
        knn.train()
        if includeNB: nb = NB(fold['trainDA'], delta=delta)
        if fold['testDA']: da_test = fold['testDA']
        else: da_test = da['da_val'] 
        if debug: da_test.m_reviews = np.random.choice(da_test.m_reviews, size=30, replace=False)
        knn_preds, nb_preds, true_lbls = [],[], []
        for rev in tqdm(da_test.m_reviews):
            knn_preds.append(knn.classify(rev))
            if includeNB: nb_preds.append(nb.classify(rev))
            true_lbls.append(rev.sent)
        knn_perf = evalPreds(true_lbls,knn_preds)
        if includeNB: nb_perf = evalPreds(true_lbls,nb_preds)
        fold_results['knn'].append(knn_perf)
        if includeNB: fold_results['nb'].append(nb_perf)
    return fold_results
def kfoldCV(da,l, knn_k, debug, k=10, delta=.1, val=False, fdata=None,includeNB=True):
    if fdata: fData = fdata
    else: fData = getFoldData(da,k, val=False)
    fold_results = {'knn':[],'nb':[]}
    for f_idx, fold in fData['folds'].items():
        #create models based only on fold data
        knn = KNN(fold['trainDA'],k=knn_k,l=l)
        knn = setHashes(knn)
        knn.train()
        if includeNB: nb = NB(fold['trainDA'], delta=delta)
        if fold['testDA']: da_test = fold['testDA']
        else: da_test = da['da_val'] 
        if debug: da_test.m_reviews = np.random.choice(da_test.m_reviews, size=15, replace=False)
        knn_preds, nb_preds, true_lbls = [],[], []
        for rev in tqdm(da_test.m_reviews):
            knn_preds.append(knn.classify(rev))
            if includeNB: nb_preds.append(nb.classify(rev))
            true_lbls.append(rev.sent)
        knn_perf = evalPreds(true_lbls,knn_preds)
        if includeNB: nb_perf = evalPreds(true_lbls,nb_preds)
        fold_results['knn'].append(knn_perf)
        if includeNB: fold_results['nb'].append(nb_perf)
def kfoldCV(da,l, knn_k, debug, k=10, delta=.1, val=False, fdata=None,includeNB=True):
    if fdata: fData = fdata
    else: fData = getFoldData(da,k, val=False)
    fold_results = {'knn':[],'nb':[]}
    for f_idx, fold in fData['folds'].items():
        #create models based only on fold data
        knn = KNN(fold['trainDA'],k=knn_k,l=l)
        knn = setHashes(knn)
        knn.train()
        if includeNB: nb = NB(fold['trainDA'], delta=delta)
        if fold['testDA']: da_test = fold['testDA']
        else: da_test = da['da_val'] 
        if debug: da_test.m_reviews = np.random.choice(da_test.m_reviews, size=15, replace=False)
        knn_preds, nb_preds, true_lbls = [],[], []
        for rev in tqdm(da_test.m_reviews):
            knn_preds.append(knn.classify(rev))
            if includeNB: nb_preds.append(nb.classify(rev))
            true_lbls.append(rev.sent)
        knn_perf = evalPreds(true_lbls,knn_preds)
        if includeNB: nb_perf = evalPreds(true_lbls,nb_preds)
        fold_results['knn'].append(knn_perf)
        if includeNB: fold_results['nb'].append(nb_perf)
    return fold_results
res = tune_params(da,debug=True)
def appendResults(data, outname='temp_results.txt'):
    if os.path.isfile(outname):  out = open(outname, 'a')
    else:
        out = open(outname, 'w')
        out.write('k,l,precision,recall,f_score\n')
    out.write(str(data)+'\n')
    out.close()
def kfoldCV(da,l, knn_k, debug, k=10, delta=.1, val=False, fdata=None,includeNB=True):
    if fdata: fData = fdata
    else: fData = getFoldData(da,k, val=False)
    fold_results = {'knn':[],'nb':[]}
    for f_idx, fold in fData['folds'].items():
        #create models based only on fold data
        knn = KNN(fold['trainDA'],k=knn_k,l=l)
        knn = setHashes(knn)
        knn.train()
        if includeNB: nb = NB(fold['trainDA'], delta=delta)
        if fold['testDA']: da_test = fold['testDA']
        else: da_test = da['da_val'] 
        if debug: da_test.m_reviews = np.random.choice(da_test.m_reviews, size=10, replace=False)
        knn_preds, nb_preds, true_lbls = [],[], []
        for rev in tqdm(da_test.m_reviews):
            knn_preds.append(knn.classify(rev))
            if includeNB: nb_preds.append(nb.classify(rev))
            true_lbls.append(rev.sent)
        knn_perf = evalPreds(true_lbls,knn_preds)
        if includeNB: nb_perf = evalPreds(true_lbls,nb_preds)
        fold_results['knn'].append(knn_perf)
        if includeNB: fold_results['nb'].append(nb_perf)
    return fold_results
res = tune_params(da,debug=True)

## ---(Sun Apr 22 16:09:11 2018)---
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/monitoringScripts/netstats.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/monitoringScripts')
for i in range(0,3):
    print i
    
cpuDict = {'cpu'+str(i):None for i in range(0,24)}

## ---(Mon Apr 23 14:50:33 2018)---
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/monitoringScripts/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/monitoringScripts')
pull_data('bea3ch', 'Br#nD0$@')
def build_dfs(dire='.', device="em2", join_key="minute"):
    assert(join_key in ['minute','hour','day'])
    files = os.listdir(dire)
    #make lists of capture loss and stat files
    statfiles, capfiles = [],[]
    for f in files:
        if f.endswith('.log'):
            if 'stats' in f: statfiles.append(f)
            elif 'cap' in f: capfiles.append(f)
    #create stat dataframe from stat list
    print('parsing stats.bro logs...')
    df_stats = build_df_from_list(statfiles, dire)
    #create stat dataframe from capture loss list
    print('parsing capture loss logs...')
    df_cl = build_df_from_list(capfiles, dire)
    #get trafficStats
    print('parsing trafficStats.txt...')
    df_dev = pd.read_csv(dire+'/trafficStats_'+device+'.txt', index_col=False)
    if 'time' in df_dev.columns: df_dev = add_datetime(df_dev)
    df_dev = add_hashes(df_dev)

#    print('\njoining dfs by time...')
#    df_comb = df_stats.set_index(join_key).join(df_cl.set_index(join_key),rsuffix="cl")
#    df_comb = df_comb.join(df_dev.set_index(join_key),rsuffix="_dev")
#    df_comb = df_comb.join(df_dev,rsuffix="_dev")
    return df_stats,df_cl, df_dev
    #return df_comb
stats, cl, dev = build_dfs('tmp_2018-04-23')
stats, cl, dev = build_dfs('./tmp_2018-04-23')
stats, cl, dev = build_dfs('./tmp_2018-4-23')
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/monitoringScripts/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/monitoringScripts')
pull_data('bea3ch', 'Br#nD0$@')
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/monitoringScripts/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/monitoringScripts')
pull_data('bea3ch', 'Br#nD0$@')
stats, cl, dev = build_dfs('tmp_2018-4-23')
def build_dfs(dire='.', device="em2", join_key="minute"):
    assert(join_key in ['minute','hour','day'])
    files = os.listdir(dire)
    #make lists of capture loss and stat files
    statfiles, capfiles = [],[]
    for f in files:
        if f.endswith('.log'):
            if 'stats' in f: statfiles.append(f)
            elif 'cap' in f: capfiles.append(f)
    #create stat dataframe from stat list
    print('parsing stats.bro logs...')
    df_stats = build_df_from_list(statfiles, dire)
    #create stat dataframe from capture loss list
    print('parsing capture loss logs...')
    df_cl = build_df_from_list(capfiles, dire)
    #get trafficStats
    print('parsing trafficStats.txt...')
    df_dev = pd.read_csv(dire+'/trafficStats_v1_'+device+'.txt', index_col=False)
    if 'time' in df_dev.columns: df_dev = add_datetime(df_dev)
    df_dev = add_hashes(df_dev)

#    print('\njoining dfs by time...')
#    df_comb = df_stats.set_index(join_key).join(df_cl.set_index(join_key),rsuffix="cl")
#    df_comb = df_comb.join(df_dev.set_index(join_key),rsuffix="_dev")
#    df_comb = df_comb.join(df_dev,rsuffix="_dev")
    return df_stats,df_cl, df_dev
stats, cl, dev = build_dfs('tmp_2018-4-23')
df_dev = pd.read_csv(dire+'/trafficStats_v1_'+device+'.txt', index_col=False)
dire = 'tmp_2018-4-23'
df_dev = pd.read_csv(dire+'/trafficStats_v1_'+device+'.txt', index_col=False)
device='em2'
df_dev = pd.read_csv(dire+'/trafficStats_v1_'+device+'.txt', index_col=False)
df_dev
def build_dfs(dire='.', device="em2", join_key="minute"):
    assert(join_key in ['minute','hour','day'])
    files = os.listdir(dire)
    #make lists of capture loss and stat files
    statfiles, capfiles = [],[]
    for f in files:
        if f.endswith('.log'):
            if 'stats' in f: statfiles.append(f)
            elif 'cap' in f: capfiles.append(f)
    #create stat dataframe from stat list
    print('parsing stats.bro logs...')
    df_stats = build_df_from_list(statfiles, dire)
    #create stat dataframe from capture loss list
    print('parsing capture loss logs...')
    df_cl = build_df_from_list(capfiles, dire)
    #get trafficStats
    print('parsing trafficStats.txt...')
    df_dev = pd.read_csv(dire+'/trafficStats_v1_'+device+'.txt', index_col=False)
    if 'time' in df_dev.columns: df_dev = add_datetime(df_dev)
    df_dev = add_hashes(df_dev)

#    print('\njoining dfs by time...')
#    df_comb = df_stats.set_index(join_key).join(df_cl.set_index(join_key),rsuffix="cl")
#    df_comb = df_comb.join(df_dev.set_index(join_key),rsuffix="_dev")
#    df_comb = df_comb.join(df_dev,rsuffix="_dev")
    return df_stats,df_cl, df_dev
    #return df_comb
stats, cl, dev = build_dfs('tmp_2018-4-23')
df_dev = pd.read_csv(dire+'/trafficStats_v1_'+device+'.txt', index_col=False)
if 'time' in df_dev.columns: df_dev = add_datetime(df_dev)
df_dev.columns
df_dev.dtypes
df['ts'] = df['ts'].apply(lambda x: dt.datetime.fromtimestamp(x))
df <- df_dev
df = df_dev
df['ts'] = df['ts'].apply(lambda x: dt.datetime.fromtimestamp(x))
df['ts'].dtypes
df.dtypes
def add_datetime(df):
    if 'time' in df.columns:
        df = df.rename(columns={'time':'ts'})
    df['ts'] = df['ts'].apply(lambda x: dt.datetime.fromtimestamp(x))
    return df
df_dev = pd.read_csv(dire+'/trafficStats_v1_'+device+'.txt', index_col=False)
df_dev = add_datetime(df_dev)
df_dev = add_hashes(df_dev)
def build_dfs(dire='.', device="em2", join_key="minute"):
    assert(join_key in ['minute','hour','day'])
    files = os.listdir(dire)
    #make lists of capture loss and stat files
    statfiles, capfiles = [],[]
    for f in files:
        if f.endswith('.log'):
            if 'stats' in f: statfiles.append(f)
            elif 'cap' in f: capfiles.append(f)
    #create stat dataframe from stat list
    print('parsing stats.bro logs...')
    df_stats = build_df_from_list(statfiles, dire)
    #create stat dataframe from capture loss list
    print('parsing capture loss logs...')
    df_cl = build_df_from_list(capfiles, dire)
    #get trafficStats
    print('parsing trafficStats.txt...')
    df_dev = pd.read_csv(dire+'/trafficStats_v1_'+device+'.txt', index_col=False)
    df_dev = add_datetime(df_dev)
    df_dev = add_hashes(df_dev)

#    print('\njoining dfs by time...')
#    df_comb = df_stats.set_index(join_key).join(df_cl.set_index(join_key),rsuffix="cl")
#    df_comb = df_comb.join(df_dev.set_index(join_key),rsuffix="_dev")
#    df_comb = df_comb.join(df_dev,rsuffix="_dev")
    return df_stats,df_cl, df_dev
    #return df_comb
stats, cl, dev = build_dfs('tmp_2018-4-23')
cl.describe()
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/monitoringScripts/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/monitoringScripts')
pull_data('bea3ch', 'Br#nD0$@', allData=True)
stats, cl, dev = build_dfs('tmp_2018-4-23')
cl.describe()
old_dfs = build_dfs('tmp_2018-4-18')
def build_dfs(dire='.', device="em2", join_key="minute"):
    assert(join_key in ['minute','hour','day'])
    files = os.listdir(dire)
    #make lists of capture loss and stat files
    statfiles, capfiles = [],[]
    for f in files:
        if f.endswith('.log'):
            if 'stats' in f: statfiles.append(f)
            elif 'cap' in f: capfiles.append(f)
    #create stat dataframe from stat list
    print('parsing stats.bro logs...')
    df_stats = build_df_from_list(statfiles, dire)
    #create stat dataframe from capture loss list
    print('parsing capture loss logs...')
    df_cl = build_df_from_list(capfiles, dire)
    #get trafficStats
    print('parsing trafficStats.txt...')
    df_dev = pd.read_csv(dire+'/trafficStats_v1_'+device+'.txt', index_col=False)
    df_dev = add_datetime(df_dev)
    #df_dev = add_hashes(df_dev)

#    print('\njoining dfs by time...')
#    df_comb = df_stats.set_index(join_key).join(df_cl.set_index(join_key),rsuffix="cl")
#    df_comb = df_comb.join(df_dev.set_index(join_key),rsuffix="_dev")
#    df_comb = df_comb.join(df_dev,rsuffix="_dev")
    return df_stats,df_cl
old_dfs = build_dfs('tmp_2018-4-18')
def build_dfs(dire='.', device="em2", join_key="minute"):
    assert(join_key in ['minute','hour','day'])
    files = os.listdir(dire)
    #make lists of capture loss and stat files
    statfiles, capfiles = [],[]
    for f in files:
        if f.endswith('.log'):
            if 'stats' in f: statfiles.append(f)
            elif 'cap' in f: capfiles.append(f)
    #create stat dataframe from stat list
    print('parsing stats.bro logs...')
    df_stats = build_df_from_list(statfiles, dire)
    #create stat dataframe from capture loss list
    print('parsing capture loss logs...')
    df_cl = build_df_from_list(capfiles, dire)
    #get trafficStats
    print('parsing trafficStats.txt...')
    #df_dev = pd.read_csv(dire+'/trafficStats_v1_'+device+'.txt', index_col=False)
    #df_dev = add_datetime(df_dev)
    #df_dev = add_hashes(df_dev)

#    print('\njoining dfs by time...')
#    df_comb = df_stats.set_index(join_key).join(df_cl.set_index(join_key),rsuffix="cl")
#    df_comb = df_comb.join(df_dev.set_index(join_key),rsuffix="_dev")
#    df_comb = df_comb.join(df_dev,rsuffix="_dev")
    return df_stats,df_cl

def build_df_from_
def build_dfs(dire='.', device="em2", join_key="minute"):
    assert(join_key in ['minute','hour','day'])
    files = os.listdir(dire)
    #make lists of capture loss and stat files
    statfiles, capfiles = [],[]
    for f in files:
        if f.endswith('.log'):
            if 'stats' in f: statfiles.append(f)
            elif 'cap' in f: capfiles.append(f)
    #create stat dataframe from stat list
    print('parsing stats.bro logs...')
    df_stats = build_df_from_list(statfiles, dire)
    #create stat dataframe from capture loss list
    print('parsing capture loss logs...')
    df_cl = build_df_from_list(capfiles, dire)
    #get trafficStats
    print('parsing trafficStats.txt...')
    #df_dev = pd.read_csv(dire+'/trafficStats_v1_'+device+'.txt', index_col=False)
    #df_dev = add_datetime(df_dev)
    #df_dev = add_hashes(df_dev)

#    print('\njoining dfs by time...')
#    df_comb = df_stats.set_index(join_key).join(df_cl.set_index(join_key),rsuffix="cl")
#    df_comb = df_comb.join(df_dev.set_index(join_key),rsuffix="_dev")
#    df_comb = df_comb.join(df_dev,rsuffix="_dev")
    return df_stats,df_cl
old_dfs = build_dfs('tmp_2018-4-18')
stats, cl = old_dfs
stats_old, cl_old = stats, cl
stats, cl = build_dfs('tmp_2018-4-23')
cl.describe()
cl_old.describe()
cf_old.shape
cl_old.shape
cl.shape

## ---(Tue Apr 24 15:54:20 2018)---
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/monitoringScripts/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/monitoringScripts')
pull_data('bea3ch', 'Br#nD0$@', allData=True)
def build_dfs(dire='.', device="em2", join_key="minute"):
    assert(join_key in ['minute','hour','day'])
    files = os.listdir(dire)
    #make lists of capture loss and stat files
    statfiles, capfiles = [],[]
    for f in files:
        if f.endswith('.log'):
            if 'stats' in f: statfiles.append(f)
            elif 'cap' in f: capfiles.append(f)
    #create stat dataframe from stat list
    print('parsing stats.bro logs...')
    df_stats = build_df_from_list(statfiles, dire)
    #create stat dataframe from capture loss list
    print('parsing capture loss logs...')
    df_cl = build_df_from_list(capfiles, dire)
    #get trafficStats
    print('parsing trafficStats.txt...')
    df_dev = pd.read_csv(dire+'/trafficStats_v1_'+device+'.txt', index_col=False)
    df_dev = add_datetime(df_dev)
    df_dev = add_hashes(df_dev)

#    print('\njoining dfs by time...')
#    df_comb = df_stats.set_index(join_key).join(df_cl.set_index(join_key),rsuffix="cl")
#    df_comb = df_comb.join(df_dev.set_index(join_key),rsuffix="_dev")
#    df_comb = df_comb.join(df_dev,rsuffix="_dev")
    return df_stats,df_cl
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/monitoringScripts/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/monitoringScripts')
def build_dfs(dire='.', device="em2", join_key="minute", export=True):
    assert(join_key in ['minute','hour','day'])
    files = os.listdir(dire)
    #make lists of capture loss and stat files
    statfiles, capfiles = [],[]
    for f in files:
        if f.endswith('.log'):
            if 'stats' in f: statfiles.append(f)
            elif 'cap' in f: capfiles.append(f)
    #create stat dataframe from stat list
    print('parsing stats.bro logs...')
    df_stats = build_df_from_list(statfiles, dire)
    #create stat dataframe from capture loss list
    print('parsing capture loss logs...')
    df_cl = build_df_from_list(capfiles, dire)
    #get trafficStats
    print('parsing trafficStats.txt...')
    df_dev = pd.read_csv(dire+'/trafficStats_v1_'+device+'.txt', index_col=False)
    df_dev = add_datetime(df_dev)
    df_dev = add_hashes(df_dev)
    #Export if necessary
    if export:
        df_stats.to_csv('stats_df.csv')
        df_dev.to_csv('trafficStats_df.csv')
        df_cl.to_csv('captureloss_df.csv')

#    print('\njoining dfs by time...')
#    df_comb = df_stats.set_index(join_key).join(df_cl.set_index(join_key),rsuffix="cl")
#    df_comb = df_comb.join(df_dev.set_index(join_key),rsuffix="_dev")
#    df_comb = df_comb.join(df_dev,rsuffix="_dev")
    return df_stats,df_cl, df_dev
res = build_dfs('tmp_2018-4-24')
dire = 'tmp_2018-4-24'
os.listdir(dire)
device="em2"
join_key="minute"
export=True
files = os.listdir(dire)
#make lists of capture loss and stat files
statfiles, capfiles = [],[]
for f in files:
    if f.endswith('.log'):
        if 'stats' in f: statfiles.append(f)
        elif 'cap' in f: capfiles.append(f)
statfiles
df_stats = build_df_from_list(statfiles, dire)
df_cl = build_df_from_list(capfiles, dire)
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/monitoringScripts/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/monitoringScripts')

## ---(Tue Apr 24 16:13:24 2018)---
runfile('/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/monitoringScripts/get_bro_performance.py', wdir='/Users/babraham/Box Sync/1-CyberSecurity-Project/BEA-Work/trafficAnalysis/monitoringScripts')
pull_data('bea3ch', 'Br#nD0$@')
stats, cl, dev = build_dfs('tmp_2018-4-24')
cl.columns
cl['percent_lost'].plot()
dev.columns
def.utilization.plot()
dev.utilization.plot()
np.correlate(cl['percent_lost'].tolist(), dev['utilization'].tolist())
from scipy.stats.stats import pearsonr
res = pearsonr(cl['percent_lost'].tolist(), dev['utilization'].tolist())
res = np.corrcoef(cl['percent_lost'].tolist(), dev['utilization'].tolist())
util = np.random.choice(dev['utilization'].tolist(), size=len(cl['percent_lost'].tolist()))
util = np.random.choice(dev['utilization'].tolist(), size=len(cl['percent_lost'].tolist()), replace=False)
np.corrcoef(util, cl['percent_lost'].tolist())

## ---(Tue Apr 24 23:39:30 2018)---
import sqlite3
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project/mxm_to_db.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project')
import sqlite3
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project/mxm_analysis.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project')
os.listdir('.')
sqlite_file = "sqldb.db"
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
c.execute('show tables;')
c.execute('show tables')
c.execute('SELECT top 100 from words')
c.execute('SELECT * from words limit 5;')
all_rows = c.fetchall()
all_rows
c.execute('SELECT * from words limit 50;')
all_rows = c.fetchall()
all_rows
c.execute('SELECT * FROM lyrics limit 5;'
)
res = c.fetchall()
res
c.execute('SELECT COUNT (DISTINCT track_id) from lyrics;')
res = c.fetchone()
res
c.execute('SELECT word,count from lyrics where mxm_id = 4623710;')
c.execute('SELECT word,count from lyrics where mxm_tid = 4623710;')
res = c.fetchall()
res
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk/su_adapter.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk')
os.listdir('.')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk/history.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk')
H = History('history')
H.load('180725_0104_100.pickle')
su= Su_env(['SuAI', 'BetterAI', 'BetterAI'])
su.history_class= history_class
su= Su_env(['SuAI', 'BetterAI', 'BetterAI'])
su= Su_env(['SuAI', 'BetterAI', 'BetterAI'])
su.history_class= history_class
path = dict()
actions = list()
rewards = list()
obs = list()
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk/su_adapter.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk')

## ---(Wed Apr 25 16:11:03 2018)---
class q_learner():
    def __init__self(self,init_Q,gamma=1,num_episodes=10,epsilon=0.1):
        self.Q = init_Q
        self.num_states, self.num_actions = init_Q.shape
        self.num_eps = num_episodes
        self.gamma = gamma
        self.epsilon = epsilon
    
    def train(self, env, num_eps=None, Q=None):
        if not num_eps: num_eps = self.num_eps
        if not Q: Q = self.Q
        steps = np.zeros(num_eps)
        rewards = np.zeros(num_eps)
        for ep in tqdm(range(num_eps)):
            s = env.reset()
            terminal = False
            while not terminal:
                if self.actOptimally(): a = np.argmax(Q[s])
                else: a = env.game.su_sampler.sample()
                terminal, r, s_new = env.step(s)
                Q[s,a] = Q[s,a] + self.alpha*(r + self.gamma * np.max(Q[s_new]) - Q[s,a])
                steps[ep] +=1
                rewards[ep] += r
                s = s_new
        
        self.Q = Q
        self.rewards = rewards
        self.steps = steps
    
    def actOptimally(self):
        x = np.random.random()
        return (x > self.epsilon)

## ---(Wed Apr 25 19:36:22 2018)---
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk/algorithms_test/q_learner.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk/algorithms_test')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk/q_learner.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk/su_adapter.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk/q_learner.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk/ai/__init__.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk/ai')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk/q_learner.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk')
su= Su_env(['BetterAI', 'SuAI', 'SuAI'])
print(su.game.world.territories.keys())
print(list(su.game.world.territories.values()))
print(su.game.world.territories.items())
actions = list()
rewards = list()
obs = list()
num_states = 42*3 + 1
num_actions = (167+42) * 200
init_Q = np.zeros([num_states, num_actions])
ql = q_learner(init_Q, num_episodes=1)
ob = su.reset()
total_steps_taken = 0
total_rewards = 0
ep=1
game_over = False
action = su.game.su_sampler.sample()
action
su.game.asv.validate_action(action)
t_src,t_target,forces = su.game.player.ai.get_src_target_force_from_index(action[0])
actions.append(action)
t_src,t_target,forces
game_over, reward, new_obs = su.step(action)
game_over, reward, new_obs
su.step(action)
ep,obs,action,reward,new_obs
action
ep,ob,action,reward,new_obs
ql.online_update(ep,ob,action,reward,new_obs)
ep
obj
obs
ob
action
ql.online_update(ep,ob,action[0],reward,new_obs)
action[0]
int(action[0])
ob
h = '-'.join([str(o) for o in ob])
h
h = '-'.join([str(int(o)) for o in ob])
h
def hash_state(state):
    return '-'.join([str(int(count)) for count in state])
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk/q_learner.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk')
action = su.game.su_sampler.sample()
   su= Su_env(['BetterAI', 'SuAI', 'SuAI'])
   print(su.game.world.territories.keys())
   print(list(su.game.world.territories.values()))
   print(su.game.world.territories.items())

#su.history_class= history_class
   actions = list()
   rewards = list()
   obs = list()
   num_states = 42*3 + 1
   num_actions = (167+42) * 200
   init_Q = np.zeros([num_states, num_actions])
   ql = q_learner(init_Q, num_episodes=1)
   ob = su.reset()
   total_steps_taken = 0
   total_rewards = 0
   ep=1
   game_over = False
action = su.game.su_sampler.sample()
action
game_over, reward, new_obs = su.step(action)
s,a,r,s_new = hash_state(ob),int(action[0]),reward, hash_state(new_obs)
s,a,r,s_new
ql.online_update(ep,s,a,r,s_new)
def online_update(ql, ep, s,a,r,s_new):
    ql.Q[s,a] += ql.alpha*(r + ql.gamma * np.max(ql.Q[s_new]) - ql.Q[s,a])
    ql.policy[s] = np.argmax(ql.Q[s])
    ql.steps[ep] +=1
    ql.rewards[ep] += r
    return ql
r + ql.gamma
np.max(ql.Q[s_new])
ql.Q[s_new]
s_new
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk/q_learner.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk')
def sample(env):
    action = env.game.su_sampler.sample()
    if not env.game.asv.validagte_action(action):
        while not env.game.asv.validagte_action(action):
            action = env.game.su_sampler.sample()
    return action
sample(su)
su
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk/q_learner.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk/sampler.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk/su_adapter.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk/q_learner.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk')
action = su.game.su_sampler.sample_2(1)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk/sampler.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk')
su= Su_env(['BetterAI', 'SuAI', 'SuAI'])
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk/q_learner.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk')
su= Su_env(['BetterAI', 'SuAI', 'SuAI'])
actions = list()
rewards = list()
obs = list()
num_states = 42*3 + 1
num_actions = (167+42) * 200
init_Q = np.zeros([num_states, num_actions])
ql = q_learner(num_states,num_actions, num_episodes=1)
ob = su.reset()
total_steps_taken = 0
total_rewards = 0
ep=1
game_over = False
action = su.game.su_sampler.sample_2(1)
action
action[0][0]
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk/sampler.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk/q_learner.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk')
env = su
action = env.game.su_sampler.sample()
action= su.game.su_sampler.sample()
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk/q_learner.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk/q_learner.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk')
su= Su_env(['BetterAI', 'SuAI', 'SuAI'])
action = env.game.su_sampler.sample()
env=su
action = env.game.su_sampler.sample()
action
def sample(env):
    action = env.game.su_sampler.sample()
    if not env.game.asv.validagte_action(action[0]):
        while not env.game.asv.validagte_action(action):
            action = env.game.su_sampler.sample()
    return action
sample(su)
def sample(env):
    action = env.game.su_sampler.sample()
    if not env.game.asv.validagte_action(action[0]):
        while not env.game.asv.validate_action(action):
            action = env.game.su_sampler.sample()
    return action
sample(su)
def sample(env):
    action = env.game.su_sampler.sample()
    if not env.game.asv.validate_action(action[0]):
        while not env.game.asv.validate_action(action):
            action = env.game.su_sampler.sample()
    return action
sample(su)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk/q_learner.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk')
def online_update(ql, ep, s,a,r,s_new):
    if s not in ql.Q: ql.Q[s] = {}
    if s_new not in ql.Q: ql.Q[s_new] = {}
    ql.Q[s][a] = ql.Q[s].get(a,0) +  ql.alpha*(r + ql.gamma * np.max(ql.Q[s_new].items()) - ql.Q[s][a])
    ql.policy[s] = np.argmax(ql.Q[s].items())
    return ql
s,a,r
s,a,r,s_new = hash_state(ob),int(action[0]),reward, hash_state(new_obs)
ob = su.reset()
su= Su_env(['BetterAI', 'SuAI', 'SuAI'])
actions = list()
rewards = list()
obs = list()
num_states = 42*3 + 1
num_actions = (167+42) * 200
init_Q = np.zeros([num_states, num_actions])
ql = q_learner(num_states,num_actions, num_episodes=1)
ob = su.reset()
total_steps_taken = 0
total_rewards = 0
ep=1
game_over = False
action = su.game.su_sampler.sample_2(1)
t_src,t_target,forces = su.game.player.ai.get_src_target_force_from_index(action[0])
actions.append(action)
game_over, reward, new_obs = su.step(action)
s,a,r,s_new = hash_state(ob),int(action[0]),reward, hash_state(new_obs)
if s not in ql.Q: ql.Q[s] = {}

if s_new not in ql.Q: ql.Q[s_new] = {}
ql.Q[s][a] = ql.Q[s].get(a,0) +  ql.alpha*(r + ql.gamma * np.max(ql.Q[s_new].items()) - ql.Q[s][a])
ql.Q[s].get(a,0)
np.max(ql.Q[s_new].items())
ql.Q[s_new].items()
def online_update(ql, ep, s,a,r,s_new):
    if s not in ql.Q: ql.Q[s] = {0:0}
    if s_new not in ql.Q: ql.Q[s_new] = {0:0}
    ql.Q[s][a] = ql.Q[s].get(a,0) +  ql.alpha*(r + ql.gamma * np.max(ql.Q[s_new].items()) - ql.Q[s][a])
    ql.policy[s] = np.argmax(ql.Q[s].items())
    return ql
if s not in ql.Q: ql.Q[s] = {0:0}

if s_new not in ql.Q: ql.Q[s_new] = {0:0}

ql.Q[s][a] = ql.Q[s].get(a,0) +  ql.alpha*(r + ql.gamma * np.max(ql.Q[s_new].items()) - ql.Q[s][a])
ql.policy[s] = np.argmax(ql.Q[s].items())
ql.Q[s_new]
ql.Q = {}
if s not in ql.Q: ql.Q[s] = {0:0}

if s_new not in ql.Q: ql.Q[s_new] = {0:0}

ql.Q[s][a] = ql.Q[s].get(a,0) +  ql.alpha*(r + ql.gamma * np.max(ql.Q[s_new].items()) - ql.Q[s][a])
ql.policy[s] = np.argmax(ql.Q[s].items())
ql.alpha*(r + ql.gamma * np.max(ql.Q[s_new].items())
ql.alpha
r + ql.gamma * np.max(ql.Q[s_new].items()
r + ql.gamma * np.max(ql.Q[s_new].items())
ql.Q[s][a]
if s not in ql.Q: ql.Q[s] = {0:0}

if s_new not in ql.Q: ql.Q[s_new] = {0:0}

ql.Q[s][a] = ql.Q[s].get(a,0) +  ql.alpha*(r + ql.gamma * np.max(ql.Q[s_new].items()) - ql.Q[s].get(a,0))
ql.policy[s] = np.argmax(ql.Q[s].items())
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk/q_learner.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk')
obs.append(ob)
action = None
while(True):
    action = su.game.su_sampler.sample_2(1)
    print('action taken: {}'.format(action[0]))
    t_src,t_target,forces = su.game.player.ai.get_src_target_force_from_index(action[0])
    actions.append(action)
    game_over, reward, new_obs = su.step(action)
    s,a,r,s_new = hash_state(ob),int(action[0]),reward, hash_state(new_obs)
    ql.online_update(ep,s,a,r,s_new)
    rewards.append(reward)
    total_rewards += reward
    if reward != 0:
        break
    total_steps_taken += su.game.turn
    q=0
    q_path = []
    gamma = .99

for r in reversed(rewards):
    q = r + gamma * q
    q_path.append(q)

q_path.reverse()
   su= Su_env(['BetterAI', 'SuAI', 'SuAI'])
   print(su.game.world.territories.keys())
   print(list(su.game.world.territories.values()))
   print(su.game.world.territories.items())

#su.history_class= history_class
   actions = list()
   rewards = list()
   obs = list()
   num_states = 42*3 + 1
   num_actions = (167+42) * 200
   init_Q = np.zeros([num_states, num_actions])
   ql = q_learner(num_states,num_actions, num_episodes=1)
   ob = su.reset()
   total_steps_taken = 0
   total_rewards = 0
   ep=1
   game_over = False
obs.append(ob)
action = None
action = su.game.su_sampler.sample_2(1)
print('action taken: {}'.format(action[0]))
t_src,t_target,forces = su.game.player.ai.get_src_target_force_from_index(action[0])
actions.append(action)
game_over, reward, new_obs = su.step(action)
s,a,r,s_new = hash_state(ob),int(action[0]),reward, hash_state(new_obs)
ql.online_update(ep,s,a,r,s_new)
def a_max(arr):
    if len(arr) == 0:
        return 0
    return np.argmax(arr)
def a_max(arr):
    if len(arr) == 0: return 0
    return np.argmax(arr)


def maxi(arr):
    if len(arr) == 0: return 0
    return np.max(arr)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk/q_learner.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk')
rewards
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk/q_learner.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk')
   su= Su_env(['BetterAI', 'SuAI', 'SuAI'])
   print(su.game.world.territories.keys())
   print(list(su.game.world.territories.values()))
   print(su.game.world.territories.items())

#su.history_class= history_class
   actions = list()
   rewards = list()
   obs = list()
   num_states = 42*3 + 1
   num_actions = (167+42) * 200
   init_Q = np.zeros([num_states, num_actions])
   ql = q_learner(num_states,num_actions, num_episodes=1)
   ob = su.reset()
   total_steps_taken = 0
   total_rewards = 0
   ep=1
   game_over = False
   counter = 0
sample(su)
def sample(env):
    action = env.game.su_sampler.sample()
    if not env.game.asv.validate_action(action):
        while not env.game.asv.validate_action(action):
            action = env.game.su_sampler.sample()
    return action
sample(su)
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk/q_learner.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk/sampler.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk/q_learner.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk')
def sample(env):
    if type(env.game.player.ai) is not SuAI:
        return None
    else:
        action = env.game.su_sampler.sample()
        if not env.game.asv.validate_action(action):
            while not env.game.asv.validate_action(action):
                action = env.game.su_sampler.sample()
        return action
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk/q_learner.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk')
su= Su_env(['BetterAI', 'BetterAI', 'SuAI'])
sample(su)
su.game.player.ai
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk/q_learner.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Reinforcement_Learning/RiskRL/pyrisk')
sqlite_file = "sqldb.db"
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project/mxm_analysis.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project')
db = sqldb()
db.query('SELECT * FROM words')
db.query('SELECT * FROM words;')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project/mxm_analysis.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project')
db = sqldb()
db.query('SELECT * FROM words;')
db.query('SELECT * FROM lyrics limit 100;')
conn = sqlite3.connect('mysql.db')
c = conn.cursor()
conn.execute('SELECT * FROM words limit 10;')
conn.execute('SHOW TABLES;')
conn.execute('.tables')
c.execute('SELECT * FROM lyrics limit 10;')
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
c.execute("SELECT name FROM sqlite_master WHERE type='table';")
c.fetchall()
res = c.execute("SELECT name FROM sqlite_master WHERE type='table';")
res.fetchall()
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project/mxm_analysis.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project')
db = sqldb()
db.query('SELECT * from lyrics limit 10;')
res = db.query('select distinct artist from lyrics;')
c.execute("SELECT name FROM sqlite_master WHERE type='table';")
c.fetchall()
db.query('select * from lyrics limit 1;')
db.query("pragma table_info('lyrics')")
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project/mxm_analysis.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project')
db = sqldb()
res = db.getSongs()
len(res)
res[:5]
res[0]
res[0][0]
db.getLyrics('TRAAAAV128F421A322')
db.query('select * from lyrics where track_id = TRAAAAV128F421A322')
db.query('select track_id from lyrics limit 10;')
db.query('select * from lyrics where track_id = TRAAAAV128F421A322')
db.query("select * from lyrics where track_id = 'TRAAAAV128F421A322'")
db.query("pragma table_info('lyrics')")
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project/mxm_analysis.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project')
songs = db.getSongs()
songs[:10]
songs[0][0]
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project/mxm_analysis.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project')
db = sqldb()
res = db.getSongs()
res[:5]
songs = res
del(res)
db.getSchema('lyrics')
db.getSchema('words')
db.getLyrics(songs[0])
v = db.query('SELECT distinct word from lyrics')
len(v)
db.query('select sum counts from lyrics group by word')
db.query('select sum(counts) from lyrics group by word')
db.query('select sum(count) from lyrics group by word')
db.query('select word, sum(count) from lyrics group by word limit 50')
db.query('select word, count(distinct track_id) from lyrics group by word limit 50')
db.query("select count(*) from lyrics where word = 'absurd'")
db.query("select count(DISTINCT track_id) from lyrics where word = 'absurd'")
db.query("select count(DISTINCT track_id) from lyrics where word = 'a'")
db.query("select count(*) from lyrics where word = 'a'")
res = db.query("select * from lyrics where word='absurd'")
res[:5]
songs = set([t[0] for t in res])
len(songs)
len(res)
counts = [int(t[-1]) for t in res]
sum(counts)
counts[:5]
counts = [int(t[-2]) for t in res]
sum(counts)
db.query("select sum(count) from lyrics where word = 'absurd'")
db.query("select count(count) from lyrics where word = 'absurd'")
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project/mxm_analysis.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project')
sdb = sqldb('sqldb.db')
sdb.getSchema('lyrics')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project/mxm_analysis.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project')
sdb = sqldb('sqldb.db')
sdb.tableNames()
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project/mxm_analysis.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project')
sdb = sqldb('sqldb.db')
sdb.showTables()
sdb.tableNames()
sdb.getSchema('words')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project/mxm_analysis.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project')
sdb = sqldb('sqldb.db')
sdb.showTables()
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project/mxm_analysis.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project')
sdb = sqldb('sqldb.db')
sdb.showTables()
sdb.query('select * from lyrics limit 20')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project/mxm_analysis.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project')
xmx = xmxdb('sqldb.db')
xmx.vocab[:10]
xmx.N
xmx.TF('love')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project/mxm_analysis.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project')
xmx = xmxdb('sqldb.db')
xmx.N
xmx.N[0]
xmx.vocab[:10]
xmx.TF('love')
word='love'
xmx.query("select sum(count) from lyrics where word = '{}'".format(word))
res = [(298043,)]
int(res[0][0])
songs = xmx.getSongs()
songs[:5]
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project/mxm_analysis.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project')
xmx = xmxdb('sqldb.db')
xmx.TF('love')
xmx.query('select sum(count) from lyrics group by word')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project/mxm_analysis.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project')
xmx = xmxdb('sqldb.db')
tups = xmx.getFStats()
tups = xmx.getFStast()
tups[:5]
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project/mxm_analysis.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project/mxm_analysis.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project')
xmx = xmxdb('sqldb.db')
def buildTFIDFMat(db):
    print ('building tf-idf matrix...')

#        for v in tqdm(self.vocab):
#            tf = self.TF(v)
#            df = self.DF(v)
#            tf_idf = self.calcTFIDF(tf,df)
#            self.tfidf[v] = [tf,df,tf_idf]
    ti = time.time()
    tfdf_tups = db.getFreqStats()
    for word,tf,df in tfdf_tups:
        tf_idf = db.calcTFIDF(tf,df)
        db.tfidf[word] = [tf,df,tf_idf]
    print('total time: {} seconds'.format(time.time()-ti))
    return db
xmx = buildTFIDFMat(xmx)
xmx.tfidf
df = xmx.DF('shout')
tf = xmx.TF('shout')
df,tf
xmx.calcTFIDF(tf,df)
xmx.N
x.xmN / df
xmx.N / df
def calcTFIDF(db, tf,df, norm_tf=True):
    if norm_tf: tf = 1 + np.log(tf+1)
    return tf * np.log(1 + float(db.N) / df)
xmx.calcTFIDF(tf,df)
calcTFIDF(xmx,tf,df)
tfidfm = xmx.tfidf
import pandas as pd
df = pd.DataFrame.from_dict(tfidfm)
df.head()
df = pd.DataFrame.from_dict(tfidfm, orient='index')
df.head()
df = pd.DataFrame.from_dict(tfidfm, orient='index', columns=['TF','DF','IDF'])
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project/mxm_analysis.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project')
xmx = xmxdb('sqldb.db')
xmx.buildTFIDFMat()
xmx.tfidf.items()[:5]
df = pd.DataFrame.from_dict(xmx.tfidf, orient="index")
df.head()
df.to_csv('tfidf.csv')
df.to_csv('tfidf.csv', encoding='utf-8')
f = open('train_triplext.txt' ,'r')
f = open('train_triplets.txt' ,'r')
lines = f.readlines()
lines[:5]
outfile = 'userdata.db'
conn = sqllite3.connect(outfile)
c = conn.cursor()
outfile = 'userdata.db'
conn = sqlite3.connect(outfile)
c = conn.cursor()
songs = mxm.getSongs()
songs = xmx.getSongs()
q = "CREATE TABLE userdata (user_id TEXT PRIMARY KEY,"
q += "song_id INT,"
q += " count INT);"
conn.execute(q)
s = 'brendan\abraham'
s.split('\')
s.split('\\')
s
lines[0]
lines[0].split('\t')
lines[0].strip().split('\t')
def buildUserDB(outfilename):
    #initialize database
    conn = sqlite3.connect(outfilename)
    c = conn.cursor()
    # create user data table
    q = "CREATE TABLE userdata (user_id TEXT PRIMARY KEY,"
    q += "song_id INT,"
    q += " count INT);"
    conn.execute(q)
    #read data from flat file
    fpath = 'train_triplets.txt'
    with open(fpath, 'r') as f:
        lines = f.readlines()
    #populate table
    for l in lines:
        user, song, playct = l.strip().split("\t")
        q = 'INSERT INTO userdata VALUES({},{},{})'.format(user,song,playct)
        c.execute(q)
    conn.close()
buildUserDB('userdata.db')
def buildUserDB(outfilename):
    #initialize database
    conn = sqlite3.connect(outfilename)
    c = conn.cursor()
    # create user data table
    q = "CREATE TABLE userdata (user_id TEXT PRIMARY KEY,"
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
        q = 'INSERT INTO userdata VALUES({},{},{})'.format(user,song,playct)
        c.execute(q)
    conn.close()
buildUserDB('userdata.db')
def buildUserDB(outfilename):
    #initialize database
    conn = sqlite3.connect(outfilename)
    c = conn.cursor()
    # create user data table
    q = "CREATE TABLE userdata (user_id TEXT PRIMARY KEY,"
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
    conn.close()
buildUserDB('userdata.db')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project/mxm_analysis.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project')
buildUserDB('userdata.db')
buildUserDB('userdata2.db')
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
    conn.close()
buildUserDB('userdata2.db')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project/MSD_Song_Prediction/mxm_analysis.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project/MSD_Song_Prediction')
class userdb(sqldb):
    def __init__(self, fpath='userdata.db'):
        sqldb.__init__(self, fpath)
        self.fpath = fpath
        self.buildDB()
udb = userdb()
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project/MSD_Song_Prediction/mxm_analysis.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project/MSD_Song_Prediction')
udb = userdb()
udb.query('select * from userdata limit 10')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project/MSD_Song_Prediction/mxm_analysis.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project/MSD_Song_Prediction')
buildUserDB('userdata2.db')
udb = userdb()
udb.query('select * from userdata limit 10')
udb = userdb()
udb.query('select * from userdata limit 10')
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project/MSD_Song_Prediction/mxm_analysis.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project/MSD_Song_Prediction')
udb = userdb()
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project/MSD_Song_Prediction/mxm_analysis.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project/MSD_Song_Prediction')
udb = userdb()
udb = get_user_dists(udb)
udb.user_dists.items()[:3]
udb
udb = userdb()
runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project/MSD_Song_Prediction/mxm_analysis.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/Project/MSD_Song_Prediction')
os.listdir('~/Downloads')
os.listdir('/Users/babraham/Downloads')
conn = sqlite3.connect('lastfm_tags.db')
c = conn.cursor()
c.execute('select * from tags limit 10')
c.fetchall()
tdb = sqldb('lastfm_tags.db')
tdb.showTables()
tdb.query('select * from tid_tag limit 5')
tdb.query('select tid from tid_tag limit 10')
print '************** DEMO 2 **************'
   print 'We get all tracks with at least one tag'
   sql = "SELECT tid FROM tids"
   res = conn.execute(sql)
   data = res.fetchall()
   for k in range(10):
       print data[k]
   print '...'
   print '(total number of track IDs: %d)' % len(data)
print '************** DEMO 2 **************'
print 'We get all tracks with at least one tag'
sql = "SELECT tid FROM tids"
res = conn.execute(sql)
data = res.fetchall()
for k in range(10):
    print data[k]

print '...'
print '(total number of track IDs: %d)' % len(data)
tdb.query('select tid from tids where rowid = 1')
tag = tdb.query('select tid from tids where rowid = 1')[0]
tag
tag = tag[0]
tdb.query('select tag from tags where rowid = 1')
track = tag
tag = tdb.query('select tag from tags where rowid = 1')
tag = tag[0][0]
track, tag
mxm = mxmdb()
mxm.query("select * from trackdata where track_id = '{}'.format(track)")
mxm.query("select * from trackdata where track_id = '{}'".format(track))
mxm.query('create table trackdata(track_id TEXT primary key, song_id TEXT, song_name TEXT, artist TEXT)')
mxm.showTables()
 = open('unique_tracks.txt', 'r')
lines = f.readlines()
lines[:5]
l = lines[0].split('<SEP>')
l
l = lines[0].strip().split('<SEP>')
f = open('unique_tracks.txt', 'r')
lines = f.readlines()
lines[:5]
lines = [l.strip().replace("'","").split('<SEP>') for l in lines]
lines[:5]
for l in lines:
    tid,sid,art,song = l
    mxm.query("insert into trackdata values('{}','{}','{}','{}')".format(tid,sid,art,song))
    
mxm.query('select * from trackdata limit 5')
mxm.c.commit()
mxm.conn.commit()
mxm.query('alter table lyrics rename to lyrics_old')
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

q = "CREATE TABLE lyrics (track_id,"
q += " mxm_tid INT,"
q += "song_id TEXT,"
q += " word TEXT,"
q += " count INT,"
q += " is_test INT,"
q += " FOREIGN KEY(word) REFERENCES words(word))"
mxm.query(q)
mxm.showTables()

mxm.query('insert into lyrics (track_id, mxm_tid, song_id, word, count, is_test) select a.track_id, a.mxm_tid, b.song_id, a.word, a.count, a.is_test from lyrics_old as a INNER JOIN trackdata as b ON a.track_id = b.track_id')
mxm.query('select * from lyrics limit 5')

mxm.query('drop table lyrics_old')
mxm.query('alter table lyrics_old rename to lyrics')
_res = mxm.query('select song_id from lyrics')
u_res = udb.query('select song_id from userdata')

import gc
gc.collect()
udb = userdb()
_res = mxm.query('select song_id from lyrics')
u_res = udb.query('select song_id from userdata')

overlap = set(l_res).intersection(set(u_res))
len(overlap)

overlap = set(_res).intersection(set(u_res))
len(overlap)

overlap = list(overlap)
overlap[0]
overlap = [l[0] for l in overlap]
overlap[0]

with open('overlapping_songs.txt', 'w') as out:
    out.write('\n'.join(overlap))
    
del(overlap)
del(_res, u_res)
outfilename
overlap = open('overlapping_tracks.txt', 'r').readlines()
overlap = open('overlapping_songs.txt', 'r').readlines()
overlap[:5]
overlap = [o.strip() for o in overlap]
t_tracks = tdb.query('select tid from tids')
len(t_tracks)
t_tracks[:2]
ttracks = [t[0][0] for t in t_tracks]
del(t_tracks)
ttracks[:2]
ttracks
t_tracks = tdb.query('select tid from tids')
ttracks[0][0]
ttracks[0]
t_tracks[0][0]
ttracks = [t[0][0] for t in t_tracks]
ttracks[0]
ttracks = [t[0] for t in t_tracks]
ttracks[0]
tag_overlap = set(overlap).intersection(set(ttracks))
len(tag_overlap)
overlap[0]
mxm.query("select track_id from trackdata where song_id = '{}'".format(overlap[0]))
mxm.query("select track_id from trackdata where song_id = '{}'".format(overlap[0]))[0][0]
overlap_tracks = []
overlap_tracks = [mxm.query("select track_id from trackdata where song_id = '{}'".format(o))[0][0] for o in tqdm(overlap)]
res = mxm.query('select track_id, song_id from trackdata')
len(res)
res[0]
songToTrack = {t[1]:t[0] for t in res}
overlap_tracks = [songToTrack[o] for o in tqdm(overlap)]
songToTrack[overlap[0]]
save_obj(songToTrack, 'songToTrack')
overlap_tracks[:3]
res = set(overlap_tracks).intersection(set(ttracks))
len(res)
res = list(res)
res[:5]
save_obj(res, 'final_overlap')
q = "CREATE TABLE lyrics_sub (track_id,"
q += " mxm_tid INT,"
q += "song_id TEXT,"
q += " word TEXT,"
q += " count INT,"
q += " is_test INT,"
q += " FOREIGN KEY(word) REFERENCES words(word))"
mxm.query(q)
trackstr = ', '.join([t for t in res])
trackstr[:20]
trackstr[:200]
mxm.query("insert into lrics_sub select * from lyrics where track_id in ({})".format(trackstr))
mxm.query("insert into lyrics_sub select * from lyrics where track_id in ({})".format(trackstr))
mxm.query("insert into lyrics_sub select * from lyrics where track_id in ('{}')".format(trackstr))
mxm.showTables()
mxm.query('select * from lyrics_sub limit 5')
res = mxm.query("select * from lyrics where track_id in ('{}')".format(trackstr))
len(res)
mxm.query('select * from lyrics limit 5')
trackstr[:200]
ltracks = mxm.query('select track_id from lyrics')
ltracks[0]
ltracks = [l[0] for l in ltracks]
len(ltracks)
mxm.query("select * from lyrics where track_id in ('TRHAGFQ128F428B8EA')")
trackstr = ', '.join(['{}'.format(t) for t in res])
mxm.query("insert into lyrics_sub select * from lyrics where track_id in ('{}')".format(trackstr))
mxm.query('select * from lyrics_sub limit 5')
trackstr[:200]
final_overlap =  load_obj('final_overlap')
final_overlap[:5]
trackstr = ', '.join(['{}'.format(t) for t in final_overlap])
trackstr[:200]
mxm.query("insert into lyrics_sub select * from lyrics where track_id in ({})".format(trackstr))
mxm.query("insert into lyrics_sub select * from lyrics where track_id in ('{}')".format(trackstr))
mxm.query('select * from lyrics_sub limit 5')
trackstr[:200]
trackstr = ', '.join(['{}'.format(t) for t in final_overlap])
trackstr[:200]
['{}'.format(t) for t in final_overlap]
trackstr = ', '.join(["'{}'".format(t) for t in final_overlap])
trackstr[:200]
mxm.query("insert into lyrics_sub select * from lyrics where track_id in ({})".format(trackstr))
mxm.q = mxm.query
mxm.q('select * from lyrics_sub limit 5')
mxm.q('select count(*) from lyrics_sub')
mxm.N
mxm.q('select count(*) from lyrics')
float(9221374) / 19045332
mxm.conn.commit()
udb.showTables()
q = "CREATE TABLE userdata_sub (user_id TEXT,"
q += " song_id TEXT,"
q += "count INT)"

udb.query(q)
udb.showTables()
overlap
len(overlap)
len(final_overlap)
final_song_overlaps = load_obj('final_overlap')
final_song_overlaps[:2]
trackToSong = {v:k for k,v in songToTrack.items()}
trackToSong[final_overlap[0]]
final_songs = [trackToSong[t] for t in final_overlap]
final_songs[:3]
save_obj(final_songs, 'final_songs')
save_obj(final_overlap, 'final_tracks')
songstr = [', '.join(["'{}'".format(s) for s in final_songs])]
songstr[:200]
songstr = ', '.join(["'{}'".format(s) for s in final_songs])
songstr[:200]
udb.query("insert into userdata_sub select * from userdata where song_id in ({})".format(songstr))
udb.q = udb.query
udb.q('select count(*) from userdata_sub')
udb.q('select count(*) from userdata')
udb.conn.commit()
gc.collect()
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
udb = get_user_dists(udb)
udb.user_dists.values()items()[0]
udb.user_dists.items()[0]
udb.user_dist.keys()[:3]
udb.user_dists.keys()[:3]
def sparse_cos_sim(d1,d2):
    common_keys = set(d1.keys()).intersection(set(d2.keys()))
    num = 0
    for k in common_keys: num += d1[k]*d2[k]
    denom = np.linalg.norm(d1.values()) * np.linalg.norm(d2.values())
    return float(num) / denom
ud = udb.user_dists
k1 = '85c1f87fea955d09b4bec2e36aee110927aedf9a'
k2 = '5b1643f46a5e379eaebd26b32da8614e29d28dec'
sparse_cos_sim(ud[k1],ud[k2])
len(ud)
counter = 0
for v in ud.values():
    if len(v) == 0:
        counter +=1
        
counter
ud[k2]
ud[k1]
sparse_cos_sim(ud[k1],ud[k1])
sims = [(k,sparse_cos_sim(ud[k],ud[k1])) for k in ud.keys()]
sims = [(k,sparse_cos_sim(ud[k],ud[k1])) for k in tqdm(ud.keys())]
sorted(sims, key=lambda x:x[1], reverse=True)[:10]
lens = [len(v) for v in ud.values()]
np.mean(lens)
np.min(lens)
ud['9d96462f6b833abe4fb4e8a2a73e9011f5384b6c']
def filter_users(db, n, songlist=None):
    filt_tups = []
    if not songlist: songlist = db.valid_songs
    for k,v in db.user_dists.items():
        if len(set(v).intersection(songlist)) > n:
            filt_tups.append((k,v))
    return dict(filt_tups)
final_songs
users = filter_users(udb,30,final_songs)
def filter_users(db, n, songlist=None):
    filt_tups = []
    if not songlist: songlist = db.valid_songs
    for k,v in tqdm(db.user_dists.items()):
        if len(set(v).intersection(songlist)) > n:
            filt_tups.append((k,v))
    return dict(filt_tups)
users = filter_users(udb,30,final_songs)
db[k1]
ud[k1]
def filter_users(db, n, songlist=None):
    filt_tups = []
    if not songlist: songlist = db.valid_songs
    for k,v in tqdm(db.user_dists.items()):
        if len(set(v.keys()).intersection(songlist)) > n:
            filt_tups.append((k,v))
    return dict(filt_tups)
users = filter_users(udb,30,final_songs)
songlist[:5]
final_songs[:5]
def filter_users(db, n, songlist=None):
    filt_tups = []
    if not songlist: songlist = db.valid_songs
    for k,v in tqdm(db.user_dists.items()):
        if len(set(v.keys()).intersection(set(songlist))) > n:
            filt_tups.append((k,v))
    return dict(filt_tups)
users = filter_users(udb,30,final_songs)
def filter_users(db, n, songlist=None):
    filt_tups = []
    if not songlist: songlist = db.valid_songs
    songlist = set(songlist)
    for k,v in tqdm(db.user_dists.items()):
        if len(set(v.keys()).intersection(songlist)) > n:
            filt_tups.append((k,v))
    return dict(filt_tups)
users = filter_users(udb,30,final_songs)
len(users)
res = mxm.q('select song_id, word, count from lyrics')
res[:5]
def buildSongVocab(songdb, songlist=None):
    if not songlist: songlist = songdb.getSongs()
    vocabs = {s:{} for s in songlist}
    songlist = set(songlist)
    print('pulling data from db...')
    rows = songdb.query('select song_id, word, count from lyrics')
    for sid, word, ct in rows:
        vocabs[sid][word] = vocabs[sid].get(word,0) + ct
    return vocabs
def buildSongVocab(songdb, songlist=None):
    if not songlist: songlist = songdb.getSongs()
    vocabs = {s:{} for s in songlist}
    songlist = set(songlist)
    print('pulling data from db...')
    rows = songdb.query('select song_id, word, count from lyrics')
    for sid, word, ct in tqdm(rows):
        vocabs[sid][word] = vocabs[sid].get(word,0) + ct
    return vocabs
song_vocabs = buildSongVocab(mxm, final_songs)
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
res = buildSongVocabs(mxm, final_songs)
res.items()[0]
def buildUserVocab(userdict, songdict):
    uservocabs = {k:{} for k in userdict.keys()}
    for user, songs in tqdm(userdict.items()):
        for song in songs:
            for k,count in songdict[song].items():
                uservocabs[user][k] = uservocabs[user].get(k,0) + count
    return uservocabs
users.keys()[0]
songdict = res
res = buildUserVocab(users, songdict)