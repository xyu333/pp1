def diffrent(n1,n2,n3):
    if n1 != n2 and n2 !=n3:
        return True
    else:
        return False



n1=input(print("Please input first number: "))
n2=input(print("Please input the second number: "))
n3=input(print("Please input the third number: "))

if diffrent(n1,n2,n3):
    print(f"Numbers: {n1,n2,n3} are diffrent    ")
else:
    print("Numbers are not diffrent")
    