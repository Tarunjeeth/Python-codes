import random
d=random.randint(1,50)
while True:
      a=int(input("Guess the number (1-50)"))
      if(a<1 or a>50):
            print("please enter the number 1-50 only")
      elif(a>d):
            print("your guess is more")
      elif(a<d):
            print("your guess is less")
      else:
            print("you won")
            break
