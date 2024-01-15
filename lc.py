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


# group anagrams
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # Create a dictionary to store the groups
        groups = {}

        # Loop through each string in the input list
        for s in strs:
            # Sort the string and use it as a key
            key = "".join(sorted(s))

            # If the key is in the dictionary, append the string to that list
            if key in groups:
                groups[key].append(s)
            # If the key is not in the dictionary, create a new list with the string
            else:
                groups[key] = [s]

        # Return the grouped anagrams
        return list(groups.values())


# subsequence
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_index = 0
        for char in t:
            if s_index == len(s):
                break
            if char == s[s_index]:
                s_index += 1
        return s_index == len(s)

    # valid palindrome:

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # convert the entire string into lower case
        # loop through the entire string from the back
        # if the ascii value of the letter is between 97-122 and 48-57 add to a temp string
        # compare if the temp string == final_string backwards
        s = s.lower()
        final_string = ""
        for i in range(len(s) - 1, -1, -1):
            if (ord(s[i]) <= 122 and ord(s[i]) >= 97) or (
                ord(s[i]) <= 57 and ord(s[i]) >= 48
            ):
                final_string += s[i]
        return final_string == final_string[::-1]

    # valid parentheses:


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        hashmap = {"(": ")", "{": "}", "[": "]"}

        for char in s:
            if char in hashmap:
                stack.append(char)
            elif len(stack) == 0 or hashmap[stack.pop()] != char:
                return False

        return len(stack) == 0
