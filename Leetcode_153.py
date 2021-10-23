def findMin(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    if nums[0] < nums[-1]:
        return nums[0]
    if n == 2:
        return nums[1]
    mid = int(n / 2)
    if nums[mid] < nums[0]:
        return findMin(nums[:mid+1])
    else:
        return findMin(nums[mid:])


print(findMin([6,18,-6,1,2,3,4,5]))