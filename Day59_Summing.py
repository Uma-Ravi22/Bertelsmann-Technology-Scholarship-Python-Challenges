# Day 59 Challenge - Summation.
# The result of mysum('abc', 'def') will be the string abcdef. Return 6 for mysum(1, 2, 3)
# And the result of mysum([1,2,3], [4,5,6]) will be the six-element list [1,2,3,4,5,6]. 

def mysum(*items):
    if not items:
        return items 
    output = items[0]
    for item in items[1:]:
        output += item
    return output


# Main
print(mysum([1,2,3], [4,5,6], [7, 8, 9, 10]))
print(mysum(10, 20, 30))
print(mysum("ABC", "DEF", "G", "H"))
print(mysum())
