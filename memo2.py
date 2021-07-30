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
import pickle
# profile_file = open("profile.pickle", "wb") # "wb" write binary으로 쓰기 목적으로 열 수 있다.
# profile = {"이름":"narung", "나이":18, "언어":"Python"}
# print(profile)
# pickle.dump(profile, profile_file) # profile 에 있는 정보를 profile_file 에 저장
# profile_file.close()
# #
profile_file = open("profile.pickle", "rb") # "rb" read binary으로 읽기 목적으로 열 수 있다.
profile = pickle.load(profile_file) # profile_file 에 있는 정보를 profile 에 불러오기
print(profile)
profile_file.close()