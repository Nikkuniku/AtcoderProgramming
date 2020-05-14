foods=[]

for _ in range(5):
    foods.append(int(input()))

from itertools import permutations

l = [0,1,2,3,4]

p = permutations(l,5)

time=pow(10,9)
for v in p:
    order = v

    tmp_time=0

    for i in range(5):

        tmp_time+=foods[order[i]]

        if tmp_time%10!=0 and i<4:

            tmp_time = ((tmp_time//10)+1) * 10

    
    time= min(time,tmp_time)

print(time)