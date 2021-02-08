# Day 51 Challenge: SUMMING NUMBERS
# The challenge here is to write a mysum function that does the same thing as the built-in sum function.
# However, instead of taking a single sequence as a parameter, it should take a variable number of arguments. 
# Thus, although you might invoke sum([1,2,3]), you’d instead invoke mysum(1,2,3) or mysum(10,20,30,40,50).

def mysum(*numbers):
    ans = 0
    for num in numbers:
        ans += num
    return ans

# Main   
# Case 1: Only Tuple.
print(mysum(10,20,30,40,50,))

# Case 2:Only List
print(mysum(*[1,2,3,]))

# Case 3: Tuple, List.
print(mysum(1, 2.5, 4.5, *[1,2,3], *(5,10)))