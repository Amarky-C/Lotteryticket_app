#random lottery ticket application
#lottery numbers to be generated (0-50)
#user enters the players name
#user enters the number
#the application generates a random number within the range specified
#if number matches the application random number
#the user wins the lottery
#if the number doesn't match, the user loses and will try again

import random
def lottery_calc():
    lottery_player = input('Enter players name: ')
    lottery_number = int(input('Enter any number from 0-50: '))
    lottery_gen = random.randint(0,50)
    if lottery_gen == lottery_number:
        print(lottery_player, 'congratulations', lottery_number, 'is the lottery winning number')
    else:
        print(lottery_player, 'sorry you lost try again', lottery_number, 'is not the lottery winning number')




lottery_calc()
