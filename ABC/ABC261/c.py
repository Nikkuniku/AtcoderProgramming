from collections import defaultdict
n = int(input())
d = defaultdict(int)

ans = []
for i in range(n):
    s = input()
    cnt = d[s]
    if cnt > 0:
        ans.append(s+'('+str(cnt)+')')
    else:
        ans.append(s)
    d[s] += 1
print(*ans, sep="\n")
