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

def removeDuplicates2(nums):
    actualPos = 0
    newPos = 0
    minRepets = 0
    
    while newPos < len(nums):
        if nums[actualPos] == nums[newPos]:
            newPos += 1
            minRepets +=1
        elif minRepets > 1:
            actualPos+=2
            newPos,minRepets = fillIn(actualPos,nums,newPos)
        else:
            actualPos += 1
            newPos,minRepets = fillIn(actualPos,nums,newPos)
    minRepets = 2 if minRepets>=2 else minRepets
    return actualPos + minRepets

def fillIn(actualPos,nums,newPos):
    repetNewNumber = actualPos
    while repetNewNumber < newPos:
        nums[repetNewNumber] = nums[newPos]
        repetNewNumber += 1
    minRepets = actualPos - newPos
    newPos = actualPos
    return newPos,minRepets

nums = [1,1,1,1,1,1,1,1]
print(nums)
print(removeDuplicates2(nums))
print(nums)