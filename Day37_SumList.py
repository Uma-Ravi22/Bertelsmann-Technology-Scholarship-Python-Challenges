
# Day 37 Challenge: Sum a List of Numbers

# Create a program that sums all of the numbers entered by the user while ignoring any lines entered by the 
# user that are not valid numbers. Your program should display the current sum after each number is entered. 
# It should display an appropriate error message after any invalid input, and then continue to sum any 
# additional numbers entered by the user. Your program should exit when the user enters a blank line. 
# Ensure that your program works correctly for both integers and floating point numbers.

value = input("Enter a Number: ")
total = 0

# Read numbers from users until blank.
while value != "":
    try:
        # Convert value to number.
        num = float(value)
        total += num
        print("Current Total :", total)
    
    # Raise Exception if not a number.
    except valueError:
        print("Entered value is NOT a Number.")
        
    value = input("Enter a Number:")
    
# Display the Total.
print("The Total is:", total)
