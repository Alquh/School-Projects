""" cardGame.py
    basic card game framework
    keeps track of card locations for as many hands as needed
"""
#importing random module
from random import *

#declaring initial variables, arrays and tuples
NUMCARDS = 52
DECK = 0
PLAYER = 1
COMP = 2

cardLoc = [0] * NUMCARDS
suitName = ("hearts", "diamonds", "spades", "clubs")
rankName = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven", 
            "Eight", "Nine", "Ten", "Jack", "Queen", "King")
playerName = ("deck", "player", "computer")

#function to clear the deck
def clearDeck():
    global cardLoc
    for i in range(len(cardLoc)):
        cardLoc[i] = DECK

#function to assing cards to computer and player
def assignCard(name):
    global cardLoc
    num = randint(0,51)
    
    #conditions to make sure that same card is not allocated to computer or player again
    if cardLoc[num] == 0:
        cardLoc[num] = name
    else:
        assignCard(name)

#function to show deck
def showDeck():
    print("Location of all cards")
    print("# " + "\t" + "   card " + "\t\t" + "location")
    num = len(cardLoc)
    for i in range(num):
        card_rank = rankName[i%13]
        suit = i//13
        card_suit = suitName[suit]
        
        #one line if condition to get the values for location points 1  and 2
        pos = "deck" if (cardLoc[i] == 0) else ("player" if (cardLoc[i] == 1) else "computer")

        #condition to manually print in a tabular manner
        if i in [15, 16, 17, 19, 20, 21, 23, 24, 25]:
            print(str(i) + "\t" + card_rank + " of " + card_suit + "\t" + pos)
        else:
            print(str(i) + "\t" + card_rank + " of " + card_suit + "\t\t" + pos)
    print()

#function to show hand of player and computer
def showHand(name):
    #finding the index number in array of each card with the value of name variable
    indices = [i for i, x in enumerate(cardLoc) if x == name]
    player = "computer" if name == 2 else "player"
    print("Displaying " + player + " hand:")
    for i in indices:
        card_rank = rankName[i%13]
        suit = i//13
        card_suit = suitName[suit]
        print(card_rank + " of " + card_suit )
    print()
    
def main():
    clearDeck()
    for i in range(5):
        assignCard(PLAYER)
        assignCard(COMP)

    showDeck()
    showHand(PLAYER)
    showHand(COMP)  

if __name__ == '__main__':
    main()
