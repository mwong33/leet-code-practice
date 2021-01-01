class Solution:
    # O(n) time O(1) space
    def plusOne(self, digits: List[int]) -> List[int]:
        return self.plusOneHelper(digits, len(digits) - 1)
        
    def plusOneHelper(self, digits, index): 
        if digits[index] != 9:
            digits[index] += 1
            return digits
        else:
            digits[index] = 0
            if index != 0:
                return self.plusOneHelper(digits, index-1)
            else:
                return [1] + digits
