from bisect import bisect_left, bisect_right
s = input()
t = input()

indexes = [[] for _ in range(26)]

for i in range(len(s)):
    indexes[ord(s[i])-97].append(i)


ans = 0
pre = -1
cnt = 0
for i in range(len(t)):
    p = ord(t[i])-97
    if not indexes[p]:
        print(-1)
        exit()
    idx = bisect_right(indexes[p], pre)
    if idx == len(indexes[p]):
        idx = indexes[p][0]
    else:
        idx = indexes[p][idx]

    if pre < idx:
        pass
    else:
        cnt += 1
    pre = idx

ans = len(s)*cnt + idx+1
print(ans)
