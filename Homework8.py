# task1
September = {"Ivanov", "Shevchenko", "Popli", "Lidia"}
October = {"Oser", "Ivanov", "Serb", "Shevchenko"}
both = September.intersection(October)
only_october = October.difference_update(September)
print(both)
print(October)

# task2
permissions = {}
n = int(input('Put the number of files: '))
for _ in range(n):
    s = input().split()
    permissions[s[0]] = set(s[1:])
for _ in range(int(input('Put the number of files for checking: '))):
    perm, file = input().split()
    if perm == 'read':
        perm = 'R'
    if perm == 'write':
        perm = 'W'
    if perm == 'execute':
        perm = 'X'
    if perm in permissions[file]:
        print('OK')
    else:
        print('Access denied')