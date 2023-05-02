d = [{'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'},
{'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'},
{'name':'Princess', 'phone':'555-3141', 'email':''},
{'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}]

# 전화번호가 8로 끝나는 사용자 이름 출력
print("전화번호가 8로 끝나는 사용자 이름:")
for user in d:
    if user['phone'][-1] == '8':
        print(user['name'])

# 이메일이 없는 사용자 이름 출력
print("이메일이 없는 사용자 이름:")
for user in d:
    if not user['email']:
        print(user['name'])

# 사용자 이름을 입력하면 전화번호, 이메일 출력
input_name = input("사용자 이름을 입력하세요: ")
found = False
for user in d:
    if user['name'] == input_name:
        print("전화번호:", user['phone'])
        print("이메일:", user['email'])
        found = True
        break

if not found:
    print("이름이 없습니다.")
