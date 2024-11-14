def maxProfit(prices):
    pos = 1
    n = len(prices)
    if n == 1: return 0
    lastResta = 0
    sumaTotal = 0
    sustraendo = prices[0]
    minuendo = prices[0]
    "resta = minuendo-sustraendo"
    while pos<n:
        elemento = prices[pos]
        restaActual = elemento - sustraendo
        if elemento<minuendo or pos+1 == n:
            sumaTotal+=minuendo-sustraendo if restaActual < minuendo-sustraendo else restaActual
            minuendo = prices[pos] 
            sustraendo = prices[pos] 
        else:
            if elemento < sustraendo:
                sustraendo = elemento
            elif elemento > minuendo:
                minuendo = elemento
            elif restaActual<0: 
                minuendo = elemento
                sustraendo = elemento
            
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

prices = [2,4,1]


print(prices)
expected = "2"
print("expected:",expected)
print("result:",maxProfit(prices))

'''
Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

Example 2:
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
 
'''
