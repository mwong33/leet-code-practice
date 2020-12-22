class Solution:
    # O(n^2) time O(n) space
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Loop through the digits
        # For each digit:
        # 1) Set that digits max subsequence to be 1 by default initially
        # 2) Check to see if the digit is greater than each digit before it
        # 3) If it is greater, check its max increasing subsequence
        # 4) Add 1 to each subsequence and replace that digits max subsequence if it is greater than the max subsequence it already has
        # 5) Save the max subarray for that digit in an array
        
        max_subarray_array = []
        
        for i in range(len(nums)):
            max_subarray_array.append(1)
            
            for j in range(0, i):
                if nums[j] < nums[i]:
                    potential_max = 1 + max_subarray_array[j]
                    if potential_max > max_subarray_array[i]:
                        max_subarray_array[i] = potential_max
        
        return max(max_subarray_array)
