a=int (input("enter a number"))
b=int (input("enter another number"))
c=input("enter option 1-7")
if(c=="1"):
      ans=a+b
      print(f"addition of two numbers {ans}")
elif(c=="2"):
      ans=a-b
      print(f"subtraction of two numbers {ans}")
elif(c=="3"):
      ans=a/b
      print(f"division of two numbers %.2f" %ans)
elif(c=="4"):
      ans=a*b
      print(f"multiplication of two numbers {ans}")
elif(c=="5"):
      ans=a%b
      print(f"remainder= {ans}")
elif(c=="6"):
      ans=a**b
      print(f"exponent= {ans}")
elif(c=="7"):
      ans=a//b
      print(f"quotient= {ans}")
