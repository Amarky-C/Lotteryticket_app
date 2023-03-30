#enter the players name
#enter the number
#random randit within an inclusive range
#random
#input
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
