import heapq
from itertools import count

def Min_Heap():
    heap = [7, 3, 5, 1, 2]
    heapq.heapify(heap)             # 원본 리스트를 최소 힙으로 변환
    heapq.heappush(heap, 0)         # 원소 추가

    if heap:                       # 빈 힙이면 접근·꺼내기에서 IndexError 발생
        print(heap[0])             # 0: 확인만 하고 제거하지 않음
        print(heapq.heappop(heap))  # 0: 최솟값을 제거하고 반환

    while heap:
        print(heapq.heappop(heap))  # 1, 2, 3, 5, 7

def Max_Heap_A():
    heap = []
    for number in [5, 1, 9, 3]:
        heapq.heappush(heap, -number)

    while heap:
        print(-heapq.heappop(heap))  # 9, 5, 3, 1

def Max_Heap_B():
    heap = [5, 1, 9, 3]
    heapq.heapify_max(heap)
    heapq.heappush_max(heap, 7)
    print(heap[0])                  # 9
    print(heapq.heappop_max(heap))  # 9

def Priority_Queue():
    heap = []
    sequence = count()  # next()를 호출할 때마다 0, 1, 2, ... 반환
    heapq.heappush(heap, (2, next(sequence), {"name": "작업 A"}))
    heapq.heappush(heap, (1, next(sequence), {"name": "작업 B"}))
    heapq.heappush(heap, (2, next(sequence), {"name": "작업 C"}))

    while heap:
        priority, order, task = heapq.heappop(heap)
        print(task["name"])  # 작업 B → 작업 A → 작업 C

def Top_K_Heap():
    k = 3  # 양의 정수
    heap = []
    for number in [5, 1, 9, 3, 7, 2]:
        if len(heap) < k:
            heapq.heappush(heap, number)
        else:
            heapq.heappushpop(heap, number)

"""
heappushpop(): 새 값을 넣고 최솟값을 꺼내는 효과. 빈 힙에서도 사용 가능.
heapreplace(): 기존 최솟값을 먼저 꺼내고 새 값을 넣음. 빈 힙에서는 오류.
두 함수는 결과가 다를 수 있으므로 무조건 서로 바꾸면 안 된다.

이미 가진 데이터에서 한 번만 K개를 고르려면 다음 함수도 사용 가능하다.
heapq.nlargest(k, data)   # 큰 값 K개를 내림차순 리스트로 반환
heapq.nsmallest(k, data)  # 작은 값 K개를 오름차순 리스트로 반환
"""