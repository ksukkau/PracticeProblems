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
    hashMap = {nums[i]: i for i in range(len(nums))}
    for i in range(len(nums)):
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
    pair = dict(('()', '[]', '{}'))
    stack = []
    for x in s:
        if x in '([{':
            stack.append(x)
        elif len(stack) == 0 or x != pair[stack.pop()]:
            return False
    return len(stack) == 0


if __name__ == '__main__':
    print(running_sum([1, 2, 3, 4]))
    print(pivot_index([1, 7, 3, 6, 5, 6]))
    print(is_isomorphic("paper", "title"))
    print(twoSum([2, 7, 11, 15]))
    print(valid_parentheses('([{}])'))
