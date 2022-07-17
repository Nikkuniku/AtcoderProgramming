from itertools import groupby
n = int(input())
s = input()
gr = groupby(s)
runs = []
for k, v in gr:
    runs.append((k, len(list(v))))
vs = []
cnt_one = 0
for i in range(len(runs)-2):
    if runs[i][0] == 'A' and runs[i+1][0] == 'R' and runs[i+2][0] == 'C':
        if runs[i+1][1] == 1:
            p = min(runs[i][1], runs[i+2][1])
            if p == 1:
                cnt_one += 1
            else:
                vs.append(p)
vs.sort(reverse=True)
ans = 0

for i in range(len(vs)):
    if vs[i] > cnt_one:
        ans += 2*cnt_one
        vs[i] -= cnt_one
        if vs[i] == 1:
            cnt_one = 1
        else:
            cnt_one = 0
    else:
        ans += 2*(vs[i]-1)
        cnt_one -= (vs[i]-1)
        cnt_one += 1
        vs[i] = 1
ans += 2*len([i for i in vs if i >= 2])
ans += cnt_one

print(ans)
