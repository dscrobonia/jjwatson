import nfldb
import nflgame

db = nfldb.connect()

#player, dist = nfldb.player_search(db, 'tom brady')

#for some in player:
#    print some

#print player

q = nfldb.Query(db).game(season_year=2015, season_type='Regular', week=10)



res = q.aggregate(passing_yds__ge=1)
for o in res.as_aggregate():
    print o.player, o.passing_yds


julio, dist = nfldb.player_search(db, 'Karlos Williams')
print 'looking for: %s' % (julio)
q1 = nfldb.Query(db).game(season_year=2015, season_type='Regular', week=10)
res1 = q1.aggregate()
for p in res1.as_aggregate():
    if p.player == julio:
        print p.player, o.rushing_yds
    #else:
    #    print p.player

'''
q_player = nfldb.Query(db).game(season_year=2015, season_type='Regular', week=10, name='Julio Jones')

print 'printing Query object'
print q_player
print 'printing aggergate()'
print q.aggregate()

'''






















