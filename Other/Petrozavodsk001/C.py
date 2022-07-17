n = int(input())

l = 0
r = n
print(l, flush=True)
s = input()
even = s
if s == 'Male':
    odd = 'Female'
elif s == 'Female':
    odd = 'Male'
else:
    exit(0)
while True:
    mid = (l+r)//2
    print(mid, flush=True)
    s = input()
    if s == 'Vacant':
        exit(0)
    if mid % 2 == 0:
        if s == even:
            l = mid
        else:
            r = mid
    else:
        if s == odd:
            l = mid
        else:
            r = mid
