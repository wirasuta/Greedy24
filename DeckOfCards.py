# Kelas deck of cards
from Cards import Cards
import random

class DeckOfCards :

    availablecards = 0;
    newlist = []

    def __init__(self) :
        for i in range (1,53) :
            newcard = Cards(i)
            self.newlist.append(newcard)

        random.shuffle(self.newlist)
        DeckOfCards.availablecards = 52

    def getAvailable() :
        return DeckOfCards.availablecards # Static atribute

    def draw(self) :
        a = random.randrange(DeckOfCards.availablecards)
        newcardx = self.newlist[a]
        del self.newlist[a]
        DeckOfCards.availablecards = DeckOfCards.availablecards - 1
        return newcardx

    def isEmpty(self) :
        return (len(self.newlist) == 0)
