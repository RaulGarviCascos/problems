def canJump(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n_jumps = 0
        n = len(nums)
        posActual = 0 
        jumpsTotal = 0
        while posActual<n:
            n_jumps = nums[posActual]
            if posActual == n-1:
                return jumpsTotal
            elif n_jumps == 0: 
                return False
            maxJumps = 0
            for i in range(posActual+1,n_jumps+posActual+1):
                if i == n-1:
                    return jumpsTotal+1
                if nums[i]+i>=maxJumps:
                    maxJumps=nums[i] + i
                    provisionalPos = i
            posActual = provisionalPos if nums[provisionalPos]+provisionalPos > posActual+n_jumps + nums[posActual+n_jumps] or nums[posActual+n_jumps] == 0 else posActual+n_jumps
            jumpsTotal+=1
        return jumpsTotal 


nums = [2,3,1,1,4] #-> true
nums2= [4,1,1,3,1,1,1] 

nums3 = [2,3,1,1,4]
nums4 = [9,8,2,2,0,2,2,0,4,1,5,7,9,6,6,0,6,5,0,5]




print(canJump(nums4))