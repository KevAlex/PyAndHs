def mayorE(lista):
    mayor =[]
        
    for i in lista:
        mayor.append(max(i))
        print i
    return mayor

#print (mayorE([[5,35,69,32],[34,56,76]]))


def prom(lista):
    med=[]

    for i in lista:
        for j in i:
            if j%5 ==0:
                med.append((sum(i)/(len(i))))
    print (float(sum(i)/len(i)))
                

    #return med

print(prom([[4,6,7],[1,2,5]]))
