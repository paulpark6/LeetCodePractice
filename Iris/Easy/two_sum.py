def twoSum(nums, target):
    d = dict()
    for idx, num in enumerate(nums):
        if (target-num) in d.keys():
            return [d[target-num], idx]
        else:
            d[num] = idx

print(twoSum([2,7,11,15], 9)) # [0, 1]