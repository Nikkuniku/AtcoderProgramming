n, m = map(int, input().split())
if m < 0:
    print(-1)
    exit()

if n == 1:
    if m != 0:
        print(-1)
    else:
        print(1, 2)
    exit()

if n >= 2:
    if 0 <= m <= n-2:
        ans = []
        for i in range(m+1):
            ans.append([2*i+1, 2*i+2])

        for i in range(n-(m+1)):
            ans.append([-10**7+i, 10**7 - i])

        for j in range(n):
            ans[j][0] += 10**8
            ans[j][1] += 10**8
            print(*ans[j])
    else:
        print(-1)
