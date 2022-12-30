from collections import Counter
N, M = map(int, input().split())
A = list(map(int, input().split()))
C = Counter(A)
print(C)
cards = sorted(list(C.items()), key=lambda x: x[0])
cards = 2*cards
suma = sum(A)
INF = 1 << 62
S = [INF]*len(cards)
# for i in range(len(cards)):
