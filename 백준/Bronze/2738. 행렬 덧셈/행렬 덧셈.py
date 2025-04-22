N, M = map(int, input().split())

A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

B = []
for _ in range(N):
    B.append(list(map(int, input().split())))

for i in range(N):
    row_sum = [a + b for a, b in zip(A[i], B[i])]
    print(*row_sum)
