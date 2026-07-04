class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = [0] * 26
        max_freq = 0
        left = 0
        
        for right in range(len(s)):
            # Convert uppercase letter to an index 0-25
            idx = ord(s[right]) - 65
            counts[idx] += 1
            
            # Update the highest frequency of a single character in our window
            if counts[idx] > max_freq:
                max_freq = counts[idx]
            
            # If the number of characters we need to replace exceeds k, 
            # shift the entire window one step to the right.
            if (right - left + 1) - max_freq > k:
                counts[ord(s[left]) - 65] -= 1
                left += 1
                
        # The window never shrunk, it only grew when valid and shifted when invalid.
        # Therefore, the final window size is our maximum length.
        return len(s) - left