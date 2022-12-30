n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

a_max = max(a)
b_min = min(b)

ans=0
if a_max<=b_min:
    ans=b_min-a_max+1

print(ans)
