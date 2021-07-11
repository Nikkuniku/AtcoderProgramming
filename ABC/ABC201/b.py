n=int(input())
s=[]
t=[]

for _ in range(n):
    s_i,t_i =input().split()
    t_i=int(t_i)
    s.append(s_i)
    t.append(t_i)

h=max(t)
tmp=0
index=-1
for i in range(n):
    if tmp<t[i] and t[i]!=h:
        tmp=t[i]
        index=i

print(s[index])