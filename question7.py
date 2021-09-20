"""A program that removes any repeated items from a list so
that each item appears at most once.

>>>[1,1,2,3,4,3,0,0]
[1,2,3,4,0]."""

def antidub(l: list):
    return list(set(l))

#instance
print(antidub([1,1,2,3,4,3,0,0]))
