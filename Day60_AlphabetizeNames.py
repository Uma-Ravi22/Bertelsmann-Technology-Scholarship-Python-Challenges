# Day 60 Challenge - Alphabetizing Names.

import operator

# Function takes List of Dictionaries as parameter, sorting elements as per lastname then with firstname.
# More than one sorting key, so Itemgetter is used.
# Itemgetter takes any no.of arguments, returns a function that applies each of its arguments.

def alphabetize_names(data):
    return sorted(data, key = operator.itemgetter('last', 'first'))
    
# Main
PEOPLE = [{'first':'Reuven', 'last':'Lerner','email':'reuven@lerner.co.il'}, 
          {'first':'Donald', 'last':'Trump','email':'president@whitehouse.gov'},
          {'first':'Vladimir','last':'Putin','email':'president@kremvax.ru'}]
          
print(alphabetize_names(PEOPLE))