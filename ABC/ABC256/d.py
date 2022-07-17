n = int(input())
m = 2 * pow(10, 5)
arr = [0]*(m+3)

for _ in range(n):
    l, r = map(int, input().split())
    arr[l] += 1
    arr[r] -= 1

for i in range(m+2):
    arr[i+1] += arr[i]

Fro = True
ans = []
l = 0
r = 0
for i in range(1, m+3):
    if Fro:
        if arr[i] > 0:
            l = i
            Fro = False
    else:
        if arr[i] == 0:
            r = i
            Fro = True
            ans.append([l, r])

for p in ans:
    print(*p)
