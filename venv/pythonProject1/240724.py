# # [숙제] - 07.19
# # 각 엘리먼트를 다 더해주세요
# # 예시 입력 값: a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # 출력 값: 45
# # 참고) 각 요소 다 더하기(1 + 2 + 3 + 4....)
#
# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# sum_list=0          # 변수값 0 설정
# for i in a:         #for 문을 통해 a리스트 안에 요소를 i에 추가
#     for j in i:     # i에 추가한 값을 다시 j에 추가
#         sum_list+=j # j매개변수 전체 sum_list에 추가
# print(sum_list)     #출력
#
# # --------------------------------------------------------------------------
# [숙제] - 07.19
# 두 개의 리스트의 모든 요소를 덧셈 후 결과를 출력해주세여
# 입력 값
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# 참고) - 1+4, 1+5, 1+6, 2+4……
# 결과 값5 6 7 6 7 8 7 8 9

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
#
# a_list=[]                           #빈리스트 생성
# for i in list1:                     # list1 매개변수 i로 설정
#     for j in list2:                 # list2 매개변수 j로 설정
#         a_list.append(i + j)        # a_list에 i+j값 추가
# print(a_list)                       # 출력

# # --------------------------------------------------------------------------
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# def main_lists(list1, list2):
#     a_list = []
#     for i in list1:
#         for j in list2:
#             a_list.append(i + j)
#     return a_list
# print(main_lists(list1, list2))
# # --------------------------------------------------------------------------
#주석달기
def recursive_func_1(n): # 함수 선언
    if n == 0:           # n이 0이라면
        return           # 함수값 반환
    else:                # n값이 0이 아니면
        recursive_func_1(n-1)         # 함수n에 -1
        print(n, end=' ')             # n값 출력, 공백출력

        # 밑에서부터 5 4 3 2 1 순서대로 스택이 쌓인다.


recursive_func_1(5)                   # 함수 n은 5
#출력값 : 1 2 3 4 5
# # --------------------------------------------------------------------------
def recursive_func(n):        # 함수선언
    if n == 0:                # n이 0이면
        return                # 함수반환
    else:                     # 함수 n이 0이 아니면
        print(n, end=' ')     # n값 출력, 공백출력
        recursive_func(n-1)   # 함수 n값 호출 후 -1

recursive_func(5)
#출력 값 5 4 3 2 1
#
#
# # --------------------------------------------------------------------------
# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_idx = i
#         for j in range(i + 1, n):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
#
#     return arr
#
#
# # Example usage
# if __name__ == "__main__":
#     arr = [44, 490, 83, 1, 0, 34, 65, 97]
#     sorted_arr = selection_sort(arr)
#     print(sorted_arr)

# --------------------------------------------------------------------------
# 대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True,
# 다르면 False를 return 하는 solution를 완성하세요.
# 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.
# 예를 들어 s가 "pPoooyY"면 true를 return하고 "Pyy"라면 false를 return합니다.
#
# 제한사항
# 문자열 s의 길이 : 50 이하의 자연수
# 문자열 s는 알파벳으로만 이루어져 있습니다.
s = ('pPoooyY','PyY')
def solution(s):
    answer = True
    s.lower.count('p')
    s.lower.count('y')
    s.lower.count('p') == s.lower.count('y')
    return answer
# ===============1차 오류=============
# AttributeError: 'builtin_function_or_method' object has no attribute 'count'
# 메소드나 속성을 잘못 사용하거나 찾을 수 없는 경우에 발생합니다
#
# ===============2차 수정 =============
s = ('pPoooyY','PyY')
def solution(s):
    for i in range(len(s)):
        if s[i] == 'p':
            for j in range(len(s)-1, i, -1):
                if s[j] != 'y':
                    return j
# ===================2차 오류=============
# 테스트 1
# 입력값 〉	"pPoooyY"
# 기댓값 〉	true
# 실행 결과 〉	실행한 결괏값 6이 기댓값 true과 다릅니다.
# 테스트 2
# 입력값 〉	"Pyy"
# 기댓값 〉	false
# 실행 결과 〉	실행한 결괏값 null이 기댓값 false과 다릅니다.
# ===============3차 수정 =============
# 정리해보자... s의 문자열들을 소문자로 바꾼다
# 소문자로 바꾼 문자들을 p,y의 갯수를 각각 세어준다
# p의 갯수와 y의 갯수가 같으면 True, 틀리면 false하고 리턴.

def solution(s):
    return s.lower.count('p') == s.lower.count('y')

#해석 : s의 문자열을 소문자로 변경하고 p와 y의 갯수를 산정하고 p와 y의 갯수가 같으면 값을 반환한다.







# --------------------------------------------------------------------------

# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#
#         j = i - 1
#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
#
#     return arr
# if __name__ == "__main__":
#     arr = [44, 490, 83, 1, 0, 34, 65, 97]
#     sorted_arr = insertion_sort(arr)
#     print(sorted_arr)
#
# 1. arr함수 선언을 해준다
# 2. range함수로 arr리스트 내의 범위와 요소들의 길이를 i 매개변수를 for문을 이용하여 반복설정을 해주고
# 3. arr의 i번째에 있는 요소를 key변수에 저장한다.
# 4. j는 현재 삽입할 요소의 전 위치를 j로 설정한다.
# 5. j가 0보다 크거나 같고 key값이 arr[j]보다 작으면
# 6. arr[j]의 위치를 한칸 오른쪽으로 이동한다.
# 7. j가


# --------------------------------------------------------------------------
