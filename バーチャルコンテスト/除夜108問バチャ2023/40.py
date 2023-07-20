N = int(input())
A = list(map(int, input().split()))
P = [0, 0, 0, 0, 0]
for i in range(N):
    P[0] += 1
    for j in range(3, -1, -1):
        P[min(j+A[i], 4)] += P[j]
        P[j] = 0
print(P[4])
