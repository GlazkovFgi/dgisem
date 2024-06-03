def change_list(list):
    list.append('Hello!')
    print('List meaning after change =', list)
    print('List ID after change = ', id(list))
    print('\n')

my_list=['PT1,']
print('List meaning before =', my_list)
print('List ID before = ', id(my_list))
print('\n')

change_list(my_list)
print('List meaning after =', my_list)
print('List ID after = ', id(my_list))
print('\n')