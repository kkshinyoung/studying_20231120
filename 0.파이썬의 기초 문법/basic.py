def input_str():
    s = input("값을 입력하여 주세요:")
    print(f'입력한 문자열: {s}')


def input_str_2():
    a = input("첫 번째 문자열 입력:")
    b = input("두 번째 문자열 입력:")

    print(a + b)

def input_int():
    a = 10
    b = 10
    c = a + b

    print(f'{a} + {b} = {c}')

    e = 3.14
    f = 10
    g = e + f

    print(f'{e} + {f} = {g}')

    h = 10
    i = 10
    j = float(h) + float(i)
    print(f'{float(h)} + {float(i)} = {g}')

def input_error():
    a = 10
    b = '10'
    c = ''

    print(f'{a} + {b} = {c}')

def input_fix_error():
    c = 10
    d = '10'

    print(c + int(d))

def type_show():
    a = True
    b = False
    c = 1
    d = 0

    print(a)
    print(b)
    print(type(a))
    print(type(b))
    print(c)
    print(d)
    print(type(c))
    print(type(d))

if __name__ == '__main__':
    type_show()
