N = int(input())
A = []
for _ in range(N):
    P = sorted(list(map(int, input().split()))[1:])
    A.append(P)
A.sort()
B = sum(A, [])
C = sorted(sum(A, []))
ans = 'No'
if B == C:
    ans = 'Yes'
print(ans)
