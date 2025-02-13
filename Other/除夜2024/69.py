M = int(input())
ans = []
while M > 0:
    for k in range(10, -1, -1):
        res = pow(3, k)
        if M >= res:
            M -= res
            ans.append(k)
            break
print(len(ans))
print(*ans)
