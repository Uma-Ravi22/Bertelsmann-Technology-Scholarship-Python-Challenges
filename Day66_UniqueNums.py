# Day 66: How many different Numbers?

# Function takes a List of numbers with duplicate elements. 
# List is converted to SET to remove duplicates. Set is returned.
def numbersDifferent(num):
    uniquenum = set(num)
    return uniquenum
    
# Main
# List with duplicate elements, passed as an argument to numbersDifferent function.
ans = numbersDifferent([1, 2, 3, 1, 2, 3, 4, 5, 6, 4, 7, 8, 9, 10])

# The SET with unique elements, its length are displyed.
print("The Set of Unique Numbers:")
print(ans)
print("Count of Unique Numbers:", len(ans))
    
