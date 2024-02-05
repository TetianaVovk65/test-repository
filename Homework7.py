"""# task1
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
"""
# task5
A = []
for i in range(5):
    number = input(f'Enter number {i} =')
    A.append(number)
print(A)
C = []
for c in A:
    if c.isdigit():
        if c > 5:
            C.append(c)
print(C)

# task6
A = []
n = int(input('Enter number ='))
for i in range(n):
    number = input(f'Enter number {i} =')
    A.append(number)
print(A)
#task7

