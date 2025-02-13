from collections import deque

N = int(input())
A = list(map(int, input().split()))
ans = []
q = deque()
tmp = 0
for a in A:
    if q and q[-1][0] == a:
        v, c = q.pop()
        if c + 1 >= a:
            tmp -= c
            pass
        else:
            q.append((a, c + 1))
            tmp += 1
    else:
        q.append((a, 1))
        tmp += 1
    ans.append(tmp)
print(*ans, sep="\n")
