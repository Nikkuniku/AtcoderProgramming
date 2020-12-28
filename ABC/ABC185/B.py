n,m,t=map(int,input().split())
battery=n

ans='Yes'
b_last=0
for _ in range(m):
    a_i,b_i=map(int,input().split())
    
    battery = battery - (a_i-b_last)
    if battery<=0:
        ans='No'
        break
    
    battery = battery + (b_i-a_i)
    if battery>=n:
        battery=n


    b_last=b_i

battery = battery - (t - b_last)

if battery<=0:
    ans='No'

print(ans)
