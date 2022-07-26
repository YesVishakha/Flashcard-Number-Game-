def choose_ran():
    import random
    lt=[0,1,2,3,4,5,6,7,8,9,10]
    global num1
    global num2
    num1=random.choice(lt)
    num2=random.choice(lt)
    
def img_name():
    img1=""+str(num1)+".png"
    img2=""+str(num2)+".png"
    return [img1,img2]

def check_ans(ans):
    try:
        if int(ans)==(num1+num2):
            return False
        else:
            return True
    except:
        return True
def main(user_name,n,score):
    import pygame
    import answer
    import main_menu

    if n==0:
        main_menu.main(user_name)
    pygame.init()

    global font
    font=pygame.font.Font('BRUSHSCI.ttf',30)
    base_font = pygame.font.Font(None, 32)
    
    background_colour = (234, 212, 252)
    black=(0,0,0)
    grey=(169,169,169)
    white=(255,255,255)
    purple=(102,0,102)
    green=(0,200,0)
    blue=(0,0,255)
    red=(255,0,0)
    yellow=(255,255,0)
    
    global win
    win = pygame.display.set_mode((700, 600))
    pygame.display.set_caption('FlashCards')
    win.fill(background_colour)

    p_font=pygame.font.Font('BRUSHSCI.ttf',100)
    b1text=p_font.render('+',True,black,background_colour)
    b1surf=b1text.get_rect()
    b1surf.center=(320,250)
    win.blit(b1text,b1surf)

    choose_ran()
    lt=img_name()
    img1,img2=lt[0],lt[1]
    image1 = pygame.image.load(img1)
    win.blit(image1,(80,100))
    image2 = pygame.image.load(img2)
    win.blit(image2,(380,100))

    user_text = ''
    input_rect = pygame.Rect(290, 450,50,40)

    b1text=base_font.render('SUBMIT',True,black,grey)
    b1surf=b1text.get_rect()
    b1surf.center=(340,520)
    win.blit(b1text,b1surf)
    
    b2text=base_font.render('HOME',True,black,background_colour)
    b2surf=b1text.get_rect()
    b2surf.center=(50,25)
    win.blit(b2text,b2surf)

    for i in range(n):
        image2 = pygame.image.load('lives.png')
        win.blit(image2,(560+(i*25),25))
    
    pygame.display.flip()
    running = True
    while running:
            for event in pygame.event.get():	
                    if event.type == pygame.QUIT:
                            running = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            user_text = user_text[:-1]
                        else:
                            user_text += event.unicode
            pygame.draw.rect(win, yellow, input_rect)
            text_surface = base_font.render(user_text, True, black)
            win.blit(text_surface, (input_rect.x+5, input_rect.y+5))
            input_rect.w = max(100, text_surface.get_width()+10)
            pygame.display.flip()
            if pygame.mouse.get_pressed()[0]==1 and pygame.mouse.get_pos()[0] in range(298,383) and pygame.mouse.get_pos()[1] in range(509,532):
                running=check_ans(user_text)
                if not running:
                    running=False
                    pygame.quit()
                answer.ans(not running,0,n,user_name,score)
            if pygame.mouse.get_pressed()[0]==1 and pygame.mouse.get_pos()[0] in range(7,75) and pygame.mouse.get_pos()[1] in range(14,35):
                main_menu.main(user_name)
    pygame.quit()

