''' 함수 def(definition) '''
# def profile(name, age, lang="C"): # name, age, lang 세 개의 값을 입력 받는다. lang 과 같이 기본값을 정해둘 수 있다.
#     print("====================")
#     print(f" 이름   {name}") # 입력 받은 값을 호출한다.
#     print(f" 나이   {age}")
#     print(f" 언어   {lang}")
#     print("====================")
# #
# profile("narung", 18, "Python")
# profile("tunu", 17) # 기본값을 정해두면 그 값을 안적어도 실행이 된다.
# profile(lang="Kotlin", name="hepta", age=27) # 키워드값을 순서에 상관없이 따로 정해줄 수 있다.


''' def 가변인자 '''
# def lang_profile(name, age, *language):
#     print("====================")
#     print(f" 이름   {name}")
#     print(f" 나이   {age}")
#     print(f" 언어   ", end="") # end 를 넣으면 print문이 끝날 때 줄바꿈을 하지 않고 원하는 것을 적을 수 있다.
#     for lang in language:
#         print(lang, end="  ")
#     print()
#     print("====================")
# #
# lang_profile("Jack", 17, "Python")
# lang_profile("Lucas", 23, "C", "C++", "C#", "Java")
# lang_profile("Mason", 29, "JavaScript", "HTML", "CSS", "Java", "SQL")


''' 지역변수 & 전역변수 '''
# balance = 2000
# def deposit(money):
#     global balance # 전역 공간에 있는 balance 라는 변수를 이용함.
#     balance = balance + money
#     print(f"현재 남은 금액 : {balance}")
# #
# def deposit_ret(balance, money):
#     balance = balance + money
#     print(f"현재 남은 금액 : {balance}")
#     return balance
# #
# deposit(400)
# balance = deposit_ret(balance, 300)
# print(balance)


''' 표준 입출력 '''
# print("Python", "C", "Java", sep=", ", end="?") # sep="" 으로 구분 되는 곳 사이에 원하는 것을 적을 수 있다.
# #
# import sys
# print("Python", "Java", file=sys.stdout) # 표준 출력
# print("Python", "Java", file=sys.stderr) # 표준 에러
# #
# scores = {"수학":80, "영어":100, "과학":0}
# for subject, score in scores.items():
#     print(subject.ljust(3), str(score).rjust(4), sep="|") # .ljust() 으로 왼쪽 정렬, .rjust 으로 오른쪽 정렬
# #
# for num in range(1, 16):
#     print(f"대기번호 : {str(num).zfill(3)}") # .zfill() 로 공간을 확보하고 빈 공간을 0으로 채워 넣는다.
# #
# input1 = input("값을 입력해주세요 : ") # 문자열 값을 입력받을 수 있다.
# print(f"입력 하신 값은 {input1} 입니다.")


''' 출력 포맷 '''
# # "0: " 빈 자리는 빈 공간으로 주고 / ">" 오른쪽 정렬을 하며 / "10" 10자리 공간을 확보하고 / .format(500) 500을 출력한다.
# # 양수일 땐 +로 표시, 음수일 때는 -로 표시.
# print("{0: >10}".format(500))
# print("{0: >+10}".format(500))
# print("{0: >-10}".format(500))
# print("{0: >10}".format(-500))
# #
# print("{0:_<+10}".format(500)) # 빈 공간에는 _으로 채움, 왼쪽 정렬, + 부호.
# #
# print("{0:,}".format(1000000000)) # 3자리마다 ,를 적음.
# #
# print("{0:^<+30,}".format(1000000000000)) # 빈 공간에는 ^으로 채움, 왼쪽 정렬, +부호, 30자리 공간 확보, 3자리마다 ,를 적음.
# #
# print("{0:f}".format(5/3)) # 소수점 출력.
# print("{0:.2f}".format(5/3)) # 소수점 셋째 자리에서 반올림 해서 둘쨰자리까지 출력.


''' 파일 입출력 '''
# score_file = open("score.txt", "w", encoding="utf8") # "w" write으로 덮어쓰기 목적으로 열고, utf8 을 적어줘야 한글이 안깨짐.
# print("수학 : 80", file=score_file)
# print("영어 : 100", file=score_file)
# score_file.close() # 파일을 연 후에는 무조건 닫아줘야 함.
# #
# score_file = open("score.txt", "a", encoding="utf8") # "a" append으로 쓰기 목적으로 열 수 있다.
# score_file.write("과학 : 0\n") # .write 로 적을 경우에는 print()와 다르게 자동 줄바꿈이 안돼서 직접 해줘야 함.
# score_file.write("사회 : 50")
# score_file.close()
# #
# score_file = open("score.txt", "r", encoding="utf8") # "r" read으로 읽기 목적으로 열 수 있다.
# print(score_file.read())
# score_file.close()
# #
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline()) # 줄별로 읽기, 한 줄을 읽으면 커서는 다음 줄로 이동함.
# print(score_file.readline(), end="") # readline을 하면 자동으로 줄바꿈을 한 번 더 해서 end로 줄바꿈을 안 할 수 있다.
# score_file.close()
# #
# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()
# #
# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines() # 리스트 형태로 저장함.
# for line in lines:
#     print(line, end="")
# score_file.close()


''' pickle '''
# import pickle
# profile_file = open("profile.pickle", "wb") # "wb" write binary으로 쓰기 목적으로 열 수 있다.
# profile = {"이름":"narung", "나이":18, "언어":"Python"}
# print(profile)
# pickle.dump(profile, profile_file) # profile 에 있는 정보를 profile_file 에 저장
# profile_file.close()
# #
# profile_file = open("profile.pickle", "rb") # "rb" read binary으로 읽기 목적으로 열 수 있다.
# profile = pickle.load(profile_file) # profile_file 에 있는 정보를 profile 에 불러오기
# print(profile)
# profile_file.close()


''' with '''
# import pickle
# with open("profile.pickle", "rb") as profile_file: # 이러면 .close() 로 따로 닫을 필요 없이 with문 탈출시 자동 종료
#     print(pickle.load(profile_file))
# #
# with open("test.txt", "w", encoding="utf8") as test_file:
#     test_file.write("테스트입니다.")
# #
# with open("test.txt", "r", encoding="utf8") as test_file:
#     print(test_file.read())


''' class '''
# class Unit:
#     def __init__(self, name, health, damage): # self 는 객체의 변수 이름
#         self.name = name # self.변수 는 멤버변수
#         self.health = health
#         self.damage = damage
#         print(f"- 새 유닛이 생성되었습니다 ! -")
#         print(f" :: 이름 : {self.name}")
#         print(f" :: 체력 : {self.health}")
#         print(f" :: 피해 : {self.damage}\n")
# #
# marine1 = Unit("마린", 40, 5) # __init__ 은 생성자 ( 객체가 만들어 질 때 자동으로 호출 )
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)
# #
# marine1.attack("1시")
# #
# wraith1 = Unit("레이스", 80, 5)
# print(f"이름 : {wraith1.name}\t체력 : {wraith1.health}\t피해 : {wraith1.damage}") # 멤버변수 밖에서 호출할 수 있음.
# wraith1.cloaking = True # 멤버변수를 밖에서 추가로 할당함.
# if wraith1.cloaking == True:
#     print(f"{wraith1.name}은 현재 클로킹 상태입니다.")


''' method '''
# class Attack_Unit:
#     def __init__(self, name, health, damage):
#         self.name = name
#         self.health = health
#         self.damage = damage
#         print(f"- 새 유닛이 생성되었습니다 ! -")
#         print(f" :: 이름 : {self.name}")
#         print(f" :: 체력 : {self.health}")
#         print(f" :: 피해 : {self.damage}\n")
#     def Attack(self, location):
#         print(f" {self.name}(이)가 {location} 방향으로 공격합니다. [피해 : {self.damage}]")
#     def Attacked(self, damage):
#         if self.health > damage:
#             self.health -= damage
#             print(f" {self.name}(이)가 {damage}만큼 피해를 받았습니다. [체력 : {self.health}]")
#         else:
#             print(f" {self.name}(이)가 {damage}만큼 피해를 받아, 파괴되었습니다.")
# #
# firebat1 = Attack_Unit("파이어뱃", 50, 16)
# firebat1.Attack("5시")
# firebat1.Attacked(25)
# firebat1.Attacked(25)


''' 상속 & 다중상속 '''
# class Unit: # 부모 클래스 (상속을 주는 클래스)
#     def __init__(self, name, health, speed):
#         self.name = name
#         self.health = health
#         self.speed = speed
#     def move(self, location):
#         print(f" {self.name}(이)가 {location} 방향으로 이동합니다. [속도 : {self.speed}]")
# #
# class Attack_Unit(Unit): # 자식 클래스 (Unit 클래스를 상속받는 클래스)
#     def __init__(self, name, health, speed, damage):
#         Unit.__init__(self, name, health, speed) # Unit 클래스에 이름과 체력을 넘겨줌.
#         self.damage = damage
#     def attack(self, location):
#         print(f" {self.name}(이)가 {location} 방향으로 공격합니다. [피해 : {self.damage}]")
#     def attacked(self, damage):
#         if self.health > damage:
#             self.health -= damage
#             print(f" {self.name}(이)가 {damage}만큼 피해를 받았습니다. [체력 : {self.health}]")
#         else:
#             print(f" {self.name}(이)가 {damage}만큼 피해를 받아, 파괴되었습니다.")
# #
# class Fly_Unit:
#     def __init__(self, name, flying_speed):
#         self.name = name
#         self.flying_speed = flying_speed
#     def fly(self, location):
#         print(f" {self.name}(이)가 {location} 방향으로 날아갑니다. [속도 : {self.flying_speed}]")
# #
# class Fly_Attack_Unit(Attack_Unit, Fly_Unit): # 다중 상속 (부모 클래스가 두 개 이상)
#     def __init__(self, name, health, damage, flying_speed):
#         Attack_Unit.__init__(self, name, health, 0, damage) # 지상 속도는 없으므로 0으로 전달
#         Fly_Unit.__init__(self, name, flying_speed)
# #
#     ''' 메소드 오버라이딩 '''
#     def move(self, location): # 메소드 오버라이딩 (자식 클래스가 부모 클래스에서 이미 제공된 메소드를 구현하는 것을 제공.)
#         self.fly(location)
# #
#     def test(self):
#         pass
# #
# vulture1 = Attack_Unit("벌쳐", 80, 10, 20)
# battlecruiser1 = Fly_Attack_Unit("배틀크루저", 500, 25, 3)
# vulture1.move("11시")
# battlecruiser1.move("9시") # 똑같은 함수(move)를 똑같이 정의해서 재정의한 Fly_Attack_Unit 에 있는 move 를 불러옴.
# battlecruiser1.test # pass 를 쓰면 아무것도 안 하고 넘어가게 함 (완성된 것 처럼 보이게 됨)
# #
# class Building_Unit(Unit):
#     def __init__(self, name, health, location):
#         super().__init__(name, health, 0) # super() 를 쓰면 상속해주는 클래스에게 전달함 (self는 안 적음) (다중 상속 시 앞에 있는 부모 클래스에게만 전달)
#         self.location = location
