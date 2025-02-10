import random

#generates random number and assigns to r_num
rand_num=random.randint(1,100)

#user guesssing of random number
user_num=int(input("enter the guessed number: "))


#while loop  run infinite time until break statement is encountered
while(True):

    #comparing user input and generated number
    if(rand_num==user_num):
        print("Nice! your guess is right")
        print("number is",rand_num)
        break

    elif(user_num<rand_num):
        print("Hint: too low, try again!")
        user_num=int(input("enter the guessed number: "))
        continue
    
    elif(user_num>rand_num):
        print("Hint: too high, try again!")
        user_num=int(input("enter the guessed number: "))
        continue