Q, H, S, D = map(int, input().split())
N = int(input())
A = min(S, 2*H, 4*Q)
B = D
ans = N*A
if N > 1:
    ans = min(ans, (N//2)*D+(0 if N % 2 == 0 else A))
print(ans)
