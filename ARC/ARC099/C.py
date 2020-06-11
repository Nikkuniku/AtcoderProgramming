n,k=map(int,input().split())
a = list(map(int,input().split()))

t = (n-1)%(k-1)
if t==0:
    ans=(n-1)//(k-1)
else:
    ans =(n-1)//(k-1)+1

print(ans)


# index = a.index(1)

# if index==0 or index==n-1:
#     t = (n-1)%(k-1)
#     if t==0:
#         ans=(n-1)//(k-1)
#     else:
#         ans =(n-1)//(k-1)+1

#     print(ans)
# else:
#     fr = 0
#     to =n-1

#     if (to-index)%(k-1)==0:
#         ans_to=(to-index)//(k-1)
#     else:
#         ans_to=(to-index)//(k-1) + 1
    
#     if index%(k-1)==0:
#         ans_fr = index//(k-1)
#     else:
#         ans_fr = index//(k-1) + 1

#     print(ans_fr + ans_to)
