

A = input()   # 입력 문자열 (전역 변수)
B = input()   # 목적 문자열 (전역 변수)

def is_match(start):
    # A의 start번째부터 len(B)만큼 잘라낸 게 B와 같은지 True/False로 리턴
    return A[start:start+len(B)] == B

def find_index():
    for start in range(len(A) - len(B) + 1):
        if is_match(start):
            return start   # 처음으로 맞는 위치를 찾으면 바로 리턴
    return -1               # 못 찾으면 -1 (문제에 따라 다르게 처리할 수도 있음)

print(find_index())