class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        max_len = 0
        start = 0
        
        for i, char in enumerate(s):
            # If the character is already in our window, instantly jump the start pointer
            if char in seen and seen[char] >= start:
                start = seen[char] + 1
            else:
                # Calculate the current window size
                current_len = i - start + 1
                if current_len > max_len:
                    max_len = current_len
            
            # Update the character's latest index
            seen[char] = i
            
        return max_len
        