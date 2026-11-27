# def solution(arr1, arr2):
#     answer = []
#     for a,b in zip(arr1, arr2):
#         row = []
#         for i in range(len(a)):
#             row.append(a[i] + b[i])
#         answer.append(row)
#     return answer


def solution(A,B):
    answer = [[c+d for c,d in zip(a,b)] for a,b in zip(A,B)]
    return answer

print(solution([[1,2],[2,3]], [[3,4],[5,6]]))
