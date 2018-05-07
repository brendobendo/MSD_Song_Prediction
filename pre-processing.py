import os
ldf = pd.read_csv('ldf_all_final.csv')
songlist = ldf['song_id'].tolist()
mxm = mxmdb()
mxm.vocab = set(np.random.choice(list(mxm.vocab), size=1500
mxm.sv = buildSongVocabs(mxm, songlist)
if os.path.isfile('tfidf.pkl'): mxm.tfidf = load_obj('tfidf')
else: mxm.tfidf = mxm.buildTFIDFMat()
mxm = filter_vocab(1500, mxm)

udb = userdb()
udb.get_user_dists(songList=songlist)
user_dists = filter_users(udb, 20, songlist)
user_dists = dict(user_dists.items()[:80000])
udb.user_dists = user_dists
udb.users = set(udb.user_dists.keys())
save_obj(udb.user_dists, 'user_dists_final')
if os.path.isfile('user_vocab_final'):  udb.uv = load_obj('user_vocab_final')
else: udb.uv = buildUserVocabs(mxm,udb.user_dists, mxm.sv, tfidf=True)

tracklist = [mxm.songToTrack[s] for s in songlist]
tdb = tagdb(trackList=tracklist)
tdb.buildTrackTags()

dbc = db_container(mxm,udb,tdb)
dbc.buildUserTags()
