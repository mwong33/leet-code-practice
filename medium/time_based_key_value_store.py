# O(key*value) space O(1) time to set O(log(number of values for key)) time for get
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [(value, timestamp)]
        else:
            self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        key_array = self.store[key]
                
        start = 0
        end = len(key_array) - 1
        
        while start <= end:
            mid = (start + end)//2
            if key_array[mid][1] == timestamp:
                return key_array[mid][0]
            
            if key_array[mid][1] < timestamp:
                start = mid + 1
            elif key_array[mid][1] > timestamp:
                end = mid - 1
                
        mid = (start + end)//2
        
        if key_array[mid][1] < timestamp:
            return key_array[mid][0]
        else:
            return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

"""

{

    "key": [(value, time), (value, time)]

}

"""
