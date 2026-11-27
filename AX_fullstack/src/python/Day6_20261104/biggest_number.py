from functools import cmp_to_key

def compare(a,b):
    if a + b > b + a:
        return -1
    if a + b < b + a:
        return 1
    return 0

def solution(numbers):
    answer = []
    for n in numbers:
        answer.append(str(n))
    answer.sort(key=cmp_to_key(compare))
    
    return '0' if answer[0] == '0' else "".join(answer)

print(solution([3, 30, 34, 5, 9]))