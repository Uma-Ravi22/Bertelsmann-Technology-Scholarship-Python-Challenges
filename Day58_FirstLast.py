# Day 58 Challenge : Extract First & Last of a sequence.

# Function takes String, List, Tuple as arguments, Print the first and last characters 
# based on Slicing concept.
def FirstLast(data):
    return data[:1] + data[-1:]
    
# Main

# Case 1: String   
print(FirstLast("PythonProgram"))                   # Output: Pm
print(FirstLast('a'))                               # Output: aa

# Case 2: Tuple
print(FirstLast((10, 20, 30, 40, 50)))               # Output: (10, 50)

# Case 3: List
print(FirstLast([15,"A", "B", "C", "D", 50, "E"]))   # Output: [15, 'E']
print(FirstLast([1, 2, 3, 4, 5]))                    # Output: [1, 5]


