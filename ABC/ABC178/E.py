n=int(input())
arr=[]
for _ in range(n):
    x,y=map(int,input().split())
    arr.append([x,y])

Z=[]
W=[]
for i in range(n):
    z=arr[i][0]+arr[i][1]
    w=arr[i][0]-arr[i][1]

    Z.append(z)
    W.append(w)

ans1=abs(max(Z)-min(Z))
ans2=abs(max(W)-min(W))

print(max(ans1,ans2))

# arr=sorted(sorted(arr,key=lambda x:x[1]),key=lambda x: x[0])
# arr2=sorted(sorted(arr,key=lambda x:x[0]),key=lambda x: x[1])

# # print(arr)
# # print(arr2)

# d1=0
# D1=[]
# for i in range(1,n):
#     tmp=0
#     x1=arr[i-1][0]
#     y1=arr[i-1][1]

#     x2=arr[i][0]
#     y2=arr[i][1]

#     if y1<=y2:
#         tmp=abs(x1-x2)+abs(y1-y2)
#     else:
#         tmp=abs(x1-x2)-abs(y1-y2)

#     d1+=tmp
#     D1.append(d1)
# d2=0
# D2=[]
# for i in range(1,n):
#     tmp=0
#     x1=arr2[i-1][0]
#     y1=arr2[i-1][1]

#     x2=arr2[i][0]
#     y2=arr2[i][1]

#     if x1<=x2:
#         tmp=abs(y1-y2)+abs(x1-x2)
#     else:
#         tmp=abs(y1-y2)-abs(x1-x2)

#     d2+=tmp
#     D2.append(d2)

# print(max(max(D1),max(D2)))