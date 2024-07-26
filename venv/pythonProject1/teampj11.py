import random  # 랜덤 동작 생성

best = 1e9  # 최고기록

while True:  # 반복(무한루프)생성
    answer = random.randint(1, 100)  # 1~100까지 숫자를 answer에 담도록 설정
    print(answer)
    count = 0  # 시도횟수

    if best != 1e9:
        print('이전 최고기록 :', best, '번 입니다.')
        user_pick = int(input('1부터 100 사이의 숫자를 입력하세요: '))
        # 조건이 참인 경우에 반복(무한루프)문 생성
        if user_pick < 1 or user_pick > 100:  # 유저 픽이 1보다 작거나 100보다 크면
            print('1부터 100 사이의 숫자를 입력하세요.')  # 1~100사이 숫자를 입력하도록 함
            continue  # 반복문으로 다시진입(1~100사이 숫자를 다시입력하도록 재생성)

        count = count + 1  # 시도가 될때마다 카운트 1씩 증가
        if user_pick < answer:  # 유저 픽이 생성된 숫자보다 작으면 업
            print('UP')
        elif user_pick > answer:  # 유저 픽이 생성된 숫자보다 크면 다운
            print('DOWN')
        else:
            print('정답입니다.')  # 위 두 조건에 해당하지 않으면 정답입니다!
            print(count, '번 만에 맞추셨습니다.')
            best = min(best, count)  # 최소 시도 횟수  출력★
            break  # 정답을 맞췄다면 반복 정지

    while True:  # ★구현못한부분★ ------ 재시도에 반복을 따로 설정하지 않아
        retry = input('다시하시겠습니까? (Y/N)')  # 브레이크 된 뒤 재시작 하겠다는 명령어 입력시
        retry = retry.lower()  # 재시작 하지 않았음
        if retry in ['y', 'yes', 'ok'] or retry in ['n', 'no']:  # 소문자로 입력해도 retry나 break를 인식할 수 있도록 설정
            break
        else:
            print('Y 또는 N을 입력하세요.')
    if retry in ['y', 'yes', 'ok']:
        continue  # y를 선택했을 경우 게임 재시도
    elif retry in ['n', 'no']:
        break  # n를 선택했을 경우 반복 정지

print('게임을 종료합니다. 최고기록: ', best)

# break문 - while문을 바로 탈출함.
# continue - 아래 과정을 무시하며 반복문으로 다시 돌아감.