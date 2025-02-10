import random

print("\t\t\t\t\tWelcome to Number Guessing Game")

#taking lower and upper bound of the range
lower=int(input("Enter lowerbound of range: "))
upper=int(input("Enter upperbound of range: "))

#generate random number in sepcified range
rand_num=random.randint(lower,upper)

#user guessing of random number
guess=int(input("Enter the guessed number: "))


#while loop run infinite time until break statement is encountered
while(True):

    #comparing user input and generated number
    if(guess==rand_num):
        print("Congratulations! your guess is right")
        break

    elif(guess<rand_num):
        print("Too low, try again!")
        guess=int(input("enter the guessed number: "))
        continue
    
    elif(guess>rand_num):
        print("Too high,try agaIn!")
        guess=int(input("Enter the guessed number: "))
        continue