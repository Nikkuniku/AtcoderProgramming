n = int(input())
a = list(map(int, input().split()))
even = []
odd = []

for i in range(n):
    if a[i] % 2 == 0:
        even.append(a[i])
    else:
        odd.append(a[i])

ans = []
even.sort()
odd.sort()
if len(even) >= 2:
    ans.append(even[-2]+even[-1])
if len(odd) >= 2:
    ans.append(odd[-2]+odd[-1])

if ans:
    print(max(ans))
else:
    print(-1)
