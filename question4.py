"""A store charges 12peritemifyoubuylessthan10items.Ifyoubuybetween10and99items,thecostis10 per item.
If you buy 100 or more items, the cost is $7 per item.
Write a program that asks the user how many items they are buying and prints the total cost."""

items = int(input("How many items would you like to buy? "))
if items <10 and items>0:
    print(f"Total cost {items*12}$")
elif items >= 10 and items <=99:
    print(f"Total cost {items*10}$")
elif items >= 100:
    print(f"Total cost {items*7}$")
else: print("choose at least 1 item")
