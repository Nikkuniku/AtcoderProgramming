a=[4,6,7,8,1,2,110,2,4,12,3,9]
n=len(a)
x = 25
cnt=0
right = 0
total=0
for left in range(n):
    
    while right < n and total + a[right] <= x:
        total+= a[right]
        right+=1

    cnt += right - left

    if left == right:
        right+=1
    else:
        total-=a[left]


print(cnt)
    
