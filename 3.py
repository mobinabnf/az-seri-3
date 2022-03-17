from random import randint
n=int(input('Input n : '))
l=[]
for i in range(n):
    while True:
        num=randint(0,100)
        if num not in l:
            l.append(num)
            break
print(l)