# 합격 컷트 라인은 60점
# 점수 : [80, 40, 90, 55, 94, 30, 60, 44]
# answer = 합격자 수(4)
# 1번문제 완료
# def count_passer(score, c):                 #점수와 커트라인 함수를 설정해준다
#     answer = 0                              #변수는 0으로 설정
#     for i in score:                         #for문을 통해 점수안에 매개변수를 설정하고
#         if i >= c:                          #매개변수(i)가 컷트라인 c보다 크거나 같을경우
#             answer += 1                     #answer에 하나씩 더해준다1
#     return answer                           #answer값을 반환한다.
#
# print(count_passer([80, 40, 90, 55, 94, 30, 60, 44], 60))
# print(count_passer([20, 50, 20, 80, 45], 30))

# nums의 길이 3 < = n < = 100.000
# O(???)
# 배열의 nums 원소는 정수
# 배열의 원소는 중복된 값이 없다.
# [23, 20, 73, 98, 11, 4, 288]
# [33, 423 32, 435, 235, 7, 56]


# def remove_duplicates(d_list):    #리스트가 있는 함수를 설정
#     result = []                   #리스트를 초기화한다.
#     for i in d_list:              #for문으로 입력받은 리스트를 순회한다
#         if i not in result:       # 결과안에 i(리스트)가 없으면
#             result.append(i)      # 초기화 한 리스트에 i를 추가한다.
#     return result                 # 중복제거된 리스트를 출력한다



# alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
#                  'U', 'V', 'W', 'X', 'Y', 'Z']
#
# def split_n_list(split_size=3):          #알파벳을 3개씩나눠서 설정한다.
#     # answer = list()
#     answer = []                          # answer를 담을 리스트를 초기화하고
#     for i in range(0, len(alphabet_list), split_size): #0에서 시작해서 alphabet리스트의 길이까지 스플릿 사이즈간격으로 반복한다.
#         answer.append(alphabet_list[i:i + split_size])    #각 부분에 리스트를 추가한다
#     return answer
#
#
# print(f"결과: {split_n_list(3)}")
#
# duplicated_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]



# 문제 2 - 최소값 구하기(index)
# nums의 길이 3 < = n < = 100.000
# O(???)
# 배열의 nums 원소는 정수
# 배열의 원소는 중복된 값이 없다.
# [23, 20, 73, 98, 11, 4, 288]
# [33, 423, 32, 435, 235, 7, 56]
def minimum_value(nums):  #함수 정의
    answer = 0            #변수 선언

    for i in range(len(nums)):   #반복문으로 nums의 범위에 있는 수를 i에 대입
        if nums[i] < nums[answer]:     #nums의 i가 최소값인데 nums변수가 i보다 크면 --- 이부분 제일오래걸림.. 이해 못하고 구글링
            answer = i                #최소값을 변수값 i로 선언

    return answer                     #최소값 인덱스 반환


# [23, 20, 73, 98, 11, 4, 288]
print(minimum_value([23, 20, 73, 98, 11, 4, 288])) # 5
print(minimum_value([33, 423, 32, 2, 56])) # 3




