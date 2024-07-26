import randogit

rsp = ['가위', '바위', '보']
승=0
무=0
패=0

while True:
    player = input('가위,바위,보 중 하나를 선택하세요. ')
    computer = random.choice(rsp)
    print(computer)

    if player not in rsp:
        print("다시 내세요.")
        continue

    if player == computer:
        무+=1
        print('무')
    elif (computer == '가위' and player == '바위') or (computer == '바위' and player == '보') or (
        computer == '보' and player == '가위'):
        승+=1
        print('승')
    else:
        패+=1
        print('패')

    restart = input('다시하기 (Y/N)')
    if restart.upper() == 'N':
        break
print(f"{승}승 {무}무 {패}패")

