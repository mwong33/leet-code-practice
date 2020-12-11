class Solution:
    # O(n) space O(n) where n is the larger list between nums1 and nums2 
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set = set()
        nums2_set = set()
        
        for num in nums1:
            if num not in nums1_set:
                nums1_set.add(num)
        
        for num in nums2:
            if num not in nums2_set:
                nums2_set.add(num)
                
        intersection_list = []
        
        for num in nums1_set:
            if num in nums2_set:
                intersection_list.append(num)
                
        return intersection_list
