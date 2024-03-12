x={'k1':'v1','k2':'v2','k3':'v3'}
y={}
for i in x:
    y.update({x[i]:i})
print(y)
