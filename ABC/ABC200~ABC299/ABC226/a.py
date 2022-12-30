from decimal import Decimal
import decimal

x=decimal.Decimal(input())

round=lambda x:(x*2+1)//2
ans = round(x)
print(ans)