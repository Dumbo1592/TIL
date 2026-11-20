class HashTable:
    def __init__(self, capacity=8):
        self.capacity = max(1, capacity)
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]

    def _index(self, key):
        return hash(key) % self.capacity

    def put(self, key, value):
        """key가 있으면 갱신, 없으면 삽입."""
        bucket = self.buckets[self._index(key)]

        for i, (stored_key, _) in enumerate(bucket):
            if stored_key == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self.size += 1

        if self.size / self.capacity > 0.75:
            self._resize()

    def get(self, key, default=None):
        """key에 해당하는 값을 조회."""
        bucket = self.buckets[self._index(key)]

        for stored_key, value in bucket:
            if stored_key == key:
                return value

        return default

    def remove(self, key):
        """key를 삭제하고 값을 반환."""
        bucket = self.buckets[self._index(key)]

        for i, (stored_key, value) in enumerate(bucket):
            if stored_key == key:
                bucket.pop(i)
                self.size -= 1
                return value

        raise KeyError(key)

    def _resize(self):
        """테이블을 두 배로 확장하고 항목을 재배치."""
        old_buckets = self.buckets

        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]

        for bucket in old_buckets:
            for key, value in bucket:
                index = self._index(key)
                self.buckets[index].append((key, value))

    def __len__(self):
        return self.size