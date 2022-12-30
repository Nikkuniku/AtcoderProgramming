s=input()
n=len(s)
k=int(input())

index=-1
for i in range(n):
    if s[i]!='1':
        index=i
        break

if index==-1:
    print(1)
else:
    if k<=index:
        print(s[k-1])
    else:
        print(s[index])