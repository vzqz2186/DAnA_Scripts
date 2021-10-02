"""
          Program: Deck of cards.
           Author: Daniel Vazquez
             Date: 02/28/2018 (v3.00)

       Assignment: Initialize a deck of cards, shuffle it, and draw seven
                   cards.

         Due Date: 03/02/2018

        Objective: Draw the player seven cards from a shuffled deck.
                   (WORKS: v3.00)

      Execute via: >>python vazquez_deck030218_v3.00.py

    Sample output: 


**            Template based on Dr. Nichols program example.                 **
"""
#----------------------------------------------------------------------------80
import time # Used to get current time and the timer for the program.
import random # Used to fill the list with the 10 random numbers.

def main():
    # Initialized deck
    deck = ["H1","H2","H3","H4","H5","H6","H7","H8","H9","HT","HJ","HQ","HK", \
            "S1","S2","S3","S4","S5","S6","S7","S8","S9","ST","SJ","SQ","SK", \
            "D1","D2","D3","D4","D5","D6","D7","D8","D9","DT","DJ","DQ","DK", \
            "C1","C2","C3","C4","C5","C6","C7","C8","C9","CT","CJ","CQ","CK"] 

    random.shuffle(deck) # Shuffles the deck.

    hand = deck[:7] # Draws 7 cards from the deck.
    del(deck[:7]) # Gets the drawn cards out of the deck. Source: last hw.

    print("Your Hand: \n",hand, "\n") # Shows the player's hand.

    disDate() # Prints date.
    return 0

# Date/Time Function---------------------------------------------------------80
#  Source:
#   https://www.pythoncentral.io/how-to-display-the-date-and-time-using-python/
def disDate():
    print(time.strftime('%m/%d/%Y %H:%M'))


# Call Main------------------------------------------------------------------80
main()