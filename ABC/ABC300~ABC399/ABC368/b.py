N = int(input())
A = list(map(int, input().split()))
ans = 0
while 1:
    ans += 1
    A.sort(reverse=True)
    for i in range(2):
        A[i] -= 1
    cnt = 0
    for a in A:
        cnt += a > 0
    if cnt <= 1:
        break
print(ans)
