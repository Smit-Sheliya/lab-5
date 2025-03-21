import random
lst=[random.randrange(1,10) for i in range(20)]
print(f'list of 20 random numbers:{lst}')
number=int(input("enter a number of your choice of you want to know position: "))
a=[]
for i in lst:
      if number in lst:
            print(lst.index(number))
