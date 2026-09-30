n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()
sum_value = nums[n-1] + nums[n]
print(sum_value)