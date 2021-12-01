def threeSum(nums):
    ans = []
    if not nums:
        return ans
    length = len(nums)
    if length < 3:
        return ans
    if sum(nums) == sum([abs(i) for i in nums]):
        return ans
    if len(nums) == 3 and sum(nums) == 0:
        return nums
    for i in range(length):
        pass


s = [1]
print(threeSum(s))

