# Day 69: Word Count.
# Unix systems contain many utility functions. One of the most useful is wc, the word count program. 
# If you run wc against a text file, it’ll count the characters, words, and lines that the file contains.
# The challenge for this exercise is to write a wordcount function that mimics the wc Unix command.
# The function will take a filename as input and will print four lines of output:
# 1. Number of characters (including whitespace)
# 2. Number of words (separated by whitespace)
# 3. Number of lines
# 4. Number of unique words (case sensitive, so “NO” is different from “no”)

# Function wordcount takes the wcfile.txt as argument, counts the no.of lines, characters & words.
# After splitting each line into words, the words list is converted to a set (uniquewords), to avoid duplicates.
# The results are displayed.

def wordcount(fname):
    chars = 0
    lines = 0
    words = 0
    w = 0
    uniquewords = 0
    uniqueset = set()
    for line in open(fname):
        lines += 1
        chars += len(line)
        w = line.split()
        words += len(w)
        uniqueset.update(w)
        
    print("Number of Lines        :", lines)
    print("Number of Words        :", words)
    print("Number of Unique Words :", len(uniqueset))
    print("Number of Characters   :", chars)
    
# Main
wordcount("wcfile.txt")
        
    
