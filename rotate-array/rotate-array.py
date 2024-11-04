def rotate(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        aux = nums[0]
        n = len(nums)
        posAux = 0
        for _ in range(n):
            nextPosAux =  posAux + k if posAux+k < n else posAux+k - n
            nextAux = nums[nextPosAux]
            nums[nextPosAux] = aux
            aux = nextAux
            posAux = nextPosAux 
            
                
            
    

nums = [-1,-100,3,99]

rotate(nums,2)
print(nums)