slownik = {'imie':'Jan', 'nazwisko':'Kowalski'}
print(slownik)
print(type(slownik))
print(slownik['nazwisko'])

print("----------------------------")
salaries = {'John':20, 'Sally':30, 'Sammy':15}
print(salaries)

salaries['Bobby']=22
salaries['Sammy']=22
print(salaries)

print("----------------------------")
salaries = {'John':20, 'Sally':30, 'Sammy':15}
print(salaries.get('John', 24))
print(salaries.get('Alibaba', 24))

print("----------------------------")
people = {'John':[1,2,3], 'Sally':[4,5,6]}
print(people)
print(people['John'])
print(people['John'][0])

print("----------------------------")
people = {'John':{'age':50,'salary':50}, 'Sally':{'age':32}}
print(people)
print(people['John'])
print(people['John']['age'])

print("----------------------------")
print(people.keys())
print(people.values())
print(people.items())