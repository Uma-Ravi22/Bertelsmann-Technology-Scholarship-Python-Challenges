# Day 53 Challenge - Pig Latin

# Function does the following...
# If word starts with vowel, add 'way' at the end, return it.
# Else put the first letter as last & add 'ay' at end, return it.
def PigLatin(word):
    word = word.lower()
    if word[0] in 'aeiou':
        return f'{word}way'
    return f'{word[1:]}{word[0]}ay'
    
# Main
word = input("Enter a Word:")
print("PigLatin Code:", PigLatin(word))
