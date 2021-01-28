# Day 43 Challenge: Missing Comments.
# When one writes a function, it is generally a good idea to include a comment that outlines the function’s purpose, 
# its parameters and its return value. However, sometimes comments are forgotten, or left out by well-intentioned 
# programmers that plan to write them later but then never get around to it. Create a Python program that reads one 
# or more Python source files and identifies functions that are not immediately preceded by a comment. For the 
# purposes of this exercise, assume that any line that begins with def, followed by a space, is the beginning of a 
# function definition. Assume that the comment character, #, will be the first character on the previous line when 
# the function has a comment. Display the names of all of the functions that are missing comments, along with the 
# filename and line number where the function definition is located. The user will provide the names of one or more 
# Python files as command line arguments, all of which should be analyzed by your program. An appropriate error 
# message should be displayed for any files that do not exist or cannot be opened. Then your program should process 
# the remaining files.

import sys

#Main
# If no filename in Command line, print error messge.
n = len(sys.argv)
#print(n)
if n == 1:
    print("Atleast one file name apart from source file is needed.")
    quit()

# Process all files in Command-line.   
try:
    for i in range(1, n):
        prev = " "
        num = 1
        name = sys.argv[i]
        fhand = open(name, "r")
        for line in fhand:
            # If previous line of Function definition not startswith '#', find line number, function name to 
            # print error message
            if line.startswith("def ") and prev[0] != "#":
                pos = line.index("(")
                fun_name = line[4 : pos]
                print("%s line %d: %s" %(name, num, fun_name))
            prev = line
            num += 1
        fhand.close()
except:
    printf("Error with File '%s' " %name)
    print("Processing the next one...")