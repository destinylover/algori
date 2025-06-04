n = int(input())

for _ in range(n):
    quiz = input()
    score = 0
    streak = 0  

    for char in quiz:
        if char == 'O':
            streak += 1
            score += streak
        else:
            streak = 0

    print(score)
