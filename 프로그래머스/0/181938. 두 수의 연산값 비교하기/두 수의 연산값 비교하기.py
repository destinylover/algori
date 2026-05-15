def solution(a, b):
    answer = 0
    ab = str(a) + str(b)
    c = 2 * a * b
    
    if int(ab) == c:
        answer = int(ab)
    elif int(ab) > c:
        answer = int(ab)
    else:
        answer = c
    
    return answer