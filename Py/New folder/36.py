a=input("enter a word")
m=""
j=0
while(j<len(a)):
      m=a[j]+m
      j=j+1
if(m==a):
      print("palindrome")
else:
      print("not palindrome")
