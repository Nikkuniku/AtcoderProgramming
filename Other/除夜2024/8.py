H = int(input())
res = 0
i = 0
while 1:
    res += 1 << i
    i += 1
    if res > H:
        break
print(i)
