meow = input()

def finder(string):
    cnt = 0
    for i in range(len(meow) - len(string) + 1):
        same = True
        for j in range(len(string)):
            if meow[i + j] != string[j]:
                same = False
                break
        if same:
            cnt += 1
    return cnt

print(finder('ee'), finder('eb'))