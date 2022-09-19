p=int (input("enter price of the product"))
q=int (input("enter Quantity"))
ttl_amt=p*q
"""if(ttl_amt>1000):
       a=20/100*ttl_amt
       x=ttl_amt-a
       print("20percent",x)
elif(ttl_amt>500):
       b=10/100*ttl_amt
       y=ttl_amt-b
       print("10percent",y)
else:
       print(ttl_amt)"""
if(ttl_amt>1000):
       per=20
elif(ttl_amt>500):
       per=10
else:
       per=5
discount=ttl_amt*per/100
net_amt=ttl_amt-discount
print("Amount before discount", ttl_amt)
print("discount=", discount)
print("Amount after Discount", net_amt)
