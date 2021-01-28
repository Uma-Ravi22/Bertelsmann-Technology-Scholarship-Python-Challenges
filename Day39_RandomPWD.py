#Day 39 Challenge - Generate Two Word Random Password
# Write a program that reads a file containing a list of words, randomly selects two of them, and concatenates them
# to produce a new password. When producing the password ensure that the total length is between 
# 8 and 10 characters, and that each word used is at least three letters long. 
# Capitalize each word in the password so that the user can easily see where one word ends and the next one begins. 
# Finally, your program should display the password for the user.

import sys
from random import randrange

# Open the data file.
try:
    fhand = open("data.txt", "r")
except:
    # Raise exception when file not exists.
    print("File not exist/Couldn't open file.")
    quit()
    
# Extract words (length 3 to 7 characters) from data file, store in words list. 
words = []
for line in fhand:
    line = line.rstrip()
    if len(line) >= 3 and len(line) < 8:
        words.append(line)
fhand.close()

# Select any word from list as firstword of Password.
one = words[randrange(0, len(words))]
one = one.lower()
pwd = one

# Select second word such that len(pwd) lies between 8 to 10 characters.
while len(pwd) < 8 or len(pwd) > 10:
    two = words[randrange(0, len(words))]
    two = two.lower()
    pwd = one + two
    
# Display the generated Password.
print("Random Password is:", pwd)
