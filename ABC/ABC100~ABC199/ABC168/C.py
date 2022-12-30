a,b,h,m = map(int,input().split())

import math
import numpy as np 

rad_1 =( (h/6) * math.pi ) + ( (m/360) * math.pi )

rad_2 = m/30 * math.pi 

angle_1 = a * np.array([np.cos(rad_1),np.sin(rad_1)])

angle_2 = b * np.array([np.cos(rad_2),np.sin(rad_2)])

# print(angle_1,angle_2)

# print(np.linalg.norm(angle_1))
# print(np.linalg.norm(angle_2))

inner = np.inner(angle_1,angle_2)

cos_theta = inner/(a*b)


# print(np.arccos(cos_theta)*180/math.pi)

ans = (a**2) + (b**2) - 2 * a * b * cos_theta

print(np.sqrt(ans))
# print(np.linalg.norm(angle_2-angle_1))