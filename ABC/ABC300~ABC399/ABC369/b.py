N = int(input())
L = []
R = []
for _ in range(N):
    a, s = input().split()
    a = int(a)
    if s == "L":
        L.append(a)
    else:
        R.append(a)
ans = 0
for i in range(len(L) - 1):
    ans += abs(L[i + 1] - L[i])
for i in range(len(R) - 1):
    ans += abs(R[i + 1] - R[i])
print(ans)
