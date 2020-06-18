n=int(input())
a=list(map(int,input().split()))

if n<=2:
    print(1)
    exit(0)


flg=0
cnt=0

tmp=[]
for i in range(1,n):
    if a[i]>a[i-1]:
        tmp.append(1)
    elif a[i]==a[i-1]:
        tmp.append(0)
    else:
        tmp.append(-1)
flg=0
swi=0
for j in range(len(tmp)):
    if swi==1:
        flg=tmp[j]
        swi=0
        continue
    
    if flg==0:
        flg=tmp[j]
    elif flg==1:
        if tmp[j]==-1:
            cnt+=1
            flg=-1
            swi=1
    elif flg==-1:
        if tmp[j]==1:
            cnt+=1
            flg=1
            swi=1

print(cnt+1)


    

# for i in range(1,n):
#     if swi==1:
#         if a[i-1]==a[i]:
#             flg==0
#         elif a[i-1]<a[i]:
#             flg=1
#         elif a[i-1]>a[i]:
#             flg=-1
#         swi=0
#         continue

#     if a[i-1]<a[i]:
#         if flg==-1:
#             cnt+=1
#             swi=1
#         flg=1
#     elif a[i-1]>a[i]:
#         if flg ==1:
#             cnt+=1
#             swi=1
#         flg=-1

# print(cnt+1)