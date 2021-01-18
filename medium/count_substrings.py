class Solution:
    # Bottom Up Table - O(s^2) time O(s^2) space
    def countSubstrings(self, s: str) -> int:
        dp = [[0] * len(s) for _ in range(len(s))]
        palindrome_count = 0
        
        for i in range(len(s)):
            row = 0
            col = i
            
            while col < len(s):
                # Substring of length 1
                if row == col:
                    dp[row][col] = 1
                    palindrome_count += 1
                # Substring of length 2
                elif col - row == 1:
                    if s[row] == s[col]:
                        dp[row][col] = 1
                        palindrome_count += 1
                # Substring of length greater than 2
                else:
                    if s[row] == s[col] and dp[row+1][col-1] == 1:
                        dp[row][col] = 1
                        palindrome_count += 1
                
                row += 1
                col += 1
        
        return palindrome_count
                        
"""
Palindrome Definition:

1) Strings of length 1 ARE palindromes
2) Strings of length 2 ARE palindromes IFF both characters are the same
3) Strings of length > 2 ARE palindromes IFF FIRST and LAST characters are the same 
   AND the substring between first and last characters IS a palindrome
   
    0 1 2 3
    a b b a
0 a 1 0 0 1
1 b   1 1 0
2 b     1 0
3 a       1

0, 0
1, 1
2, 2
3, 3

0, 1
1, 2
2, 3

0, 2
1, 3

0, 3
"""
