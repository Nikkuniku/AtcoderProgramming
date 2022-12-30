n, x = map(int, input().split())
A = []
B = []
cuma = [0]
cumb = [0]
for _ in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    cuma.append(a+cuma[-1])
    cumb.append(b+cumb[-1])
ans = float('inf')
for i in range(n):
    cnt = i+1
    tmp = cuma[i+1]+cumb[i+1]

    if cnt == x:
        ans = min(ans, tmp)
    elif cnt < x:
        tmp += (x-cnt)*B[i]
        ans = min(ans, tmp)

print(ans)
