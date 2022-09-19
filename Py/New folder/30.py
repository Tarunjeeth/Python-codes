n=int (input("enter a number"))
i=2
s=0
while (i<=int(n/2)):
      if (n%i==0):
            s=1
      i=i+1
if (s==1):
      print("not prime")
else:
      print("prime")
