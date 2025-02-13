A = []
while 1:
    a = int(input())
    A.append(a)
    if a == 0:
        break
print(*A[::-1], sep="\n")
