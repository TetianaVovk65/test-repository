def check2rec(num):
    if num == 1:
        res = 'Yes'
        print(res)
        return res
    if num & 1:
        res = 'No'
        print(res)
        return res
    return check2rec(num >> 1)


if __name__ == '__main__':
    num = int(input('Type the number: '))
    check2rec(num)