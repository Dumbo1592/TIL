
def solution(prices):
    cnt, answer, result = 1, [], [0]

    for i in range(len(prices)//2):
        prices[i], prices[-i-1] = prices[-i-1], prices[i]

    for i in range(0, len(prices)):
        if i <1: answer.append([prices[i],i])
        else:
            if prices[i-1] >= prices[i]:
                while answer:
                    if answer[-1][0] >= prices[i]:
                        cnt += answer[-1][1]
                        answer.pop()
                    else: break
                answer.append([prices[i],cnt])
                result.append(cnt)
                cnt = 1  
            else: 
                answer.append([prices[i],1]) 
                result.append(1)

    return list(reversed(result))

# 브루트 포스 쓰레기 코드
# def solution(prices):
#     answer = [0, 1]

#     for i in range(len(prices)//2):
#         prices[i], prices[-i-1] = prices[-i-1], prices[i]

#     for i, price in enumerate(prices[2:], start=1):
#         if price <= prices[i]: # 가격이 떨어졌을 때
#             cnt = 1
#             for j in range(i-1,-1, -1): #몇 번째로 떨어졌는지 탐색
#                 if prices[j] < prices[i+1]: 
#                     answer.append(cnt+1)
#                     break
#                 else: cnt += 1
#             if j == 0: answer.append(cnt)
#         else: answer.append(1) # 가격이 올랐을 때

#     for i in range(len(answer)//2):
#         answer[i], answer[-i-1] = answer[-i-1], answer[i]

#     # print(prices)

#     return answer

print(solution([1, 2, 3, 5, 2, 1, 3]))
#                  4           1
''''
init: [1, 2, 3, 5, 2, 1, 3]
                      1  0
                1  1  1
             2     1  1
          4           1

prices: [3, 1, 2, 5, 3, 2, 1]
        [1, 2, 3, 2, 3]
answer: [0, 1, 1, 1, 2, 4, 6]

step 1) 가격이 올랐을 때
    그냥 1초

step 2) 가격이 떨어졌을 때
    앞 배열의 크기에서 현 인덱스보다 가격이 더 낮은 것을 찾기
'''