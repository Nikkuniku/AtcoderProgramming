N = int(input())
S = []
T = 0
for _ in range(N):
    s, t = input().split()
    S.append(s)
    T += int(t)
S.sort()
T %= N
ans = S[T]
print(ans)
