N = int(input())
ans = 'Yes'
cards = set()
prefix = list('HDCS')
number = list('A23456789TJQK')
for _ in range(N):
    S = input()
    if S[0] in prefix and S[1] in number:
        pass
    else:
        ans = 'No'
    cards.add(S)
if len(cards) != N:
    ans = 'No'
print(ans)
