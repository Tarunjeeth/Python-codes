a=int (input("enter no. of students"))
x=1
while (x<=a):
      b=input("enter name")
      c=int(input("enter the mark of 1st subject"))
      d=int(input("enter the mark of 2nd subject"))
      e=int(input("enter the mark of 3rd subject"))
      average=(c+d+e)/3
      if(90<=average):
            print("grade a")
      elif(70<=average):
            print("grade b")
      else:
            print("grade c")
      x=x+1
