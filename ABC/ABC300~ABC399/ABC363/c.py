from itertools import permutations

N, K = map(int, input().split())
S = list(input())
P = list(set(permutations(S)))
ans = len(P)

for s in P:
    for i in range(N - K + 1):
        isPalindrome = True
        for j in range(K):
            if s[i + j] != s[i + K - 1 - j]:
                isPalindrome = False
                break
        if isPalindrome:
            ans -= 1
print(ans)
