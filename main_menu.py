def main(user_name):
    import pygame
    import flash
    import player
    import pickle
    import stats
    import highsc
    pygame.init()

    username=open('username.dat','rb')
    pers_score=open('score.dat','rb')
    userlt=pickle.load(username)
    scorelist=pickle.load(pers_score)
    if user_name.lower() in userlt:
        pos=userlt.index(user_name)
        username.close()
        pers_score.close()
    else:
        userlt.append(user_name.lower())
        scorelist.append([0,0,0])
        username.close()
        pers_score.close()
        username=open('username.dat','wb')
        pers_score=open('score.dat','wb')
        pickle.dump(userlt,username)
        pickle.dump(scorelist,pers_score)
        username.close()
        pers_score.close()

    font=pygame.font.Font(None,40)
    h_font=pygame.font.Font('EDU.ttf',50)

    background_colour = (234, 212, 252)
    black=(0,0,0)
    white=(255,255,255)
    purple=(102,0,102)
    green=(0,200,0)
    blue=(0,0,255)
    red=(255,0,0)
    yellow=(255,255,0)

    win = pygame.display.set_mode((660, 400))
    pygame.display.set_caption('FlashCards')
    win.fill(background_colour)

    b1text=h_font.render('Main Menu',True,red,background_colour)
    b1surf=b1text.get_rect()
    b1surf.center=(330,50)
    win.blit(b1text,b1surf)

    b1text=font.render('Play',True,green,background_colour)
    b1surf=b1text.get_rect()
    b1surf.center=(330,150)
    win.blit(b1text,b1surf)

    b2text=font.render('Stats',True,green,background_colour)
    b1surf=b2text.get_rect()
    b1surf.center=(330,200)
    win.blit(b2text,b1surf)

    b3text=font.render('Total High Score',True,green,background_colour)
    b1surf=b3text.get_rect()
    b1surf.center=(330,250)
    win.blit(b3text,b1surf)

    b4text=font.render('Change Profile',True,green,background_colour)
    b1surf=b4text.get_rect()
    b1surf.center=(330,300)
    win.blit(b4text,b1surf)

    pygame.display.flip()
    running = True
    while running:
                    for event in pygame.event.get():    
                                    if event.type == pygame.QUIT:
                                                    running = False
                    if pygame.mouse.get_pressed()[0]==1 and pygame.mouse.get_pos()[0] in range(296,361) and pygame.mouse.get_pos()[1] in range(133,165):
                            running=False
                            pygame.quit()
                            flash.main(user_name)
                    if pygame.mouse.get_pressed()[0]==1 and pygame.mouse.get_pos()[0] in range(293,367) and pygame.mouse.get_pos()[1] in range(185,211):
                            running=False
                            pygame.quit()
                            stats.main(user_name)
                    if pygame.mouse.get_pressed()[0]==1 and pygame.mouse.get_pos()[0] in range(216,441) and pygame.mouse.get_pos()[1] in range(233,269):
                            running=False
                            pygame.quit()
                            highsc.main(user_name)
                    if pygame.mouse.get_pressed()[0]==1 and pygame.mouse.get_pos()[0] in range(226,435) and pygame.mouse.get_pos()[1] in range(282,319):
                            running=False
                            pygame.quit()
                            player.main()
    pygame.quit()
