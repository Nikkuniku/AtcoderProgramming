N = int(input())
A = [int(input()) for _ in range(N)]
ans = 0
j = N
for i in range(N-1, -1, -1):
    if i > j:
        continue
    if i >= A[i]:
        ans += A[i]
        for j in range(i, i-A[i]-1, -1):
            if A[j] == A[i]+(j-i):
                pass
            elif A[j] > A[i]+(j-i):
                break
            else:
                print(-1)
                exit()
    else:
        ans = -1
        break
print(ans)
