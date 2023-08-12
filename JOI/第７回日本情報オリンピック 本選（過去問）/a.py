N = int(input())
A = []
for i in range(N):
    S = int(input())
    if i % 2 == 0:
        if A and A[-1][0] == S:
            c, cnt = A.pop()
            cnt += 1
            A.append((c, cnt))
        else:
            A.append((S, 1))
    else:
        if A[-1][0] == S:
            c, cnt = A.pop()
            cnt += 1
            A.append((S, cnt))
        else:
            tmp = 0
            while A:
                c, cnt = A.pop()
                tmp += cnt
                if c == S:
                    break
            A.append((S, tmp+1))
ans = sum([p if c == 0 else 0 for c, p in A])
print(ans)
