d=input("enter a character")
e=int(input("enter a no.of rows"))
for i in range(1,e+1):
      for j in range(1,i+1):
            print(d," ",end="")
      print()
for i in range(e,0,-1):
      for j in range(1,i+1):
            print(d," ",end="")
      print()
