def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        actualPos = 0
        newPos = 0

        while newPos < len(nums):
            if nums[actualPos] != nums[newPos]:
                 actualPos += 1
                 nums[actualPos] = nums[newPos]
            newPos += 1
        return actualPos + 1

nums = [0,0,0,1,1,1,2,2,2,2,2,3]
print(nums)
print(removeDuplicates(nums))
print(nums)