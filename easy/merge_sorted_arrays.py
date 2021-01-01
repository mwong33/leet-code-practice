class Solution:
    # O(m * nlogn) time and O(1) space
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        
        nums1_index = 0
        nums2_index = 0
        
        while nums1_index < m + n:
            if nums1_index < m:
                if nums2[nums2_index] < nums1[nums1_index]:
                    temp = nums1[nums1_index]
                    nums1[nums1_index] = nums2[nums2_index]
                    nums2[nums2_index] = temp
                    nums2.sort()
                
                nums1_index += 1
            else:
                nums1[nums1_index] = nums2[nums2_index]
                nums1_index += 1
                nums2_index += 1
                
    # O(m) time and O(1) space
    def mergeNoSort(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Start from the end
        m -= 1
        n -= 1
        
        index = len(nums1) - 1
        
        while index >= 0:
            if m >= 0 and n >= 0:
                if nums1[m] >= nums2[n]:
                    nums1[index] = nums1[m]
                    m -= 1
                else:
                    nums1[index] = nums2[n]
                    n -= 1
            elif n >= 0:
                nums1[index] = nums2[n]
                n -= 1
                
            index -= 1
