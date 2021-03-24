




labels = []
costs = []
with open('tFeilds.txt' , 'r') as fin:
    labelsIndex = 0
    costsIndex = 0
    for line in fin:

        lenth = len(line)
        if lenth < 6:
            #print(type(line))
            labels.append(line)
        else:
            cost =[]
            cost = line.split(',')    
            costs.append(cost)
wood = []
clay = []
iron = []
crop = []
print(len(costs))
i = 0 
for n in costs:
    for c in n:
        if i <= 19:
            if c.endswith('\n'):
                a = c[:-1]
                wood.append(a)
                #print(a)
            else:    
                wood.append(c)
                #print(c)
        elif i <= 39:
            if c.endswith('\n'):
                a = c[:-1]
                clay.append(a)
            else:    
                clay.append(c)
        elif i <= 59:
            if c.endswith('\n'):
                a = c[:-1]
                iron.append(a)
            else:    
                iron.append(c)

        elif i <= 79:
            if c.endswith('\n'):
                a = c[:-1]
          
                crop.append(a)
            else:    
                crop.append(c)
    i +=1


maxNum = int(len(wood)/5)    

i = 0
for count in range(0 , maxNum):
  
    #print('level = ' , wood[i] , ' wood = ', wood[i+1] , ' clay = ' ,wood[i+2] , ' iron = ' ,wood[i+3] , ' crop = ' ,wood[i+4])
    i +=5
-------------------------------------------

def rep():
    with open('travianFeildsV2.txt') as fin, open('tFeilds.txt', 'w') as fout:
        for line in fin:
            fout.write(line.replace('\t', ','))
            a = line[len(line)-2]
            if a ==',':
                newLine  = line[:-2]
                fin.write(newLine)
    print('done')            

labels = []
costs = []
with open('tFeilds.txt' , 'r') as fin:
    labelsIndex = 0
    costsIndex = 0
    for line in fin:

        lenth = len(line)
        if lenth < 6:
            #print(type(line))
            labels.append(line)
        else:
            cost =[]
            cost = line.split(',')    
            costs.append(cost)
wood = []
clay = []
iron = []
crop = []
print(len(costs))
i = 0 
for n in costs:
    for c in n:
        if i <= 19:
            if c.endswith('\n'):
                a = c[:-1]
                wood.append(a)
                #print(a)
            else:    
                wood.append(c)
                #print(c)
        elif i <= 39:
            if c.endswith('\n'):
                a = c[:-1]
                clay.append(a)
            else:    
                clay.append(c)
        elif i <= 59:
            if c.endswith('\n'):
                a = c[:-1]
                iron.append(a)
            else:    
                iron.append(c)

        elif i <= 79:
            if c.endswith('\n'):
                a = c[:-1]
          
                crop.append(a)
            else:    
                crop.append(c)
    i +=1
maxNum = int(len(wood)/5)   
print(maxNum) 

i = 0
for count in range(0 , maxNum):
  
    print('level = ' , wood[i] , ' wood = ', wood[i+1] , ' clay = ' ,wood[i+2] , ' iron = ' ,wood[i+3] , ' crop = ' ,wood[i+4])
    i +=5
