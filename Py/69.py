words=("qwerty","alpha","stigma","black","intel")
for i in words:
    s=i.lower()
    f=s[0]
    if (f=="a" or f=="e" or f=="i" or f=="o" or f=="u"):
        print(i)
