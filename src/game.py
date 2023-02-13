import pygame
import random
import os
from time import sleep , strftime
def main():
    global game, settings
    width, height = 1280, 720

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Awesome Game')
    icon = pygame.image.load('icon.png')
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
    saved_score = False
    #default-options
    Bullet_endsize = 75
    amount_of_bullet = 30
    difficulty = 4
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
                self.vel = 2
            elif keys[pygame.K_LSHIFT]:
                self.vel = 8
            else:
                self.vel = 4

    p1 = Player('p1', (width/2), (height/2), (50, 50, 230))

    class Bullet(object):
        def __init__(self):
            self.x, self.y = random.randint(0, width), random.randint(0, height)
            self.width = 300
            self.height = 300
            self.color = (75, 0, 100)
            self.charge = 300
            self.difficulty = difficulty
            self.reattack = 50
            self.bullet = pygame.Rect(self.x - self.width/2, self.y - self.height/2, self.width, self.height)
        
        def attack(self):
            global game, objectives, saved_score
            if self.reattack <= 0:
                self.__init__()
                
            elif self.charge < Bullet_endsize:
                if p1.player.colliderect(self.bullet):
                    self.__init__()
                    objectives = False
                    game = False
                    saved_score = False
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

    font = pygame.font.Font('./fonts/MALDINISTYLE.ttf', 60)
    small_font = pygame.font.Font('./fonts/MALDINISTYLE.ttf', 44)
    smallest_font = pygame.font.Font('./fonts/MALDINISTYLE.ttf', 30)
    
    #score
    score_label = font.render(str(score), True, (60, 60, 60))
    score_labelRect = score_label.get_rect()
    score_labelRect.center = (width / 2, score_labelRect.height + 20)
    
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
    
    #Bullet Size
    size_text = font.render('Bullet Size', True, (60, 60, 60))
    size_text_rect = size_text.get_rect()
    size_text_rect.center = (width / 3, height / 2 - 40)
    val1 = font.render(str(Bullet_endsize), True, (60, 60, 60))
    val1_rect = val1.get_rect()
    val1_rect.center = (width / 3, height / 2 + 40)
    minusplus1 = font.render('<      >', True, (60, 60, 60))
    minusplus1_rect = minusplus1.get_rect()
    minusplus1_rect.center = (width / 3, height / 2 + 40)
    
    #Bullet Amount
    amount = font.render('Bullet Amount', True, (60, 60, 60))
    amount_rect = amount.get_rect()
    amount_rect.center = (width / 2, height / 2 + 120)
    val2 = font.render(str(amount_of_bullet), True, (60, 60, 60))
    val2_rect = val2.get_rect()
    val2_rect.center = (width / 2, height / 2 + 200)
    minusplus2 = font.render('<      >', True, (60, 60, 60))
    minusplus2_rect = minusplus2.get_rect()
    minusplus2_rect.center = (width / 2, height / 2 + 200)
    
    
    #Difficulty
    Difficulty = font.render('Difficulty', True, (60, 60, 60))
    Difficulty_rect = Difficulty.get_rect()
    Difficulty_rect.center = ((width / 3)*2, height / 2 - 40)
    val3 = font.render(str(difficulty), True, (60, 60, 60))
    val3_rect = val3.get_rect()
    val3_rect.center = ((width / 3)*2, height / 2 + 40)
    minusplus3 = font.render('<      >', True, (60, 60, 60))
    minusplus3_rect = minusplus3.get_rect()
    minusplus3_rect.center = ((width / 3)*2, height / 2 + 40)
    
    #hard
    hard = smallest_font.render('Hard', True, (60, 60, 60))
    hard_rect = hard.get_rect()
    hard_rect.center = (width - hard_rect.width, height - hard_rect.height - 5)
    #middle
    medium = smallest_font.render('Middle', True, (60, 60, 60))
    medium_rect = medium.get_rect()
    medium_rect.center = (width - medium_rect.width + 10, height - hard_rect.height - medium_rect.height - 15)
    #easy
    easy = smallest_font.render('Easy', True, (60, 60, 60))
    easy_rect = easy.get_rect()
    easy_rect.center = (width - easy_rect.width, height - hard_rect.height - medium_rect.height - easy_rect.height - 25)
    
    #Main Menu
    Back = small_font.render('Main Menu', True, (60, 60, 60))
    Back_rect = Back.get_rect()
    Back_rect.center = (0 + Back_rect.width + 10, height - Back_rect.height - 10)
    
    
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
                    if Playtext_Rect.left <= mouse[0] <= Playtext_Rect.right and Playtext_Rect.top <= mouse[1] <= Playtext_Rect.bottom:
                        menu = False
                        objectives = False
                        game = True
                    
                    #settings button event
                    if Settingstext_Rect.left <= mouse[0] <= Settingstext_Rect.right and Settingstext_Rect.top <= mouse[1] <= Settingstext_Rect.bottom:
                        menu = False
                        settings = True
                    
                    #quit button event
                    if Quittext_Rect.left <= mouse[0] <= Quittext_Rect.right and Quittext_Rect.top <= mouse[1] <= Quittext_Rect.bottom:
                        pygame.quit()
                        quit()
                
                elif settings:
                    print(mouse)
                    #Main Menu button event
                    if (Back_rect.left) <= mouse[0] <= (Back_rect.right) and (Back_rect.top) <= mouse[1] <= (Back_rect.bottom):
                        menu = True
                        settings = False
                        
                        
                    #bulletsize
                        # < button event
                    if (width/3 - 100) <= mouse[0] <= (width/3 - 30) and (height/2 + 10) <= mouse[1] <= (height/2 + 70):
                        if 50 < Bullet_endsize:
                            Bullet_endsize -= 10
                        # > button event
                    if (width/3 + 40) <= mouse[0] <= (width/3 + 100) and (height/2 + 10) <= mouse[1] <= (height/2 + 70):
                        if Bullet_endsize < 200:
                            Bullet_endsize += 10
                        # center
                    if 50 <= Bullet_endsize < 100:
                        val1_rect.centerx = width / 3 + 5
                    elif Bullet_endsize == 200:
                        val1_rect.centerx = width / 3 - 5
                    else:
                        val1_rect.centerx = width / 3
                    
                    
                    
                    #bullet amount
                        # < button event
                    if (width/2 - 100) <= mouse[0] <= (width/2 - 30) and (height/2 + 170) <= mouse[1] <= (height/2 + 220):
                        if 0 < amount_of_bullet:
                            if amount_of_bullet == 10 or (amount_of_bullet < 10 and amount_of_bullet >= 1):
                                if amount_of_bullet == 1:
                                    pass
                                else:
                                    amount_of_bullet -= 1
                            else:
                                amount_of_bullet -= 10
                        # > button event
                    if (width/2 + 40) <= mouse[0] <= (width/2 + 100) and (height/2 + 170) <= mouse[1] <= (height/2 + 220):
                        if amount_of_bullet < 100:
                            if amount_of_bullet < 10 and amount_of_bullet >= 1:
                                amount_of_bullet += 1
                            else:
                                amount_of_bullet += 10
                        # center
                    if 10 <= amount_of_bullet < 100:
                        val2_rect.centerx = width / 2
                    elif amount_of_bullet == 1:
                        val2_rect.centerx = width / 2 + 15
                    elif amount_of_bullet < 10:
                        val2_rect.centerx = width / 2 + 10
                        
                    else:
                        val2_rect.centerx = width / 2 - 10
                        
                        
                        
                    #difficulty
                        # < button event
                    if (width/3*2 - 100) <= mouse[0] <= (width/3*2 - 30) and (height/2 + 10) <= mouse[1] <= (height/2 + 70):
                        if 1 < difficulty:
                            difficulty -= 1
                        # > button event
                    if (width/3*2 + 40) <= mouse[0] <= (width/3*2 + 100) and (height/2 + 10) <= mouse[1] <= (height/2 + 70):
                        if difficulty < 15:
                            difficulty += 1
                        # center
                    if 10 <= difficulty <= 15:
                        val3_rect.centerx = width / 3*2 - 5
                    elif 1 == difficulty:
                        val3_rect.centerx = width / 3*2 + 5
                    else:
                        val3_rect.centerx = width / 3*2
                    
                    
                    #easy
                    if easy_rect.left <= mouse[0] <= easy_rect.right and easy_rect.top <= mouse[1] <= easy_rect.bottom:
                        Bullet_endsize = 50
                        amount_of_bullet = 20
                        difficulty = 3
                        
                        
                        if 50 <= Bullet_endsize < 100:
                            val1_rect.centerx = width / 3 + 5
                        elif Bullet_endsize == 200:
                            val1_rect.centerx = width / 3 - 5
                        else:
                            val1_rect.centerx = width / 3
                        
                        
                        if 10 <= amount_of_bullet < 100:
                            val2_rect.centerx = width / 2
                        elif amount_of_bullet == 1:
                            val2_rect.centerx = width / 2 + 15
                        elif amount_of_bullet < 10:
                            val2_rect.centerx = width / 2 + 10
                        else:
                            val2_rect.centerx = width / 2 - 10
                            
                            
                        if 10 <= difficulty <= 15:
                            val3_rect.centerx = width / 3*2 - 5
                        elif 1 == difficulty:
                            val3_rect.centerx = width / 3*2 + 5
                        else:
                            val3_rect.centerx = width / 3*2
                        
                    #medium
                    if medium_rect.left <= mouse[0] <= medium_rect.right and medium_rect.top <= mouse[1] <= medium_rect.bottom:
                        Bullet_endsize = 75
                        amount_of_bullet = 30
                        difficulty = 4
                        
                        
                        if 50 <= Bullet_endsize < 100:
                            val1_rect.centerx = width / 3 + 5
                        elif Bullet_endsize == 200:
                            val1_rect.centerx = width / 3 - 5
                        else:
                            val1_rect.centerx = width / 3
                        
                        
                        if 10 <= amount_of_bullet < 100:
                            val2_rect.centerx = width / 2
                        elif amount_of_bullet == 1:
                            val2_rect.centerx = width / 2 + 15
                        elif amount_of_bullet < 10:
                            val2_rect.centerx = width / 2 + 10
                        else:
                            val2_rect.centerx = width / 2 - 10
                            
                            
                        if 10 <= difficulty <= 15:
                            val3_rect.centerx = width / 3*2 - 5
                        elif 1 == difficulty:
                            val3_rect.centerx = width / 3*2 + 5
                        else:
                            val3_rect.centerx = width / 3*2  
                            
                    #hard
                    if hard_rect.left <= mouse[0] <= hard_rect.right and hard_rect.top <= mouse[1] <= hard_rect.bottom:
                        Bullet_endsize = 100
                        amount_of_bullet = 30
                        difficulty = 5
                        
                        
                        if 50 <= Bullet_endsize < 100:
                            val1_rect.centerx = width / 3 + 5
                        elif Bullet_endsize == 200:
                            val1_rect.centerx = width / 3 - 5
                        else:
                            val1_rect.centerx = width / 3
                        
                        
                        if 10 <= amount_of_bullet < 100:
                            val2_rect.centerx = width / 2
                        elif amount_of_bullet == 1:
                            val2_rect.centerx = width / 2 + 15
                        elif amount_of_bullet < 10:
                            val2_rect.centerx = width / 2 + 10
                        else:
                            val2_rect.centerx = width / 2 - 10
                            
                            
                        if 10 <= difficulty <= 15:
                            val3_rect.centerx = width / 3*2 - 5
                        elif 1 == difficulty:
                            val3_rect.centerx = width / 3*2 + 5
                        else:
                            val3_rect.centerx = width / 3*2
                        
                
                elif game == False:
                    #play button event
                    if Playtext_Rect.left <= mouse[0] <= Playtext_Rect.right and Playtext_Rect.top <= mouse[1] <= Playtext_Rect.bottom:
                        objectives = False
                        game = True
                        saved_score = False
                        score = 0
                
                    #main menu button event
                    if menutext_Rect.left <= mouse[0] <= menutext_Rect.right and menutext_Rect.top <= mouse[1] <= menutext_Rect.bottom:
                        menu = True
                    
        ''' print(str(mouse)) '''
        #menu
        if menu:
            screen.blit(MainText, MainText_Rect)
            screen.blit(Playtext, Playtext_Rect)
            screen.blit(Settingstext, Settingstext_Rect)
            screen.blit(Quittext, Quittext_Rect)
            
        elif settings == True:
            val1 = font.render(str(Bullet_endsize), True, (60, 60, 60))
            val2 = font.render(str(amount_of_bullet), True, (60, 60, 60))
            val3 = font.render(str(difficulty), True, (60, 60, 60))
            
            screen.blit(MainText, MainText_Rect)
            
            screen.blit(size_text,size_text_rect)
            screen.blit(val1,val1_rect)
            screen.blit(minusplus1,minusplus1_rect)
            
            screen.blit(amount,amount_rect)
            screen.blit(val2,val2_rect)
            screen.blit(minusplus2,minusplus2_rect)
            
            screen.blit(Difficulty,Difficulty_rect)
            screen.blit(val3,val3_rect)
            screen.blit(minusplus3,minusplus3_rect)
            
            screen.blit(easy, easy_rect)
            screen.blit(medium, medium_rect)
            screen.blit(hard, hard_rect)
            
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
                if saved_score == False:
                    exist_scores = os.path.isfile('./scores.txt')
                    if exist_scores:
                        with open('./scores.txt', 'a', encoding='utf-8') as file:
                            file.writelines(('\n\nScore: ' + str(int(score)) + ' - ' + str(strftime('%Y-%M-%D %H:%M:%S'))))
                    else:
                        with open('./scores.txt', 'w', encoding='utf-8') as file:
                            file.writelines(('My Awesome Game Scores \n\n' + str(strftime('%Y-%M-%D %H:%M:%S')), '\n'))
                        with open('./scores.txt', 'a', encoding='utf-8') as file:
                            file.writelines(('\n\nScore: ' + str(int(score)) + ' - ' + str(strftime('%Y-%M-%D %H:%M:%S'))))
                    saved_score = True

                    
                screen.blit(MainText, MainText_Rect)
                screen.blit(Playtext, Playtext_Rect)
                screen.blit(menutext, menutext_Rect)
                gameend_score = font.render(('Your Score is ' + str(int(score))), True, (60, 60, 60))
                screen.blit(gameend_score, gameend_score_Rect)

        pygame.display.update()

if __name__ == '__main__':
    main()