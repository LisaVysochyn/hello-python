"""A function which sorts
and returns the list. By default it should sort alphabetically,
but if numflag==True, it sorts numerically. """

def mysort(mylist=[], numflag=False):
    if numflag == False:
        key = str
    else: key = int
    return sorted(mylist, key=key)
#main
a = [10, 1, 101, 2, 111, 212, 100000, 22, 222, 112, 10101, 1100, 11, 0]
print(mysort(a, numflag=False))
print(mysort(a, numflag=True))
print("Done")
