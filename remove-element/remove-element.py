def removeElement(nums, val):

    actualPos = len(nums) - 1
    aux = '_'
    adds = 0
    while actualPos >= 0:
        if nums[actualPos] != val and aux == '_':
            aux = nums[actualPos]
            newPos = 0
            while newPos < len(nums) and nums[newPos] != val:
                newPos += 1
            if newPos != len(nums):
                nums[newPos] = aux
                nums[actualPos] = '_'
                aux = '_'
                adds += 1
                
        elif nums[actualPos] == val:
            nums[actualPos] = '_'
            adds += 1
        actualPos -= 1
    return len(nums) - adds


nums = [0,1,2,2,3,0,4,2]
expected = [0,1,4,0,3]

val = 2
print(nums)
print(removeElement(nums, val))
print(nums)