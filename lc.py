# 217. Contains Duplicate
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # if array is distinct - size of array after dedup will be same
        if len(nums) == len(set(nums)):
            return False
        return True


# Valid Anagram
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashmap = {}
        for i in range(len(s)):
            hashmap[s[i]] = 1 + hashmap.get(s[i], 0)
        for j in range(len(t)):
            if t[j] in hashmap:
                hashmap[t[j]] -= 1
            else:
                return False
        for value in hashmap.values():
            if value != 0:
                return False
        return True


# Two Sum
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Create an empty dictionary to store the numbers and their indices
        hashmap = {}

        # Loop through the list of numbers
        for i, num in enumerate(nums):
            # Calculate the complement of the current number with respect to the target
            complement = target - num

            # If the complement is found in the hashmap, it means we have found two numbers
            # whose sum is equal to the target, so we return their indices
            if complement in hashmap:
                return [hashmap[complement], i]

            # If the complement is not found, we add the current number and its index to the hashmap
            hashmap[num] = i

        # If no pair of numbers sum up to the target, we return None
        return None
