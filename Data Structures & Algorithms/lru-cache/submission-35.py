class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keys = {}
        self.cache = []


    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1
        else:
            self.cache.remove(key)
            self.cache.append(key)
            return self.keys[key]

    def put(self, key: int, value: int) -> None:
        self.keys[key] = value
        if key not in self.cache:
            self.cache.append(key)
            if len(self.cache)>self.capacity:
                lkey = self.cache.pop(0)
                self.keys.pop(lkey)
        else:
            self.keys[key] = value
            self.cache.remove(key)
            self.cache.append(key)
