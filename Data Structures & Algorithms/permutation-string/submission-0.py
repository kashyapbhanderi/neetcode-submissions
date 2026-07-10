class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target, window = [0] * 26, [0] * 26
        for c in s1: target[ord(c) - 97] += 1
        
        for i, c in enumerate(s2):
            window[ord(c) - 97] += 1
            
            # Once the window size exceeds s1, remove the oldest character
            if i >= len(s1): 
                window[ord(s2[i - len(s1)]) - 97] -= 1
                
            if target == window: 
                return True
                
        return False