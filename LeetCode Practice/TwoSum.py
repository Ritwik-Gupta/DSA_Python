#Leetcode problem link - https://leetcode.com/problems/two-sum/


from ast import List

def twoSum(self, nums: List[int], target: int) -> List[int]:
    myHashmap = dict()
    for i,j in enumerate(nums):
        diff = target - j
        if diff in myHashmap:
            return [myHashmap[diff], i]
        myHashmap[j] = i


'''
Explanation

1. We will use a hashmap to store the value:indices pair as we iterate through the list
2. if we get a value which is equal to (target-current) it the hashmap we will return both the indices
'''