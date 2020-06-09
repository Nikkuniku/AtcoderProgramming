a,b,c,d = map(int,input().split())
from fractions import gcd

lcm = c*d//gcd(c,d)

num_b_c = b//c
num_b_d = b//d
num_b_cd = b//lcm

if a%c==0:
    num_a_c = a//c - 1
else:
    num_a_c = a//c

if a%d==0:
    num_a_d = a//d - 1
else:
    num_a_d = a//d

if a%lcm==0:
    num_a_cd = a//lcm - 1 
else:

    num_a_cd = a//lcm


alls = b - a + 1


c_div = num_b_c - num_a_c
d_div = num_b_d - num_a_d

cd_div = num_b_cd -num_a_cd


print(alls - ( c_div + d_div - cd_div))

