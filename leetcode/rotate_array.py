__author__ = 'Arthur'


def rotate(nums, k):
    # for i in range(k):
    #     nums.insert(0, nums.pop())
    k %= len(nums)
    nums = nums[len(nums) - k:] + nums[: len(nums) - k]


a = [1, 2, 3, 4]
rotate(a, 2)
print(a)