# Day 56 Challenge - Ubbi Dubbi

# Function takes word as an argument.Iterate over each character of word, add to a list (OUT).
# If char is vowel, add 'ub' before the letter else just add the letter.
# At end, join then print letters together.

def ubbi_dubbi(word):
    out = []
    word=word.strip().lower()
    for letter in word:
        if letter in 'aeiou':
            out.append(f'ub{letter}')
        else:
            out.append(letter)
    return "".join(out)

# Main
# Input a word to be translated, if blank quit.
while True:
        word = input("Enter a Word to Translate or Blank to quit:")
        if not word:
            print("No Word. Exiting...")
            break
        print(ubbi_dubbi(word))
