class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        d = {}
        n = len(nums)
        for x in range(n):
            if target - nums[x] in d.keys():
                return d[target-nums[x]], x
            else:
                d[nums[x]] = x
