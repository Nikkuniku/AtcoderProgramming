n,l = map(int,input().split())

import numpy as np

apple = np.array([l+(i+1)-1 for i in range(n)])

ringo = np.argmin(np.array(list(map(abs,apple))))

apple=np.delete(apple,ringo)

print(sum(apple))