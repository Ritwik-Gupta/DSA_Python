class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashMap = dict()
        for val in nums:
            if val not in hashMap:
                hashMap[val] = True
            else:
                return True
        return False
    

'''
Leetcode link - https://leetcode.com/problems/contains-duplicate/

Explanation - Iterate through the list and add items to hashmaps, while iterating check if value has already been added to the hashmap
'''