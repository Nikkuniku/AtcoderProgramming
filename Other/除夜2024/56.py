N = int(input())
A = list(map(int, input().split()))
ans = 0
while 1:
    ans += 1
    A.sort()
    p = A.pop()
    q = A.pop()
    p -= 1
    q -= 1
    if p > 0:
        A.append(p)
    if q > 0:
        A.append(q)
    cnt = 0
    for a in A:
        cnt += a > 0
    if cnt <= 1:
        break
print(ans)
