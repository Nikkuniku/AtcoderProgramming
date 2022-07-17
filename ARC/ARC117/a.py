a, b = map(int, input().split())

ans = []
if a == b:
    for i in range(1, a+1):
        ans.append(i)
        ans.append(-i)
elif a > b:
    for i in range(1, b):
        ans.append(i)
        ans.append(-i)

    tmp = 0
    for i in range(b, a+1):
        ans.append(i)
        tmp += i
    ans.append(-tmp)
else:
    for i in range(1, a):
        ans.append(i)
        ans.append(-i)
    tmp = 0
    for i in range(a, b+1):
        ans.append(-i)
        tmp += -i
    ans.append(-tmp)
print(*ans)
