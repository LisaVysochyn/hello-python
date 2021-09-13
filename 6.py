n = input()
if int(n)>=0:
    suma = int(n)+int(n*2)+ int(n*3)
else:
    n = f'{int(n)*(-1)}'
    suma = -int(n)-int(n*2)-int(n*3)
print(suma)
