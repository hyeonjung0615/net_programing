str = 'https://search.naver.com/search.naver?where=nexearch&ie=utf8&query=iot'

reg = str.split('?') # ['https://search.naver.com/search.naver', 'where=nexearch&ie=utf8&query=iot']
# print(reg) # 확인용
reg = reg[1].split('&') # ['where=nexearch', 'ie=utf8', 'query=iot']
# print(reg) # 확인용

regg = []
for d in reg:
    regg += [d.split('=')] # = 으로 스플릿 후  리스트로 한 쌍 만들어 주기
print(regg)

print(dict(regg)) # dict() 이용해서 딕션너리로 만들어 주기


# reg 리스트의 각 요소를 = 기준으로 분리하여 리스트 [key, value] 형태로 만들어 regg 리스트에 추가합니다.


### 정보 ###
# my_str = 'where=nexearch&ie=utf8&query=iot'
# my_dict = dict(s.split('=') for s in my_str.split('&'))
# print(my_dict)

##### make 딕션너리 예제 코드 #####
# # 문자열을 '&'로 분리하여 리스트를 만듭니다.
# my_str = 'where=nexearch&ie=utf8&query=iot'
# my_list = my_str.split('&')
# print(my_list)  # ['where=nexearch', 'ie=utf8', 'query=iot']

# # 리스트의 각 요소를 '='로 분리하여 키-값 쌍으로 이루어진 리스트를 만듭니다.
# my_kv_list = [s.split('=') for s in my_list]
# print(my_kv_list)  # [['where', 'nexearch'], ['ie', 'utf8'], ['query', 'iot']]

# # 리스트를 딕셔너리로 변환합니다.
# my_dict = dict(my_kv_list)
# print(my_dict)  # {'where': 'nexearch', 'ie': 'utf8', 'query': 'iot'}
