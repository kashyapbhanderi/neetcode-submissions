class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each number
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
            
        # Step 2: Create "buckets" where the index is the frequency
        # We need len(nums) + 1 to account for 0 frequency up to the max possible frequency
        freq = [[] for _ in range(len(nums) + 1)]
        
        # Place numbers into their respective frequency buckets
        for num, c in count.items():
            freq[c].append(num)
            
        # Step 3: Gather the top k elements by iterating backwards (highest frequency first)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                # Once we have k elements, we can return immediately
                if len(res) == k:
                    return res