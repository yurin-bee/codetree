unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

# Please write your code here.
class wires:
    def __init__(self, u, w, s):
        self.u = u
        self.w = w
        self.s = s

meow = wires(unlock_code, wire_color, seconds)
print(f"""code : {unlock_code}
color : {wire_color}
second : {seconds}""")