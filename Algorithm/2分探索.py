a=[1,3,5,7,9,11,13,15,17,19]

b=10

l = 0
r = len(a)
c = int((l+r)/2)

while r-l>1:
    if b == a[c]:
        print(c)
        exit(0)
        
    if b > a[c]:
        l = c
        c = int((l+r)/2)
    else:
        r = c
        c = int((l+r)/2)

print(c)