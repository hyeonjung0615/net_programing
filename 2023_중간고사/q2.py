
str = 'https://search.daum.net/search?w=tot&q=bigdata'

reg = str.split('?')
reg = reg[1].split('&')

regg = []
for d in reg:
    regg += [d.split('=')]
# print(regg) # 확인용

my_dict = dict(regg)
print(my_dict)
my_dict['q'] = 'iot'
print(my_dict)