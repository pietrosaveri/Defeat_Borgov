import pygame
from pygame import mixer
import time 
#inizialize everything 
pygame.init()

#windw
wn = pygame.display.set_mode((852, 480))
#title
pygame.display.set_caption("First Game")

# This goes outside the while loop, near the top of the program
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('Bg1.png')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()

bulletSound = pygame.mixer.Sound('bullet.wav')
hitSound = pygame.mixer.Sound('hit.wav')

music = pygame.mixer.music.load('BeepBox-Song.mp3')
pygame.mixer.music.play(-1)

score =  0

class player(object):
    def __init__(self, x, y, widht, height):
        self.x= x
        self.y= y
        self.widht = widht
        self.height =height
        self.vel = 5
        self.isJump = False
        self.jumpCount =10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        
        
    def draw(self,wn):
        if self.walkCount +1 >=27:
            self.walkCount = 0
            
        if not(self.standing):
            if self.left:
                wn.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
            elif self.right:
                wn.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
        else:
            if self.right:
                wn.blit(walkRight[0], (self.x, self.y))
            else:
                wn.blit(walkLeft[0], (self.x, self.y))
        #self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        pygame.draw.rect(wn, (255,0,0), self.hitbox,2)

    def hit(self):
        self.isJump = False
        self.jumpCount = 10 
        self.x = 60
        self.y = 410
        self.walkCount = 0
        font1 =pygame.font.SysFont('comicsans', 100)
        text = font1.render('-5',1, (255,0,0))
        wn.blit(text, (250- (text.get_width()/2),200))
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()
        

class projectitle(object):
    def __init__(self,x,y,radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing
        
    def draw(self,wn):
        pygame.draw.circle(wn, self.color, (self.x, self.y), self.radius, )

class enemy(object):
    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
    walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]

    def __init__(self, y, x, widht, height, end):
         self.y = y
         self.x= x
         self.widht =widht
         self.height = height
         self.end= end
         self.path= [self.x, self.end]
         self.walkCount = 0
         self.vel = 3
         self.hitbox = (self.x + 17, self.y + 2, 31, 57)
         self.health = 10
         self.visible = True
         

    def draw(self, wn):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.vel >0:
                wn.blit(self.walkRight[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            else:
                wn.blit(self.walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1

            pygame.draw.rect(wn, (255,0,0), (self.hitbox[0], self.hitbox[1] -20,50,10 ))
            pygame.draw.rect(wn, (0,128,0), (self.hitbox[0], self.hitbox[1] -20, 50 - (5 * (10-self.health)),10 ))
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            #pygame.draw.rect(wn, (255,0,0), self.hitbox,2)
    
    def move(self):
        if self.vel >0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
                
    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False 
        

def redrawGameWindow():
 
    wn.blit(bg, (0, 0))
    text = font.render('Score: '+str(score), 1, (0,0,0))
    text2 = font.render('Health: '+str(health1), 1, (0,0,0))
    gameover= font.render('GAME OVER', 1, (255,0,0))
    wn.blit(text2, (150, 10))
    #wn.blit(text, (350,10))
    man.draw(wn)
    goblin.draw(wn)
    for bullet in bullets:
        bullet.draw(wn)
        
    pygame.display.update()
    
def Game_over():
    print('Game Over')
    gameover= font.render('GAME OVER', 1, (255,0,0))
    wn.blit(gameover, (350, 10))
    pygame.display.update()


#main loop


font = pygame.font.SysFont('comicsans', 30, True)
gameover= font.render('GAME OVER', 1, (255,0,0))
man = player(200, 410, 64, 64)
goblin = enemy(415, 50, 64, 64, 450)
shootLoop = 0 
bullets = []
health1 = 10
run = True
while run:
    clock.tick(27)
    if goblin.visible == True:
        if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1]  + man.hitbox[3]> goblin.hitbox[1]:
            if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0]< goblin.hitbox[0] + goblin.hitbox[2]:
                man.hit()
                score -=5
                health1 -= 5

                #if health1 == 0:
                    #print('game over')
                    #wn.blit(gameover, (350, 10))

    if shootLoop >0:
        shootLoop +=1
    if shootLoop > 3:
        shootLoop = 0
        
    
    #any event in pygame wn, mouse, keyboard ecc.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y +bullet.radius > goblin.hitbox[1]:
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                hitSound.play()
                goblin.hit()
                score += 1
                bullets.pop(bullets.index(bullet))
                
        
        if bullet.x < 500 and bullet.x >0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
    

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop ==0 :
        bulletSound.play()
        if man.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) <5:

            bullets.append(projectitle(round(man.x + man.widht //2), round(man.y + man.height //2), 6, (0,0,0), facing))

        shootLoop = 1
            
    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left= True
        man.right=False
        man.standing = False

    elif keys[pygame.K_RIGHT] and man.x < 500 - man.widht - man.vel:
        man.x += man.vel
        man.right = True
        man.left= False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0
        
        
    if not(man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right= False
            man.left= False
            man.walkCount = 0
            
    else:
        if man.jumpCount >= -10:
            neg= 1
            if man.jumpCount < 0:
                neg =-1
            man.y -= (man.jumpCount**2) *0.5*neg
            man.jumpCount -= 1

        else:
            man.isJump = False
            man.jumpCount = 10
            
    if health1  == 0:
        gameover= font.render('GAME OVER', 4, (255,0,0))
        wn.blit(gameover, (350, 10))
        pygame.display.update()
        time.sleep(2)
        print(' ')
        print('You lost against Borvog')
        print(' ')
        print('GAME OVER')
        time.sleep(5)
        quit()
    if goblin.visible == False:
        win = font.render('YOU WON!', 4, (255,0,0))
        wn.blit(win, (350, 10))
        pygame.display.update()
        print(' ')
        print('You defeated Borvog!')
        print(' ')
        print('Congratulations!')
        print('You can go back to the village, they are really happy to see you.')
        print('You save them! The village is now safe thanks to you.')
        print(' ')
        print('VICTORY!')
        time.sleep(20)
        quit()
    
    redrawGameWindow()

    
pygame.quit()
        
    
