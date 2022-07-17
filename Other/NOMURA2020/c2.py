n = int(input())
a = list(map(int, input().split()))

b = []
for i in range(n+1):
    if i == 0:
        p = 1-a[i]
    else:
        p = 2*b[i-1]-a[i]
    if p < 0:
        print(-1)
        exit()
    b.append(p)

ans = 0
answer = [0]*(n+1)
for j in range(n, -1, -1):
    if j < n:
        answer[j] += min(b[j], answer[j+1])
    answer[j] += a[j]
ans = sum(answer)
print(ans)
