"""A function that asks the user to enter a list of integers and print the following:

*the total number of items in the list.
*the last item in the list.
*the list in reverse order.
*Yes if the list contains a 5 and No otherwise.
*the number of fives in the list.
*the result of removing the first and last items from the list and sorting the remaining items.
*how many integers in the list are less than 5.

>>> enter the list of integers: 1, 3, 6, 7
Your integer list:  [1, 3, 6, 7]
the total number of items in the list: 4
the last item in the list: 7
the list in reverse order: [7, 6, 3, 1]
No
the number of fives in the list: 0
[3, 6]
number of integers in the list are less than 5: 2"""

def listdata(l=input("enter the list of integers: ")):
    l = l.split(', ')
    for i in range(len(l)):
        l[i] = int(l[i])
    print('Your integer list: ', l)
    print(f"the total number of items in the list: {len(l)}")
    print(f"the last item in the list: {l[-1]}")
    print(f"the list in reverse order: {l[::-1]}")
    print('Yes' if 5 in l else 'No')
    print(f'the number of fives in the list: {l.count(5)}')
    print(sorted(l[1:-1]))
    print(f'number of integers in the list are less than 5: {sum(i<5 for i in l)}')
    
listdata()
