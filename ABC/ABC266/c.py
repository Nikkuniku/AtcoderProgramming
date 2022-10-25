import math
import numpy as np
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))

ab = np.array([b[0]-a[0], b[1]-a[1]])
ad = np.array([d[0]-a[0], d[1]-a[1]])
bc = np.array([c[0]-b[0], c[1]-b[1]])
cd = np.array([d[0]-c[0], d[1]-c[1]])

absvecAB = np.linalg.norm(ab)
absvecAD = np.linalg.norm(ad)
absvecBC = np.linalg.norm(bc)
absvecCD = np.linalg.norm(cd)

cosDAB = np.inner(ab, ad)/(absvecAB*absvecAD)
cosABC = np.inner(-ab, bc)/(absvecAB*absvecBC)
cosBCD = np.inner(cd, bc)/(absvecCD*absvecBC)
cosCDA = np.inner(cd, -ad)/(absvecCD*absvecAD)
DAB = math.degrees(math.acos(cosDAB))
ABC = math.degrees(math.acos(cosABC))
BCD = math.degrees(math.acos(cosBCD))
CDA = math.degrees(math.acos(cosCDA))

print(DAB)
print(ABC)
print(BCD)
print(CDA)
