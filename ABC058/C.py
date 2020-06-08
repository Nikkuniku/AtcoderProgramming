n=int(input())

from collections import Counter


ans={}
for i in range(n):
    s = input()

    c= dict(Counter(s))

    if i==0:
        ans=c
    else:
        ans_merge = ans.copy()

        delete=[]

        for k,v in ans_merge.items():
            if k in c:
                ans_merge[k] = min(ans_merge[k],c[k])
            else:
                delete.append(k)

        for j in delete:
            del ans_merge[j]

        ans = ans_merge

ans = sorted(ans.items(),key=lambda x:x[0])

string=''

for k in ans:
    string+=k[0]*k[1]

print(string)