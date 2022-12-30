N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ca = [0]*N
cb = [0]*N
sa, sb = set(), set()
ka, kb = [], []
for i in range(N):
    if A[i] not in sa:
        sa.add(A[i])
        ka.append(A[i])
    if B[i] not in sb:
        sb.add(B[i])
        kb.append(B[i])
    ca[i] = len(sa)
    cb[i] = len(sb)

issame = [False]*(N+1)
s = set()
for i in range(min(len(ka), len(kb))):
    if ka[i] in s:
        s.discard(ka[i])
    else:
        s.add(ka[i])
    if kb[i] in s:
        s.discard(kb[i])
    else:
        s.add(kb[i])
    if len(s) == 0:
        issame[i+1] = True

ans = []
Q = int(input())
for _ in range(Q):
    x, y = map(lambda x: int(x)-1, input().split())
    res = 'No'
    if ca[x] == cb[y] and issame[ca[x]]:
        res = 'Yes'
    ans.append(res)
print(*ans, sep="\n")
