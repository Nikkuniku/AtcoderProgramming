n = int(input())
s = list(map(int, input().split()))
a = [0, 0, 0]
for i in range(n-1):
    d = -(s[i]-s[i+1])
    p = a[i]+d
    a.append(p)
alpha = [a[::3], a[1::3], a[2::3]]
ans = []
for i in range(3):
    ans.append(-min(alpha[i]))
if sum(ans) > s[0]:
    print('No')
    exit()
elif sum(ans) < s[0]:
    ans[0] += s[0]-sum(ans)

for i in range(3, n+2):
    ans.append(ans[i % 3]+a[i])
print('Yes')
print(*ans)
