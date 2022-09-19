l=[1,1]
for i in range(1,20):
      l.append(l[len(l)-1]+l[len(l)-2])
print(l)
