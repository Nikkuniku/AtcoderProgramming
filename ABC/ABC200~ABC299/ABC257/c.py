from bisect import bisect_left
n = int(input())
s = input()
w = list(map(int, input().split()))
vals = set(w)
child = []
adult = []
for i in range(n):
    if s[i] == '0':
        child.append(w[i])
    else:
        adult.append(w[i])
child.sort()
adult.sort()
ans = 0
for p in vals:
    p1 = p-0.1
    p2 = p+0.1

    id1 = bisect_left(child, p1)
    id2 = bisect_left(adult, p1)
    ans = max(ans, id1+len(adult)-id2)

    id1 = bisect_left(child, p2)
    id2 = bisect_left(adult, p2)
    ans = max(ans, id1+len(adult)-id2)

print(ans)
