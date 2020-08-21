s=list(input())
n=int(input())

ans=s
for _ in range(n):
    l,r=map(int,input().split())

    tmp=ans[(l-1):r]
    tmp=list(reversed(tmp))

    ans=ans[:(l-1)]+tmp+ans[r:] 


ans_string = ''.join(ans)
print(ans_string)
    