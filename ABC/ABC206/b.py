n=int(input())

coin=0

day=0
for i in range(n):
    coin+=(i+1)
    day=(i+1)
    
    if coin>=n:
        break

print(day)