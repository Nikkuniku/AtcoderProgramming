n= int(input())

v = list(map(int,input().split()))
c = list(map(int,input().split()))


x_y = 0
for i in range(2**n):

    tmp_x_y = 0
    tmp_cost=0
    tmp_value=0

    for j in range(n):
        if (i>>j) &1:
            tmp_cost+=c[j]
            tmp_value+=v[j]

    tmp_x_y = tmp_value - tmp_cost

    x_y = max(x_y,tmp_x_y)

print(x_y)