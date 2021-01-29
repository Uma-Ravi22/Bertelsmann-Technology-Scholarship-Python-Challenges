
#  Day 44 Challenge: Total the Values
# Write a program that reads values from the user until a blank line is entered. Display the total of all of the 
# values entered by the user (or 0.0 if the first value entered is a blank line). Complete this task using recursion.
# Your program may not use any loops.

# FInding Sum of entered values until blank.
def summation():
    line = input("Enter a Number:")
    # Breaking condition for Recursion. If blank, stop process, return 0.
    if line == "":
        return 0.0
    else:
        # Convert "String" to "Float", Adding them, Rcursive call.
        return float(line) + summation()
        
        
# Main
# Function Call
sum = summation()
# Printing the Result.
print("The Sum is:", sum)
        