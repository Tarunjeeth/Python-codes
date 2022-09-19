def hcf(x,y):
    if (x>y):
        m=x
        n=y
    else:
        m=y
        n=x
    r=m%n
    if (r==0):
        h=n
    else:
        h=hcf(n,r)
    return(h)


def lcm(x,y):
    l=int((x*y)/hcf(x,y))
    return(l)

a=int(input("enter a number"))
b=int(input("enter another number"))
h=hcf(a,b)
l=lcm(a,b)
print(f"hcf of {a} and {b} is {h}")
print(f"lcm of {a} and {b} is {l}")
