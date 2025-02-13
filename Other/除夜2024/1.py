ans = []
while 1:
    a = int(input())
    ans.append(a)
    if a == 0:
        break
print(*ans[::-1], sep="\n")
