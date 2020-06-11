s=input()

import re

result = re.findall('@[a-z]+',s)

result =set(result)

result = list(result)
result = sorted(result)

for i in result:
    print(i[1:])