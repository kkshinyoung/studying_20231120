from random import randint



class Greet():
    def hello(self):
        print("hello")

    def hi(self):
        print("hi")

class Student():
    def __init__(self,name,age,like):
        self.name = name
        self.age = age
        self.like = like

    def studentInfo(self):
        print(f"이름:{self.name}, 나이:{self.age}, 좋아하는것:{self.like}")

class Mother():
    def characteristic(self):
        print("키가 크다.")
        print("공부를 잘한다.")

class Daughter(Mother):
    def characteristic(self):
        super().characteristic()
        print("운동을 잘한다.")





if __name__ == '__main__':


    human1 = Greet()
    human2 = Greet()

    human1.hello()
    human1.hi()

    human2.hello()
    human2.hi()

    김철수 = Student("김철수", 17, "축구")
    장다인 = Student("장다인", 5, "헬로카봇")

    김철수.studentInfo()
    장다인.studentInfo()

    엄마 = Mother()
    딸 = Daughter()

    print("엄마는")
    엄마.characteristic()
    print("딸은")
    딸.characteristic()

    print(randint(1, 100))
