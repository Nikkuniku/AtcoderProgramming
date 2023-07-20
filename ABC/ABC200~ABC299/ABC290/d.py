N, D = map(int, input().split())
cnt = 1
x = 0
res = [0]*N
res[x] = cnt
x = (x+D) % N
while 1:
    if res[x] == 0:
        cnt += 1
        res[x] = cnt
        x = (x+D) % N
    else:
        x = (x+1) % N
    if cnt == N:
        break
print(res)
for i in range(1, N+1):
    print(res.index(i))
