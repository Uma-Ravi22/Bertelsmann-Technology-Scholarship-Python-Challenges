# Day 62: Printing Tuple Records.
# A common use for tuples is as records, similar to a STRUCT in some other languages.
# For this exercise, write a Python function, format_sort_records, that takes the PEOPLE list: 
# PEOPLE = [('Joe', 'Biden', 7.85),('Vladimir', 'Putin', 3.626),('Jinping', 'Xi', 10.603)] and
# returns a formatted string that looks like the following:

# Biden      Joe         7.85
# Putin      Vladimir    3.63
# Xi         Jinping    10.60

import operator

# Function takes list of Tuples as argument. Sorting tuples on last name.
# Print sorted record in the format given. 
def format_sort_records(data):
    sorted(data, key=operator.itemgetter(1,0))
    for item in data:
        print("{1:10} {0:10} {2:5.2f}".format(*item))

# Main
PEOPLE = [('Joe', 'Biden', 7.85), ('Vladimir', 'Putin', 3.626), ('Jinping', 'Xi', 10.603)]
format_sort_records(PEOPLE)

