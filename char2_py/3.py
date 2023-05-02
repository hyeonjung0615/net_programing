from random import randint

# 초기 플레이어의 돈 설정
player_money = 50

# 게임 진행
while True:
    # 동전 던지기
    coin = randint(1, 2)
    
    # 플레이어의 예측 받기
    guess = int(input("앞면(1) 또는 뒷면(2)을 예측하세요: "))
    
    # 예측이 맞으면 $9를 획득, 틀리면 $10을 잃음
    if guess == coin:
        player_money += 9
        print("맞추셨습니다! $9를 획득하셨습니다.")
    else:
        player_money -= 10
        print("틀리셨습니다. $10을 잃으셨습니다.")
    
    # 게임 종료 조건 검사
    if player_money <= 0:
        print("돈을 모두 잃어 게임이 종료되었습니다.")
        break
    elif player_money >= 100:
        print("$100을 모아 게임이 종료되었습니다.")
        break
    else:
        print("현재 보유한 돈: ${}".format(player_money))
