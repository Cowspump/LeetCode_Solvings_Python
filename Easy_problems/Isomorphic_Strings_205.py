class Solution:
    def findclosestnumber(self, nums: list[int]) -> int:
        cnd = nums[0]

        for i in range(0, len(nums)):

            if abs(cnd) > abs(nums[i]):
                cnd = nums[i]

        if cnd < 0 and (cnd * -1) in nums:
            return cnd * -1
        else:
            return cnd

s = Solution()
print(s.findclosestnumber([2077, -2077, 1]))