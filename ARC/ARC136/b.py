N = int(input())
A = input().split()
B = input().split()

ans = 'No'
for i in range(N):
    for j in range(N-i-2):
        x, y, z = A[j], A[j+1], A[j+2]
        if y+z+x <= x+y+z and y+z+x <= z+x+y:
            A[j], A[j+1], A[j+2] = y, z, x
        elif z+x+y <= x+y+z and z+x+y <= y+z+x:
            A[j], A[j+1], A[j+2] = z, x, y
for i in range(N):
    for j in range(N-i-2):
        x, y, z = B[j], B[j+1], B[j+2]
        if y+z+x <= x+y+z and y+z+x <= z+x+y:
            B[j], B[j+1], B[j+2] = y, z, x
        elif z+x+y <= x+y+z and z+x+y <= y+z+x:
            B[j], B[j+1], B[j+2] = z, x, y
if A == B:
    ans = 'Yes'
print(ans)
