import math
H=int(input())

def nested(v,depth):
    while v!=1:
        depth+=1
        v=math.floor(v/2)

    return depth+1

print(sum([2**i for i in range(nested(H,0)) ]))
        