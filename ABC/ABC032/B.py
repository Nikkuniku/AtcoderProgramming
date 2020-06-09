s=input()
k=int(input())

n = len(s)

d={}


if n<k:
    print(0)
elif n==k:
    print(1)
else:
    for i in range(n-k+1):
        sub = s[i:i+k]

        if sub not in d:
            d[sub]=1
        else:
            d[sub]+=1
        
    # print(d)
    print(len(d))
