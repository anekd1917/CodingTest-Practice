def solution(survey, choiced):
    answer = ''
    score_list = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    for i in range(len(choices)):
        if choices[i] >= 4:
            score_list[survey[i][1]]+=choices[i]-4
        else:
            score_list[survey[i][0]]+=4-choices[i]

    #점수 더 높은 거 저장   
    answer += 'R' if score_list['R']>=score_list['T'] else 'T'
    answer += 'C' if score_list['C']>=score_list['F'] else 'F'
    answer += 'J' if score_list['J']>=score_list['M'] else 'M'
    answer += 'A' if score_list['A']>=score_list['N'] else 'N'
    
    
    return answer

survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]

# survey = ["TR", "RT", "TR"]
# choices = [7, 1, 3]

# survey = []
# choices =[]

print(solution(survey, choices))