def main(user_name):
    import pygame
    import addition
    import subtraction
    pygame.init()

    font1=pygame.font.Font('EDU.ttf',50)
    font=pygame.font.Font(None,50)

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

    b1text=font1.render('Choose Problem '+user_name,True,red,background_colour)
    b1surf=b1text.get_rect()
    b1surf.center=(300,100)
    win.blit(b1text,b1surf)

    b1text=font.render('ADDITION',True,green,background_colour)
    b1surf=b1text.get_rect()
    b1surf.center=(160,200)
    win.blit(b1text,b1surf)

    b1text=font.render('SUBTRACTION',True,green,background_colour)
    b1surf=b1text.get_rect()
    b1surf.center=(470,200)
    win.blit(b1text,b1surf)

    pygame.display.flip()
    running = True
    while running:
                    for event in pygame.event.get():    
                                    if event.type == pygame.QUIT:
                                                    running = False
                    if pygame.mouse.get_pressed()[0]==1 and pygame.mouse.get_pos()[0] in range(33,267) and pygame.mouse.get_pos()[1] in range(169,231):
                            running=False
                            pygame.quit()
                            addition.main(user_name,5,score=0)
                    if pygame.mouse.get_pressed()[0]==1 and pygame.mouse.get_pos()[0] in range(322,618) and pygame.mouse.get_pos()[1] in range(170,230):
                            running=False
                            pygame.quit()
                            subtraction.main(user_name,5,score=0)
    pygame.quit()
