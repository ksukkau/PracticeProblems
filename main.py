def running_sum(nums: list[int]) -> list[int]:
    """
    Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
    Return the running sum of nums.
    Input: nums = [1,2,3,4]
    Output: [1,3,6,10]
    Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
    """
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums


if __name__ == '__main__':
    print(running_sum([1, 2, 3, 4]))
