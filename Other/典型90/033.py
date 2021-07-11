h,w=map(int,input().split())

from math import ceil

ans = ceil(h/2)*ceil(w/2)
if h==1 or w==1:
    ans=h*w

print(ans)

# led =[['.']*w for _ in range(h)]


# for i in range(h):
#     for j in range(w):
#         if led[i][j]=='.':
#             flg=0
#             for x in [-1,0]:
#                 for y in [-1,0]:
#                     if 0<=i+x<=h-1 and 0<=j+y<=w-1:
#                         if led[i+x][j+y]=='.':
#                             continue
#                         else:
#                             flg+=1
            
#             if flg==0:
#                 led[i][j]='#'
#             else:
#                 continue

# ans=0
# for i in range(h):
#     for j in range(w):
#         if led[i][j]=='#':
#             ans+=1

# print(ans)
# print(**led,sep="\n")
