S = input()
T = input()
N = len(S)
for i in range(N):
    for j in range(i + 1, N + 1):
        tmp = S[:i]
        tmp += S[i + 1 : j] + S[i] + S[j:]
        if tmp == T:
            print(S[i], j - i - 1)
            break
