for i in range (1,1000):
      s=0
      for j in str(i):
            s=s+(int (j))**3
      if i==s:
            print(s)
