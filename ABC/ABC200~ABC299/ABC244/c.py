n=int(input())
nums=[]
for i in range(1,2*n+2):
    nums.append(i)

nums=set(nums)
v=min(nums)
print(v,flush=True)
nums.discard(v)
while True:
    x=int(input())
    if x==0:
        exit(0)
    else:
        nums.discard(x)
        v=min(nums)
        print(v,flush=True)
        nums.discard(v)