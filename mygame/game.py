import pygame
import random
import sys
from time import sleep
def main():
    global game, settings
    width, height = 1280, 720

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Awesome Game')
    icon = pygame.image.load('warlord-helmet.png')
    pygame.display.set_icon(icon)

    fps = 60
    clock = pygame.time.Clock()
    run = True
    keys = None
    score = 0
    objectives = None
    game = False
    menu = True
    settings = False
    #default-options
    Bullet_endsize = 100
    amount_of_bullet = 30
    player_width, player_height = 100, 100

    class Player(object):
        def __init__(self, name, x, y, color):

            self.name = name
            self.width, self.height = player_width, player_height
            self.x = x
            self.y = height - y
            self.vel = 2
            self.color = color
            self.player = pygame.Rect(self.x - self.width/2, self.y - self.height/2, self.width, self.height)
        def render(self):
            pygame.draw.rect(screen, self.color,self.player, 2, 3)
        
        def movement_check(self):
            if keys[pygame.K_a]:
                if self.player.x < 0:
                    self.player.x = 0
                else:
                    self.player.x -= self.vel
            if keys[pygame.K_d]:
                if self.player.x > width - self.width:
                    self.player.x = width - self.width
                else:
                    self.player.x += self.vel
            if keys[pygame.K_s]:
                if self.player.y > height - self.height:
                    self.player.y = height - self.height
                else:
                    self.player.y += self.vel
            if keys[pygame.K_w]:
                if self.player.y < 0:
                    self.player.y = 0
                else:
                    self.player.y -= self.vel
            if keys[pygame.K_LCTRL]:
                self.vel = 1.5
            elif keys[pygame.K_LSHIFT]:
                self.vel = 6
            else:
                self.vel = 3

    p1 = Player('p1', (width/2), (height/2), (50, 50, 230))

    class Bullet(object):
        def __init__(self):
            self.x, self.y = random.randint(0, width), random.randint(0, height)
            self.width = 300
            self.height = 300
            self.color = (75, 0, 100)
            self.charge = 300
            self.difficulty = 2.5
            self.reattack = 50
            self.bullet = pygame.Rect(self.x - self.width/2, self.y - self.height/2, self.width, self.height)
        
        def attack(self):
            global game, objs, objectives
            if self.reattack <= 0:
                self.__init__()
                
            elif self.charge < Bullet_endsize:
                if p1.player.colliderect(self.bullet):
                    self.__init__()
                    objectives = False
                    game = False
                self.color = (230, 20, 20)
                self.width , self.height = Bullet_endsize , Bullet_endsize
                pygame.draw.rect(screen, self.color,self.bullet, 2, 3)
                self.reattack -= 1
                    
            else:
                self.charge -= self.difficulty
                self.bullet.width = 100 * (self.charge/100)
                self.bullet.height = 100 * (self.charge/100)
                self.bullet.centerx, self.bullet.centery = self.x , self.y
                pygame.draw.rect(screen, self.color,self.bullet, 2, 3)
    """ 
    try:
        Bullet_endsize_cache = input('set Bullet size (default=100, cant be under 50):\n')
        if Bullet_endsize_cache == '':
            pass
        elif int(Bullet_endsize_cache) < 50:
            print('Bullet size cant be under 50')
            pygame.quit()
            quit()
        else:
            Bullet_endsize = int(Bullet_endsize_cache)
    except ValueError:
        print('Wrong Value was given')
        pygame.quit()
        quit()
    try:
        amount_of_bullet_cache = input('set Bullets amount (default=30):')
        if amount_of_bullet_cache == '':
            pass
        elif int(amount_of_bullet_cache) == 0:
            print('Bullet size cant be 0')
            pygame.quit()
            quit()
        else:
            amount_of_bullet_cache = int(amount_of_bullet_cache)
    except ValueError:
        print('Wrong Value was given')
        pygame.quit()
        quit()
    """
    font = pygame.font.Font('./fonts/MALDINISTYLE.ttf', 60)
    small_font = pygame.font.Font('./fonts/MALDINISTYLE.ttf', 44)
    
    #score
    score_label = font.render(str(score), True, (60, 60, 60))
    score_labelRect = score_label.get_rect()
    score_labelRect.center = (width / 2, height / 20)
    
    #title
    MainText = font.render('My Awesome Game', True, (60, 60, 60))
    MainText_Rect = MainText.get_rect()
    MainText_Rect.center = (width / 2, height / 5)
    
    #main menu 
    Playtext = font.render('Play', True, (60, 60, 60))
    Playtext_Rect = Playtext.get_rect()
    Playtext_Rect.center = (width / 2, height / 2 - 40)
    
    Settingstext = font.render('Settings', True, (60, 60, 60))
    Settingstext_Rect = Settingstext.get_rect()
    Settingstext_Rect.center = (width / 2, height / 2 + 40)
    
    Quittext = font.render('Quit', True, (60, 60, 60))
    Quittext_Rect = Quittext.get_rect()
    Quittext_Rect.center = (width / 2, height / 2 + 120)
    
    #settings
    size_text = font.render('Bullet Size', True, (60, 60, 60))
    size_text_rect = size_text.get_rect()
    size_text_rect.center = (width / 2, height / 2 - 40)
    
    val1 = font.render(('< ' + str(Bullet_endsize) + ' >'), True, (60, 60, 60))
    val1_rect = val1.get_rect()
    val1_rect.center = (width / 2, height / 2 + 40)
    
    amount = font.render('Bullet Amount', True, (60, 60, 60))
    amount_rect = amount.get_rect()
    amount_rect.center = (width / 2, height / 2 + 120)
    
    val2 = font.render(('< ' + str(amount_of_bullet) + ' >'), True, (60, 60, 60))
    val2_rect = val2.get_rect()
    val2_rect.center = (width / 2, height / 2 + 200)
    
    Back = small_font.render('Main Menu', True, (60, 60, 60))
    Back_rect = Back.get_rect()
    Back_rect.center = (width / 6, height / 2 + 280)
    
    
    #endgame
    menutext = font.render('Main Menu', True, (60, 60, 60))
    menutext_Rect = menutext.get_rect()
    menutext_Rect.center = (width / 2, height / 2 + 40)
    
    gameend_score = font.render(('Your Score is ' + str(int(score))), True, (60, 60, 60))
    gameend_score_Rect = gameend_score.get_rect()
    gameend_score_Rect.center = (width / 2, height / 2 + 120)

    
    
    while run:
        clock.tick(fps)
        screen.fill((220,220,220))

        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            if keys[pygame.K_j]:
                game = False
                print(str(game))
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                width_check = (width/2 - 150) <= mouse[0] <= (width/2 + 150)
                if menu:
                    #play button event
                    if width_check and (height/2 - 70) <= mouse[1] <= (height/2 - 10):
                        menu = False
                        objectives = False
                        game = True
                    
                    #settings button event
                    if width_check and (height/2 + 10) <= mouse[1] <= (height/2 + 70):
                        menu = False
                        settings = True
                    
                    #quit button event
                    if width_check and (height/2 + 90) <= mouse[1] <= (height/2 + 140):
                        pygame.quit()
                        quit()
                
                elif settings:
                    print(mouse)
                    #Main Menu button event
                    if (width/6 - 100) <= mouse[0] <= (width/6 + 100) and (height/2 + 260) <= mouse[1] <= (height/2 + 300):
                        menu = True
                        settings = False
                    
                
                elif game == False:
                    #play button event
                    if width_check and (height/2 - 70) <= mouse[1] <= (height/2 - 10):
                        objectives = False
                        game = True
                
                    #main menu button event
                    if width_check and (height/2 + 10) <= mouse[1] <= (height/2 + 70):
                        menu = True
                    
        ''' print(str(mouse)) '''
        #menu
        if menu:
            screen.blit(MainText, MainText_Rect)
            screen.blit(Playtext, Playtext_Rect)
            screen.blit(Settingstext, Settingstext_Rect)
            screen.blit(Quittext, Quittext_Rect)
            
        elif settings == True:
            screen.blit(MainText, MainText_Rect)
            screen.blit(size_text,size_text_rect)
            screen.blit(val1,val1_rect)
            screen.blit(amount,amount_rect)
            screen.blit(val2,val2_rect)
            screen.blit(Back,Back_rect)
            
        else:
        #game
            if game:        
                p1.render()
                p1.movement_check()
                if objectives == False:
                    objs = []
                    objs = [Bullet() for i in range(amount_of_bullet)]
                    objectives = True
                    sleep(0.1)
                elif objectives:
                    score_label = font.render(str(int(score)), True, (60, 60, 60))
                    screen.blit(score_label, score_labelRect)
                    score += 1/60
                    for obj in objs:
                        try:
                            obj.attack()
                        except:
                            pass
            elif game == False:
                screen.blit(MainText, MainText_Rect)
                screen.blit(Playtext, Playtext_Rect)
                screen.blit(menutext, menutext_Rect)
                gameend_score = font.render(('Your Score is ' + str(int(score))), True, (60, 60, 60))
                screen.blit(gameend_score, gameend_score_Rect)

        pygame.display.update()

if __name__ == '__main__':
    main()