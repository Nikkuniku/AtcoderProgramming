n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

set_a=set()
set_b=set()
kyotsu=set()
ans1=0
for i in range(n):
    if a[i]==b[i]:
        kyotsu.add(a[i])
        ans1+=1
    else:
        set_a.add(a[i])
        set_b.add(b[i])

ans2=len(set_a&set_b)
print(ans1)
print(ans2)