n,k=map(int,input().split())
s=input()
p=[0]*n
d={}
alpha="abcdefghijklmnopqrstuvwxyz"
for i in range(len(alpha)):
    d[alpha[i]]=i+1
print(d)

for j in range(n):
    p[j]=d[s[j]]
print(p)