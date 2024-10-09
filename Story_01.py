import time
import pygame
from pygame import mixer
pygame.init()
attack=3
stamina=10
satiety=10

sad1 = pygame.mixer.Sound('sad song.wav')

def music():
    music = pygame.mixer.music.load('Danny Olson - Tide.mp3')
    pygame.mixer.music.play(-1)
    
def boom():
    boom = pygame.mixer.Sound('boom_02.wav')
    boom.play()
    
def quit_game():
    time.sleep(10)
    quit()
    
def sad_music():
    mixer.music.stop()
    sad1.play()
    
def Welcome():
    print('Welcome in the first story game of Pietro Saveri.')
    time.sleep(2)
    global name_player
    name_player = input('Please insert your name to play: ')
    #print(name_player)
    time.sleep(1)
    print('You will be able to make choices in the game that can change your destiny, be careful.')
    time.sleep(5)
    print('Good luck!')
    print(' ')
    time.sleep(4)

def Rules():
    print('RULES: ')
    time.sleep(2)
    print('There are no rules, just type in the right way your answer and the story will continue.[you will find the 2 possible answers in this brackets]')
    print(' ')
    time.sleep(7)
    print('In the game you have to care about the level of your attack, stamina and satiety')
    print(' ')
    time.sleep(6)

def Character():
    print('The choice of the character is vital to the story you will face.')
    print(' ')
    time.sleep(2)
    print('Choose your character: ')
    print('-Elf (fast, bow, accurate)')
    print('-Human (intelligent, sword)')
    print('-Dwarf (slow, hammer, strong during night)')
    time.sleep(1)
    global character
    character=input('Your choice: ')
    
    while not (character == 'Human' or character =='Elf' or character == 'Dwarf'):
        if not (character == 'Human' or character =='Elf' or character == 'Dwarf'):
            print('Please insert a valid name.')
            character=input('Your choice: ')
            #print(character)
        
    print(' ')
    time.sleep(2)
    print('You will start with the maximum level of stamina and satiety.')
    print(' ')
    print('satiety=15')
    print('stamina=15')
    print(' ')
    time.sleep(3)
    

def Start_story():
    print('START!')
    print(' ')
    time.sleep(4)
    print('You are in a village, not very far from the big city. You are here because the habitants need your help.')
    time.sleep(4)
    print('An evil man in stealing the food from this village and takes the inhabitants as hostage.')
    time.sleep(4)
    print('Borvog is his name, you have to defeat him and save the village.')
    print(' ')
    time.sleep(3)


def foor_or_weapon():
    global weapon
    print('Before you go, you have to prepare yourself, let\'s buy some food and weapons.')
    print(' ')
    time.sleep(0.5)
    
    food_or_weapons=input('Wich one would you like to buy before? [food/weapons]')

    while not (food_or_weapons == 'food' or food_or_weapons =='weapons'):
        if not (food_or_weapons == 'food' or food_or_weapons =='weapons'):
            print('Please insert a valid name.')
            food_or_weapons=input('Your choice: ')
    
    if(food_or_weapons == 'food'):
        time.sleep(1)
        print('Very good, there is a cheap market 10 meters forward.')
        time.sleep(2)
        print('What would you like to buy?')
        print(' ')
        time.sleep(1)
        print('-Bread [satiety +5, stamina +1]')
        print('-Cake [satiety +9, stamina +0]')
        print('-Carrots [satiety +2, stamina +5]')
        print('-Beef [satiety +6, stamina +9]')
        time.sleep(1)
        global food
        food=input('Your choiche: ')

        while not (food == 'Bread' or food =='Cake' or food =='Carrots'or food == 'Beef'):
        
            if not (food == 'Bread' or food =='Cake' or food =='Carrots'or food == 'Beef'):
                print('Please insert a valid name.')
                food=input('Your choice: ')
        
        if(food=='Beef'):
            print('You don\'t have enouth money for this.')
            time.sleep(2)
            print('Do you want to help a person and recive the money that you need? [Yes/No]')
            time.sleep(2)
            asw_money=input('Your choiche: ')
            if(asw_money=='Yes'):
                print('You are a good person, helping the grandmother you have earned the money for the beef!')
            if(asw_money=='No'):
                print('What would you like to buy?')
                print(' ')
                print('-Bread [satiety +5, stamina +1]')
                print('-Cake [satiety +9, stamina +0]')
                print('-Carrots [satiety +2, stamina +5]')
                food=input('Your choiche: ')


            while not (asw_money == 'No' or asw_money =='Yes'):
                if not (asw_money == 'No' or asw_money =='Yes'):
                    print('Please insert a valid name.')
                    asw_money=input('Your choice: ')
                
        weapons_choice()
    

    if(food_or_weapons == 'weapons'):
        print('Very good, there is a workshop near you!')
        time.sleep(2)
        print(' ')
        print('Your attack is now equal to 3')
        print(' ')
        time.sleep(2)
        print('Which weapon would you like to buy?')
        print(' ')
        print('-Bow')
        print('-Sword')
        print('-Hammer')
        print(' ')
        global weapon
        weapon=input('Your choice: ')
        
        while not (weapon == 'Bow' or weapon =='Sword' or weapon =='Hammer'):
        
            if not (weapon == 'Bow' or weapon =='Sword' or weapon =='Hammer'):
                    print('Please insert a valid name.')
                    weapon=input('Your choice: ')
                
        global attack
        if(weapon=='Bow'and character =='Elf'):
            attack=9
            print('Attack='+str(attack))
        if(weapon=='Sword'and character =='Human'):
            attack=9
            print('Attack='+str(attack))
        if(weapon=='Hammer'and character =='Dwarf'):
            attack=9
            print('Attack='+str(attack))
        if(weapon=='Bow'and character !='Elf'):
            attack=6
            print('Attack= '+str(attack))
        if(weapon=='Sword'and character !='Human'):
            attack=6
            print('Attack= '+str(attack))
        if(weapon=='Hammer'and character !='Dwarf'):
            attack=6
            print('Attack= '+str(attack))
        
        food_choice()

def food_choice():
    print('Very good, now is time for the food, there is a cheap market 10 meters forward.')
    time.sleep(2)
    print('What would you like to buy?')
    print(' ')
    time.sleep(1)
    print('-Bread [satiety +5, stamina +1]')
    print('-Cake [satiety +9, stamina +0]')
    print('-Carrots [satiety +2, stamina +5]')
    print('-Beef [satiety +6, stamina +9]')
    global food
    food=input('Your choiche: ')
    
    while not (food == 'Bread' or food =='Cake' or food =='Carrots'or food == 'Beef'):
        if not (food == 'Bread' or food =='Cake' or food =='Carrots'or food == 'Beef'):
            print('Please insert a valid name.')
            food=input('Your choice: ')
    
    if(food=='Beef'):
        print('You don\'t have enouth money for this.')
        time.sleep(2)
        print('Do you want to help a person and recive the money that you need? [Yes/No]')
        asw_money=input('Your choiche: ')
        if(asw_money=='Yes'):
            print('You are a good person, helping the grandmother you have earned the money for the beef!')
            time.sleep(2)
        if(asw_money=='No'):
            print('What would you like to buy?')
            print(' ')
            print('Bread [satiety +5, stamina +1]')
            print('Cake [satiety +9, stamina +0]')
            print('Carrots [satiety +2, stamina +5]')
            food=input('Your choiche: ')
            
        while not (asw_money == 'No' or asw_money =='Yes'):
            if not (asw_money == 'No' or asw_money =='Yes'):
                    print('Please insert a valid name.')
                    asw_money=input('Your choice: ')

def weapons_choice():
    time.sleep(3)
    global weapon
    print('Very good, now is time for the weapons, there is a workshop near you!')
    print(' ')
    time.sleep(3)
    print('Your attack is now equal to 3')
    print(' ')
    time.sleep(2)
    print('Which weapon would you like to buy?')
    print(' ')
    print('-Bow')
    print('-Sword')
    print('-Hammer')
    print(' ')
    global attack
    weapon=input('Your choice: ')
    
    while not (weapon == 'Bow' or weapon =='Sword' or weapon =='Hammer'):
        if not (weapon == 'Bow' or weapon =='Sword' or weapon =='Hammer'):
            print('Please insert a valid name.')
            weapon=input('Your choice: ')
                
    if(weapon=='Bow'and character =='Elf'):
        attack=9
        print('Attack='+str(attack))
    if(weapon=='Sword'and character =='Human'):
        attack=9
        print('Attack='+str(attack))
    if(weapon=='Hammer'and character =='Dwarf'):
        attack=9
        print('Attack='+str(attack))
    if(weapon=='Bow'and character !='Elf'):
        attack=6
        print('Attack= '+str(attack))
    if(weapon=='Sword'and character !='Human'):
        attack=6
        print('Attack= '+str(attack))
    if(weapon=='Hammer'and character !='Dwarf'):
        attack=6
        print('Attack= '+str(attack))
        
def start_walking():
    global stamina
    global satiety
    global food
    global attack
    global weapon
    print(' ')
    print('You are now ready to go, take your things and let\'s go!')
    print(' ')
    time.sleep(2)
    print('You start walking outside the village, everything seems calm.')
    time.sleep(2)
    print('Thanks to the map that the leader of the village gave you, you have found the correct way.')
    time.sleep(3)
    print('You have walked for 5 hours now, and path 30 Kilometres')
    time.sleep(2)
    print('stamina = 4')
    print('satiety = 5')
    stamina = 4
    satiety = 5
    print(' ')
    time.sleep(2)
    print('Do you want to rest and find something to eat or to continue walking? [walk/Rest]')
    rest_or=input('Your choice: ')
    
    while not (rest_or == 'Rest' or rest_or =='walk'):
        if not (rest_or == 'Rest' or rest_or =='walk'):
            print('Please insert a valid name.')
            rest_or=input('Your choice: ')
    
    if(rest_or == 'Rest'):
        print('since you are in the forest you decide to create a fire.')
        time.sleep(2)
        print('The warm of the fire is heating you but hunger begins to be felt')
        time.sleep(2)
        print('You hear a sound, animals are near you.')
        time.sleep(2)
        print('Do you want to eat your food or to hunt some animals? [food/hunt]')
        hunt_or=input('Your choice: ')
        
        while not (hunt_or == 'food' or hunt_or =='hunt'):
            if not (hunt_or == 'food' or hunt_or =='hunt'):
                print('Please insert a valid name.')
                hunt_or=input('Your choice: ')
        
        if(hunt_or =='food'):
            print('In your bag you have the ' +str(food))
            if(food=='Beef'):
                stamina = 13
                satiety = 11
                print('After eating your Beff, these are your new level of stamina and satiety')
            if(food=='Carrots'):
                stamina = 9
                satiety = 7
                print('After eating your Carrots, these are your new level of stamina and satiety')
            if(food =='Cake'):
                stamina = 4
                satiety = 14
                print('After eating your Cake, these are your new level of stamina and satiety')
            if(food =='Bread'):
                stamina = 5
                satiety = 10
                print('After eating your Bread, these are your new level of stamina and satiety')
                
            print('stamina= '+str(stamina))
            print('satiety= '+str(satiety))
            time.sleep(4)
            print('Now is time to sleep and wait for the next day')
            
        if(hunt_or =='hunt'):   
            print('There is a boar near you, you follow him and with your '+str(weapon)+' you manage to kill the boar!')
            time.sleep(2)
            print('Your attack is increased of 3')
            attack = int(attack)+3
            print('Attack= '+str(attack))
            print(' ')
            print('You can eat your boar and rest for the night.')
            print(' ')
            time.sleep(1)
            stamina = 15
            satiety = 15
            print('Stamina= '+str(stamina))
            print('Satiety= '+str(satiety))
            
    if(rest_or =='walk'):
        print('You continue walking for others 20 Kilometres.')
        time.sleep(2)
        print('but but hunger and fatigue start to be felt, it\'s time to rest.')
        time.sleep(1)
        stamina = stamina-3
        satiety = satiety-3
        print('Stamina= '+str(stamina))
        print('Satiety= '+str(satiety))
        
def wake_up():
    global attack
    time.sleep(4)
    print('You wake up in the early morning, after a good sleep you area ready to walk again.')
    time.sleep(4)
    print('You\'ve been walking for 3 hours now and you start hearing a noise.')
    print(' ')
    time.sleep(3)
    print('It\'s a slave of Borvog!')
    time.sleep(2)
    print('Do you want to fight him or to spy him? [spy/fight]')
    fight_spy = input('Your choice: ')
    
    while not (fight_spy == 'spy' or fight_spy =='fight'):
        if not (fight_spy == 'spy' or fight_spy =='fight'):
            print('Please insert a valid name.')
            fight_spy=input('Your choice: ')

    
    if (fight_spy == 'fight'):
        print('He doesn\'t semms so strong.')
        print(' ')
        time.sleep(1)
        print('Your attack is now at '+str(attack))
        print(' ')
        if(attack >= 9):
            print('Your are strong enoughth to kill the slave.')
            time.sleep(1)
            attack +=3
            print('Your attack increased of 3')
            print('Attack= '+str(attack))
            time.sleep(2)
            print('After killing him you see a map inside his pocket, you take it')
            time.sleep(2)
            print('You follow the map and discover that bring at a cave.')
            time.sleep(2)
            print('Go inside or don\'t go? [go/do not go]')
            go_inside=input('Your choice: ')
            
            while not (go_inside == 'go' or go_inside =='do not go'):
                if not (go_inside == 'go' or go_inside =='do not go'):
                    print('Please insert a valid name.')
                    go_inside=input('Your choice: ')
            
            if(go_inside == 'go'):
                go_inside_cave()
  
            if(go_inside == 'do not go'):
                dont_go_cave()
                
        if(attack <9):
            sad_music()
            print('You are not strong enoughth to beat him, burt he sow you!')
            time.sleep(2)
            print('After a tough battle he defeat you.')
            time.sleep(3)
            print('GAME OVER')
            quit_game()
    if (fight_spy == 'spy'):
        print('You start to follow him furtively and you discover a cave, he went inside this cave.')
        time.sleep(2)
        print('Go inside or don\'t go? [go\do not go]')
        go_inside=input('Your choice: ')
        
        while not (go_inside == 'go' or go_inside =='do not go'):
            if not (go_inside == 'go' or go_inside =='do not go'):
                print('Please insert a valid name.')
                go_inside=input('Your choice: ')
        
        if(go_inside == 'go'):
            go_inside_cave()

        if(go_inside == 'do not go'):
            dont_go_cave()
        
def dont_go_cave():
    sad_music()
    print('You start to go back but an ambush from the slaves of Borvog catches you off guard!')
    time.sleep(3)
    print('They take you and bring to Borvog, you can finally see his face.')
    time.sleep(2)
    print('But you can\'t do anything.')
    time.sleep(2)
    print('He kill you.')
    print(' ')
    time.sleep(3)
    print('GAME OVER')
    quit_game()

def go_inside_cave():
    global attack
    print('You start to enter in the cave.')
    time.sleep(2)
    print('You hide between rocks and you discover that this is the headquarters of Borvog.')
    time.sleep(4)
    print('There are thousand slaves of him, the general house is well protected.')
    time.sleep(4)
    print('But you have to go inside it.')
    time.sleep(3)
    print('You start to get closer but a slave is coming!')
    time.sleep(3)
    print('Attack him or try to hide? [attack/hide]')
    attack_hide = input('Your choiche: ')
    
    while not (attack_hide == 'attack' or attack_hide =='hide'):
        if not (attack_hide == 'attack' or attack_hide =='hide'):
            print('Please insert a valid name.')
            attack_hide=input('Your choice: ')

    
    if(attack_hide =='attack'):
        print('Stealthily manage to knock out the slave.')
        time.sleep(3)
        print('You notice that around his neck he has a key, you take it.')
        print(' ')
        time.sleep(3)
        print('New item: Key')
        print(' ')
        attack +=3
        print('New attack= '+str(attack))
        time.sleep(3)
        go_inside_door()
    if(attack_hide =='hide'):
        print('Hopefully he didn\'t see you.')
        time.sleep(3)
        print('You arrive at the general house but the door is close!')
        time.sleep(3)
        print('Search for the key or try to smash the door? [search/smash]')
        smash_search = input('Your choice: ')
        
        while not (smash_search == 'search' or smash_search =='smash'):
            if not (smash_search == 'search' or smash_search =='smash'):
                print('Please insert a valid name.')
                smash_search=input('Your choice: ')
        
        if(smash_search=='search'):
            time.sleep(3)
            print('You start to look around for the key.')
            time.sleep(3)
            print('After a while you see a slave with a key in his neck')
            time.sleep(3)
            print('Stealthily manage to knock him out.')
            print(' ')
            time.sleep(3)
            print('New item: Key')
            print(' ')
            attack +=3
            print('New attack= '+str(attack))
            go_inside_door()
        if(smash_search=='smash'):
            time.sleep(1)
            print('You try to smash the door with your shoulder and with your foot.')
            time.sleep(3)
            print('The door is very strong!')
            time.sleep(3)
            print('You only realize now that you are too noisy!')
            time.sleep(3)
            print('The slaves of Borvog see you.')
            time.sleep(3)
            print('They take you and bring to Borvog, you can finally see his face.')
            time.sleep(4)
            sad_music()
            print('But you can\'t do anything.')
            time.sleep(3)
            print('He kill you.')
            print(' ')
            time.sleep(3)
            print('GAME OVER')
            quit_game()
def go_inside_door():
    global character
    print('With the kew item you can finally go inside the general house.')
    time.sleep(4)
    print('When you are inside you notice that no one is with you, everything is silent and calm.')
    print(' ')
    time.sleep(6)
    print('You start to look around and see a control panel, there are a lot of buttons and levers.')
    time.sleep(8)
    print('You can also see a number under the dust,469.. there is a another number after the 9 but is diffult to see it.')
    print(' ')
    time.sleep(8)
    print('9? 0? 8? you can\'t see.')
    time.sleep(4)
    print('This control panel can controll all the headquarters of Borvog!')
    time.sleep(5)
    print('You just have to understand how it works.')
    print(' ')
    time.sleep(4)
    
    if(character == 'Human'):
        print('Since you are a human and intelligence it\'s one of your characteristic you can hack to controll panel.')
        time.sleep(5)
        print('After hacking it you discover the position of a secret room.')
        time.sleep(4)
        print('Go to the room or stay in the genral house? [go/stay]')
        secret_room = input('Your choice: ')
        
        while not (secret_room == 'go' or secret_room =='stay'):
            if not (secret_room == 'go' or secret_room =='stay'):
                print('Please insert a valid name.')
                secret_room=input('Your choice: ')
        
        if(secret_room =='go'):
            time.sleep(3)
            print('You start to follow the path for the room.')
            time.sleep(4)
            print('You find the door for the room, but it is close')
            time.sleep(4)
            print('Maybe the key can works?')
            time.sleep(3)
            print('Try the key, find another way. [key/way]')
            key_or = input('Your choice: ')
            
            while not (key_or == 'key' or key_or =='way'):
                if not (key_or == 'key' or key_or =='way'):
                    print('Please insert a valid name.')
                    key_or=input('Your choice: ')
            
            if(key_or=='key'):
                print('You try to insert the key but...')
                time.sleep(2)
                print('As espected the key doesn\'t work.')
                time.sleep(2)
                print('You have to find another way.')
                time.sleep(2)
                pass_code()
                
            if(key_or=='way'):
                time.sleep(2)
                pass_code()
                
        if(secret_room =='stay'):
            sad_music()
            print('After a few the alarm starts to sound!')
            time.sleep(3)
            print('Borvog see you and kill you!')
            print(' ')
            time.sleep(3)
            print('GAME OVER')
            quit_game()
    if(character =='Elf'):
        global weapon
        global attack
        print('Since you are an Elf you can\'t undersatand how it works.')
        time.sleep(4)
        print('Despite this you see some stairs behind you.')
        time.sleep(4)
        print('Follow the stairs or stay here? [here/follow]')
        stairs_or = input('Your choice: ')
        
        while not (stairs_or == 'follow' or stairs_or =='here'):
            if not (stairs_or == 'follow' or stairs_or =='here'):
                print('Please insert a valid name.')
                stairs_or=input('Your choice: ')
        
        if(stairs_or == 'here'):
            sad_music()
            print('After a few the alarm starts to sound!')
            time.sleep(3)
            print('Borvog see you and kill you!')
            print(' ')
            time.sleep(3)
            print('GAME OVER')
            quit_game()
        if(stairs_or == 'follow'):
            time.sleep(3)
            print('This stairs bring at the top of the general house.')
            time.sleep(3)
            if(weapon=='Bow'):
                print('This is the perfect spot for an archer.')
                time.sleep(2)
                print('Start to kill the slaves from the top of the house or live them alone and find a way to reah Borvog? [kill/way]')
                kill_or_way = input('Your choice: ')

                while not (kill_or_way == 'kill' or kill_or_way =='way'):
                    if not (kill_or_way == 'kill' or kill_or_way =='way'):
                        print('Please insert a valid name.')
                        kill_or_way=input('Your choice: ')
                    
                if(kill_or_way == 'kill'):
                    print('Ther are a lot of them, you have the high ground.')
                    time.sleep(4)
                    print('You manage to kill 20 of them!')
                    time.sleep(3)
                    print('Your attack increased of 60.')
                    attack +=60
                    print('Attack= '+str(attack))
                    #altura borvog fight!!+ see altura and find a way to go there
                    time.sleep(3)
                    final_fight()
                if(kill_or_way == 'way'):
                    print('You can see a rope and a hill.')
                    time.sleep(3)
                    print('You use the rope to reach the hill there is Borvog!!')
                    time.sleep(4)
                    print('Finally you can fight him.')
                    time.sleep(3)
                    print('His attack is at 60.')
                    time.sleep(1)
                    print('Your attack is at: '+str(attack))
                    if(attack <= 60):
                        sad_music()
                        print('You are to weak.')
                        time.sleep(2)
                        print('He defeat you.')
                        print(' ')
                        time.sleep(3)
                        print('GAME OVER')
                        quit_game()
                    if(attack >60):
                        print('oh wow you win')
                        time.sleep(2)
                        print('Actually is impossible that you won, so if you see this message congratulations, you beat Borvog, the game and me.')
                    
            if(weapon !='Bow'):
                print('You cans see a bow!')
                time.sleep(3)
                print('You take the bow and your attack increase of 10.')
                time.sleep(4)
                weapon = 'Bow'
                attack +=10
                print(' ')
                print('Attack= '+str(attack))
                print('This is the perfect spot for an archer.')
                time.sleep(2)
                print('Start to kill the slves from the top of the house or live them alone and find a way to reah Borvog? [way/kill]')
                kill_or_way = input('Your choice: ')
                
                while not (kill_or_way == 'kill' or kill_or_way =='way'):
                    if not (kill_or_way == 'kill' or kill_or_way =='way'):
                        print('Please insert a valid name.')
                        kill_or_way=input('Your choice: ')
                
                if(kill_or_way == 'kill'):
                    print('Ther are a lot of them, you have the high ground.')
                    time.sleep(3)
                    print('You manage to kill 20 of them!')
                    time.sleep(3)
                    print('Your attack increased of 60.')
                    attack +=60
                    print('Attack= '+str(attack))
                    #altura borvog fight!!+ see altura and find a way to go there
                    time.sleep(3)
                    final_fight()
                    
                if(kill_or_way == 'way'):
                    print('You can see a rope and a hill.')
                    time.sleep(3)
                    print('You use the rope to reach the hill there is Borvog!!')
                    time.sleep(3)
                    print('Finally you can fight him.')
                    time.sleep(3)
                    print('His attack is at 60.')
                    time.sleep(3)
                    print('Your attack is at: '+str(attack))
                    
                    if(attack <= 60):
                        sad_music()
                        print('You are to weak.')
                        time.sleep(3)
                        print('He defeat you.')
                        print(' ')
                        time.sleep(3)
                        print('GAME OVER')
                        quit_game()
                    if(attack >60):
                        print('oh wow you win')
                        time.sleep(2)
                        print('Actually is impossible that you won, so if you see this message congratulations, you beat Borvog, the game and me.')
                        
    if(character =='Dwarf'):
        print('Since you are a Dwarf, you can\'t understant how it works!')
        time.sleep(4)
        print('You have to find another way.')
        time.sleep(3)
        print('There is a button, you press it.')
        time.sleep(3)
        print('All the light in the cave are off!')
        time.sleep(3)
        print('The Dwarfs are strongest in the dark.')
        print(' ')
        time.sleep(2)
        print('Attack +10')
        print(' ')
        attack +=10
        print('Attack= '+str(attack))
        print(' ')
        print('Now you are more powerfull.')
        time.sleep(3)
        print('Attack all the slaves or try to hide? [hide/attack]')
        jump_or = input('Your choice: ')
        
        while not (jump_or == 'attack' or jump_or =='hide'):
            if not (jump_or == 'attack' or jump_or =='hide'):
                print('Please insert a valid name.')
                jump_or=input('Your choice: ')
        
        if(jump_or == 'attack'):
            time.sleep(0.5)
            print('You go out from the house and start to fight against the slaves.')
            time.sleep(5)
            print('You defeat 20 of them.')
            print(' ')
            time.sleep(3)
            print('Your attack increased of 60')
            attack += 60
            print(' ')
            print('Attack= '+str(attack))
            
            #altura borvog fight!!+ see altura and find a way to go there
            time.sleep(3)
            final_fight()
            
        if(jump_or == 'hide'):
            sad_music()
            print('After a few the alarm starts to sound!')
            time.sleep(3)
            print('Borvog see you and kill you!')
            print(' ')
            time.sleep(3)
            print('GAME OVER')
            quit_game()
        
        
def pass_code():
    global attack 
    n=3
    print('You can see a screen on the right.')
    time.sleep(3)
    print('The screen says: passcode')
    time.sleep(2)
    print('You need a 4 digit passcode to enter in this room.')
    time.sleep(3)
    print('Find the passcode and you will be able to enter in the room.')
    passcode=input('PASSCODE: ')
    while(passcode !='4690'):
        if(passcode !='4690'):
            n = n-1
            print('Passcode wrong')
            print(str(n)+' attempts left')
            passcode=input('PASSCODE: ')
            if(n==1 and passcode !='4690' ):
                sad_music()
                print('The alarm start to go! Borvog see you and kill you')
                print(' ')
                time.sleep(3)
                print('GAME OVER')
                quit_game()
                break
    if(str(passcode) == '4690'):
        print('Passcode correct!')
        time.sleep(3)
        print('You can go inside the room')
        time.sleep(4)
        print('Inside the room there is the famous sword of the thousand soldiers.')
        time.sleep(5)
        print('You take it.')
        time.sleep(3)
        print('This weapon is very powerful, it increase you attack of 100.')
        time.sleep(4)
        attack +=100
        print('Attack: '+str(attack))
        #altura borvog fight!!+ see altura and find a way to go there
        final_fight()


def final_fight():
    global character
    if(character == 'Human'):
        print('You can see a hill, and decided to climb it.')
        time.sleep(3)
        see_fight_borvog()
        
    if(character =='Elf' and weapon =='Bow'):
        print('You can see a hill, and with the bow and a rope you manage to reach the top')
        time.sleep(3)
        see_fight_borvog()
    if(character =='Elf' and weapon !='Bow'):
        print('You can see a hill.')
        time.sleep(2)
        print('You are a Elf but without a bow, reaching the top will be more difficult.')
        time.sleep(4)
        print('You start to climb the hill, you arrive at the top.')
        time.sleep(4)
        see_fight_borvog()
    if(character =='Dwarf'):
        print('You can see a hill but you don\'t know how to reach the top.')
        time.sleep(4)
        print('Give up and go back to the village or find a way to reach the top? [give up/way]')
        give_or_way = input('Your choiche: ')
        
        while not (give_or_way == 'give up' or give_or_way =='way'):
            if not (give_or_way == 'give up' or give_or_way =='way'):
                print('Please insert a valid name.')
                give_or_way=input('Your choice: ')
        
        if(give_or_way == 'give up'):
            sad_music()
            print('You go back to the village without taking revenge on Borvog.')
            time.sleep(3)
            print('No one will trust you again.')
            time.sleep(3)
            print('You are banished from the village')
            print(' ')
            time.sleep(4)
            print('GAME OVER')
            quit_game()
            
        if(give_or_way =='way'):
            print('There are metals and pieces of wood, with your skills you can build a catapult.')
            time.sleep(4)
            print('Using this you finally reach the top af the hill')
            time.sleep(3)
            see_fight_borvog()


def see_fight_borvog():
    print('Finally you can see Borvog!')
    time.sleep(3)
    print('He on sitting in a throne.')
    print(' ')
    time.sleep(3)
    print('Borvog: I was waiting for you.')
    time.sleep(3)
    print('You: This is your end Borvog.')
    time.sleep(3)
    print('Borvog: I see that you are way stronger than before, killing my slaves helped you.')
    time.sleep(5)
    print('You: You were watching me for all this time?')
    time.sleep(4)
    print('Borvog: Exactly.')
    time.sleep(3)
    print('You: You just used your slaves? How dare you?')
    time.sleep(4)
    print('Borvog: They are just pawns.')
    time.sleep(3)
    print('You: I can\'t accept this!! Prepare to die!')
    time.sleep(4)
    print('Borvog: Yes, we will see.')
    print(' ')
    time.sleep(2)
    print('FIGHT')
    print(' ')
    time.sleep(1)
    fight()
    
def fight():
    print('Attack first or wait? [first/wait]')
    first_or = input('Your choice: ')

    while not (first_or == 'first' or first_or =='wait'):
        if not (first_or == 'first' or first_or =='wait'):
            print('Please insert a valid name.')
            first_or=input('Your choice: ')
    
    if(first_or == 'first'):
        
        first()
        
    if(first_or == 'wait'):
        wait()


def first():
    global satiety
    global stamina
    global name_player
    time.sleep(1)
    print('With a feline snap you start to attack him!')
    time.sleep(3)
    print('He deflect your atack easily!')
    time.sleep(2)
    print('He has a big scythe, he\'s very strong.')
    time.sleep(3)
    print('Depside this you continue to fight.')
    time.sleep(3)
    print('Your level of stamina and satiety are very low')
    satiety = 2
    stamina = 3
    print(' ')
    print('Stamina= '+str(stamina))
    print('Satiety= '+str(satiety))
    print(' ')
    time.sleep(4)
    print('He is winning, you have to find a way to turn this situation!')
    time.sleep(3)
    print('Show me how to fight ' +str(name_player))
    time.sleep(2)
    import game_02
    game_02.my_func()
    execfile('game_02.py')

def wait():
    global name_player
    time.sleep(1)
    print('He attack first!')
    time.sleep(2)   
    print('A strong attack directly on your face!')
    time.sleep(3)
    print('You strat to defend and try to attck as well.')
    time.sleep(3)
    print('He is very strong')
    time.sleep(3)
    print('Your level of stamina and satiety are very low')
    satiety = 2
    stamina = 3
    print(' ')
    print('Stamina= '+str(stamina))
    print('Satiety= '+str(satiety))
    time.sleep(4)
    print('He is winning, you have to find a way to turn this situation!')
    time.sleep(3)
    print('Show me how to fight ' +str(name_player))
    time.sleep(3)
    import game_02
    game_02.my_func()
    execfile('game_02.py')
    
    from game_02 import goblin, visible, health1
    
    if goblin.visible == False:
        print('You won!!')
    if health1 ==0:
        print('You lost!')
music()
Welcome()
Rules()
Character()
Start_story()
foor_or_weapon()
start_walking()
wake_up()
