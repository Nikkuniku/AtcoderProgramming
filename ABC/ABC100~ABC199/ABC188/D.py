n,C=map(int,input().split())
d={}
for i in range(n):
    a,b,c=map(int,input().split())
    if a in d:
        d[a]+=c
    else:
        d[a]=c

    if b+1 in d:
        d[b+1]-=c
    else:
        d[b+1]=-c
p=list(d.items())
p=sorted(p)
p_list=[]
for k in range(len(p)):
    p_list.append(list(p[k]))

# # いもす法
for j in range(1,len(p_list)):
    p_list[j][1]+=p_list[j-1][1]
ans = 0
for m in range(len(p_list)-1):
    if p_list[m][1]>C:
        tmp = C
    else:
        tmp = p_list[m][1]
    ans+=tmp*(p_list[m+1][0]-p_list[m][0])
print(ans)