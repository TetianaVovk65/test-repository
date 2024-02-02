# task1
question = int(input("number="))
for triangle_rows in range(1, question + 1):
    for triangle_elements in range(1, question+2-triangle_rows):
        print("*", end=" ")
    print(" ")

# task2
question = int(input("number="))
for triangle_rows in range(1, question + 1):
    for triangle_elements in range(1, triangle_rows+1):
        print("*", end=" ")
    print(" ")

# task3
question = int(input('Enter the number: '))
for i in range(question):
    print(f"{' ' * i}{'*' * (question - i)}")

# task4
question = int(input('Enter the number: '))
for i in range(question):
    print(f"{' ' * (question - (i + 1))}{'*' * (i+1)}")
