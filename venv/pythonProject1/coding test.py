
# 문제 2
# cars = ['audi', 'bmw', 'subaru', 'kia', 'toyota', 'hyundai']
#
# 새로운 리스트에 kia, hyundai를 대문자로 추가하라.
# upper()
# len 함수
# range 함수
# 인덱싱
# bool
# or
# if True/Flase

# cars = ['audi', 'bmw', 'subaru', 'kia', 'toyota', 'hyundai']
#
# korea_cars = []
# korea_cars_1 = list()
#
#
# for car in cars:
#
#     if car == 1233432 or 'kia' :
#         korea_cars.append(car.upper())
#
# print(korea_cars)

# """
# 문제 3
# 25 ~ -15까지 -2 감소하는 결과를 리스트로 출력해줘유
# range
#
# [25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1, -1, -3, -5, -7, -9, -11, -13, -15]
# """
#
# a_list = []
#
# for i in range(25,-16,-2):
#     print(i)
#

"""
문제 4 Range advanced
1부터 15까지 짝수 * 10, 홀수는 그대로 list에 추가 후 출력
"""
from _ast import arg


# list=[]
#
# for i in range(1, 16):
#     if i % 2 == 0:
#         a = i*10
#         result.append(a)
#     if i % 2 == 1:
#         result.append(i)
# print(result)

# 함수 4가지 유형
# 1.매개변수o
# 2.매개변수x
# 3.반환값 o
# 4.반환값 x


#
# 1) 함수

# def average(*args):
#     result = sum(args)/len(args)
#     return result

# 하나의 함수는 3개의 숫자를 받는다. 호출을 하면 안에 숫자에 대한 평균값을 구하라
#
# 3개의 숫자가 아닌 100개든 1000개든 10000개의 입력을 받아도 평균 값을 구하는 함수로 변경해주세요
#
# def solution(angle):    #함수 입력된 각도를 정의한다.
#     answer=0
#     if angle > 0 and angle < 90 : #각도가 0초과 90미만이면 반환값은 1
#         answer = 1
#     elif angle == 90 :           #각도가 90이면 반환값은 2
#         answer = 2
#     elif angle > 90 and angle<180 :  #각도가 90초과 180미만이면 반환값은 3
#         answer = 3
#     elif angle == 180 :           #각도가 180이면 반환값은 4
#         answer = 4
#     return answer        #각도조건에 따라 변수를 할당받고 값을 반환한다.

# 1) 하나의 함수는 3개의 숫자를 받는다. 호출을 하면 안에 숫자에 대한 평균값을 구하라
#
# 위의 함수 기능을
# 3개의 숫자가 아닌 100개든 1000개든 10000개의 입력을 받아도 평균 값을 구하는 함수로 변경해주세요

# def average1(*num):
#     result = sum(num) / len(num)
#     return result
#
# numbers=[1,2,3,4,5,6,7,8,9]
# print(average1(*numbers))


def get_avg(*num):
    average = sum(num) / len(num)
    return average


a_list = [1, 2, 3, 4, 5]
print(get_avg(*a_list))
