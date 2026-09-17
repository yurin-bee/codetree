input_str = input()
target_str = input()

# Please write your code here.
inp = len(input_str)
t = len(target_str)

for i in range(inp-t+1):
    if input_str[i:i+t] == target_str:
        print(i)
        break
else:
    print(-1)