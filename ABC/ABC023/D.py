n=int(input())
h,s=[],[]

for _ in range(n):
    h_i,s_i=map(int,input().split())
    
    h.append(h_i)
    s.append(s_i)

H=[]
for i in range(n):
    H.append(h[i] + n*s[i])

l=0
r=max(H)

while r-l>1:
    # # binary search
    mid = (r+l)//2

    ok=True
    t=[]

    for i in range(n):
        if (mid - h[i])<0:
            ok=False
            break
        else:
            t.append((mid - h[i])/s[i])
    
    t=sorted(t)

    for i in range(len(t)):
        if t[i]<i:
            ok=False
            break

    if ok:
        r=mid
    else:
        l=mid

print(r)