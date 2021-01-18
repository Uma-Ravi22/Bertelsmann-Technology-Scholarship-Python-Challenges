
# Day 33 Challenge - Create BINGO Card.
# Write a function that creates a random Bingo card and stores it in a dictionary. 
# The keys will be the letters B, I, N, G and O. The values will be the lists of five numbers that appear under each 
# letter.Write a second function that displays the Bingo card with the columns labeled appropriately.
# The numbers appear under B range from 1-15, I range from 16-30, N range from 31-45 and so on.

from random import randrange

# Generating Bingo Card Numbers (Random Numbers using Randrange)
def createCard():
    low = 1
    high = 15
    # Create Dictionary for Bingo Card (Key as Letters 'B', 'I', 'N', 'G', 'O')
    # Values are List of numbers Columnwise.('B' Column,  1 to 15 'I' Column 16 to 30 and so on.)
    card = {}
    letters = ['B', 'I', 'N', 'G', 'O']
    for c in letters:
        card[c] = []
        while len(card[c]) != 5:
            num = randrange(low, high+1)
            # Check for duplicates
            if num not in card[c]:
                card[c].append(num)
        low = low + 15
        high = high + 15
    
    return card

# Display the Numbers on the Bingo card.    
def displayCard(card):
    letters = ['B', 'I', 'N', 'G', 'O']
    print("B  I  N  G  O")
    print("-------------")
    for i in range(5):
        for ch in letters:
            print("%2d " %card[ch][i], end="")
        print("\n")        

# Main
card = createCard()
displayCard(card)