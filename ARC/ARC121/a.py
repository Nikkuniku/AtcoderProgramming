n=int(input())
arr=[]


for j in range(n):
    x,y = map(int,input().split())
    arr.append([x,y,j])

arr_x=sorted(arr,key=lambda x :x[0])
arr_y=sorted(arr,key=lambda x :x[1])

target=set()
for i in (0,1,-1,-2):
    target.add(arr_x[i][2])

for i in (0,1,-1,-2):
    target.add(arr_y[i][2])
candidate =[]

for k in range(n):
    if arr_y[k][2] in target:
        candidate.append([arr_y[k][0],arr_y[k][1]])


import itertools
p = list(itertools.combinations(candidate, 2))

ans=[]
for c in p:
    d1 = abs(c[0][0]-c[1][0])
    d2 = abs(c[0][1]-c[1][1])

    ans.append(max(d1,d2))

ans = sorted(ans,reverse=True)

print(ans)
print(ans[1])

# # 前回答のダメなケース
# 4
# -4 -4
# -2 -2
# 2 2
# 4 4