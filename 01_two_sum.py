def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if target - nums[i] == nums[j]:
                return [i, j]
    return None

nums = [2, 7, 11, 9]
target = 11
print(twoSum(nums, target))