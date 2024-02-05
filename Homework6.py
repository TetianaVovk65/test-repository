# task1
word = str(input("write a word="))
reverse_word = word[::-1]
if reverse_word == word:
    print("+")
else:
    print("-")

# task2
phrase = str(input("write a phrase="))
search_for = str(input("write a word that you are search for="))
result = phrase.find(search_for)
if result != -1:
    print("yes")
else:
    print("no")

#task3
phrase = str(input("write a phrase="))
if phrase.startswith("abc"):
    change1 = phrase.replace("abc", "www")
    print(change1)
else:
    print(phrase + "zzz")

# task4
phrase = (input("write a phrase="))
removed_numbers = ''
for i in phrase:
    if i not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
        removed_numbers = removed_numbers + i
print(removed_numbers)

#task5
email = (input("Type text: "))
verify_for_dog = email.find("@")
verify_for_dot = email.find(".")
if verify_for_dot and verify_for_dog:
    print("yes")
else:
    print("no")
