A = input()

def has_two_or_more(A):
    first = A[0]              # 기준이 될 첫 글자
    for ch in A:
        if ch != first:       # 기준과 다른 글자를 하나라도 발견하면
            return True        # 즉시 True — 서로 다른 알파벳이 2개 이상 있다는 뜻
    return False               # 끝까지 다 같았으면 False

if has_two_or_more(A):
    print("Yes")
else:
    print("No")