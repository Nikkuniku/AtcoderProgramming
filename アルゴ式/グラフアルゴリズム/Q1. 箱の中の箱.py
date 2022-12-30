N, X = map(int, input().split())
A = [0]+list(map(int, input().split()))
depth = [0]*N
for i in range(1, N):
    depth[i] = depth[A[i]]+1
print(depth[X])
