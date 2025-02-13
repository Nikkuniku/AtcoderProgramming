from collections import defaultdict

N = int(input())
T = 0
User = []
for _ in range(N):
    s, c = input().split()
    User.append(s)
    T += int(c)
User.sort()
d = defaultdict(int)
for i in range(N):
    d[i] = User[i]
p = T % N
print(d[p])
