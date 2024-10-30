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
    vectorResultados = []
    if sneakFinded == -1:
        vectorVisitados = [len(vector)-1]
        election(len(vector)-1,abs(vector[-1]),k-1,vector,vectorVisitados,vectorResultados)
    elif sneakFinded == 0:
        vectorVisitados = [0]
        election(0,abs(vector[0]),k-1,vector,vectorVisitados,vectorResultados)  
    else:
        
        vectorVisitados1=[sneakPos[0]]
        election(sneakPos[0],abs(vector[sneakPos[0]]),k-1,vector,vectorVisitados1,vectorResultados)
        vectorVisitados2=[sneakPos[1]]
        election(sneakPos[1],abs(vector[sneakPos[1]]),k-1,vector,vectorVisitados2,vectorResultados)
        '''
       
        vectorVisitados1=[sneakPos[0]]
        res1 = simpleElection(sneakPos[0],abs(vector[sneakPos[0]]),k-1,vector,vectorVisitados1)
        vectorVisitados2=[sneakPos[1]]
        res2 = simpleElection(sneakPos[1],abs(vector[sneakPos[1]]),k-1,vector,vectorVisitados2)
        vectorResultados.append(res1)
        vectorResultados.append(res2)
        '''
    print("resultados: ",vectorResultados)
    print("len(vectorResultados =",len(vectorResultados))
    sum = min(vectorResultados)
    return sum
    
def election(sneakPos,sum,n,vector,visitados,vectorResultados):
    if n>0:
        prevPos = sneakPos-1
        nextPos = sneakPos+1
        while prevPos>=0:
            if prevPos not in visitados:
                dif = abs(-(vector[prevPos])+vector[sneakPos])
                visitados.append(prevPos)
                election(prevPos,sum+dif, n-1, vector, visitados,vectorResultados)
                visitados.pop()
                break
            else:
                prevPos-=1
        while nextPos<len(vector):
            if nextPos not in visitados:
                dif = abs(-(vector[sneakPos])+vector[nextPos])
                visitados.append(nextPos)
                election(nextPos,sum+dif, n-1, vector, visitados,vectorResultados)
                visitados.pop()
                break
            else:
                nextPos+=1
    else:
        vectorResultados.append(sum)

def minPos(a1,a2,currentPos,vector):
    dif1 = abs(-(vector[a1])+vector[currentPos])
    dif2 = abs(-(vector[currentPos])+vector[a2])
    if dif1<=dif2:
        return a1,dif1
    else:
        return a2,dif2
    
def simpleElection(sneakPos,sum,n,vector,visitados):
    if n>0:
        prevPos = sneakPos -1
        nextPos = sneakPos +1
        while prevPos>=0 and prevPos not in visitados:
            prevPos-=1
        while nextPos<len(vector) and nextPos not in visitados:
            nextPos+=1
        posMin,valMin = minPos(prevPos,nextPos,sneakPos,vector)
        return simpleElection(posMin,sum+valMin, n-1, vector, visitados)
    else:
        return sum

vector = [-20,5,10] # -> correct path -10, 10, 20 = 40 sec
k=3
print("n =",len(vector))
print(findMinorPath(vector,k))
