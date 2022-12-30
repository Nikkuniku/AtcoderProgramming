n,d,k=map(int,input().split())
root=[]
for _ in range(d):
    l,r=map(int,input().split())
    root.append([l,r])

for _ in range(k):
    s,t=map(int,input().split())

    for i in range(d):
        l=root[i][0]
        r=root[i][1]
        if s <l or r<s:
            continue
        elif (l<=s and s<=r) and (l<=t and t<=r):
            print(i+1)
            break
        elif l<=s and s<=r:
            if s<t:
                s=r
            else:
                s=l