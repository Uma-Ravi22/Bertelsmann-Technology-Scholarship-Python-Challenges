# Day 57 - Challenge: Sort a String.

import sys

# This program doesn't use Built-in function.
# Function takes the String as an argument, remove spaces, convert to lower case.
# Copy string to a list (s).
# Iterate over string, compare first and next character, if first letter greater, then swap, till end.
# Print the sorted string.

def sorting(str):
    if str != "":
        str = str.strip().lower()
        s = []
        n = len(str)
        for i in range(n):
            s.append(str[i])
        
        for i in range(n):
            for j in range(n):
                if s[i] < s[j]:
                    temp = s[i]
                    s[i] = s[j]
                    s[j] = temp
        res = ""
        for i in range(n):
            res = res + s[i]
        print("The Sorted String:", res)
    else:
        print("Empty String.Exiting...")
        quit()
        
# Main
# Get a String.
str = input("Enter a String:")
sorting(str)
