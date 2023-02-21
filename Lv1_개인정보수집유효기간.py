def solution(today, terms, privacies):
    answer = []
    terms_dic = {} 
    for t in terms: terms_dic[t.split()[0]] = int(t.split()[1]) #유효기간 정보를 dic으로 저장

    for i in range(len(privacies)):
        p = privacies[i]    
        y = terms_dic[p.split()[1]]//12 + int(p[0:4]) #각 유형에 맞는 정보를 리스트 속 기간과 계산
        m = terms_dic[p.split()[1]]%12 + int(p[5:7])
        if m>12: #계산한 월이 12월보다 클 경우 처리
            m-=12
            y+=1

        if y < int(today.split('.')[0]): #유효기간 지난 정보의 인덱스를 answer에 저장
              answer.append(i+1)
        elif y == int(today.split('.')[0]):
            if m < int(today.split('.')[1]):
                answer.append(i+1)
            elif m == int(today.split('.')[1]):
                if int(p.split()[0][8:10])<=int(today.split('.')[2]): 
                    answer.append(i+1)                      

    return answer

today="2022.05.19"
terms= ["A 6", "B 12", "C 3"]
privacies= ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

# today="2020.01.01"
# terms= ["Z 3", "D 5"]
# privacies=["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]

print(solution(today, terms, privacies))