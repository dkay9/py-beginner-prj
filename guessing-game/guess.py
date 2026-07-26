#import method that generates random numbers
import random #python standard library module for generating random numbers
#generrate random numbers between 1 - 100 and store in a variable 
number = random.randint(1, 100) 
#create placeholder variable for user's guess   
guess = None
#write while loop
while guess != number:
    #get input from user inside the loop
    guess = int(input("Guess a number (1-100): "))
    #give user feed back user if statements
    if guess < number:
        print("Higher!")
    elif guess > number:
        print("Lower!")
#print success message once guess is right         
print("you got it!")