N = int(input())
S = input()
M = N // 2
A = S[:M]
B = S[M + 1 :]
ans = "No"

if N % 2 != 0 and A == "1" * M and S[M] == "/" and B == "2" * M:
    ans = "Yes"
print(ans)
