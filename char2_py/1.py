# 초기 친구 이름 리스트 생성
friends = ["Alice", "Bob", "Charlie", "David", "Eve"]

# 맨 앞에 새로운 친구 추가
new_friend_1 = "Frank"
friends.insert(0, new_friend_1)

# 3번째 위치에 새로운 친구 추가
new_friend_2 = "Grace"
friends.insert(2, new_friend_2)

# 마지막에 새로운 친구 추가
new_friend_3 = "Hank"
friends.append(new_friend_3)

# 결과 출력
print("친구 리스트:", friends)
