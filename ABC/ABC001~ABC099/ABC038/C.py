n=int(input())
a=list(map(int,input().split()))

cnt=0
r=1
for l in range(n):

    while r<n and a[l]<a[r]:
        if a[r-1]<a[r]:
            r+=1
        else:
            break

    if a[l]<a[r-1]:
        cnt+=(r-1)-l

    if l==r-1:
        r+=1

print(cnt+n)  