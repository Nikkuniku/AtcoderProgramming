
n= int(input())
n=30 + (n%30)
cards=[i+1 for i in range(6)]

for i in range(n):
    k1 = (i%5)+1
    k2 = (i%5)+2
    cards[k1-1],cards[k2-1]=cards[k2-1],cards[k1-1]

cards =list(map(str,cards))
ans =''.join(cards)

print(ans)