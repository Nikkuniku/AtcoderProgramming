n,m=map(int,input().split())
l = 1
r = n
for j in range(m):

    l_i,r_i = map(int,input().split())

    l = max(l,l_i)
    r = min (r,r_i)

if r>=l:
    print(r-l+1)
else:
    print(0)



