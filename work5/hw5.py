# 1
x = input()

list = ['temur', 'amir']
list2 = [x for x in list if 'r' in x]
print(list2)

# 2
my_list = [x for x in range(1, 11)]
print(my_list)

# 3
my_list = [x**2 for x in range(1, 22)]
print(my_list)

# 4
my_list = [x for x in range(1, 11) if x % 2 == 0]
print(my_list)

# 5
list1 = [1, 2, 3]
list2 = [4, 5, 6]
my_list = [(x, y) for x in list1 for y in list2]
print(my_list)

#6
my_dict = {"apple": 1, "banana": 2, "orange": 3}
my_list = [key for key in my_dict]
print(my_list)

#7
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = [x for x in my_list if x % 2 == 0]
print(new_list)
