from collections import Counter, deque
n = int(input())
a = list(map(int, input().split()))
c = Counter(a)
b = list(c.items())
books = sorted(list(c.keys()))
for i in range(len(b)):
    if b[i][1] > 1:
        for _ in range(b[i][1]-1):
            books.append(b[i][0])

q = deque(books)
now = 0

while q:
    v = q[0]
    if v == now+1:
        q.popleft()
        pass
        now += 1
    else:
        if len(q) >= 2:
            q.pop()
            q.pop()
            now += 1
        else:
            break

print(now)
