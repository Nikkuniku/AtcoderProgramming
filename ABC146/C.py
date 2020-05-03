A,B,X=map(int,input().split())

# Maxes = [A*((10**i)-1) + B*i for i in range(1,10+1)]

# index=0
# for j in range(len(Maxes)):
#     if X>=Maxes[j]:
#         index=j

# rng_min = (10**(index+1))-1
# rng_max = 10**(index+2)

# ans=0
# for k in range(rng_min,rng_max):
#     if k==rng_min:
#         if A*k + B*(index+1)<=X:
#             ans=k
#     else:
#         if A*k + B*(index+2)<=X:
#             ans=k
#         else:
#             break

# print(ans)


min_val = 0
max_val = 10**9+1

l = min_val
r = max_val

c = int((l+r)/2)

def keta(n):
    return len(str(n))

def f(x):
    return A*x + B*keta(x)

while r-l>1:
    if f(c)==X:
        print(c)
        exit(0)

    if f(c)<=X:
        l = c
        c = int((l+r)/2)
    else:
        r = c
        c = int((l+r)/2)
        
    
print(c)



