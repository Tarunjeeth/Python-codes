l=[2,3,4,5]
l1=[]
l2=[]
k=0
for i in range(4):
    in1=input("enter a number")
    l1.append(in1)
l2.append(int(l[0])+int(l1[0]))
l2.append(int(l[1])+int(l1[1]))
l2.append(int(l[2])+int(l1[2]))
l2.append(int(l[3])+int(l1[3]))
print(l2)
