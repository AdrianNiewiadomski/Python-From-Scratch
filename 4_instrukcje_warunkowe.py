print("Podaj swoj wiek")
wiek = int(input())

if wiek >=35:
    print("Mozesz kandydowac na prezydenta")
elif wiek >= 21:
    print("Mozesz kandydowac na posla")
else:
    print('Nie mozesz kandydowac')

print("-----------------------------------------------------")

login_correct = True
password_correct = True
if login_correct and password_correct:
    print("Access granted!")
else:
    print("Podaj poprawny login i haslo!")

print("-----------------------------------------------------")

PIN_correct = False
if not PIN_correct:
    print("Podaj poprawny PIN!")