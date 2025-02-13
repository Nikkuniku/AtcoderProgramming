H = int(input())
now = 0
for i in range(60):
    now += pow(2, i)
    if now > H:
        break
print(i + 1)
