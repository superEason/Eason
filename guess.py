#coding=gbk 
import random
secret=random.randint(1,100)
guess=0
tries=0
print "Hey,卢彬,I'm the Dread Pirate Roberts,and I have a secret!"
print "It is a number from 1 to 99. I'll give you 6 tries."
while guess !=secret and tries<6:
    guess=input("what's you guess?")
    if guess<secret:
        print"Too low,you are silly!"
    elif guess>secret:
        print"Too high,so pitty!"
    tries = tries + 1
if guess==secret:
    print"You got it!"
else:
    print"no more guesses"
    print"The secret number is",secret
