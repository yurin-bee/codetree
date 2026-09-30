user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Please write your code here.
class id:
    def __init__(self, id="codetree", level=10):
        self.i = id
        self.l = level
user1 = id()
user2 = id(user2_id, user2_level)
print(f"""user {user1.i} lv {user1.l}""")
print(f"""user {user2.i} lv {user2.l}""")