import random
lst=[random.randrange(-10,10) for i in range(30)]
lst1=[]
lst2=[]
print(lst)
for i in lst:
    if i>=0:
        lst1.append(i)
    else:
        lst2.append(i)
print(lst1)
print(lst2)
