def findMin(nums):
    if nums[0] <= nums[-1]:
        return nums[0]
    mid = len(nums)// 2
    if nums[mid] < nums[0]:
        return findMin(nums[1:mid+1])
    else:
        return findMin(nums[mid+1:])


print(findMin([4,5,6,7,-5,0,1,2]))