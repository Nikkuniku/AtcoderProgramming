N = int(input())
A = list(map(int, input().split()))

q = []
for a in A:
    q.append(a)
    while len(q) > 1:
        if q[-2] != q[-1]:
            break
        q.pop()
        v = q.pop()
        q.append(v + 1)
print(len(q))
