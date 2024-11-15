def canJump(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n_jumps = 0
        n = len(nums)
        posActual = 0 
        while posActual<n:
            n_jumps = nums[posActual]
            if posActual == n-1:
                return True
            elif n_jumps == 0: 
                return False
            maxJumps = 0
            for i in range(posActual+1,n_jumps+posActual+1):
                if i == n-1:
                    return True
                if nums[i]>=maxJumps:
                    maxJumps=nums[i]
                    provisionalPos = i
            posActual = provisionalPos if nums[provisionalPos] > posActual+n_jumps or nums[posActual+n_jumps] == 0 else posActual+n_jumps
        return True


nums = [2,3,1,1,4] #-> true
nums2= [3,2,1,0,4] #-> false

nums3 = [1,1,2,2,0,1,1]


print(canJump(nums3))