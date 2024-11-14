def maxProfit(prices):
    max = -1
    min = -1
    pos = 0
    n = len(prices)
    if n == 1: return 0
    lastResta = 0
    while pos<n:
        elemento = prices[pos]
        if min==-1:
            min = elemento
        elif elemento>max:
            max=elemento
        if elemento<=min and pos+1<n:
            lastMin = min
            min=elemento
            if max!=-1:
                lastResta = max - lastMin if max - lastMin > lastResta else lastResta
                max = elemento
        pos+=1
    resta = max-min if max-min>lastResta else lastResta
    return resta if resta>0 else 0 


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

prices = [7,6,4,3,1]


print(prices)
expected = easyWay(prices)
print("result:",maxProfit(prices))
print("expected:",easyWay(prices))
