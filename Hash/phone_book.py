def solution(phone_book):
    numbers = set(phone_book)
    for n in numbers:
        for i in range(len(n)):
            if n[:i] in numbers: return False
    return True

print(solution(["12","123","1235","567","88"]))

