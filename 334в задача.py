n = 0
for i in range(1, 101):
    for j in range(1, 101):
        n += (j-i+1)/(i+j)


print (n)