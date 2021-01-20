
# Day 35 Challenge - Display Tail of the File.
# Unix-based operating systems also typically include a tool named tail. It displays the last 10 lines of a file 
# whose name is provided as a command line parameter. Write a Python program that provides the same behavior. 
# Display an appropriate error message if the file requested by the user does not exist or if the command line parameter 
# is omitted.You can use the attached "elements.txt" file if you need a file to work with.

import sys

# Main

if len(sys.argv) != 2:
    print("You must provide the file name as a command line parameter.")
    quit()

# Read file name as Command Line argument
try:
    fhand = open(sys.argv[1], "r")
except:
     # raising exception for wrong/not existing filename.
    print("File Not Found, Enter correct file name.")
    quit()
 
# Store file contents ina list.  
data = []
for line in fhand:
    line = line.rstrip()
    data.append(line)

# Printing last 10 lines of list.
n = len(data)
for i in range(n-10, n) :
    print(data[i], end="\n")
    