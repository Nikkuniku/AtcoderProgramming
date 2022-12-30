import bisect
from collections import defaultdict
k = int(input())
s = list(input())
t = list(input())
t_card = defaultdict(int)
a_card = defaultdict(int)
for i in range(4):
    t_card[int(s[i])] += 1
    a_card[int(t[i])] += 1

t_score = 0
a_score = 0
for i in range(1, 11):
    t_score += i*pow(10, t_card[i])
    a_score += i*pow(10, a_card[i])
cards = []
for i in range(1, 10):
    for j in range(k-t_card[i]-a_card[i]):
        cards.append(i)
takahashi_cards = []
aoki_cards = []
for p in cards:
    q = 9*p*pow(10, t_card[p])
    r = 9*p*pow(10, a_card[p])
    takahashi_cards.append((q, p))
    aoki_cards.append((r, p))

takahashi_cards.sort(key=lambda x: x[0])
aoki_cards.sort(key=lambda x: x[0])
a_cards = []
idx = [[] for _ in range(11)]
for i, value in enumerate(aoki_cards):
    a_cards.append(value[0])
    idx[value[1]].append(i)

cnt = 0
for p in takahashi_cards:
    a = p[0]+(t_score-a_score)
    ge = bisect.bisect_left(a_cards, a)
    idx_a = bisect.bisect_left(idx[p[1]], ge)
    cnt += ge
    if idx_a > 0:
        cnt -= 1

ans = cnt/((9*k-8)*(9*k-9))
print(ans)
