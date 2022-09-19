def askcountry (i="india"):
      print("your country is", i)
a=input("From which country you are?")
if (a==""):
      askcountry()
else:
      askcountry(a)
