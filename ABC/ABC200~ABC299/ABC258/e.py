from bisect import bisect_left
n, q, x = map(int, input().split())
w = list(map(int, input().split()))
for _ in range(q):
    k = int(input())

cumw = [0]
for i in range(n):
    cumw.append(cumw[-1]+w[i])
print(*cumw)

i = 0
idx = set({i})
z = sum(w)
tmp = 0
cnt = 0
box = []
while True:
    if tmp < x:
        if tmp+z < x:
            tmp += z*(x//z)
            cnt *= n*(x//z)
        else:
            j = bisect_left(cumw, x-tmp)
            cnt += j
            tmp += cumw[j]-cumw[i]
            i = j
        if tmp >= x:
            box.append(cnt)
            cnt = 0
            tmp = 0
            if i in idx:
                break
            else:
                idx.add(i)
