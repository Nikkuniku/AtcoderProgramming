n = int(input())
p = list(map(int,input().split()))

p = sorted(p)

c_left = p[int(n/2)-1]
c_right = p[int(n/2)]

print(c_right-c_left)