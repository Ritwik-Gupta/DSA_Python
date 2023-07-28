class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currMin = 1
        currMax = 1
        for n in nums:
            if n == 0:
                currMax = 1
                currMin = 1

            tmp = n * currMax
            currMax = max(tmp, n*currMin, n)
            currMin = min(tmp, n*currMin, n)

            if currMax > res:
                res = currMax

        return res
