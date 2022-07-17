from collections import deque
n = int(input())
a = list(map(int, input().split()))
neg = []
pos = []
for i in range(n):
    if a[i] >= 0:
        pos.append(a[i])
    else:
        neg.append(a[i])

neg.sort()
pos.sort()
neg = deque(neg)
pos = deque(pos)
ope = []
while len(neg)+len(pos) > 2:
    if not pos and neg:
        y = neg.pop()
        x = neg.pop()
        pos.append(x-y)
    elif pos and not neg:
        x = pos.popleft()
        y = pos.popleft()
        neg.append(x-y)
    elif pos and len(neg) > 1:
        x = pos.pop()
        y = neg.pop()
        pos.append(x-y)
    elif len(pos) > 1 and neg:
        x = neg.popleft()
        y = pos.popleft()
        neg.appendleft(x-y)
    ope.append([x, y])
ans = -1
if pos and neg:
    x = pos.pop()
    y = neg.pop()
elif not pos and neg:
    x = neg.pop()
    y = neg.pop()
elif pos and not neg:
    x = pos.pop()
    y = pos.pop()
ope.append([x, y])
ans = x-y
print(ans)
for p in ope:
    print(*p)
