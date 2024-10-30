

def findMinorPathBackTrack(vector,k) -> int:
    sneakPos = (0,0)
    sneakFinded, sneakPos= findInitSnake(vector)

    
    
    '''
    if sneakFinded == -1:
        vectorVisitados = [len(vector)-1]
        electionBackTrack(len(vector)-1,abs(vector[-1]),k-1,vector,vectorVisitados,vectorResultados)
    elif sneakFinded == 0:
        vectorVisitados = [0]
        electionBackTrack(0,abs(vector[0]),k-1,vector,vectorVisitados,vectorResultados)  
    '''
    if sneakFinded == 1:
        vectorResultados = []
        vectorVisitados1=[sneakPos[0]]
        electionBackTrack(sneakPos[0],abs(vector[sneakPos[0]]),k-1,vector,vectorVisitados1,vectorResultados)
        vectorVisitados2=[sneakPos[1]]
        electionBackTrack(sneakPos[1],abs(vector[sneakPos[1]]),k-1,vector,vectorVisitados2,vectorResultados)
        print("resultados: ",vectorResultados)
        print("len(vectorResultados =",len(vectorResultados))
        sum = min(vectorResultados)
        
        '''
        vectorVisitados1=[sneakPos[0]]
        res1 = simpleElection(sneakPos[0],abs(vector[sneakPos[0]]),k-1,vector,vectorVisitados1)
        vectorVisitados2=[sneakPos[1]]
        res2 = simpleElection(sneakPos[1],abs(vector[sneakPos[1]]),k-1,vector,vectorVisitados2)
        vectorResultados.append(res1)
        vectorResultados.append(res2)
        '''
    else:
        sum=easyWay(sneakFinded,k,vector)

    
    return sum


def findMinorPathVoraz(vector,k) -> int:
    
    sneakPos = (0,0)
    sneakFinded, sneakPos= findInitSnake(vector)
    visitados = []
    if sneakFinded == 1:
        val1 = abs(vector[sneakPos[0]])
        val2 = abs(vector[sneakPos[1]])
        if val1 <= val2:
            initialPos = sneakPos[0]
        else:
            initialPos = sneakPos[1]

        sum = abs(vector[initialPos])
        apples = 1
        actualPos = initialPos
        visitados.append(actualPos)
        while apples<k:
            leftPos = actualPos-1
            rightPos = actualPos+1
            cantLeft = False
            cantRight = False

            if leftPos<0:
                cantLeft = True
            else:
                while leftPos>0 and leftPos in visitados:
                    leftPos-=1
            
            if rightPos>=len(vector):
                cantRight = True
            else:
                while rightPos>=len(vector) and rightPos in visitados:
                    rightPos-=1
            
            if cantLeft:
                nextPos = rightPos
                nextDif = abs(-(vector[nextPos])+vector[actualPos])

            elif cantRight:
                nextPos = leftPos
                nextDif = abs(-(vector[actualPos])+vector[nextPos])
            else: 
                nextPos,nextDif = minPos(leftPos,rightPos,actualPos,vector)
                
                
            sum+=nextDif
            actualPos=nextPos
            apples+=1
            visitados.append(actualPos)

    else:
       sum=easyWay(sneakFinded,k,vector)

    return sum
    
def easyWay(sneakFinded,k,vector):
    apples = 1
    actualPos = 0 if sneakFinded == 0 else len(vector)-1
    sum = abs(vector[actualPos])
    while apples<k:
        if sneakFinded == 0:
            nextPos = actualPos+1
            dif =  abs(-(vector[actualPos])+vector[nextPos])
        else:
            nextPos = actualPos-1
            dif =  abs(-(vector[nextPos])+vector[actualPos])
        sum+=dif
        actualPos = nextPos
        apples+=1
    return sum


    
def findInitSnake(vector):
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
    return sneakFinded,sneakPos
    
def electionBackTrack(sneakPos,sum,n,vector,visitados,vectorResultados):
    if n>0:
        prevPos = sneakPos-1
        nextPos = sneakPos+1
        while prevPos>=0:
            if prevPos not in visitados:
                dif = abs(-(vector[prevPos])+vector[sneakPos])
                visitados.append(prevPos)
                electionBackTrack(prevPos,sum+dif, n-1, vector, visitados,vectorResultados)
                visitados.pop()
                break
            else:
                prevPos-=1
        while nextPos<len(vector):
            if nextPos not in visitados:
                dif = abs(-(vector[sneakPos])+vector[nextPos])
                visitados.append(nextPos)
                electionBackTrack(nextPos,sum+dif, n-1, vector, visitados,vectorResultados)
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

vector = [-20,5,10] # -> correct path 5,15,-20 = 35
k=3
print("Vector:",vector)
print("n =",len(vector))
print("k:",k)
print("Resultado por back tracking:",findMinorPathBackTrack(vector,k))

print("Resultado por voraz:",findMinorPathVoraz(vector,k))
