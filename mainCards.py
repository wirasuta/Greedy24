# Testing kelas kartu

from DeckOfCards import DeckOfCards
import random

def main() :
    newdeck = DeckOfCards()

    while (newdeck.isEmpty() == 0 ) :
        newdeck.draw()

main()
