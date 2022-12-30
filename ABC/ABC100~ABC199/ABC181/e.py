from bisect import bisect_right
n, m = map(int, input().split())
H = list(map(int, input().split()))
W = list(map(int, input().split()))
H.sort()
evens = [0]
odds = [0]

for i in range(n):
    if i % 2 == 0:
        odds.append(odds[-1]+H[i])
    else:
        evens.append(evens[-1]+H[i])

ans = []
for i in range(m):
    idx = bisect_right(H, W[i])
    k = (idx//2)+1
    tmp = 0
    tmp += evens[k-1]+odds[-1]-odds[k]
    tmp -= odds[k-1]+evens[-1]-evens[k-1]

    if idx % 2 == 0:
        tmp += H[idx]
        tmp -= W[i]
    else:
        tmp += W[i]
        tmp -= H[idx-1]

    ans.append(tmp)

print(min(ans))
