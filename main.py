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
    s = ''.join(ch for ch in s if ch.isalnum())
    s = list(s.lower())
    new_s = []
    if s == '':
        return True
    for i in range(len(s)):
        if s[i] == s[-1 - i]:
            new_s.append(s[i])
    return new_s == s


if __name__ == '__main__':
    # print(running_sum([1, 2, 3, 4]))
    # print(pivot_index([1, 7, 3, 6, 5, 6]))
    # print(is_isomorphic("paper", "title"))
    # print(twoSum([2, 7, 11, 15]))
    # print(valid_parentheses('([{}])'))
    # print(mergeTwoLists(ListNode(1,2,3), [1,2,3]))
    # print(maxProfit([7,1,5,3,6,4]))
    print(isPalindrome("A man, a plan, a canal: Panama"))
