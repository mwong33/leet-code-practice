class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_dict = {}
        phone_dict["2"] = ["a","b","c"]
        phone_dict["3"] = ["d","e","f"]
        phone_dict["4"] = ["g", "h", "i"]
        phone_dict["5"] = ["j", "k", "l"]
        phone_dict["6"] = ["m", "n", "o"]
        phone_dict["7"] = ["p", "q", "r", "s"]
        phone_dict["8"] = ["t", "u", "v"]
        phone_dict["9"] = ["w", "x", "y", "z"]
        
        # Start with the last digit of digits
        # Display each digit
        # Go to the penultimate digit
        # Combine the output of the last digit with each digit with the penultimate digit
        # Rinse and repeat
        
        index = len(digits) - 1
        master_array = []
        
        while index >= 0:
            reference_array = phone_dict[digits[index]]
            new_array = []
            
            for i in range(len(reference_array)):
                if len(master_array) > 0:
                    for j in range(len(master_array)):
                        new_array.append(reference_array[i] + master_array[j])
                else:
                    new_array = reference_array
                    break
            
            master_array = new_array
                
            index -= 1
            
        return master_array
