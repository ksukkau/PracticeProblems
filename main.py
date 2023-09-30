from collections import deque


def running_sum(nums: list[int]) -> list[int]:
    """Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
    Return the running sum of nums.
    Input: nums = [1,2,3,4]
    Output: [1,3,6,10]
    Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
    :param nums: list of int
    :return: list of int
    """
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums


def pivot_index(nums: list[int]) -> int:
    """Given an array of integers nums, calculate the pivot index of this array.
    The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
    If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
    Return the leftmost pivot index. If no such index exists, return -1.
    :param nums: list of int
    :return: int
    """
    s = sum(nums)
    left_sum = 0
    for i, x in enumerate(nums):
        if left_sum == (s - left_sum - x):
            # this is calculating the right sum by minus the pivot index and left sum from total sum
            return i  # returns the index
        left_sum += x
    return -1  # returns -1 if no pivot is found


def is_isomorphic(s: str, t: str) -> bool:
    """
    Given two strings s and t, determine if they are isomorphic.
    Two strings s and t are isomorphic if the characters in s can be replaced to get t.
    All occurrences of a character must be replaced with another character while preserving the order of characters.
    No two characters may map to the same character, but a character may map to itself.
    :param s: a String
    :param t: a String
    :return: Boolean
    """
    mapping_s_t = {}
    mapping_t_s = {}

    for c1, c2 in zip(s, t):

        if (c1 not in mapping_s_t) and (c2 not in mapping_t_s):
            mapping_s_t[c1] = c2
            mapping_t_s[c2] = c1

        elif mapping_s_t.get(c1) != c2 or mapping_t_s.get(c2) != c1:
            return False

    return True


def twoSum(nums: list[int], target: int) -> list[int]:
    """
    Given an array of integers nums and an integer target, return indices of the two numbers
    such that they add up to target.
    You may assume that each input would have exactly one solution,
    and you may not use the same element twice.
    You can return the answer in any order.
    :param nums: List[int]
    :param target: int
    :return: list[int]
    """
    length = len(nums)
    hashMap = {nums[i]: i for i in range(length)}
    for i in range(length):
        if target - nums[i] in hashMap and hashMap[target - nums[i]] != i:
            return i, hashMap[target - nums[i]]


def valid_parentheses(s: str) -> bool:
    """
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
    :param s: List
    :return: boolean
    """
    if len(s) < 2:
        return False
    pair = dict(('()', '[]', '{}'))
    stack = []
    for x in s:
        if x in '([{':
            stack.append(x)
        elif len(stack) == 0 or x != pair[stack.pop()]:
            return False
    return len(stack) == 0


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: [ListNode], list2: [ListNode]) -> [ListNode]:
    cur = dummy = ListNode()
    while list1 and list2:
        if list1.val < list2.val:
            cur.next = list1
            print(cur.next)
            list1, cur = list1.next, list1
            print(list1)
            print(cur)
        else:
            cur.next = list2
            print(cur.next)
            list2, cur = list2.next, list2
            print(list2)
            print(cur)

    if list1 or list2:
        cur.next = list1 if list1 else list2

    return dummy.next


def maxProfit(prices: list[int]) -> int:
    """
    You are given an array prices where prices[i] is the price of a given stock on the ith day.
    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day
    in the future to sell that stock.
    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
    :param prices: list ints
    :return: int
    """
    min_price = float('inf')
    max_profit = 0
    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price

    return max_profit


def isPalindrome(s: str) -> bool:
    """
    A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
    Given a string s, return true if it is a palindrome, or false otherwise.
    :param s: String
    :return: Boolean
    """
    s = ''.join(ch for ch in s if ch.isalnum())
    s = list(s.lower())
    new_s = []
    if s == '':
        return True
    for i in range(len(s)):
        if s[i] == s[-1 - i]:
            new_s.append(s[i])
    return new_s == s


def isAnagram(s: str, t: str) -> bool:
    """
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.
    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
    typically using all the original letters exactly once.
    :param s: String
    :param t: String
    :return: Boolean
    """
    s = s.lower().replace(" ", "")
    t = t.lower().replace(" ", "")

    letter_count_s = {}
    letter_count_t = {}
    for x in s:
        if x not in letter_count_s:
            letter_count_s[x] = 1
        else:
            letter_count_s[x] += 1
    for x in t:
        if x not in letter_count_t:
            letter_count_t[x] = 1
        else:
            letter_count_t[x] += 1

    return letter_count_t == letter_count_s


def floodFill(image: list[list[int]], sr: int, sc: int, newColor: int):
    R, C = len(image), len(image[0])
    color = image[sr][sc]
    if color == newColor:
        return image

    def dfs(r, c):
        if image[r][c] == color:
            image[r][c] = newColor
            if r >= 1:
                dfs(r - 1, c)
            if r + 1 < R:
                dfs(r + 1, c)
            if c >= 1:
                dfs(r, c - 1)
            if c + 1 < C:
                dfs(r, c + 1)

    dfs(sr, sc)
    return image


def findTheDifference(s: str, t: str) -> str:
    """
    You are given two strings s and t.
    String t is generated by random shuffling string s and then add one more letter at a random position.
    Return the letter that was added to t.
    :param s: string 1
    :param t: string 2
    :return: string
    """
    s_list = list(s)
    t_list = list(t)
    length = len(t_list)
    t_list.sort()
    s_list.sort()
    for i in range(0, length):
        if i <= len(s_list)-1:
            if not s_list[i] == t_list[i]:
                return t_list[i]
        else:
            return t_list[i]

def minPartitions(n: str) -> int:
    """
    A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros.
    For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.

    Given a string n that represents a positive decimal integer, return the minimum number of positive deci-binary
    numbers needed so that they sum up to n.
    theres 2 options here the one used uses memory but is slower

    this option is faster but uses more memory but is faster

            return int(max(n))

    this works because the largest # needs the max number of 1s in its place
    example
    82934
    11111
    11111
    10111
    10101
    10100
    10100
    10100
    10100
    00100

    """
    max_digit = '0'
    for digit in n:
        if digit > max_digit:
            max_digit = digit
    return int(max_digit)

def decodeAtIndex(s, k):
    """
    :type s: str
    :type k: int
    :rtype: str
    """
    total_length = 0

    # Calculate the total length of the decoded string
    for char in s:
        if char.isnumeric():
            total_length *= int(char)
        else:
            total_length += 1

    # Traverse the string in reverse to find the character at position k
    for char in reversed(s):
        k %= total_length  # Reduce k based on the total length

        if k == 0 and char.isalpha():
            return char

        if char.isnumeric():
            total_length /= int(char)
        else:
            total_length -= 1

def mergeAlternately(word1, word2):
    """
    You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
    Return the merged string.

    :type word1: str
    :type word2: str
    :rtype: str
    """
    new_word = ''

    if len(word1) > len(word2):
        length = len(word1)
    else:
        length = len(word2)

    for i in range(length):
        if len(word1) - 1 >= i:
            new_word += word1[i]
        if len(word2) - 1 >= i:
            new_word += word2[i]
    return new_word

def isMonotonic(nums: list[int]) -> bool:
    sorted_list = []
    sorted_list.extend(nums)
    sorted_list.sort()
    if nums == sorted_list:
        return True
    sorted_list.sort(reverse=True)
    if nums == sorted_list:
        return True
    return False


def find132pattern(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    """  Brute for solution takes too long but works     
    for i in range(len(nums)-2):
        for k in range(i, len(nums)-1):
            if nums[k] > nums[i]:
                for j in range(k, len(nums)):
                    if nums[k] > nums[j] and nums[j] > nums[i]:
                        return True
    return False"""

    length = len(nums)

    # check if the array is too short first dont waste time
    if length < 3:
        return False
    # create a stack to keep track of decreasing elements using a double ended q
    decreasing_stack = deque()

    # store maximum value of the third element in the 132 pattern
    max_third_element = float('-inf')

    # traverse the array from right to left
    for i in range(length - 1, -1, -1):
        current_number = nums[i]

        # check for 132 pattern
        if current_number < max_third_element:
            return True

        # maintain the stack with decreasing elements
        while decreasing_stack and decreasing_stack[0] < current_number:
            max_third_element = decreasing_stack.popleft()

        # push the current element onto the stack
        decreasing_stack.appendleft(current_number)
    return False

if __name__ == '__main__':
    # print(running_sum([1, 2, 3, 4]))
    # print(pivot_index([1, 7, 3, 6, 5, 6]))
    # print(is_isomorphic("paper", "title"))
    # print(twoSum([2, 7, 11, 15]))
    # print(valid_parentheses('([{}])'))
    # print(mergeTwoLists(ListNode(1,2,3), [1,2,3]))
    # print(maxProfit([7,1,5,3,6,4]))
    # print(isPalindrome("A man, a plan, a canal: Panama"))
    #print(isAnagram("I am Lord Voldemort", "Tom Marvolo Riddle"))
    #print(floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))
    #print(findTheDifference("abcdefghi", "abcdeffghi"))
    #print(minPartitions('32'))
    #print(decodeAtIndex("leet2code3", 10))
    #print(mergeAlternately('abc', 'pqr'))
    #print(isMonotonic([1,2,2,3]))
    print(find132pattern([3,5,0,3,4]))