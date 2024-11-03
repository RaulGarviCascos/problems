def majorityElement(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       
        majElement = 0
        repes = 0
        for i in range(len(nums)):
            if repes == 0: majElement = nums[i]
            if majElement == nums[i]: repes+=1
            else: repes-=1
        return majElement
        


nums = [3,3,1,2,3,2,2,1,2,2,2,2,3,3,2,2,1,1,3,3]

print(majorityElement(nums))