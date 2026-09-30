n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()
ref = 0
for i in range(n):
    sum_val = nums[i] + nums[2*n-i-1]
    if sum_val > ref:
        ref = sum_val
print(ref)