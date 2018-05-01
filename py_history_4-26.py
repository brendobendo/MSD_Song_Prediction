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


runfile('/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW1/DocAnalyzer.py', wdir='/Users/babraham/Google Drive/Grad_School/Spring_2018/Text_Mining/HW1')
da = DocAnalyzer(N=1)
da = loadDir(da, './yelp/train')

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