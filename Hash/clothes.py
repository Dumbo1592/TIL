class HashTable:
    def __init__(self, capacity):
        self.capacity = max(1, capacity)
        self.bucket = {}

    def put(self, key, value):
        if key not in self.bucket:
            self.bucket[key] = []
        self.bucket[key].append(value)

    def cal(self):
        answer = 1
        for key in self.bucket.keys():
            answer = answer * (len(self.bucket[key]) + 1)
        return answer - 1

def solution(clothes):
    table = HashTable(len(clothes))
    for c in clothes:
        table.put(c[1], c[0])
    return table.cal()

print(solution([["item_a", "eyewear"], ["item_b", "top"]]))

#case 1) 1가지만 입었을 때
# self.size
#case 2) 2가지만 입었을 때
# bucket 
#case 3) 3가지만 입었을 때
