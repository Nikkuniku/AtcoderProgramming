N = int(input())
A = list(map(int, input().split()))
odd = sum([A[i] % 2 for i in range(N)])
ans = 'YES'
if odd % 2 != 0:
    ans = 'NO'
print(ans)
