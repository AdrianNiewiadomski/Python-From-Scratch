print('Dictionaries in Python are data structures that hold pairs key: value.')

my_dictionary = {
    'first_name': 'Jan',
    'last_name': 'Kowalski'
}
print('my_dictionary: ', my_dictionary)
print('type(my_dictionary): ', type(my_dictionary))

print('Values may be accessed by following way:')
print('my_dictionary[\'last_name\']: ', my_dictionary['last_name'])


print('\nDictionaries may hold various data types.')
config = {
  'host': '127.0.0.1',
  'port': 90,
  1: 2,  # Notice that key may be an integer.
  'some_list': [1, 2, 3],
  'parameters': {
    'a': 1,
    'b': 2
  }
}
print('config: ', config)

print('\nChanging values stored in dictionary')
print('Dictionaries are mutable. This means that the pairs that they hold may be changed.')
salaries = {
    'John': 20,
    'Sally': 30,
    'Sammy': 15
}
print('salaries: ', salaries)

salaries['Bobby'] = 22  # Here a new value is added to dictionary 'salaries' under index 'Bobby'
salaries['Sammy'] = 22  # Here the value stored under index 'Sammy' is updated.
print('After salaries[\'Bobby\'] = 22  and salaries[\'Sammy\'] = 22')
print('salaries: ', salaries)

print('\nUpdating dictionary with other dictionary - wrong way (overwriting)')
my_dict = {
    'a': 1,
    'b': 2
}
print('my_dict: ', my_dict)
update = {
    'b': 3,
    'c': 4
}
print('update: ', update)
my_dict = update
print('my_dict: ', my_dict)

print('\nUpdating dictionary with other dictionary - with update method')
my_dict = {
    'a': 1,
    'b': 2
}
print('my_dict: ', my_dict)
update = {
    'b': 3,
    'c': 4
}
print('update: ', update)
my_dict.update(update)
print('my_dict: ', my_dict)

print('\nAccessing values from dictionary')
salaries = {
    'John': 20,
    'Sally': 30,
    'Sammy': 15
}
print('salaries = ', salaries)
print('Since the index \'John\' is in dictionary the data can be accessed.')
print('salaries[\'John\']: ', salaries['John'])
print('An attempt to access to a non-existent index results in an KeyError.')
# print('salaries[\'Alibaba\']: ', salaries['Alibaba'])
print('Therefore, it may be better to use a get method.')
print('salaries.get(\'Alibaba\'): ', salaries.get('Alibaba'))
print('You may specify a default value. This value will be used if index does not exist.')
print('salaries.get(\'Alibaba\', 24): ', salaries.get('Alibaba', 24))
print('Obviously, the method works if index does exist.')
print('salaries.get(\'John\', 24): ',salaries.get('John', 24))

print('\nGetting data from more complicated dictionaries:')
people = {
    'John': [1, 2, 3],
    'Sally': [4, 5, 6]
}
print('people: ', people)
print('people[\'John\']: ', people['John'])
print('people[\'John\'][0]: ', people['John'][0])

print('\nand likewise for dictionaries:')
people = {
    'John': {
        'age': 50,
        'salary': 50
    },
    'Sally': {
        'age': 32
    }
}
print('people: ', people)
print('people[\'John\']: ', people['John'])
print('people[\'John\'][\'age\']: ', people['John']['age'])

print('\nA variable stores a reference to dictionary.')
my_dict = {'color': 'red'}
print('my_dict: ', my_dict)
print('Let\'s assign value stored by variable my_dict to other_dict.')
other_dict = my_dict
other_dict['color'] = 'blue'
print('my_dict after update of the other_dict: ', my_dict)

print('\nSome useful methods are keys, values and items')
print('people: ', people)
print('people.keys(): ', people.keys())
print('people.values(): ', people.values())
print('people.items(): ', people.items())
