from itertools import permutations
from math import isqrt

def is_prime(n):
    if n<2: return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return False
    return True

def solution(numbers):
    answer = []
    for size in range(1, len(numbers) + 1):
        for i in permutations(numbers, size):
            makes = ""
            for n in i:
                makes += n
            if is_prime(int(makes)):
                answer.append(int(makes))
    
    answer = set(answer)

    return len(answer)

solution("011")