import player
import pickle
try:
    userfile=open('username.dat','rb')
    userfile.close()
except:
    userfile=open('username.dat','wb')
    pickle.dump([],userfile)
    userfile.close()
try:
    score=open('score.dat','rb')
    score.close()
except:
    score=open('score.dat','wb')
    pickle.dump([],score)
    score.close()
try:
    high=open('high_score.dat','rb')
    high.close()
except:
    high=open('high_score.dat','wb')
    pickle.dump([0,''],high)
    high.close()
player.main()
