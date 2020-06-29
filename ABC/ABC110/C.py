s=input()
t=input()

alp='abcdefghijklmnopqrstuvwxyz'
d={}
for i in range(len(alp)):
    d[alp[i]]=i

t_arr=[[] for _ in range(26)]
s_arr=[[] for _ in range(26)]

for j in range(len(s)):
    a=s[j]
    b=t[j]
    if a in t_arr[d[b]]:
        continue
    else:
        t_arr[d[b]].append(a)

for j in range(len(s)):
    a=s[j]
    b=t[j]
    if b in s_arr[d[a]]:
        continue
    else:
        s_arr[d[a]].append(b)


ans='Yes'
for k in range(26):
    if len(t_arr[k])>=2:
        ans='No'
        break
    if len(s_arr[k])>=2:
        ans='No'
        break

print(ans)