import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN', 4: 'SHI', 5: 'GO', 6: 'ROKU'}

print(''' Cho-Han by inventwithpython.com. In this traditional Japanese game dice game, two dice are rolled in a bamboo cup by the dealer sitting on the floor, the player must guess if the dice total is an even (cho) or odd (hand)''')

purse = 5000 

while True: 
    print('you have', purse, 'mon. How much do you bet? (or Quit)')
    while True:
        pot = input('> ')
        if pot.upper() == 'QUIT':
            print('Thanks for playing')
            sys.exit()
        elif not pot.isdecimal():
            print('PLease enter whole number')
        elif int(pot) > purse:
            print ('You do not have enough $ for the bet')
        else:
            pot= int(pot)
            break 
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print ('the dealer swirls the cup (rattle of the dice) and slams down- is it even/Cho or odd/han')  

    while True:
        bet = input('> ').upper()
        if bet != 'CHO' and bet != 'HAN':
            print("please enter CHO or HAN")
            continue 
        else:
            break

    rollIsEven = (dice1 + dice2) % 2 == 0
    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'

    playerWon = bet == correctBet

    if playerWon:
        print('You won! You take', pot, 'mon. ')
        purse = purse + pot 
        print ('the house collects a', pot//10, 'mon fee.')
        purse = purse - (pot//10 )
    else:
        purse = purse - pot 
        print ('you lost')
    
    if purse == 0:
        print('you have run out of money ')
        print('Thank you for playing')
        sys.exit()

        
            