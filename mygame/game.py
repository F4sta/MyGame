import pygame
import random
import sys

def main():
    global game_over
    width, height = 1280, 720

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Awsome Game')
    icon = pygame.image.load('warlord-helmet.png')
    pygame.display.set_icon(icon)

    fps = 60
    clock = pygame.time.Clock()
    run = True
    keys = None
    score = 0
    game = False
    game_over = False

    #default-options
    Bullet_endsize = 100
    amount_of_bullet = 30
    endless_game = False
    score_need_to_win = 50
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
            if self.reattack <= 0:
                self.__init__()
                
            elif self.charge < Bullet_endsize:
                if p1.player.colliderect(self.bullet):
                    game_over = True
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
        Bullet_endsize_cache = input('set Bullet size (default=100):\n')
        if Bullet_endsize_cache == '':
            pass
        elif int(Bullet_endsize_cache) == 0:
            print('Bullet size cant be 0')
            exit()
        else:
            Bullet_endsize = int(Bullet_endsize_cache)
    except ValueError:
        print('Wrong Value was given')
        exit()    
    try:
        amount_of_bullet_cache = input('set Bullets amount (default=30):')
        if amount_of_bullet_cache == '':
            pass
        elif int(amount_of_bullet_cache) == 0:
            print('Bullet size cant be 0')
            exit()
        else:
            amount_of_bullet_cache = int(amount_of_bullet_cache)
    except ValueError:
        print('Wrong Value was given')
        exit()
    """

    while run:
        clock.tick(fps)
        screen.fill((220,220,220))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        
        p1.render()
        p1.movement_check()

        if not score == 100 or not game_over:
            print(game_over)
            if not game:
                objs = [Bullet() for i in range(amount_of_bullet)]
                game = True
            elif game:
                for obj in objs:
                    try:
                        obj.attack()
                    except:
                        pass
        else:
            run = False
            print('Your score:', score, '\nGame Over')

        pygame.display.update()

if __name__ == '__main__':
    main()