no=[12,34,21,34,56,32,34,34,12,56,87,89]
no.sort()

def mean():
    sum1=0
    for i in no:
        sum1=sum1+i
    m=sum1/len(no)
    print("mean=",m)

def mode():
    n=0
    s=0
    for i in no:
        if (no.count(i)>n):
            n=no.count(i)
            s=i
    print("mode=",s)

def median():
    noo=len(no)
    if (len(no)%2!=0):
        median=no[(noo+1)/2]
    else:
        m1=no[noo/2]
        m2=no[(noo/2)+1]
        median=(m1+m2)/2
    print("median is",median)

def median1():
    if (len(no)%2!=0):
        m=int((len(no)+1)/2)
        a=no[m-1]
    else:
        m=int(len(no)/2)
        a=(no[m-1]+no[m])/2
    print(no)
    print("median is",a)
        

mean()
mode()
median1()

