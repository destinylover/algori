nums = []

for _ in range(9):
    num = int(input())
    nums.append(num)

max_value = max(nums)
max_index = nums.index(max_value) + 1  # index는 0부터 시작하므로 +1

print(max_value)
print(max_index)
