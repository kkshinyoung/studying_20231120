def range_end():
    for i in range(7):
        print(f'range 에서 end 를 for-loop 한 결과: {i}')


def range_start_end():
    for i in range(5, 10):
        print(f'range 에서 start-end 를 for-loop 한 결과: {i}')
def range_start_end_step():
    for i in range(10, 5, -1):
        print(f'range 에서 start-end-step 을 for-loop 한 결과: {i}')

def str_loop():
    str = "hello python"

    for i in str:
        print(f'string 을 for-loop 한 결과: {i}')

def list_enumerate():
    name_list = ["홍길동", "장다인", "김철수"]
    age_list = [500, 5, 12]

    for i, k in enumerate(name_list):
        print("인덱스=", i, end='  ')
        print("값=", k)

def enumerate_for_csv():
    name_list = ["홍길동", "장다인", "김철수"]
    age_list = [500, 5, 12]
    print('1- enumerate 방식 \n')
    for i, k in enumerate(name_list):
        print(k, end='  ')
        print(age_list[i])
    print('2- enumerate 의 key 는 list 의 인덱스와 같다. \n')
    for i, k in enumerate(name_list):
        print(name_list[i], end='  ')
        print(age_list[i])

    print('3- range 의 index 는 enumerate 의 키와 같다. \n')
    for i in range(len(name_list)):
        print(name_list[i], end='  ')
        print(age_list[i])


def comprehension():
    print('1- 컴프리헨션 적용 전 방식 \n')
    ls = []
    for i in range(10):
        ls.append(i)

    print(ls)

    print('2- 컴프리헨션 적용 방식 \n')

    ls = [i for i in range(10)]

    print(ls)

def comprehension_multiple():
    ls = [i * 5 for i in range(10)]
    print('컴프리헨션 적용한 곱셈 방식 \n')
    print(ls)

def while_demo():
    a = 0
    while a < 5:
        print(a)
        a = a + 1

def while_true():
    a = 0
    while True:
        print(a)
        a = a + 1
        if a >= 5:
            break

if __name__ == '__main__':
    comprehension_multiple()