#random lottery ticket application
#lottery numbers to be generated (0-50)
#user enters the players name
#user enters the number
#the application generates a random number within the range specified
#if number matches the application random number
#the user wins the lottery
#if the number doesn't match, the user loses and will try again

winning_number = 30
import random
def lottery_calc():
    lottery_player = input('Enter players name: ')
    lottery_number = int(input('Enter any number from 0-50: '))
    lottery_gen = random.randint(0,50)
    if lottery_gen == winning_number and lottery_number == lottery_gen and winning_number:
        print(lottery_player, 'congratulations!', lottery_gen, 'is the lottery winning number')
    else:
        print(lottery_player, 'sorry you lost try again!', lottery_gen, 'is not the winning number', winning_number, 'is the lottery winning number')




lottery_calc()
