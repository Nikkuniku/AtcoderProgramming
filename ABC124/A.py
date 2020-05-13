a,b=map(int,input().split())
import  numpy as np

point = 0

button =np.array([a,b])

point += np.max(button)
index = np.argmax(button)

button[index]-=1

point += np.max(button)

print(point)
