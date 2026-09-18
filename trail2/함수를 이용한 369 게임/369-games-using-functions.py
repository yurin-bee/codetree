def has_369(n):
    return any(d in str(n) for d in '369')

def is_multiple_of_3(n):
    return n % 3 == 0

def count_369_game(a, b):
    cnt = 0
    for i in range(a, b + 1):
        if has_369(i) or is_multiple_of_3(i):
            cnt += 1
    return cnt


a, b = map(int, input().split())
print(count_369_game(a, b))