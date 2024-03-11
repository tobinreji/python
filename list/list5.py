n1=int(input("enter the no of values in list 1 :"))
l1=[]
for i in range(n1):
    l1.append(int(input('enter the value ')))

n2=int(input("enter the no of values in list 2 :"))
l2=[]
for i in range(n2):
    l2.append(int(input('enter the value ')))

li=[]
li=[i for i in l1 if i in l2]
print(li)
