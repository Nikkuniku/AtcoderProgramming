s=input()

n=len(s)


from collections import Counter
odd=[]
even=[]
c=list(Counter(s).values())
for num in c:
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)
k=len(odd)

if k==0:
    print(n)
else:
    print(2*((n-k)//(2*k))+1)

# odd=sorted(odd)
# even=sorted(even)

# heapq.heapify(odd)

# if len(odd)==0:
#     print(sum(even))
#     exit(0)

# while even:
#     f=heapq.heappop(odd)
#     e=even.pop()
#     f+=e
#     heapq.heappush(odd,f)

# if len(odd)==1:
#     print(min(odd))
#     exit(0)

# m=min(odd)
# while True:
#     l=odd.pop()
#     s=heapq.heappop(odd)
#     if l-2>m and s+2>m:
#         heapq.heappush(odd,l-2)
#         heapq.heappush(odd,s+2)
#     else:
#         heapq.heappush(odd,s)
#         heapq.heappush(odd,l)
#         break

# print(min(odd))
    
    