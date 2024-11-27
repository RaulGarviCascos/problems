from pprint import pprint
def productExceptSelf(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        resultArray =[1]
        primerElemento = nums[0]

        for i in range(1,n):
            resultArray.append(primerElemento)
            primerElemento*= nums[i]
        actualPos = n-2
        secondElement = nums[-1]

        while actualPos>=0:
            resultArray[actualPos] *= secondElement
            secondElement*=nums[actualPos]
            actualPos-=1
        return resultArray

def easyWay(nums):
    n = len(nums)
    resultArray = [1]*n
    for i in range(0,n):
        for j in range(0,n):
            if i != j:
                resultArray[j]*=nums[i]
    return resultArray
        
        

nums = [-1,1,0,-3,3]

expected = easyWay(nums)
print('expected:',expected)
output = productExceptSelf(nums)
print('output:  ',output)

# Códigos ANSI para colores
VERDE = "\033[92m"
ROJO = "\033[91m"
RESET = "\033[0m"

# Ticks y cruces
TICK = "\u2713"  # ✓
CROSS = "\u2717"  # ✗

# Ejemplo de impresión
if output == expected:
    print(f"{VERDE}{TICK} Test passed{RESET}")
else:
    print(f"{ROJO}{CROSS} Test failed{RESET}")