# O(n) time for sumRange, O(1) time to create the object, O(n) space
class NumArrayNaive:

    def __init__(self, nums: List[int]):
        self.array = nums

    def sumRange(self, i: int, j: int) -> int:
        total = 0
        for index in range(i,j+1):
            total += self.array[index]
        
        return total


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

# O(1) time for sumRange, O(n) time to create the object, O(n) space
class NumArray:

    def __init__(self, nums: List[int]):
        self.array = nums
        self.cache = [None] * len(nums)
        previous_sum = 0
        for i in range(len(nums)):
            previous_sum += nums[i]
            self.cache[i] = previous_sum
        
    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.cache[j]
        
        return self.cache[j] - self.cache[i-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

"""
Example:

nums: [1,2,3,4]
cache: [1,3,6,10]

"""
