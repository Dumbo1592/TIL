def solution(answers):
    num_1 = [1,2,3,4,5] # len = 5
    num_2 = [2,1,2,3,2,4,2,5] # len = 8
    num_3 = [3,3,1,1,2,2,4,4,5,5] # len = 10
    a, b, c, answer = [0,1], [0,2], [0,3], []
    
    for i, x in enumerate(answers):
        if num_1[i%5] == x:
            a[0] += 1
        if num_2[i%8] == x:
            b[0] += 1            
        if num_3[i%10] == x:
            c[0] += 1
    
    highest = max(x[0] for x in [a, b, c])
    return [x[1] for x in [a, b, c] if x[0] == highest]



print(solution([1,3,2,4,2]))