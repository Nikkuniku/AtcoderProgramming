N = int(input())
A = list(map(int, input().split()))
cnt1 = A.count(1)
B = set(A)
if len(B) == 1:
    if N % 2 == 0:
        exit(print(0))
    else:
        exit(print(-1))
ans = 0
if N % 2 == 0:
    ans = -1
else:
    if cnt1 % 2 == 0:
        ans = -1
    else:
        ans = max(A) - 1
print(ans)
