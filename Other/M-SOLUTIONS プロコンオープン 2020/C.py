n,k=map(int,input().split())
a=list(map(int,input().split()))

for i in range(k,n):
    if a[i]>a[i-k]:
        print('Yes')
    else:
        print('No')



# cumpro=[]

# pro=1
# for i in range(n):
#     if i<k:
#         pro*=a[i]
#         cumpro.append(pro)
#     else:
#         pro/=a[i-k]
#         pro*=a[i]
#         cumpro.append(pro)

# for j in range(k,n):
#     if cumpro[j]>cumpro[j-1]:
#         print('Yes')
#     else:
#         print('No')

# for j in range(k,n):
#     if j==k:
#         a=cumpro[k-1]
#         b=cumpro[j]/cumpro[j-k]
#     else:
#         a=cumpro[j-1]/cumpro[j-1-k]
#         b=cumpro[j]/cumpro[j-k]

#     if b>a:
#         print('Yes')
#     else:
#         print('No')

