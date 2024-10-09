import pygame 
from pygame import mixer
pygame.init()
music = pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)
print('Hello how is going?')
asw = input('good or bad: ')

while not(asw =='good' or  asw == 'bad'):
    if not (asw == 'good' or asw == 'bad'):
        print('please insert a valid option')
        asw = input('good or bad:')

if (asw =='good'):
    print('ohh that is great!')
        
if (asw =='bad'):
    print('I\'m sorry to hear this')
        

    
