# Day 63: Restaurant.
# In this exercise, I want you to create a new constant dict, called MENU, representing the possible items you can 
# order at a restaurant.The keys will be strings, and the values will be prices (i.e., integers).
# You should then write a function, restaurant, that asks the user to enter an order:  If the user enters the name of 
# a dish on the menu, the program prints the price and the running total.
# It then asks the user again for their order.  If the user enters the name of a dish not on the menu, the program 
# scolds the user (mildly). It then asks the user again for their order.  If the user enters an empty string, 
# the program stops prompting and prints the total amount.

# Dictionary of Menu with price.
MENU = {'Caprese Salad': 12, 'Sandwich': 10, 'Ravioli': 8, 'Lasagne': 9, 'Bruschetta': 7, 'Coffee':5}
 
# Function takes oreder, if in menu, add price in total until user enters blank.
def restaurant():
    total=0
    while True:
        order = input('Order: ').strip()
        if not order:
            break
        
        if order in MENU:
            price = MENU[order]
            total += price
            print(f'{order} is {price}, total is {total}')
        else:
            print(f'We are fresh out of {order} today')
    print(f' Total Amount for the order is: {total}')
 
# Main
restaurant()

