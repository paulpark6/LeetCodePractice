class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        c_zero = 0
        i = 0
        while(i < n):
            num = nums[i]
            if num == 0:
                nums.pop(i)
                c_zero +=1
                n -= 1
                i -= 1
            i += 1
        for i in range(c_zero):
            nums.append(0)
