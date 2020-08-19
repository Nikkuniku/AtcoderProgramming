s=input()

import re

m1=re.fullmatch(r'keyence',s)
m2=re.fullmatch(r'k[a-z]+?\s+?eyence',s)
m3=re.fullmatch(r'ke*yence',s)
m4=re.fullmatch(r'key*ence',s)
m5=re.fullmatch(r'keye*nce',s)
m6=re.fullmatch(r'keyen*ce',s)
m7=re.fullmatch(r'keyenc*e',s)
m8=re.fullmatch(r'keyence*',s)

print(m1)
print(m2)
print(m3)
print(m4)
print(m5)
print(m6)
print(m7)
print(m8)
