import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN', 4: 'SHI', 5: 'GO', 6: 'ROKU'}

print(''' Cho-Han by inventwithpython.com. In this traditional Japanese game dice game, two dice are rolled in a bamboo cup by the dealer sitting on the floor, the player must guess if the dice total is an even (cho) or odd (hand)''')

purse = 5000 

while True: 
    print('you have', purse, 'mon. How much do you bet? (or Quit)')
    while True 
        pot = input('> ')
        if pot.upper() == 'QUIT':
            print('Thanks for playing')
            sys.exit
        elif not pot.isdecimal():
            print('PLease enter whole number')
        elif int(pot) > purse:
            print ('You do not have enough $ for the bet')
        else:
            pot= int(pot)
            break 

            