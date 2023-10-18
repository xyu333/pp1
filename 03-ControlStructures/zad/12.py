n1 = (input(print("Enter the first persons name: ")))
a1 = int(input(print('Enter the first persons age: ')))
n2 = (input(print("Enter the second persons name: ")))
a2 = int(input(print('Enter the second persons age: ')))

if a1>=18 and a2>=18:
    print("Both " +  n1 + "and " + n2 + " Are adults")
elif a1>=18 and a2<18:
    print(n1 + "Is an adult but " + n2 + " Is not ")
elif a1<18 and a2>=18:
    print(n1 + "Is not an adult but " + n2 + " Is.")

elif a1<18 and a2<18:
    print("None of the people provided are adults")