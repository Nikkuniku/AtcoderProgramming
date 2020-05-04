A,B = input().split()

if len(A)==2 or len(B)==2:
    print(-1)
    exit(0)

print(int(A)*int(B))