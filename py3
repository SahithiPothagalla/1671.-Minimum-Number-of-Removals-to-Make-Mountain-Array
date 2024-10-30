class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        lis = [1]*len(nums) # Longest Increasing Subsequence from right
        lds = [1]*len(nums) # Longest Decreasing Subsequence from left
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i]>nums[j]:
                    lds[i] = max(lds[i],1+lds[j])
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    lis[i] = max(lis[i],1+lis[j])
        max_mountain_length = 0 # length of maximum mountain length
        for i in range(1, len(nums) - 1):
            if lis[i] >1 and lds[i] >1 :  # min length of mountain >= 3
                max_mountain_length = max(max_mountain_length, lis[i] + lds[i] - 1)
        return len(nums) - max_mountain_length 
