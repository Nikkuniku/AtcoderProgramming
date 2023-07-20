N, K = map(int, input().split())
A = list(map(int, input().split()))+[0]
arr = A
csum = [0]*len(arr)
for i in range(len(arr)-1):
    if i < len(arr) - K:
        p = arr[i]+csum[i]
        csum[i] -= p
        csum[i+K] += p
    csum[i+1] += csum[i]
Q = int(input())
for _ in range(Q):
    L, R = map(int, input().split())
    print(csum[L], csum[R])
    print(arr[L]+csum[L], arr[R]+csum[R])


print(arr)
print(csum)
for i in range(len(arr)):
    arr[i] += csum[i]
print(arr)
