class Solution:
    # O(n + mlogm) time, O(n) space
    # n - length of releaseTimes
    # m - the number of keys with maximum time duration
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        key_duration_dict = {}
        
        # Initialize the first key
        key_duration_dict[keysPressed[0]] = releaseTimes[0]
        
        # Loop through each key starting from the second one
        for index in range(1, len(keysPressed)):
            key = keysPressed[index]
            
            if key not in key_duration_dict or releaseTimes[index] - releaseTimes[index-1] > key_duration_dict[key]:
                key_duration_dict[key] = releaseTimes[index] - releaseTimes[index-1]
            
        # Find the max duration
        max_duration = max(key_duration_dict.values())
        
        output_list = []
        
        for key, duration in key_duration_dict.items():
            if duration == max_duration:
                output_list.append(key)
                
        output_list.sort()
        
        return output_list[len(output_list)-1]
