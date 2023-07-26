class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxP = nums[0]
        currSum = 0
        for x in nums:
            if currSum < 0:
                currSum = 0
            currSum += x
            maxP = max(currSum, maxP)

        return maxP
    

'''
Problem link - https://leetcode.com/problems/maximum-subarray

Explanation - In this problem we have to find the sum of the subarray having maximum sum

1. iterate through the array and calculate the prefix sums, if sums is < 0, reset currSum to 0, because any prefix sums < 0, is of no value to us.
2. if the currSums > maXP, we update the maximum sum.
'''