N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))
H2 = []
for i in range(N):
    H2.append(abs(T-H[i]*0.006-A))
ans = H2.index(min(H2))+1
print(ans)
