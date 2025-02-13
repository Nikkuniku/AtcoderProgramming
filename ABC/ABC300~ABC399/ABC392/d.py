from collections import Counter

N = int(input())
Dice = []
Dices = [0] * N
for i in range(N):
    K, *A = map(int, input().split())
    Dices[i] = K
    C = Counter(A)
    Dice.append(C)
ans = -1
for i in range(N):
    for j in range(i + 1, N):
        bunbo = Dices[i] * Dices[j]
        P = Dice[i]
        Q = Dice[j]
        temp = 0
        for k, v in P.items():
            if k in Q:
                temp += v * Q[k]
        ans = max(ans, temp / bunbo)
print(ans)
