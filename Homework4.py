# task1
a = int(input("write number a= "))
b = int(input("write number b= "))
c = int(input("write number c= "))
if (a > 10 and b > 10 and c > 10) and ((a + b) % 3 == 0):
    print("Yes")
else:
    print("No")

# task2
a = int(input("write number a= "))
b = int(input("write number b= "))
c = int(input("write number c= "))
if a > b and a > c:
    print(f"{a} is max")
elif b > a and b > c:
    print(f"{b} is max")
else:
    print(f"{c} is max")

# task3
number = int(input("enter 3-digit number ="))
firstNumber = int(number / 100)
lastNumber = number % 10
print(f"{firstNumber} = First digit, {lastNumber} = Third digit")
reserved_number = firstNumber + lastNumber
print(reserved_number)
