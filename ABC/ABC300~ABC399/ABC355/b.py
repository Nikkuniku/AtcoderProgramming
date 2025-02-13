N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = []
for a in A:
    C.append((a, "A"))
for b in B:
    C.append((b, "B"))
C.sort()
ans = "No"
for i in range(N + M - 1):
    _, ci = C[i]
    _, cj = C[i + 1]
    if ci == cj == "A":
        ans = "Yes"
print(ans)
