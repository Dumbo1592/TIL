def solution(prices):
    answer = [0, 1]
    for i in range(len(prices)//2):
        prices[i], prices[-i-1] = prices[-i-1], prices[i]

    print(prices)

    for i, price in enumerate(prices[2:], start=2):
        if price < prices[i]:
            cnt = 0
            for j in range(i,-1, -1):
                cnt += 1
                if prices[j] < prices[i+1]: 
                    answer.append(cnt+1)
                    break
                


solution([1, 2, 3, 5, 2, 1, 3])

''''
init: [1, 2, 3, 5, 2, 1, 3]

prices: [3, 1, 2, 5, 3, 2, 1]

answer: [0, 1, 1, 1, 2, 4, 7]
step 1) 가격이 올랐을 때
        그냥 1초
step 2) 가격이 떨어졌을 때
        앞 배열의 크기에서 현 인덱스보다 가격이 더 낮은 것을 찾기
'''