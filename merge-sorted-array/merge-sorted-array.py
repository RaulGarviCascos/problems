

def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    actualPosNum2 = n - 1
    
    if m == 0:
        for i in range(n):
            nums1[i] = nums2[i]
    else:
        while actualPosNum2 >= 0:
            actualPosNum1 = len(nums1) -1
            itsEmptyPosition = True
            while nums1[actualPosNum1] == 0 and actualPosNum1 >= 0:
                if actualPosNum1 - 1 >= 0 and nums1[actualPosNum1 - 1] > nums2[actualPosNum2]:
                    nums1[actualPosNum1] = nums1[actualPosNum1 - 1]
                    nums1[actualPosNum1 - 1] = 0
                    itsEmptyPosition = False
                elif  not itsEmptyPosition or nums1[actualPosNum1 - 1] != 0  and itsEmptyPosition:
                    nums1[actualPosNum1] = nums2[actualPosNum2]
                    break
                
                actualPosNum1 -= 1
            actualPosNum2 -= 1

nums1 = [-1,0,0,3,3,3,0,0,0] 
m=6
'''nums1 = [4, 5, 6, 0, 0, 0]

m= 3'''
nums2 = [1,2,3]
n=3
print(nums1)
print(nums2)
merge(nums1,m,nums2,n)
print("nums1 after merge",nums1)
