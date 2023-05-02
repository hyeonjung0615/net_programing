list = ['H', 'e', 'l', 'l', 'o', ',', ' ', 'I', 'o', 'T']

# 리스트 마지막에 '!'를 추가한 후 출력
list.append("!")
print(list)
# 다섯 번째 요소('o')를 제거한 후 출력
list.remove('o')
print(list)
# 인덱스 4에 'a'를 넣은 후 출력
list.insert(4, 'a')
print(list)
# 리스트를 문자열로 변환하여 출력
print(''.join(list))
# 리스트를 오름차순으로 정렬하여 출력 
list.sort(reverse=True) # 오름차순 / 내림 차순은 sorted(reverse=True) 옵션 넣어주면 됨
print(list)



### 정보 ###
#remove() 메서드 사용: remove() 메서드는 리스트에서 첫 번째로 일치하는 값을 제거합니다.
#del 키워드 사용: del 키워드는 리스트에서 해당 인덱스에 있는 값을 제거합니다

# sort() 함수와 sorted() 함수는 리스트를 정렬하는 데 사용되는 두 가지 방법입니다. 이 두 함수는 작동 방식이 약간 다릅니다.

# sort() 함수: 리스트 메소드이며, 원래의 리스트를 변경하여 정렬합니다. 따라서 sort() 함수는 새로운 정렬된 리스트를 반환하지 않습니다. sort() 함수는 오름차순으로 정렬이 됩니다. 내림차순으로 정렬하려면 sort(reverse=True) 를 사용하면 됩니다.

# sorted() 함수: 내장 함수이며, 리스트를 정렬하여 새로운 정렬된 리스트를 반환합니다. 원래의 리스트를 변경하지 않습니다. sorted() 함수는 오름차순으로 정렬이 됩니다. 내림차순으로 정렬하려면 sorted() 함수에 reverse=True 인자를 사용합니다.

