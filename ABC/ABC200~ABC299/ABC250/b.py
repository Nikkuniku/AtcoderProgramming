n, a, b = map(int, input().split())
ans = [[]*(n*b) for _ in range(n*a)]

tile1 = []
tile2 = []
j = 0
b_cnt = 0
while j < n*b:
    if b_cnt < b:
        tile1.append('.')
        tile2.append('#')
        b_cnt += 1
    else:
        tile1.append('#')
        tile2.append('.')
        b_cnt += 1

    if b_cnt == 2*b:
        b_cnt = 0
    j += 1

# tilea =
tileb = [tile2 for _ in range(a)]
ans = []

for i in range(n):
    if i % 2 == 0:
        for _ in range(a):
            ans.append(tile1)
    else:
        for _ in range(a):
            ans.append(tile2)
        # ans.append(tileb)

for i in range(len(ans)):
    print(''.join(ans[i]))
