# Day 67 Challenge: Print last Line of a File.

# Function iterates over lines of file, store each line in lastline.
# When EOF, the last line of file content is stored in lastline variable.
# Print the result.

def get_final_line(fname):
    fhand = open(fname, "r")
    for line in fhand:
        fhand = line.rstrip()
        lastline = line
    print("The Last Line is:")
    print(lastline)
        
# Main
# Read the File name & pass it as an argument to get_final_line function.
fname = input('Enter a File Name:')
get_final_line(fname)
        
