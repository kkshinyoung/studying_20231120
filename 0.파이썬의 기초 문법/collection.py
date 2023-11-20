def list_index():
    ls = [1, 2, 3, 4, 5]
    print(ls)
    print(f'리스트 {ls} 중 인덱스 0 : {ls[0]}')
    print(f'리스트 {ls} 중 인덱스 1 : {ls[1]}')

def list_slice():
    ls = [1, 2, 3, 4, 5]
    print(f'리스트 {ls} 중 인덱스 2미만 : {ls[:2]}')
    print(f'리스트 {ls} 중 인덱스 2이상 : {ls[2:]}')

def list_append():
    ls = []
    ls.append(1)
    ls.append(2)
    ls.append(3)
    print(f'추가한 결과 리스트 : {ls}')

def list_show():
    ls = [1, 3.14, "hello", [1, 2, 3]]
    print(f'리스트 {ls} 중에서 인덱스 1이상 3미만 : {ls[1:3]}')

def list_index_replace():
    ls = [1, 2, 3, 4, 5]
    print(ls)

    ls[0] = 5
    print(f'리스트 {ls} 중에서 인덱스 0 값을 5로 변경 : {ls}')

def tuple_show():
    tp = (1, 2, 3, 4, 5)
    print(f'튜플 전체 출력 : {tp}')
def tuple_error():
    tp = (1, 2, 3, 4, 5)
    tp[0] = 5
    print(f'튜플 {tp} 중에서 인덱스 0 값을 5로 변경 : {tp}')

def dictionary_key_value():
    dc = {'a': 1, 'b': 2, 'c': '3'}
    print(f'딕셔너리 요소 출력 : {dc}')
    print(f"딕셔너리 a 키값 출력 : {dc['a']}")
    print(f"딕셔너리 b 키값 출력 : {dc['b']}")
    print(f"딕셔너리 c 키값 출력 : {dc['c']}")

def dictionary_has_list():
    dc = {1: 'a', 'b': [1, 2, 3], 'c': 3}
    print(f'딕셔너리 요소 출력 : {dc}')
    print(f"딕셔너리 a 키값 출력 : {dc[1]}")
    print(f"딕셔너리 b 키값 출력 : {dc['b']}")
    print(f"딕셔너리 c 키값 출력 : {dc['c']}")

def dictionary_add_value():
    dc = {1: 'a', 'b': [1, 2, 3], 'c': 3}
    dc['d'] = 4
    print(f'딕셔너리 요소 추가 결과 출력 : {dc}')

def set_print():
    st = set([1, 2, 3, 4])
    print(f'셋 요소 출력 : {st}')

def set_distinct():
    st = set([1, 1, 2, 2, 3, 3, 4, 5, 6])
    print(f'중복제거된 셋 요소 출력 : {st}')

def set_split():
    st = set("python40s")
    print(st)



if __name__ == '__main__':
    set_split()