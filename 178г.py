import math

n = int(input("Введите количество чисел: "))
a = []
for i in range(n):
    a.append(int(input(f"Введите число {i+1}: ")))

count = 0
for k in a:
    if k < ((k-1)-(k+1))/2:
        count += 1

print("Количество чисел, удовлетворяющих условию:", count)
