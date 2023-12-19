print('Sets are data types that store unordered and unindexed values.')

x = set()
print('A set may created with use of function set. Its result is printed as: ', x)

print('You may add alements to set with add method.')
x.add('John')
x.add('Doe')
print('x: ', x)

print('\nThe set object does not support indexing. Therefore attempt to access x[1] will result in TypeError.')

print('Sets may hold various data types.')
x.add(2)
x.add(0.5)
print('x: ', x)

print('\nHowever, an attempt to add a list to set will result in TypeError: unhashable type: \'list\'')
# x.add([1, 2, 3])

print('\nSets store a unique collection of data.')
print('Therefore, casting e.g list into set results in removing of repeating elements.')
my_list = [1, 1, 2, 3, 4, 5, 2, 2, 3, 1, 1, 0]
print('my_list: ', my_list)
print('set(my_list): ', set(my_list))

print('\nAnother way to create set is to simply put values between curly braces.')
print('{1, 2, 3}: ', {1, 2, 3})
print('type({1, 2, 3}): ', type({1, 2, 3}))

print('\nThe methods of class set enable convenient comparison of data sets')
set_1 = {1, 2}
set_2 = {2, 3}
print('set_1: ', set_1)
print('set_2: ', set_2)
print('set_1.intersection(set_2): ', set_1.intersection(set_2))
print('set_1.difference(set_2): ', set_1.difference(set_2))
print('set_2.difference(set_1): ', set_2.difference(set_1))
