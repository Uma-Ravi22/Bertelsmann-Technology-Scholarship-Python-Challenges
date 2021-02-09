import sys

# Day 55 Challenge - PigLatin Sentence.
# Function does PigLatin conversion.
def PigLatin(word):
        word = word.lower()
        if word[0] in 'aeiou':
            return f'{word}way'
        return f'{word[1:]}{word[0]}ay'

# Main
# Split the words in the sentence, convert each word into PigLatin, Join them, Print result.

sentence = input("Enter a Sentence:")
if not sentence:
    print("Empty String, Pls enter a Sentence for processing...")
    quit()
sentence = sentence.strip()
ans = [PigLatin(word) for word in sentence.split()]
print(" ".join(ans))

