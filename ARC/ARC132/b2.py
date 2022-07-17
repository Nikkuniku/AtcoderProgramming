n = int(input())
p = list(map(int, input().split()))

a = []
b = []
Flg = True

for i in range(n):
    if i == 0:
        a.append(p[i])
    else:
        if Flg:
            if abs(p[i-1]-p[i]) == 1:
                a.append(p[i])
            else:
                b.append(p[i])
                Flg = False
        else:
            b.append(p[i])

ansflg = True
if len(a) >= 2:
    if a[0]-a[1] > 0:
        ansflg = False
else:
    if b[0]-b[1] > 0:
        ansflg = False

if ansflg:
    if b:
        ans = min(len(a), len(b)+2)
    else:
        ans = 0
else:
    ans = min(len(a), len(b))+1
print(ans)
