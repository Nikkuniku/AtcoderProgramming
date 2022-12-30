n=int(input())
a=list(map(int,input().split()))

a=sorted(a,reverse=True)

ans=0

for i in range(n):
    ans+=(n-1-i)*a[i]

for j in range(n):
    ans-=(n-1-j)*a[n-1-j]


print(ans)

# cum=[0]
# for i in range(n):
#     cum.append(cum[-1]+a[i])

# print(cum)

# ans=0
# for i in range(n):
#     for j in range(i,n-1):
#         p=abs(cum[j+1]-cum[j+2]+a[i])

#         ans+=p