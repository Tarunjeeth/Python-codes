sen=input("enter a sentence")
l=[]
word=""
for i in sen:
    if (i==" " or i=="."):
        l.append(word)
        word=""
    else:
        word=word+i
print(l)
