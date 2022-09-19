#emp={empno:[name,age,salary],...sixitems}
#example
#emp={"E001":["Arun",22,35000],...sixitems}

def age():
    for i in emp:
        if (int(emp[i][1])>50):
            print(emp[i][0])
            

def show(nam):
    nonam=True
    for i in emp:
        if (emp[i][0]==nam):
            print("name",emp[i][0])
            print("age",emp[i][1])
            print("salary",emp[i][2])
            nonam=False
            break
    if (nonam==True):
        print(f'name "{nam}" is not there')

n=1
emp={}
while (n<=2):
    empno="E00"+str(n)
    emp[empno]=[]
    emp[empno].append(input("enter employee's name"))
    emp[empno].append(int(input("enter employee's age")))
    emp[empno].append(int(input("enter employee's salary")))
    print()
    n=n+1
print(emp)
show(input("enter name of employee to be searched"))
age()
