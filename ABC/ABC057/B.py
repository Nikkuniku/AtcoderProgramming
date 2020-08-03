n,m=map(int,input().split())

student =[] 
for _ in range(n):
    a,b=map(int,input().split())
    student.append([a,b])

check=[]

for _ in range(m):
    a,b=map(int,input().split())
    check.append([a,b])

for s in student:
    ans=10**9
    i=0
    for j in range(m):
        c=check[j]
        dist = abs(c[0]-s[0]) + abs(c[1]-s[1])
        if dist<ans:
            ans=dist
            i=j+1

    print(i)