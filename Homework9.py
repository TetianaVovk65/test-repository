import random

# task1
""""

with open("Test.txt") as file:
    numbers = [line.strip().split(',')[1] for line in file]
print(numbers)

# task2
file = open("her.txt", "w")
question = input("write text: ")
file.writelines(question)
file.close()

# task3
A = []
question_number = (int(input("Write number of iterations: ")))
for i in range(question_number):
    number = input(f'Enter number {i} =').split(' ')
    A.append(number)
file = open("numbers.txt", "w")
file.writelines(str(A))

# task4
random_numbers = {random.randint(1, 100) for _ in range(100)}
file = open("random_numbers.txt", "w")
for i in random_numbers:
    file.writelines(str(f"{i}\n"))

# task5
file = open('Test.txt')
lines = 0
words = 0
for line in file:
    lines += 1
    words += len(line.split())
print("Words:", words)

"""
# task6
file = open('Test.txt')
a = (file.readline())
b = ''
while a:
    b = b + a
    a = file.readline()
b = b.split(' ')
result = 0
for i in b:
    if i.isdigit():
        result = result + int(i)
print(result)
