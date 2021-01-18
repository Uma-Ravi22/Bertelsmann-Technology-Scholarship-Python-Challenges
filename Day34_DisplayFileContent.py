
# Day 34 Challenge - Display first 10 lines of a File.
# Unix-based operating systems usually include a tool named head. It displays the first 10 lines of a file whose name 
# is provided as a command line parameter. Write a Python program that provides the same behavior. Display an appropriate 
# error message if the file requested by the user does not exist or if the command line parameter is omitted.
# You can use the attached "elements.txt" file if you need a file to work with.

import sys

# Main
fname = input("Enter file name:")

# Raising an exception error, if wrong filename or not existing file name is entered.
try:
    # Default file open mode is Read mode.
    fhand = open(fname)
except:
    # raising exception for wrong/not existing filename.
    print("File Not Found, Enter correct file name.")
    quit()

# Display the first 10 lines of a File.
count = 0    
for line in fhand:
    if count < 10:
        # Remove white space after end of Line(string).
        line = line.rstrip()
        count  = count + 1
        print(line)
