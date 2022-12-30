K=int(input())

k=0
while True:
    if K>= 2**k:
        k+=1
    else:
        break
ans=['2']

l=2**(k-1)
r=2**k
while r-l>1:
    mid = (r+l)//2

    if K<mid:
        ans.append('0')
        r=mid
    else:
        ans.append('2')
        l=mid

print(''.join(ans))