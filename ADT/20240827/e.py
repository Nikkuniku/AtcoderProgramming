N, T = map(int, input().split())
A = list(map(int, input().split()))
tate = [0] * N
yoko = [0] * N
migishita = 0
hidarishita = 0
ans = -1
for t, v in enumerate(A):
    v -= 1
    i = v // N
    j = v % N
    tate[i] += 1
    yoko[j] += 1
    if i == j:
        migishita += 1
    if i + 1 + j + 1 == N + 1:
        hidarishita += 1
    if tate[i] == N or yoko[j] == N or migishita == N or hidarishita == N:
        ans = t + 1
        break
print(ans)
