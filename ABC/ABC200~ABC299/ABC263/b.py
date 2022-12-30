n = int(input())
p = [-1]+list(map(int, input().split()))

i = n
idx = n-1
cnt = 0
while i != 1:
    k = p[idx]
    idx = k-1
    cnt += 1
    i = k

print(cnt)
