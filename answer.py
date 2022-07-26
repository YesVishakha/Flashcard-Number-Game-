def ans(corr,p,n,user_name,score):
    import pygame
    import pickle
    import subtraction
    import addition
    pygame.init()

    user=open('username.dat','rb')
    userlt=pickle.load(user)
    user.close()
    user_score=open('score.dat','rb')
    scorelt=pickle.load(user_score)
    user_score.close()
    high=open('high_score.dat','rb')
    highlt=pickle.load(high)
    high.close()
    pos=userlt.index(user_name)

    global font
    font=pygame.font.Font('BRUSHSCI.ttf',100)
    
    background_colour = (234, 212, 252)
    green=(0,200,0)
    blue=(0,0,255)
    red=(255,0,0)

    global win
    win = pygame.display.set_mode((700, 600))
    pygame.display.set_caption('FlashCards')
    win.fill(background_colour)

    if corr:
        b1text=font.render('CORRECT !',True,(0,200,0),(234, 212, 252))        
        score=score+1
        scorelt[pos][1]=scorelt[pos][1]+1
        user_score=open('score.dat','wb')
        pickle.dump(scorelt,user_score)
        user_score.close()
    else:
        b1text=font.render('WRONG',True,(255,0,0),(234, 212, 252))
        scorelt[pos][2]=scorelt[pos][1]+1
        user_score=open('score.dat','wb')
        pickle.dump(scorelt,user_score)
        user_score.close()
        n=n-1
        if n==0:
            b1text=font.render('GAME OVER',True,(255,0,0),(234, 212, 252))
            b2text=font.render('Score :- '+str(score),True,(255,0,0),(234, 212, 252))
            b1surf=b2text.get_rect()
            b1surf.center=(350,400)
            win.blit(b2text,b1surf)
    b1surf=b1text.get_rect()
    b1surf.center=(350,250)
    win.blit(b1text,b1surf)
    
    pygame.display.flip()

    if score>scorelt[pos][0]:
        scorelt[pos][0]=score
        user_score=open('score.dat','wb')
        pickle.dump(scorelt,user_score)
        user_score.close()

    if score>highlt[0]:
        highlt[0]=score
        highlt[1]=user_name
        high=open('high_score.dat','wb')
        pickle.dump(highlt,high)
        high.close()
    
    pygame.time.wait(1000)
    pygame.quit()
    if(p==0):
        addition.main(user_name,n,score)
    else:
        subtraction.main(user_name,n,score)
