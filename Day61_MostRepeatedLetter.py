# Day 61 Challenge: Word with most repeated letter.

from collections import Counter
import operator

# Functions returns the count of the most common letter of a word
def word_repeat(data):
    return max(data, key=letter_repeat)
 
# Function  returns the string that contains the greatest number of repeated letters.
def letter_repeat(word):
    return Counter(word).most_common(1)[0][1]
    
# Main
data = ['this', 'is', 'an', 'elementary', 'test', 'example']
print(word_repeat(data))
