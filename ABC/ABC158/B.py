N,A,B =map(int,input().split()) 

# import collections

# blues = 'b' * A
# reds = 'r' * B

# set_balls = blues + reds

# all_balls = set_balls * ( N // ( A + B ) + 1 )

# balls_N = all_balls[:N]

# c = collections.Counter(balls_N)
# print(c['b'])

p = N//(A+B)

if N - p*(A+B) < A:
    print(A*p + N - p*(A+B) )
else:
    print(A*p+A)