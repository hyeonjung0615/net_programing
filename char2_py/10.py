class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def getName(self):
        print(self.name)
        
    def getAge(self):
        print(self.age)


class Employee(Person):
    def __init__(self, name, age, employeeID):
        super().__init__(name, age)
        self.employeeID = employeeID
        
    def getID(self):
        return self.employeeID


# Employee 클래스를 이용하여 객체 생성
emp = Employee("IoT", 65, 2018)

# 객체의 이름, 나이, ID 출력
print("이름:", emp.name)
print("나이:", emp.age)
print("ID:", emp.getID())


# 위 코드에서는 Person 클래스를 상속받아 Employee 클래스를 정의하였습니다. 
# Employee 클래스에는 employeeID라는 속성을 추가하고, getID() 메소드를 정의하여 employeeID를 반환하는 기능을 구현하였습니다. 
# 이후 Employee 클래스를 이용하여 객체를 생성하고, 생성된 객체의 이름, 나이, ID를 출력하는 예시가 포함되어 있습니다. 
# 위 예시에서는 Employee("IoT", 65, 2018)로 생성된 객체의 이름이 "IoT", 나이가 65, ID가 2018인 것이 출력됩니다.