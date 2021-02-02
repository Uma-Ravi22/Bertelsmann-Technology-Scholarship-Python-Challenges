def flattenList(lst):
    if len(lst) == 0:
        return lst
    if type(lst[0]) == list:
        first, rest = lst[0], lst[1:]
        return flattenList(first) + flattenList(rest)
    else:
        first, rest = lst[0], flattenList(lst[1:])
        new = []
        new.append(first)
        return new + rest

# Main
lst = [1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]
print("List Before Flattening:") 
print(lst)
print("List After Flattening:") 
out = flattenList(lst)
print(out)