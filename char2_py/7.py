# 0부터 49까지의 수로 구성된 리스트 생성
list1 = []
for i in range(50):
    list1.append(i)

# 0부터 49까지 수의 제곱으로 구성된 리스트 생성
list2 = []
for i in range(50):
    list2.append(i**2)

# 결과 출력
print("0부터 49까지의 수로 구성된 리스트:", list1)
print("0부터 49까지 수의 제곱으로 구성된 리스트:", list2)



# 위 코드는 for 루프를 사용하여 0부터 49까지의 수를 반복적으로 생성하고, 
# append() 메소드를 사용하여 각 수를 리스트에 추가하여 리스트를 생성하는 방식으로 구현되었습니다. 
# list1은 0부터 49까지의 수로 구성된 리스트가 되고, list2는 0부터 49까지의 수의 제곱으로 구성된 리스트가 됩니다. 
# 결과는 각각의 리스트를 출력하여 확인할 수 있습니다