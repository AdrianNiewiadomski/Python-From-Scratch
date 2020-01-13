import time

for i in range(10,0,-1):
    print(i)
    time.sleep(1)

print("BUM!")

print("-------------------------------")

print("czas Unixowy w sekundach:")
timer = time.time()
print(timer)

print("-------------------------------")
sekund = 0
while sekund<5:
    if time.time()-timer>1:
        print(f"sekund : {sekund}")
        sekund = sekund+1
        timer = time.time()

print("-------------------------------")
#rownolegle wykonywanie kodu
i=0
timer1 = time.time()
timer2 = time.time()

while True:
    if time.time()-timer1>1:
        print("1 sec")
        timer1 = time.time()
    if time.time()-timer2>2:
        print("2 sec")
        timer2 = time.time()
        i = i+1
        if i>3:
            break

print("-------------------------------")
timer = time.time()

sec = int(timer%60)
min = int((timer/60)%60)
godz = int((timer/3600)%24)+1   #Central European Time (CET), UTC +1
print(f"{godz} : {min} : {sec}")

print("-------------------------------")
import datetime

aktualna_data = datetime.datetime.now()
print(aktualna_data)
print(aktualna_data.hour, " : ", aktualna_data.minute)
print(aktualna_data.strftime("%H:%M %d.%m.%Y"))