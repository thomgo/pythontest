import time
import random

def  hidden_number():
    random_number = random.randint(0, 100)
    remaining_attempts = 7
    user_number = None

    print("OK let me choose a number, wait a minute...")
    time.sleep(2)
    print("OK I have choosen one \n Try to guess my choice in less than 7 attempts")

    while user_number != random_number and remaining_attempts > 1:
        user_number = int(input("type a number\n"))
        if user_number > random_number:
            print("Too high !")
            remaining_attempts -= 1
        elif user_number < random_number:
            print("Too low !")
            remaining_attempts -= 1

    if user_number == random_number:
        print("Congratulations you found my number, that was : " + str(random_number))
    else:
        print("Sorry you loose, the number was : " + str(random_number))