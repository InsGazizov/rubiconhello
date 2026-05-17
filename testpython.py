import time
import random
a = 3000
b = 0
c = 900 - random.randint(0, 900)

times = 0
text = " за минуту рандом не выпал меньше нуля и алгоритм закрылся"
count = 0
while a > 0:
    count += 1
    if a == c:
        a -= b
    else: 
        b += random.randint(0, 50)
        if b > 100:
            b = random.randint(0,50)
    d = random.randint(0, 100) - b
    a -= d
    # Используем f-строку для корректного вывода
    print(f"#{count}: a = {a}, b = {b}.")

    time.sleep(1)
    times +=1 
    if times > 90:
        break
    else:
        text = ""


print()
print("end and summary time: " + str( times) + text)

