


def binary(n):

    string = ''
    while n >0:
        string += str(n%2)
        n = n//2
    return string.count('1') == 1

print(binary(3))