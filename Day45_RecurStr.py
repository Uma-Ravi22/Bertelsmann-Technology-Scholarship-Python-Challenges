#  Day 45: Recursive (String) Palindrome

def Palindrome(s):
    # If string length < 1, return TRUE.
    if len(s) < 1:
        return True
    else:
        # Last letter is compared with first, function called recursively with argument as 
        # Sliced string (With first & last character removed.)
        if s[0] == s[-1]:
            return Palindrome(s[1:-1])
        else:
            return False

# Main
# Read Input String.
str = input("Enter a String:")
# Convert to lower case to avoid mistake.
str = str.lower()

# Function call & Print Result.
if Palindrome(str):
    print("The Given String is a Palindrome.")
else:
    print("The Given String  is Not a Palindrome.")

