from collections import deque
s = input()

cnt = [0]*30


def conv(t):
    return ord(t)-97


q = deque()
ans = []
for i in range(len(s)):
    v = s[i]
    q.append(v)
    cnt[conv(v)] += 1
    if len(q) > 1 and max(cnt) >= 1+(len(q)//2):
        ans.append((i+1-(len(q)-1), i+1))
    if len(q) >= 3:
        w = q.popleft()
        cnt[conv(w)] -= 1

if ans:
    print(*ans[0])
else:
    print(-1, -1)
