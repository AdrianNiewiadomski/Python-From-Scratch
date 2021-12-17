tuple1 = ("ser", "mleko", "parowki")
print(tuple1)
print(tuple1[0])
print(tuple1[0][0])

print("--------------------")
produkty1 = ("owoce")
#tuple1 = tuple1.__add__(produkty1) #TypeError: can only concatenate tuple (not "str") to tuple
produkty2 = ("jajka", "owoce")
tuple1 = tuple1.__add__(produkty2)
print(tuple1)

print("--------------------")
tuple1 = ("ser", 1, 2.5)
print(tuple1)

print("--------------------")
mylist = ["ser", 1, 2.5]
mylist[0] = 'NEW'
print(mylist)

mytuple = ("ser", 1, 2.5)
#mytuple[0] = 'NEW' #TypeError: 'tuple' object does not support item assignment
print(mytuple)
