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
    for i in range(length-2):
        for j in range(i+1,length-1):
            for k in range(j+1,length):
                if sum((nums[i],nums[j],nums[k])) == 0:
                    ans.append([nums[i],nums[j],nums[k]])
    return ans


s = [1,0,1,-2,4,2,-4]
print(threeSum(s))

