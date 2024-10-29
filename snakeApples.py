def findMinorPath(vector,k) -> int:
    sneakPos = (0,0)
    sneakFinded = -1                            #si es -1, significa que todas las posiciones son negativas y esta al final
    sum=0
    #primero encuentro posicion serpiente
    for i in range(len(vector)):
        if i == 0  and vector[i]>=0:    
            sneakFinded = 0                     # si es 0, significa que esta al principio    
            break
        if i != len(vector)-1:  
            if vector[i]<0 and vector[i+1]>=0:
                sneakPos = (i,i+1)
                sneakFinded = 1                 #si es 1, significa que esta en sneakPos (i,i+1)
                break
    
    if sneakFinded == -1:
        for i in reversed(range(k)):
            sum+=abs(vector[i])
    elif sneakFinded == 0:
        for i in range(k):
            sum+=abs(vector[i])
    else:
        if abs(vector[sneakPos[0]])<=abs(vector[sneakPos[1]]):
            pos = sneakPos[0]
        else:
            pos = sneakPos[1]
        sum1 = abs(vector[sneakPos[0]])
        vectorVisitados1=[sneakPos[0]]
        vectorResultados = []
        resultado1 = election(sneakPos[0],sum1,k-1,vector,vectorVisitados1,vectorResultados)
        sum2 = abs(vector[sneakPos[1]])
        vectorVisitados2=[sneakPos[1]]
        resultado2 = election(sneakPos[1],sum2,k-1,vector,vectorVisitados2,vectorResultados)
        print("resultados: ",resultado1,resultado2)
    return sum

def minPos(a1,a2,currentPos,vector):
    dif1 = abs(-(vector[a1])+vector[currentPos])
    dif2 = abs(-(vector[currentPos])+vector[a2])
    if dif1<=dif2:
        return a1,dif1
    else:
        return a2,dif2
    
def election(sneakPos,sum,n,vector,visitados,vectorResultados):
    if n>0:
        prevPos = sneakPos-1
        nextPos = sneakPos+1
        while prevPos>=0:
            if prevPos not in visitados:
                dif = abs(-(vector[prevPos])+vector[sneakPos])
                visitados.append(prevPos)
                nextSum = sum + dif
                election(prevPos,sum+dif, n-1, vector, visitados,vectorResultados)
            else:
                prevPos-=1
        while nextPos<len(vector):
            if nextPos not in visitados:
                dif = abs(-(vector[sneakPos])+vector[nextPos])
                visitados.append(nextPos)
                nextSum = sum + dif
                election(nextPos,sum+dif, n-1, vector, visitados,vectorResultados)
            else:
                nextPos+=1
    else:
        visitados.clear()
        vectorResultados.append(sum)
    return sum


vector = [-20,-10,10,20,60] # -> correct path -10, 10, 20 = 40 sec
k=3
print(findMinorPath(vector,k))
