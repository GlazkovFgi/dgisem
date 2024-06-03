def change_list(list):
    list[0][0]=4
    print('List meaning after change = ', list)
    print('List ID after change = ', id(list))
    print('\n')

base_list=[1,2,3]
my_list=[base_list]*3
print('List meaning before = ', my_list)
print('List ID before = ', id(my_list))
print('\n')

change_list(my_list)
print('List meaning after = ', my_list)
print('List ID after = ', id(my_list))
print('\n')