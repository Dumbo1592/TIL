def solution(strings, n):

    for i in range(len(strings)-1):
        min = i
        for j in range(i+1, len(strings)):
            if strings[min][n] > strings[j][n]: min = j
            elif strings[min][n] == strings[j][n]: 
                if strings[min] > strings[j]: min = j        
        strings[min], strings[i] = strings[i], strings[min]
        
    return strings

print(solution(["abce", "abcd", "cdx"], 2))

# def solution(strings, n):
#   return sorted(strings, key=lambda x: (x[n], x))     