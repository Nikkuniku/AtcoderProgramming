from collections import defaultdict
s = input()
s = s.replace('S', ' S')
s = s.replace('H', ' H')
s = s.replace('D', ' D')
s = s.replace('C', ' C')
s = list(s.split(' '))
s = s[1:]
d = defaultdict(int)
d["S10"] = 4
d["SJ"] = 4
d["SQ"] = 4
d["SK"] = 4
d["SA"] = 4
d["H10"] = 1
d["HJ"] = 1
d["HQ"] = 1
d["HK"] = 1
d["HA"] = 1
d["D10"] = 2
d["DJ"] = 2
d["DQ"] = 2
d["DK"] = 2
d["DA"] = 2
d["C10"] = 3
d["CJ"] = 3
d["CQ"] = 3
d["CK"] = 3
d["CA"] = 3
cnt = [0, 0, 0, 0, 0]
i = 0
while True:
    if s[i] in d:
        p = d[s[i]]
        cnt[p] += 1
        if cnt[p] == 5:
            break
    i += 1
j = 0
ans = []
while j != i:
    if d[s[j]] != p:
        ans.append(s[j])
    j += 1

if ans:
    print(''.join(ans))
else:
    print(0)
