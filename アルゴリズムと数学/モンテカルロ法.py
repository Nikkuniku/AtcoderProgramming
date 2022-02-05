from random import uniform,random
from matplotlib import pyplot as plt

def kyori(c_x,c_y,x,y):
    return ((c_x-x)**2 +(c_y-y)**2)**0.5 
n=1000000
m=0
ans_a=0
ans_b=0
X=[]
Y=[]
for i in range(n):
    x=6*random()
    y=9*random()

    # 円Aに含まれるかどうか
    d_a = kyori(3,7,x,y)
    if d_a<=2: 
        ans_a+=1
    # 円Bに含まれるかどうか
    d_b=kyori(3,3,x,y)
    if d_b<=3:
        ans_b+=1
    X.append(x)
    Y.append(y)

    # ともに含まれている領域

    if d_a<=2 and d_b<=3:
        m+=1
print(ans_a)
print(ans_b)
print(m)

plt.scatter(X,Y,color='white',edgecolors='red')
plt.xlim(-1,7)
plt.ylim(-1,10)
plt.show()
