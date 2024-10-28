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
        sum += abs(vector[pos])
        sum = election(pos,sum,k,vector)
    return sum

def minPos(a1,a2,currentPos,vector):
    dif1 = abs(-(vector[a1])+vector[currentPos])
    dif2 = abs(-(vector[currentPos])+vector[a2])
    if dif1<=dif2:
        return a1,dif1
    else:
        return a2,dif2
    
def election(sneakPos,sum,n,vector):
    if n>0:
        if sneakPos-1>0:
            if not sneakPos+1>len(vector):
                #miro cual de las 2 opciones esta mas cerca y en caso de empate cojo izquierda
                newVulues=minPos(sneakPos-1,sneakPos+1,sneakPos,vector)
                return election(newVulues[0],sum+newVulues[1],n-1,vector)
            else:
                dif = abs(-(vector[sneakPos-1])+vector[sneakPos])
                return election(sneakPos-1,sum+dif,n-1,vector)
        elif not sneakPos+1>len(vector):
            dif = abs(-(vector[sneakPos])+vector[sneakPos+1])
            return election(sneakPos+1,sum+dif,n-1,vector)
    return sum


vector = [-20,-10,10,20,60] # -> correct path -10, 10, 20 = 40 sec
k=3
print(findMinorPath(vector,k))
