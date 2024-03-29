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


# Remove element
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # loop through the nums and remove the val
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.remove(nums[i])
            else:
                i += 1
        return len(nums)


# Best Time to Buy and Sell Stock
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # loop through the array and find the least price
        # loop through the array with index after the least price index and find the highest number
        # return the difference between the largest and the smallest number
        l, r = 0, 1
        maxP = 0
        while r < len(prices):
            # profitable?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            # notProfitable?
            else:
                l = r
            r += 1
        return maxP


# reserve ll
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


# TOP K Elements
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # loop through the nums and store it in a hash map with value as number of times it occured in an array
        # {
        # 1 : 3
        # 2 : 2
        # 3 : 1
        # }
        # return the the topk highest value key
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]] += 1
            else:
                hashmap[nums[i]] = 1

        # Now we need to sort the hashmap based on values and return the top k keys
        return sorted(hashmap, key=hashmap.get, reverse=True)[:k]
