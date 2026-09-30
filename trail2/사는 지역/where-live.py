n = int(input())
name = []
address = []
region = []

for _ in range(n):
    name_value, address_value, region_value = input().split()
    name.append(name_value)
    address.append(address_value)
    region.append(region_value)

# Please write your code here.
class People:
    def __init__(self, name, address, region):
        self.n = name
        self.a = address
        self.r = region

arr = [People(name[i], address[i], region[i]) for i in range(n)]
last_person = arr[0]
for person in arr:
    if person.n > last_person.n:
        last_person = person
print(f"""name {last_person.n}
addr {last_person.a}
city {last_person.r}""")