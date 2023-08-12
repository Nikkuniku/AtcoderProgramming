K, N, M = map(int, input().split())
P = []
for i in range(K):
    P.append((int(input()), i+1))
P.sort()
S = [score for score, _ in P]
border = (-(-K//12))
Q = S[K-border]
maybe_gold = [P[i][1] for i in range(K-border, K)]
gold = maybe_gold[::-1]
for i in range(K-border):
    score = S[i]+100*(N-M)
    if score >= Q:
        maybe_gold.append(P[i][1])
P = S[K-border-1]
if P+100*(N-M) > Q:
    gold.pop()
print(*sorted(gold), sep="\n")
print('--------')
print(*sorted(maybe_gold), sep="\n")
