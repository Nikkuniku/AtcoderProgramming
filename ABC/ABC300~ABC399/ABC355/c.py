N, T = map(int, input().split())
A = list(map(int, input().split()))
ans = -1
tate = [0] * N
yoko = [0] * N
migishita = 0
hidarishita = 0
for t, a in enumerate(A):
    a -= 1
    i = a // N
    j = a % N
    yoko[i] += 1
    tate[j] += 1
    if i == j:
        migishita += 1
    if j == N - 1 - i:
        hidarishita += 1
    if yoko[i] == N or tate[j] == N or migishita == N or hidarishita == N:
        ans = t + 1
        break
print(ans)
