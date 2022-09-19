import random
def gen_pass (length=8):
      li=["*","#","@","!"]
      upper_case=chr(random.randint(65,90))
      lower_case=chr(random.randint(97,122))
      special=random.choice(li)
      digit=random.randint(10000,99999)
      password=upper_case+lower_case+special+str(digit)
      pas=random.sample(password,length)
      password=("").join(pas)
      return(password)
print(gen_pass())
