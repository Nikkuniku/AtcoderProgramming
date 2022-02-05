l=1
r=2
for i in range(50):
    m=(l+r)/2
    m_2 = m**2

    if m_2<2:
        l=m
    else:
        r=m 
    print(m)
    if 1.414212<=m<1.414214:
        print(i)
        break

print('実際の値')
print(2**0.5)