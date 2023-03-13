def solution(id_list,report,k):
    reported_list = [i.split()[1] for i in set(report)] #신고 당한 ID 목록(중복 제거)
    suspended_list = [reported_id for reported_id in set(reported_list) if reported_list.count(reported_id) >= k] #신고 당한 ID 중 횟수가 k가 넘어 정지당한 ID 목록
    report_list = [ i.split()[0] for i in set(report) if i.split()[1] in suspended_list] #정지 당한 ID를 신고한 ID 목록
    answer = [report_list.count(i) for i in id_list] #유효화된 신고자 목록에서 각 ID가 몇 번 언급되었는지 계산
    return answer

# id_list = ["muzi", "frodo", "apeach", "neo"]
# report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
# k = 2

id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3

print(solution(id_list,report,k))