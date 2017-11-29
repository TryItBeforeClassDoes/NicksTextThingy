import time
import random
import sys

#The Heist 30/25/37 0.0.6

print("welcome to the worst game you will play today, you're welcome")
print("in this game you as the player will be going to heaven to steal jesus' shoes")
print("so, what is your name?")
name = raw_input()
print'lol ok sure,' , name , ', if that is your real name'
print('ok moving on, what is your favorite color?')

def askcolor():
    color = raw_input()
    if color == 'white':
        print("racist")
    elif color == 'black':
        print("black isn't a real color, but whatever")
    elif color == 'red':
        print("bloodthirsty mongrel")
    elif color == 'blue':
        print("nice")
    elif color == 'yellow':
        print("yellow is a bad color")
        print("try again")
        askcolor()
    elif color == 'green':
        print("green is not a creative color")
    elif color == 'orange':
        print("it's better than yellow i guess")
    elif color == 'purple':
        print('nice')
    else:
        print("that's not a real color lmao")
        askcolor()
askcolor()
print("where are you going?")
def whereisu():
    where = raw_input()
    if where == "heaven":
        print('yeet')
    else:
        print('wrong, ur going to heaven')
        print('try again')
        whereisu()
whereisu()

print('alright hold on while i boot up the game now')
'''time.sleep(2)
print('.')
time.sleep(2)
print('.')
time.sleep(2)
print('.')
time.sleep(2)
print('.')
time.sleep(2)
print('.')
time.sleep(2)
print('.')
time.sleep(2)'''
'''encounter 3'''
print('you awake in a dark room with the whirring of a fan off in the distance')
print('a voice calls to you')
time.sleep(3)
print('"alright so the heist is simple"')
time.sleep(2)
print('"we are going to heaven to steal jesus'"'"' shoes"')
time.sleep(2)
print('"ok are u redy"')
def yeet():
    yes = raw_input()
    if yes == "yes":
        print('"ok cool"')
    elif yes == "no":
        print('"ok i'"'"'ll wait"')
        print('"let me know when you'"'"'re ready"')
        yeet()
    elif yes == "help":
        print('"ok it is just a yes or no question why do you need help"')
        yeet()
    else:
        print('"yeah i don'"'"'t know what that means please explain your answer to this yes or no question thanks"')
yeet()         
print('"alright so i'"'"'m glad you figured that one out, that was hard"')
time.sleep(3)
print('"we'"'"'re going to make this next one really easy"')
time.sleep(3)
print('as you answer the question, your mind goes completely blank as you ascend to the heavens')
time.sleep(3)
print('"alright so welcome to heaven"')
time.sleep(3)
print('"so we gotta sneak past the gate in front of you"')
time.sleep(3)
print('there is a gate in front of you')
time.sleep(3)
print('"yes there is"')
time.sleep(3)
print('"so in order to sneak in you gotta hold down the shift key to sneak"')
time.sleep(3)
print('"that'"'"'s the key most fps games use now, so we'"'"'re going to use it too"')
print('"alright so give it a shot"')
def SNEAK():
    SPOOK = raw_input()
    if SPOOK == 'SNEAK':
        tries = 0
        goodlucknerd = random.randint(1,20)
        crit = 20
        print(goodlucknerd)
        while goodlucknerd != crit:
            print('"ALRIGHT LET'"'"'S SNEAK IN"')
            print('"OK WE FAILED LET'"'"'S TRY AGAIN"')
            goodlucknerd = random.randint(1,20)    
            tries+=1
            time.sleep(.25)
            if goodlucknerd == crit:
                print('"NICE WE GOT IN, WE CAN STOP SNEAKING now"')
                print'you took', tries, 'tries to sneak in, you'"'"'re not very good at this are you.'
                break
    else:
        print "THAT'S NOT SNEAKING."
        SNEAK()
SNEAK()
print('"ok so now that we'"'"'re past the gate and there'"'"'s jesus'"'"' shoes."')
time.sleep(2)
print('you see a pair of golden yeezys by the welcome mat')
time.sleep(2)
print('"alright so stealing is just as simple as typing steal."')
time.sleep(2)
def stealing():
    steal = raw_input()
    if steal == 'steal':
        print('good job, you stole the welcome mat.')
        print('"nice choice. the real jesus'"'"'s shoes was the journey you had along the way."')
        time.sleep(5)
        print('GAME OVER')
        sys.exit()
    elif steal == 'steal shoes':
        print('"fantastic, you stole jesus'"'"'s shoes"')
        print('"now let'"'"'s get out of here"')
    elif steal == 'steal mat':
        print('"why'"'"'d you steal the welcome mat? are you some kind of loser who steals welcome mats from people?"')
        print('GAME OVER')
        sys.exit()
    else:
        print('"ok, it'"'"'s not that hard, just type in steal to steal the shoes."')
        stealing()
stealing()
print ('as you try to leave heaven, you here a voice off in the distance.')
time.sleep(3)
print('"HEY! Wait for me!"')
time.sleep(.5)
print('an overweight italian man approaches both of you, winded from the 40 steps he took to get over here.')
time.sleep(1)
print('"thank god i caught up to you guys. hey, are those jesus'"'"'s shoes?"')
print('"i was waiting here forever to steal those shoes and you two just walk right in and steal them!"')
time.sleep(2)
print('"oh yeah i forgot that you were waiting here for me, sorry about that gino"')
time.sleep(1)
print('"SORRY?!? that'"'"'s it, im'"'"'a make you pay for crossin'"'"' me"')
print('the overweight, now very angry, italian man prepares to attack')
print('cue battle music')
print('what do you do? fight, flee, or do nothing')
# encounter 4, challenge 3, boss fight
def combat():
    b = raw_input()
    if b == 'fight':
        print('with one fluid motion, you put on jesus'"'"'s shoes and kick the irate italian down through the clouds.')
    elif b == 'flee':
        print('you can'"'"'t escape!')
        combat()
    elif b == 'do nothing':
        print('you get hit in the face with the full force of one thousand bowls of spagetti')
        print('your corpse is sent to the beginning of the game to replay it until you actually do something.')
        print('game over')
        sys.exit()
combat()
print('conlaturations! you killed an overweight italian man in heaven.')
print('you earn 1 exp and 1 bowl of pasta')
print('"hey good job on killing that gino guy, i have just the idea what to do now..."')
print('your vision fades to black...')
time.sleep(1)
print('.')
time.sleep(1)
print('.')
time.sleep(1)
print('.')
time.sleep(1)
print('.')
time.sleep(1)
print('.')
time.sleep(1)
print('.')
print('your vision returns and you are back down on earth in a pizza place')
print('"good, you'"'"'re back. now that we have jesus'"'"'s shoes, this pizza place will give us unlimited pizza"')
print('a single tear rolls down your face, as you just have heard the greatest thing anyone has ever said to you.')
time.sleep(1)
print('Conlaturations, you beat this really bad video game. ign still gave it an 9/10 though')





'''herein lies the inventory system
it was supposed to list out items you have, and how many you have.
its dead now because we have no clue how lists work, but you know what? 
we'll make it work'''
'''class Item(object):
    def _init_(self,name,has):
        self.name = name
        self.has = has
        
class inventory(object):
    def _init_(self):
        self.items = []
    
    def add_item(self, item):
        self.items[item.name] = item
        
    def print_items(self):
        print('\t' .join(['Name', 'Has']))
        for item in len(self.items):
            print('\t'.join([str(x) for x in [item.name, item.has]]))
            
inv = inventory()
inv.add_item(Item('Sword', 1))'''