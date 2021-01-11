# Python 3.6+ Dictionary maintains insertion order
# O(1) for get O(1) for put
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        result = self.cache[key]
        # Move the key back to the bottom of the key list
        del self.cache[key]
        self.cache[key] = result
        
        return result

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]
            self.cache[key] = value
        else:
            if len(self.cache.keys()) >= self.capacity:
                oldest_key = list(self.cache.keys())[0]
                del self.cache[oldest_key]

            self.cache[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
