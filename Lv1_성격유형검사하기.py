survey = list(input("Input survay: >>").split(', '))
i = 0
for sur in survey:
    sur=sur.replace("\"","").replace('[','').replace(']','')
    survey[i] = sur
    i += 1

choices = list(input("Input choices: >>").split(', '))
i = 0
for cho in choices:
    cho=cho.replace('[','').replace(']','')
    choices[i] = int(cho)
    i+=1

result = []
for i in range(4):
    line=[]
    for j in range(2):
        line.append(0)
    result.append(line)


for i in range(len(choices)):
    s = survey[i][0]
    if(s=='R'):
        if(choices[i]<4):
            result[0][0] += 4-choices[i]
        elif(choices[i]>4):
            result[0][1] += choices[i]-4
        else:
            continue
    elif(s=='T'):
        if(choices[i]<4):
            result[0][1] += 4-choices[i]
        elif(choices[i]>4):
            result[0][0] += choices[i]-4
        else:
            continue
    elif(s=='C'):
        if(choices[i]<4):
            result[1][0] += 4-choices[i]
        elif(choices[i]>4):
            result[1][1] += choices[i]-4
        else:
            continue    
    elif(s=='F'):
        if(choices[i]<4):
            result[1][1] += 4-choices[i]
        elif(choices[i]>4):
            result[1][0] += choices[i]-4
        else:
            continue    
    elif(s=='J'):
        if(choices[i]<4):
            result[2][0] += 4-choices[i]
        elif(choices[i]>4):
            result[2][1] += choices[i]-4
        else:
            continue
    elif(s=='M'):
        if(choices[i]<4):
            result[2][1] += 4-choices[i]
        elif(choices[i]>4):
            result[2][0] += choices[i]-4
        else:
            continue
    elif(s=='A'):
        if(choices[i]<4):
            result[3][0] += 4-choices[i]
        elif(choices[i]>4):
            result[3][1] += choices[i]-4
        else:
            continue
    else: #if(s=='N')  
        if(choices[i]<4):
            result[3][1] += 4-choices[i]
        elif(choices[i]>4):
            result[3][0] += choices[i]-4
        else:
            continue
res=""
list =[['R','T'],['C','F'],['J','M'],['A','N']]
for i in range(4):
    if(result[i][0]<result[i][1]):
        res+=(list[i][1])
    else:
        res+=(list[i][0])

print(res)