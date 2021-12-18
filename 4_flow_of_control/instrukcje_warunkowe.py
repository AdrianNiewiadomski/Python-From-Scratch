print("Podaj swoj wiek")
wiek = int(input())

if wiek >=35:
    print("Mozesz kandydowac na prezydenta")
elif wiek >= 21:
    print("Mozesz kandydowac na posla")
else:
    print('Nie mozesz kandydowac')

print("-----------------------------------------------------")

is_login_correct = True
is_password_correct = True
if is_login_correct and is_password_correct:
    print("Access granted!")
else:
    print("Incorrect login or password!")

print("-----------------------------------------------------")

PIN_correct = False
if not PIN_correct:
    print("Podaj poprawny PIN!")
