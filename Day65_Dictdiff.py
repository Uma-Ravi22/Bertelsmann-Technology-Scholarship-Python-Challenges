# Day 65: Dictdiff.

# Function takes 2 dictionaries, return a dictionary that gives the difference of 2 dicts.

def dictDiff(x, y):
    ans = {}
    # Get all keys from both dictionaries, without duplicates.
    keys = x.keys() | y.keys()
    for k in keys:
        # Dict.get returns None if key not exists.
        if x.get(k) != y.get(k):
            ans[k] = [x.get(k), y.get(k)]
        
    return ans

# Main
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'a': 1, 'b': 2, 'd': 4}
print(dictDiff(d1, d2))
