s=input()
alp='abcdefghijklmnopqrstuvwxyz'

if s=='zyxwvutsrqponmlkjihgfedcba':
    print(-1)
    exit(0)

d={}
e={}
for i in range(len(alp)):
    d[alp[i]]=i
    e[i]=alp[i]

n=len(s)
if n!=26:
    ans=[]
    for i in range(n):
        ans.append(d[s[i]])

    for j in range(26):
        if j not in ans:
            ans.append(j)
            break

    st=''
    for k in ans:
        st+=e[k]
else:
    arr=[]

    dp=[]
    for i in range(n):
        dp.append(d[s[i]])
    
    while True:
        v=dp.pop()

        tmp=[j for j in arr if j>v]
        if len(tmp)!=0:
            dp.append(min(tmp))
            break
        
        arr.append(v)
        
    st=''
    for k in dp:
        st+=e[k]



print(st)