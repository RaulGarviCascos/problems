def maxProfit(prices):
    pos = 0
    n = len(prices)
    if n == 1: return 0
    lastResta = 0
    sumaTotal = 1
    while pos<n:
        if pos+1<n and prices:  
            pos+=1
        
    return sumaTotal 


def easyWay(prices):
    maxSol = 0
    for i in range(len(prices)):
        for j in range(i,len(prices)):
            minuendo = prices[j]
            sustraendo = prices[i]
            resta = minuendo-sustraendo
            if resta > maxSol:
                maxSol = resta
    return maxSol

prices = [7,1,5,3,6,4]


print(prices)
expected = easyWay(prices)
print("result:",maxProfit(prices))

