#greatest number using list
i=1
li=[]
while (i<=7):
      a=int(input("enter the number"))
      li.append(a)
      i=i+1
n=li[0]
for x in li:
      if (x>n):
            n=x
print(n)
