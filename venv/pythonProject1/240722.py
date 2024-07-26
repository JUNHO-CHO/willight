# # 기초 문제2
# # N개의 단위로 아래와 같이 리스트로 출력(함수)
# # 결과: [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R'], ['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z']]
#
#
#
# alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
#                  'U', 'V', 'W', 'X', 'Y', 'Z']
#
# def split_n_list(alphabet_list,n):   #함수선언
#     # answer = list()
#     answer = []                      #빈 리스트 생성
#     for i in range(0, len(alphabet_list)):       # 0부터 알파벳 마지막의 범위 및 길이 설정
#         answer.append(alphabet_list[i:n+i])      # i부터 i+n-1까지의 리스트를 answer 리스트에 추가
#
#     return answer                                # answer값 반환
#
#
# print(f"결과: {split_n_list(alphabet_list,3)}")   #프린트
# # -----------------------------------------------------------------------------------------------
# # 스택 문제 1
# # 키보드 Backspace 기능 구현
# # input_string = ‘123//45/6789///’
# # /를 만나면 앞의 값을 삭제
# # 참고 - 맨앞에 /만나면 어떻게 처리해야 되는지 생각 해보기
# # answer = ‘146’
#
# def backspace_string(input_string):  #함수선언
#     stack = []                       #빈리스트설정
#     for i in input_string:           #매개변수 i 반복문설정
#         if i != '/':                 #매개변수i가 /과 같지 않다면
#             stack.append(i)          #매개변수 i값을 리스트에 추가
#         elif i == '/':               #매개변수 i가 /와 같다면
#             stack.pop()              #리스트 값에서 제외
#         answer = ''.join(stack)      #answer의 문자열을 하나로 합친다.
#     return answer                    #answer값 반환
#
# print(backspace_string("123//45/6789///"))
# # -----------------------------------------------------------------------------------------------
# # 스택 문제 2
# # 괄호 문법 검사기
# # bracket1: [[[[]]]][] → answer ‘YES’
# # bracket2: [[[[[[[[[[[[[[[[]] → answer ‘NO’
# def is_bracket(b):
#     answer = "YES"
#
#     return answer
#
#
# # [[[[]]]][]
# # [[[[[[[[[[[[[[[[]]
#
# # YES
# print(is_bracket("[[[[]]]][]"))
#
# # No
# print(is_bracket("[[[[[[[[[[[[[[[[]]"))



# -----------------------------------------------------------------------------------------------




# def solution(n):
#     answer = []
#     for i in str(n):
#         answer.append(int(i))
#     return answer[::-1]
#
# print(solution(12345))


# def solution(n):  # 함수정의
#     answer=[]
#     return list(map(int, reversed(str(n))))  # 정수 n을 문자열 전환,  5,4,3,2,1,출력을 변환, 숫자열 전환 리스트로 출력
# print(solution(12345))
#
def solution(n):
    answer = []
    for i in str[n]:
        answer.append(int[i])
    return answer[::-1]

print(solution(12345))

# TypeError: 'type' object is not subscriptable
# 이 오류는 보통 프로그래밍 중에 실수로 인해 발생하며,
# 해당 타입(클래스)이 시퀀스 형식을 지원하지 않기 때문에 발생합니다.
# 오류 메시지가 나타내는 바는 '해당 타입의 객체는 인덱싱을 지원하지 않는다'는 것입니다.


# -----------------------------------------------------------------------------------------------
# [숙제] - 07.19
# for문 문제 1
# 아래와 같이 출력해주세요


# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------


