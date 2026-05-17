import time
a = 1000
b = 0
c = 900

while a > 0:
    a -= 1
    if a == c:
        a -= b
    else: 
        b += 1
    
    # Используем f-строку для корректного вывода
    print(f"seconds = {a} b = {b}")
    time.sleep(1)

print()
