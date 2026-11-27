def solution(arr1, arr2):
    answer = []
    data = []
    for i in range(len(arr2[0])):
        row = []
        for j in range(len(arr2)):
            row.append(arr2[j][i])
        data.append(row)

    for i in arr1: # [2, 3, 2]
        row = []
        for j in data: # [5, 2, 3]
            row.append(sum(a*b for a,b in zip(i,j)))
        answer.append(row)
    
    return answer

print(solution(
    [[1, 2]],
    [[1, 2, 3],
     [4, 5, 6]]
))
""" 
1 4 3 3 3 [1*3 + 4*3, 1*3 + 4*3], [3*3 + 2*3, 3*3 + 2*3], [4*3 + 1*3, 4*3 + 1*3]
3 2 3 3 
4 1 3 3 
"""

"""
[2, 3, 2], [5, 4, 3] [2*5 + 3*2 + 2*3, 2*4 + 3*4 + 2*1, 2*3 + 3*1 + 2*1]
[4, 2, 4], [2, 4, 1]
[3, 1, 4], [3, 1, 1]
"""