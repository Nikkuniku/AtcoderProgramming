from itertools import permutations
N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))
p = list(permutations([i+1 for i in range(N)]))
a, b = -1, -1
for i, c in enumerate(p):
    if c == P:
        a = i
    if c == Q:
        b = i
print(abs(a-b))
