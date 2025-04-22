from collections import Counter

N = int(input())
    
nums = list(map(int, input().split()))
count = Counter(nums)


v = int(input())
    
print(count[v])