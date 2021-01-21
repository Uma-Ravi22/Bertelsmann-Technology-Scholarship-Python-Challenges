
# Day 36 Challenge: Concatenate Multiple Files.
# Unix-based operating systems typically include a tool named cat, which is short for concatenate. 
# Its purpose is to concatenate and display one or more files whose names are provided as command line parameters. 
# The files are displayed in the same order that they appear on the command line.
# Create a Python program that performs this task. It should generate an appropriate error message 
# for any file that cannot be displayed, and then proceed to the next file. 
# Display an appropriate error message if your program is started without any command line parameters.

import sys

n = len(sys.argv)
# Atleast one file apart from source file should be provided for display the contents.
if n == 1:
    print("Atleast one file name should be provided.")
    quit()

# Process all the files in Command line.   
for i in range(1, n):
    fname = sys.argv[i]
    try:
        fhand = open(fname, "r")
        for line in fhand:
            line = line.rstrip()
            print(line)
        fhand.close()
    except:
        # Raise error if file not exist/couldn't open.
        print("Couldn't open file:", fname)