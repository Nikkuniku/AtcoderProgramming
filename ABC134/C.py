N=int(input())

seq=[]

for i in range(N):
    a= int(input())
    seq.append(a)

numbers=set(seq)

A_max=list(numbers)[-1]

if N>=2:
    if len(numbers)>=2:
        A_second = list(numbers)[-2]
    else:
        A_second = A_max

for k in range(N):
    if seq[k]==A_max:
        print(A_second)
    else:
        print(A_max)

# 2.両端から
# left=[0]
# for i in range(N-1):
#     left_i=max(left[i],seq[i])

#     left.append(left_i)

# right=[0]

# for j in range(N-1):
#     right_j = max(right[j],list(reversed(seq))[j])

#     right.append(right_j)

# right = list(reversed(right))

# for k in range(N):
#     print(max(left[k],right[k]))