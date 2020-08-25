n=int(input())

# total=0
# i=1
# while i*i<=n:
#     if i*i==n:
#         break

#     if n%i==0:
#         total+=(n//i)-1

    
#     i+=1

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

arr = make_divisors(n)
d={}
for i in arr:
    d[i]=0
total=0

for j in range(len(arr)):
    t = arr[j]

    if t**2 == n:
        d[t]=1
        continue
    if d[t]==0:
        total+=(n//t)-1
        d[t]=1
        d[n//t]=1

print(total)
