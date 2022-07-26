def main():
    import pygame
    import main_menu
    pygame.init()

    font=pygame.font.Font('EDU.ttf',50)
    font1=pygame.font.Font('EDU.ttf',35)
    base_font = pygame.font.Font(None, 26)

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

    b1text=font.render('WELCOME',True,red,background_colour)
    b1surf=b1text.get_rect()
    b1surf.center=(300,100)
    win.blit(b1text,b1surf)

    b1text=font.render('Enter your name : ',True,white,background_colour)
    b1surf=b1text.get_rect()
    b1surf.center=(200,200)
    win.blit(b1text,b1surf)

    user_name = ''
    input_rect = pygame.Rect(420, 180,100,80)

    b1text=base_font.render('Please press Enter key to continue',True,blue,background_colour)
    b1surf=b1text.get_rect()
    b1surf.center=(200,350)
    win.blit(b1text,b1surf)

    pygame.display.flip()
    running = True
    while running:
                    for event in pygame.event.get():	
                            if event.type == pygame.QUIT:
                                                    running = False
                            if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_BACKSPACE:
                                            user_name = user_name[:-1]
                                    elif event.key == pygame.K_RETURN:
                                            running=False
                                            pygame.quit()
                                            main_menu.main(user_name)
                                    else:
                                            user_name += event.unicode
                    pygame.draw.rect(win, background_colour, input_rect)
                    text_surface = font1.render(user_name, True, green)
                    win.blit(text_surface, (input_rect.x+5, input_rect.y+5))
                    input_rect.w = max(100, text_surface.get_width()+10)
                    pygame.display.flip()
    pygame.quit()
