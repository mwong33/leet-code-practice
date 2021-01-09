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
