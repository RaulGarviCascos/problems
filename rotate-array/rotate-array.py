
def rotate(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        initialK = 0+k
        while initialK>=len(nums):
            initialK -= len(nums)
        nums.reverse()
        nums[:initialK] = reversed(nums[:initialK])
        nums[initialK:] = reversed(nums[initialK:])

def easyWay(nums,k):
    newArray = []
    n = len(nums)
    for _ in range(n):
        newArray.append(0)

    for i in range(n):
        pos = i+k
        while pos>=n:
            pos -= n
        newArray[pos] = nums[i]          
    return newArray 

        
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54]
k=45
expected = easyWay(nums,k)

print(nums)
rotate(nums,k)
print(nums)
print(expected)
