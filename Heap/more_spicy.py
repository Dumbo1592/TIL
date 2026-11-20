import heapq

def solution(heap, K):
    heapq.heapify(heap)            
    cnt = 0
    while 1:
        if len(heap) >= 2:
            least_1, least_2 = heapq.heappop(heap), heapq.heappop(heap)
            if least_1 >= K: 
                return cnt
            else: 
                cnt += 1
                heapq.heappush(heap, least_1 + (least_2 * 2))
        else: 
            return (cnt if heap[0] >= K else -1)

solution([1, 2], 5)


# 1개 이하가 되면 팝 하면안 됨
