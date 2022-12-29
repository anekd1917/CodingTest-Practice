# 문제 설명
# 숫자로 이루어진 문자열 t와 p가 주어질 때, t에서 p와 길이가 같은 부분문자열 중에서, 이 부분문자열이 나타내는 수가 p가 나타내는 수보다 작거나 같은 것이 나오는 횟수를 return하는 함수 solution을 완성하세요.
# 예를 들어, t="3141592"이고 p="271" 인 경우, t의 길이가 3인 부분 문자열은 314, 141, 415, 159, 592입니다. 이 문자열이 나타내는 수 중 271보다 작거나 같은 수는 141, 159 2개 입니다.

# 입력
t=input("Input 't': ")
p=input("Input 'p': ")

result = 0 #결과값

len_t = len(t)
len_p = len(p)
# print('t: ',t)
# print('p: ',p)
# print('p\'s length: ',len_p)

index = 0
for j in range(len_t-len_p+1):
    partNum =  0
    cipher = 1
    for i in range(len_p-1): #partNum 저장 시 숫자가 뒤부터 호출되어 저장되므로 *10이 아닌 /10을 해줘야 함
        cipher*=10
    for i in range(index,index+len_p):
        # print('index: ',index)
        partNum += int(t[i])*cipher
        cipher /=10
    # print(partNum)
    if(partNum<=int(p)): result+=1
    index+=1

print(result)

