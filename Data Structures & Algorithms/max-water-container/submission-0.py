class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r, max_water = 0, len(height) - 1, 0
        
        while l < r:
            h_l, h_r = height[l], height[r]
            
            # 1. Calculate area using a ternary operator
            area = (r - l) * (h_l if h_l < h_r else h_r)
            if area > max_water: max_water = area
            
            # 2. Shift pointers in a single line
            l, r = (l + 1, r) if h_l < h_r else (l, r - 1)
                
        return max_water