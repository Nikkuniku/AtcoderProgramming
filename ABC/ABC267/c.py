n, m = map(int, input().split())
a = list(map(int, input().split()))
cum = [0]
for i in range(n):
    cum.append(cum[-1]+a[i])

ans = 0
for i in range(m):
    ans += (i+1)*a[i]

answer = [ans]
for j in range(m, n):
    tmp = ans-(cum[j]-cum[j-m])+m*a[j]
    ans = tmp
    answer.append(ans)

print(max(answer))
