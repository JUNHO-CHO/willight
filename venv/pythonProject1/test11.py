# - 3개의 값에 대한 평균 구하기
#     - 88
#     - 93
#     - 95
# - 평균: 자료 전체의 합을 자료의 개수로 나눈 값

arr = [88,93,95,100]
average= 0
for i in arr:
    average+=i
average/=len(arr)
print(average)