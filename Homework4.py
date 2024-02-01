"""# task1
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
    print(f"{c} is max")"""

# task3
number = (input("enter 3-digit number ="))
if number.isdigit() and len(number) == 3:
    fine_number = int(number)
    firstNumber = (fine_number // 100)
    middleNumber = fine_number % 100 // 10
    lastNumber = fine_number % 10
    print(f"{firstNumber} = First digit,{middleNumber}= Middle digit, {lastNumber} = Third digit")
    reserved_number = str(f"{lastNumber}{middleNumber}{firstNumber}")
    print(reserved_number)
else:
    print('Error')
