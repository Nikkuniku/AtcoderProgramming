a,b =map(int,input().split())

string_a  = str(a) * b
string_b = str(b) * a

d=[]
d.append(string_a)
d.append(string_b)

s= sorted(d)

print(s[0])