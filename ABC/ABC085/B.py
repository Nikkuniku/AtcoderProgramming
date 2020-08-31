n=int(input())
d = []
for _ in range(n):
    d.append(int(input()))

d=sorted(d)

cnt=1
prev =d[0]
for i in range(n-1):
    if prev != d[i+1]:
        cnt+=1
        prev =d[i+1]
    
print(cnt)