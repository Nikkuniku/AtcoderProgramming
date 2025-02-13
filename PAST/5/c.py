P = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N = int(input())
if N == 0:
    exit(print(0))
ans = []
while N:
    tmp = N % 36
    ans.append(P[tmp])
    N //= 36
ans = ans[::-1]
print(*ans, sep="")
