def calc():
    print("더하기:", 10 + 20)
    print("빼기:", 10 - 20)
    print("곱하기:", 10 * 20)
    print("나누기:", 10 / 20)

def square():
    print("c**2:", 10 ** 2)
    print("c**3:", 10 ** 3)
    print("c**4:", 10 ** 4)

def divide():
    print("몫:", 40 // 6)
    print("나머지:", 40 % 6)

def bool_check():
    print(10 == 10)
    print(10 >= 10)
    print(10 <= 10)
    print(10 < 5)
    print(10 > 5)
    print(10 != 10)

def ls_bool_check():
    ls = ['a', 2, 'hello', 3]

    print('a' in ls)
    print(1 in ls)
    print('hello' in ls)
    print(3 in ls)

def str_bool_check():
    str = "hello python"

    print("python" in str)
    print("py" in str)
    print("40" in str)

def if_example():
    a = 1
    b = 1

    if a == b:
        print("두개의 값은 같습니다.")

    if a != b:
        print("두개의 값은 같지 않습니다.")

def else_example():
    a = 1
    b = 2

    if a == b:
        print("두개의 값은 같습니다.")
    else:
        print("두개의 값은 같지 않습니다.")

def inequality(): # 부등호
    a = 1
    b = 2

    if a > b:
        print("a 값이 더 큽니다.")
    elif a < b:
        print("b 값이 더 큽니다.")
    else:
        print("두개의 값은 같습니다.")
        
def inequality2():
    a = 1
    b = 1

    if a >= b:
        print("a 값이 더 크거나 같습니다.")

    if a <= b:
        print("a 값이 더 작거나 같습니다.")
        
def inequality3():
    a = 1
    b = 1
    c = 2
    d = 2

    if a == b and c == d:
        print("두 조건 모두 만족")

    if a == b or c == d:
        print("두 조건 중 하나라도 만족하면")
        
def inequality4():
    str = "hello python"

    if str == "hello python":
        print("hello python 문자열이 같습니다.")

    if str == "hi python":
        print("hi python 문자열이 같습니다.")

    if "hello" in str:
        print("hello 가 포함되어 있습니다.")

    if "hello" not in str:
        print("hello 가 포함되어 있지 않습니다.")

    if "hi" not in str:
        print("hi 가 포함되어 있지 않습니다.")
        
def list_has_string():
    ls = ["안녕", 1, 2, "파이썬"]

    if "안녕" in ls:
        print("ls에 안녕 이 포함되어 있습니다.")

    if 2 in ls:
        print("ls에 숫자 2 가 포함되어 있습니다.")
        
def list_has_no_string():
    ls = ["안녕", 1, 2, "파이썬"]

    if "안녕" not in ls:
        print("ls에 안녕 이 포함되어 있지 않습니다.")

    if 5 not in ls:
        print("ls에 숫자 5는 없습니다.")





if __name__ == '__main__':
    str_bool_check()