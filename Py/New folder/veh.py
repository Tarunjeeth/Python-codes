print("on-road price calculator for Four wheeler in Tamilnadu")
a=float (input("To calculate on-road price for Four wheeler, enter price of the vehicle"))
rd_tx=10/100*a
insrnc=4.5/100*a
reg_char=600
on_rd_price=rd_tx+insrnc+reg_char
print("On-Road price of your vehicle is",on_rd_price)
print("Price Breakup")
print("Road tax=",rd_tx, "insurance(avg)=",insrnc,"Registration Charges=",reg_char)
