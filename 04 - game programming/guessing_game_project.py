#we first generate our number
from random import randint
our_number=randint(0,100)

#now we give the instructions to play
print("""This is a number guessing game. The number you will try to guess will be between 0 and 100
You will have 8 attempts. In each new attempt we will give you a hint.
Good luck!""")

print(our_number)
number_of_attempts=8
user_number=-1
while user_number != our_number:
    user_number=int(input("Input a number:  "))
    number_of_attempts -= 1
    if user_number < 0 or user_number >100:
        print("The number you entered is not valid, please enter a number between 0 and 100 only")

    if user_number < our_number:
        print("Your number is lower than ours. Try again")
        
    elif user_number == our_number:
        print("You win! Your number is the same as ours, you guessed right!")
        print("it took you " + str(8 - number_of_attempts) + " attemps to make it!")
        break
    
    elif user_number > our_number:
        print("Your number is greater than ours. Try again")
    
    print(f"Attempts remaining: {number_of_attempts}")
    
    if number_of_attempts ==0:
        print(" You loose!! All attempts were used. Restart the game to play again")
        print(f"The number we had was '{our_number}' ")
        break

