from collections import deque
n = int(input())
s = input()

p_ind = -1
for i in range(n):
    if s[i] == 'p':
        p_ind = i
        break
ans = []
q = deque()
for i in range(p_ind, n):
    q.appendleft(s[i])
    if s[i] == 'p':
        tmp = []
        for j in range(len(q)):
            if q[j] == 'p':
                tmp.append('d')
            else:
                tmp.append('p')
        for j in range(i+1, n):
            tmp.append(s[j])
        ans.append(''.join(tmp))

ans.sort()
out = 'd'*p_ind if p_ind >= 0 else s
if ans:
    out += ans[0]
print(out)
