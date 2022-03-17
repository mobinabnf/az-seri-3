inp=input('Please input a list : ').replace('[','').replace(']','').split(',')
l=[]
l2=[]
for i in inp:
    l.append(int(i))
    l2.append(int(i))
l2.sort()
if l==l2:
    print('The list is sorted.')
else:
    print('The list is not sorted.')