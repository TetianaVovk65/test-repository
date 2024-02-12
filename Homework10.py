# task1
"""def change(lst):
    result = lst[:]
    result[0], result[-1] = result[-1], result[0]
    return result


print(change(["Sveta", "sasha", "Katya", "Andriy"]))


# task2
def to_dict(lst):
    return {element: element for element in lst}


print(to_dict(['grey', (2, 17), 3.11, -4]))



# task3
def sum_range(start, end):
    if start > end:
        start, end = end, start
    return sum(range(start, end+1))


print(sum_range(-7, 7))
"""


def read_last(lines, file):
    if lines > 0:
        with open(file, encoding='utf-8') as text:
            file_lines = text.readlines()[-lines:]
        for line in file_lines:
            print(line.strip())
        else:
            print('positive number')


print(read_last(3, 'Homework10.txt'))