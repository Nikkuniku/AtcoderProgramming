n=int(input())

word=['a','b','c']

d=1
ans=['a','b','c']
while d<n:
    l = len(ans)
    for i in range(l):
        ans.append(ans[i]+'a')
        ans.append(ans[i]+'b')
        ans.append(ans[i]+'c')

    d+=1

ans = [p for p in ans if len(p)==n]
for p in ans:
    print(p)
