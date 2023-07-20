N = int(input())
P = list(map(int, input().split()))
q = []
a = -1
for i in range(N-1, 0, -1):
    if P[i-1] > P[i]:
        q.append(P.pop())
        a = P.pop()
        q.append(a)
        break
    else:
        q.append(P.pop())
b = -1
for c in q:
    if c < a:
        b = max(b, c)
P.append(b)
q.remove(b)
q.sort(reverse=True)
P += q
print(* P)
