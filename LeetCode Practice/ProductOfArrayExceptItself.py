class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        finalList = []
        #First pass to get the prefixes
        prev = 1
        for i in range(len(nums)):
            finalList.append(prev)
            prev = nums[i]*finalList[-1]

        #Second pass to get the postfixes
        prev = 1
        for i in range(len(nums)-1, -1, -1):
            finalList[i] = finalList[i] * prev
            prev = prev * nums[i]

        return finalList
    

'''
Leetcode link - https://leetcode.com/problems/product-of-array-except-self

Explanation: We need to return the array with each index having product of all the other index values except itself

1. Iterate through the array 2 times
2. In first iteration(left -> right), append product of previous indexes in a new list
3. In second iteratoin(right -> left), update(multiply) the new list with the product of the previous indexes
'''