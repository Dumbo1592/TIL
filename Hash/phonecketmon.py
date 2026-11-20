class HashTable:
    def __init__(self, capacity):
        self.capacity = max(1, capacity)
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]

    def _index(self, key):
        return hash(key) % self.capacity
    
    def put(self, key, value):
        bucket = self.buckets[self._index(key)]
        for i, (stored_key, value) in enumerate(bucket):
            if stored_key == key:
                bucket[i] = ((key, value))
                return 
        bucket.append((key, value))
        self.size += 1

    def get(self):
        return min(self.size, self.capacity//2)

def solution(nums):
    table = HashTable(len(nums))
    for n in nums:
        table.put(n, n)
    return table.get()

print(solution([3,3,3,2,2,2]))