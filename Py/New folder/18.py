"""amstrong number"""
a=input("enter a number")
s=0
for i in a:
      s=s+(int (i))**3
if str (s)==a:
      print("amstrong number")
else:
      print("not amstrong number")
      
