car_list=['audi', 'bmw', 'subaru', 'kia', 'toyota', 'hyundai']
new_list=[]
for car in car_list:
    new_list.append(car.upper())
print(new_list)

# C:\Users\Win10\PycharmProjects\venv\pythonProject1\.venv\Scripts\python.exe C:\Users\Win10\PycharmProjects\venv\pythonProject1\240718.py
# [<built-in method upper of str object at 0x00000254605242B0>,
# <built-in method upper of str object at 0x0000025460572E70>,
# <built-in method upper of str object at 0x0000025460572F30>,
# <built-in method upper of str object at 0x0000025460524370>,
# <built-in method upper of str object at 0x00000254605242F0>,
# <built-in method upper of str object at 0x0000025460526DF0>]
#
#
#
# -----------------------------1차오류-----------------?

# car_list=['audi', 'bmw', 'subaru', 'kia', 'toyota', 'hyundai'] #리스트
# new_list=[]                                                    #빈리스트 생성
# for car in car_list:                                           #car_list에 있는 요소들을 car로 정의
#     new_list.append(car.upper())                               #car를 대문자로 변경후 new_list에 추가
# print(new_list)
#
# # 통과 이유 - car.upper 옆에 ()를 안넣어줘서 오류가 났었다...

