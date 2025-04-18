students = set(range(1,31))
apply = set()

for _ in range(28):
    apply.add(int(input()))
missing = students - apply

for num in sorted(missing):
    print(num)