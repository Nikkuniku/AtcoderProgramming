t = int(input())
for _ in range(t):
    p = list(map(int, input().split()))
    p.sort()
    a = p[0]
    b = p[1]
    c = p[2]

    ans = []
    if (b-a) % 3 == 0:
        ans.append(b)
    if (c-b) % 3 == 0:
        ans.append(c)
    if (c-a) % 3 == 0:
        ans.append(c)
    if ans:
        print(min(ans))
    else:
        print(-1)
