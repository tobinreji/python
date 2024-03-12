n="hello world hello world"
dict={}
x=n.split()
def count(elements):
    if elements[-1]=='.':
        element=elements[0:len(elements)-1]
    if elements in dict:
        dict[elements]+=1
    else:
        dict.update({elements:1})
for elements in x:
    count(elements)
for keys in dict:
    print("frequency of ",keys,end=" ")
    print(":",end=" ")
    print(dict[keys],end=" ")
    print()
