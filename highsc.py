def main(user_name):
    import pygame
    import pickle
    import main_menu
    pygame.init()

    user_name=user_name.lower()
    font1=pygame.font.Font('HelloWorld.otf',80)
    font=pygame.font.Font('Delmon Delicate.ttf',30)
    base_font = pygame.font.Font(None, 32)

    high=open('high_score.dat','rb')
    highlt=pickle.load(high)
    high.close()

    background_colour = (234, 212, 252)
    black=(0,0,0)
    white=(255,255,255)
    grey=(169,169,169)
    purple=(102,0,102)
    green=(0,200,0)
    blue=(0,0,255)
    red=(255,0,0)
    yellow=(255,255,0)

    win = pygame.display.set_mode((660, 400))
    pygame.display.set_caption('FlashCards')
    win.fill(background_colour)

    b1text=font1.render('HIGH SCORE ',True,red,background_colour)
    b1surf=b1text.get_rect()
    b1surf.center=(350,100)
    win.blit(b1text,b1surf)

    b1text=font.render('HIGHEST SCORE : ----->  '+str(highlt[0]),True,green,background_colour)
    b1surf=b1text.get_rect()
    b1surf.center=(340,200)
    win.blit(b1text,b1surf)

    b1text=font.render('BY : ----->  '+str(highlt[1]),True,green,background_colour)
    b1surf=b1text.get_rect()
    b1surf.center=(270,250)
    win.blit(b1text,b1surf)

    b1text=base_font.render('BACK' ,True,red,background_colour)
    b1surf=b1text.get_rect()
    b1surf.center=(330,350)
    win.blit(b1text,b1surf)

    pygame.display.flip()
    running = True
    while running:
                    for event in pygame.event.get():    
                                    if event.type == pygame.QUIT:
                                                    running = False
                    if pygame.mouse.get_pressed()[0]==1 and pygame.mouse.get_pos()[0] in range(297,363) and pygame.mouse.get_pos()[1] in range(338,363):
                        running=False
                        pygame.quit()
                        main_menu.main(user_name)
    pygame.quit()
