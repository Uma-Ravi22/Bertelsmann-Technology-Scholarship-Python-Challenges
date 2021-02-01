# Day 47:  Element Sequences
# Some people like to play a game that constructs a sequence of chemical elements where each element in the sequence
# begins with the last letter of its predecessor. For example, if a sequence begins with Hydrogen, then the next element 
# must be an element that begins with N, such as Nickel. The element following Nickel must begin with L, such as Lithium. The element sequence that is constructed cannot contain any duplicates. When played alone the goal of the game is to constructed the longest possible sequence of elements. When played with two players, the goal is to select an element that leaves your opponent without an option to add to the sequence.
# Write a program that reads the name of an element from the user and uses a recursive function to find the longest 
# sequence of elements that begins with that value. Display the sequence once it has been computed. Ensure that your 
# program responds in a reasonable way if the user does not enter a valid element name.

import sys

def longseq(ele_name, names):
    # If no element name, return empty list.
    if ele_name == "":
        return []
    newseq = []
    # Find last letter of ele_name.
    lastletter = ele_name[-1].lower()
    # Find next element whose firstletter = lastletter of previous element.
    for i in range(0, len(names)):
        firstletter = names[i][0].lower()
        if firstletter == lastletter:
            # Use Recursion to find the sequence.
            item = longseq(names[i], names[0 : i] + names[i+1 : len(names)])
            
            if len(item) > len(newseq):
                newseq = item
     
    # Return the sequence with ele_name.           
    return [ele_name] + newseq

# Main
# Store all element names in a List.
names = []
inf = open("elements.txt")
for line in inf:
    line = line.rstrip()
    words = line.split(",")
    names.append(words[2])
inf.close()

# Read Starting element & Capitalize it.
ele_name = input("Enter name of any Element:")
ele_name = ele_name.capitalize()

# Remove the starting element from list.
names.remove(ele_name)

# Finding longest sequence starting with ele_name.
seq = longseq(ele_name, names)

# Display the resulting Sequence.
print("The Longest Sequence starts with", ele_name, "is:")
for ele in seq:
    print(" ", ele)
