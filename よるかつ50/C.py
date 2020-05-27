n=int(input())
h=list(map(int,input().split()))

h_min=min(h)

for i in range(n):
    h[i]-=h_min


for j in range(n):
    if h[j]==0:
        
print(h)


