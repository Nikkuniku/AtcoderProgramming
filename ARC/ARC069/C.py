n,m=map(int,input().split())

ans=0
m+=n*2

ans+=m//4

print(ans)

# if m-2*n>=0:
#     m-=2*n
#     ans+=n + (m//4)
#     print(ans)
# else:
#     ans+=m//2
#     print(ans)
#     exit(0)
