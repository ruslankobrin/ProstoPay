class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.map = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self._hash(key)
        if self.map[index] is None:
            self.map[index] = [(key, value)]
        else:
            for i, (k, v) in enumerate(self.map[index]):
                if k == key:
                    self.map[index][i] = (key, value)
                    return
            self.map[index].append((key, value))

    def get(self, key):
        index = self._hash(key)
        if self.map[index] is None:
            return None
        for k, v in self.map[index]:
            if k == key:
                return v
        return None
