x={'t1':'s1','t2':'s2'}
y={}
for i in x:
    y.update({x[i]:i})
print(y)
