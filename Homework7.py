# task1
numbers = []
for i in range(5):
    number = input(f'Enter number {i} =')
    numbers.append(number)
print(numbers)

# task2
A = [1, 2, 3, 4, 5]
removed_last_element = A.pop()
print(A)

#task3
A = []
for i in range(10):
    number = input(f'Enter number {i} =')
    A.append(number)
print(A)
question_number = (input("special N="))
counter = A.count(question_number)
print(counter)

# task4
A = []
n = int(input('Enter number ='))
for i in range(n):
    number = input(f'Enter number {i} =')
    A.append(number)
print(A)
A.reverse()
print(A)

# task5
A = []
for i in range(5):
    number = input(f'Enter number {i} =')
    A.append(number)
print(A)
C = []
for c in A:
    if c.isdigit():
        if 5 > int(c):
            continue
        C.append(c)
print(C)

# task6
A = []
n = int(input('Enter number ='))
for i in range(n):
    number = input(f'Enter number {i} =')
    A.append(number)
print(A)

a_min = A[0]
for j in range(n):
    if A[j] < a_min:
        a_min = A[j]
print(f"min = {a_min}")

a_max = A[0]
for j in range(n):
    if A[j] > a_max:
        a_max = A[j]
print(f"max = {a_max}")

#task7
text = input("write text")
digit_counter = 0
for i in text:
    if i.isdigit():
        digit_counter += 1
if digit_counter != 0:
    print(digit_counter)
else:
    print("No numbers in the text")




