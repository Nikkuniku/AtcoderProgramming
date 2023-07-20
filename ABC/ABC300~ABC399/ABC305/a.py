N = int(input())
ans = -1
P = []
for i in range(0, 105, 5):
    P.append((abs(N-i), i))
P.sort()
print(P[0][1])
