xa,ya,xb,yb,xc,yc = map(int,input().split())


xb = xb - xa
yb = yb - ya

xc = xc - xa
yc = yc - ya

xa = xa - xa
ya = ya - ya

print(abs(xb*yc - yb*xc)/2)