secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.
class spy:
    def __init__(self, s, m, t):
        self.s = s
        self.m = m
        self.t = t

meow = spy(secret_code,meeting_point, time)
print(f"""secret code : {meow.s}
meeting point : {meow.m}
time : {meow.t}""")