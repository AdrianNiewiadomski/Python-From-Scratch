import math
import matplotlib.pyplot as pl
print('You have to have matplotlib library installed for this to work.')

print('Let\'s say that we have two sets of data.')
x = [0, 1, 2, 3]
y = [1, 3, 9, 27]

print('To view a plot you have to call a method plot.')
print('Its arguments may be x and y lists of data you want to display.')
pl.plot(x, y)
print('Then simply call method show.')
pl.show()

print('\nThe method plot may accept a kind of point you want to place on the plot as a third argument.')
pl.plot(x, y, 'ro')

print('You may also specify ranges of values you want to view and call method show.')
print('Notice that you have to close the first plot to view the second.')
pl.axis([-1, 4, 0, 30])
pl.show()

print('To display more series of data just place one after the other')
x = [k/10 for k in range(63)]
y1 = [math.sin(value) for value in x]
y2 = [math.cos(value) for value in x]
pl.plot(x, y1, 'bs', x, y2, 'g^')
pl.show()
