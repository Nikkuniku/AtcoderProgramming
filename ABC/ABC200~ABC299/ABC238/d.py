t=int(input())
def bitplace(n):
    s=set()
    i=0
    while n>0:
        q,mod=divmod(n,2)
        if mod==1:
            s.add(i)
        n//=2
        i+=1
    return s

for _ in range(t):
    a,s=map(int,input().split())
    AND_bit=bitplace(a)
    for i in list(AND_bit):
        s-=2*pow(2,i)
    ans='Yes'
    if s<0:
        ans='No'
    else:
        SUM_bit=bitplace(s)
        if not AND_bit.isdisjoint(SUM_bit):
            ans='No'
    print(ans)