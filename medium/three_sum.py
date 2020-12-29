class Solution:
    # O(n^2) time O(n) space credit to 41plusplus for solution
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return []
        
        nums.sort()
        three_sum = []
        
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
                
            if i > 0 and nums[i-1] == nums[i]:
                continue

            seen = {}
            used = set()
            
            for j in range(i+1, len(nums)):
                # We only have to check if num[j] is seen and not worry about it's partner because the array is sorted
                # The smaller or equal of the two's complement will be added into the seen dict first. We don't have to worry
                # about the larger numbers complement because the array is sorted.
                if nums[j] in seen and nums[j] not in used:
                    three_sum.append([nums[i], nums[j], seen[nums[j]]])
                    used.add(nums[j])
                else:
                    seen[-1 * (nums[i] + nums[j])] = nums[j]
                    
        return three_sum
