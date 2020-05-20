s= input()

import re

str_s = re.findall('[ATGC]+',s)

length = [len(p) for p in str_s]

if length==[]:
    print(0)
else:
    print(max(length))