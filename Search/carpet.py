def solution(brown, yellow):
    r = 1
    while 1:
        if (((brown - r*2) // 2) - 2) * r != yellow:
            r += 1
        else:
            return [(brown - r*2) // 2, r + 2]

print(solution(24,24))

"""
b - r*2
(b - r*2) // 2
if (b - r*2) // 2 < yellow
    r += 1
"""

"""

"""