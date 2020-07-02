n,h=map(int,input().split())
a=[]
b=[]
for _ in range(n):
    a_i,b_i=map(int,input().split())
    a.append(a_i)
    b.append(b_i)

import bisect,math


b=sorted(b)
index = bisect.bisect_left(b,max(a))

cnt=0
for i in range(n-1,-1,-1):
    if i>=index:
        h-=b[i]
        cnt+=1
    else:
        break
    
    if h<=0:
        h=0
        break

ans=math.ceil(h/max(a))+cnt

print(ans)


# if index==0:
#     #全部投げる
#     throw=0
#     b=sorted(b,reverse=True)
#     cnt=0
#     for i in range(n):
#         throw+=b[i]
#         cnt+=1
#         if throw>=h:
#             break
#     h-=throw
#     if h>0:
#         cnt+=math.ceil(h/max(a))
        
#     print(cnt)

# else:
#     #降った方が良い場合もある
#     throw = 0
#     cnt=0
#     for i in range(n):
#         if i>=index:
#             throw+=b[i]
#             cnt+=1
#     h-=throw
#     if h>0:
#         cnt+=math.ceil(h/max(a))

#     print(cnt)
