class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = set()
        
        for i in range(len(nums) - 2):
            if nums[i] > 0: break  # Early exit hack
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    res.add((nums[i], nums[l], nums[r]))
                    l, r = l + 1, r - 1
                else:
                    # Compressed pointer logic
                    l, r = (l + 1, r) if total < 0 else (l, r - 1)
                    
        return [list(t) for t in res]