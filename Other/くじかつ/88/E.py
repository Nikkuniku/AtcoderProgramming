s=input()
n=len(s)

if s[0]==s[1]:
    print(1,2)
    exit(0)

a=-1
b=-1
for i in range(n-2):
    d={}

    for j in range(3):
        t=s[i+j]

        if t not in d:
            d[t]=1
        else:
            a=i+1
            b=i+j+1
            print(a,b)
            exit(0)

print(a,b)

