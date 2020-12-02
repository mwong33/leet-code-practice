class Solution:
  # change method to 'twoSum' to work on leetocde

  # brute force O(1) space O(n^2) time
  def twoSumBrute(self, nums: List[int], target: int) -> List[int]:        
    for i in range(len(nums)):
      first_num = nums[i]
      target_num = target - first_num
      
      for j in range(i+1, len(nums)):
        if nums[j] == target_num:
          return [i, j]

  # hash table solution O(n) space O(n) time
  def twoSumHash(self, nums: List[int], target: int) -> List[int]:
    two_sum_dict = {}

    for i in range(len(nums)):
      difference = target - nums[i]

      if difference in two_sum_dict.keys():
        return [i, two_sum_dict[difference]]
      else:
        two_sum_dict[nums[i]] = i
