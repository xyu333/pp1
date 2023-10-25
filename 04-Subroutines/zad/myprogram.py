import digits

number = int(input("Enter a number: "))
sum_d = digits.sum_digits(number)
msg = f"Sum of digits {number} is {sum_d}"
print(msg)


def read_number(n1):
    print(f'{n1}') 