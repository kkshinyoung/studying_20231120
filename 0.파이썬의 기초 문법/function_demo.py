def func():
    print("안녕하세요")
    print("파이썬과 40개의 작품들 입니다.")

def func_loop():
    for i in range(3):
        func()

def func_add(a,b):
    return a + b

def func_mux(a,b):
    mux = a * b
    return mux

def func_add_mux(a,b):
    add = a + b
    mux = a * b
    return add,mux

if __name__ == '__main__':
    print('1- 함수 기본')
    func()
    print('2- 함수 반복')
    func_loop()
    print('3- 함수 덧셈 리턴')
    c = func_add(1,2)
    print(c)
    print('4- 함수 곱셈 리턴')
    c = func_mux(2,3)
    print(c)
    print('5- 함수 덧셈,곱셈 동시 리턴')
    a, b = func_add_mux(1, 3)
    print(a, b)
    print('6- 함수 덧셈,곱셈 단일 리턴')
    _,b = func_add_mux(1,3)
    print(b)





