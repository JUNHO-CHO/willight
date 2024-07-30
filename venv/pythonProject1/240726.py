# 이 코드를 재귀함수로 바꿔봐~   (시ㅓㄹ)
# 재귀함수란?


# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a
#
# print(gcd(60, 48))

# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a
#
# print(gcd(60, 48))


# --------------------------------------------------------------------------
# 문제 설명
# 수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
#
# 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
# completion의 길이는 participant의 길이보다 1 작습니다.
# 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
# 참가자 중에는 동명이인이 있을 수 있습니다.
# 입출력 예
# participant	completion	return
# ["leo", "kiki", "eden"]	["eden", "kiki"]	"leo"
# ["marina", "josipa", "nikola", "vinko", "filipa"]	["josipa", "filipa", "marina", "nikola"]	"vinko"
# ["mislav", "stanko", "mislav", "ana"]	["stanko", "ana", "mislav"]	"mislav"
# 입출력 예 설명
# 예제 #1
# "leo"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.
#
# 예제 #2
# "vinko"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.
#
# 예제 #3
# "mislav"는 참여자 명단에는 두 명이 있지만, 완주자 명단에는 한 명밖에 없기 때문에 한명은 완주하지 못했습니다.

def solution(participant, completion):
    answer = ''
    if participant != completion:
        answer.append(participant)
    return answer






def solution(p, c):
    p_set=set(p)
    c_set=set(c)
    pcset= p_set-c_set
    return list(pcset)



p=["leo", "kiki", "eden"]
c=["eden", "kiki"]
print(solution(p,c))

def solution(participant, completion):
    participant.sort() # participant 리스트 정렬
    completion.sort()  # completion 리스트 정렬

    for i in range(len(completion)):    #completion의 길이와 범위 반복
        if participant[i] != completion[i]:  # participant 와 completion의 같은 위치인지 비교하고
            return participant[i]            # 같지 않으면 participant 반환

    return participant[-1]                   #모든 항목이 일치하면 마지막 값 반환

participant=["leo", "kiki", "eden"]
completion=["eden", "kiki"]

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------


