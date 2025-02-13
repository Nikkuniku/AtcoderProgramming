N = int(input())
P = [[], []]
for _ in range(N):
    a, s = input().split()
    if s == "L":
        P[0].append(int(a))
    else:
        P[1].append(int(a))
ans = 0
for k in range(2):
    for i in range(1, len(P[k])):
        ans += abs(P[k][i - 1] - P[k][i])
print(ans)
