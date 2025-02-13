K = int(input())
A, B = input().split()
A_ten = 0
A = A[::-1]
for i in range(len(A)):
    A_ten += pow(K, i) * int(A[i])
B_ten = 0
B = B[::-1]
for i in range(len(B)):
    B_ten += pow(K, i) * int(B[i])
ans = A_ten * B_ten
print(ans)
