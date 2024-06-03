def change_string(str):
    str='PT1, '+str
    print('Str meaning after change=', str)
    print('Str ID after change', id(str))
    print('\n')

my_str = 'Hello!'
print('Str meaning before=', my_str)
print('Str ID before', id(my_str))
print('\n')

change_string(my_str)
print('Str meaning after=', my_str)
print('Str ID after', id(my_str))
print('\n')