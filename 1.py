import random
list_odd=[random.randrange(1,100,2) for i in range(5)]
list_even=[random.randrange(2,101,2) for j in range(4)]
print(f'list of odd :{list_odd}')
print(f'list of even :{list_even}')
list_odd.pop(2)
print(f'list of odd :{list_odd}')
list_odd.insert(2,list_even)
print(f'modified list of odd :{list_odd}')
flat_list= list_odd + list_even
print(f'list of flattern list:{flat_list}')
flat_list.sort()

print(f'list of sorted list:{flat_list}')
