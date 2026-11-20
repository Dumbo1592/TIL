class HashTable:
    def __init__(self, capacity):
        # capacity는 버킷의 개수, size는 전체 버킷에 저장된 key-value 항목의 총개수
        self.capacity = max(1, capacity)
        self.buckets = [[] for _ in range(self.capacity)]

    def _index(self, key):
        return hash(key) % self.capacity

    def put(self, key, value):
        bucket = self.buckets[self._index(key)] # 해쉬 함수로 인덱스 위치를 찾아 버켓에 저장
        bucket.append((key, value))

    def get(self):
        for bucket in self.buckets:
            for _, value in bucket:
                return value
        
    def remove(self, key):
        bucket = self.buckets[self._index(key)]
        for i, (stored_key, value) in enumerate(bucket):
            if stored_key == key:
                bucket.pop(i)
                return value

    
def solution(participant, completion):
    answer = ""
    table = HashTable(len(participant))

    for name in participant:
        table.put(name, name)

    for name in completion:
        table.remove(name)

    answer = table.get()

    return answer

print(solution(["leo"],[]))