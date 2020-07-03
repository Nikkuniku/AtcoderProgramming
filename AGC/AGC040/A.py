s=input()

a=[0]*(len(s)+1)

prev=0
for i in range(len(s)):
    if s[i]=='<':
        a[i+1]=a[i]+1

for j in range(len(s)-1,-1,-1):
    if s[j]=='>':
        if a[j]>a[j+1]+1:
            continue
        else:
            a[j]=a[j+1]+1

print(sum(a))