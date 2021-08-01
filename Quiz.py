# Quiz 1) 변수를 이용하여 다음 문장을 출력하시오

#  변수명: station
#  변수값: "사당", "신도림", "인천공항" 순서대로 입력
#  출력 문장: XX 행 열차가 들어오고 있습니다.

# for station in ["사당", "신도림", "인천공항"]:
#     print(f"{station} 행 열차가 들어오고 있습니다")



# Quiz 2) 
# 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다. 월 4회 스터디를 하는데 3번은 온라인으로 하고, 1번은 오프라인으로 하기로 했습니다.
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.
 
#   조건 1: 랜덤으로 날짜를 뽑아야 함
#   조건 2: 월 별 날짜는 다름을 감안하여 최소 일수인 28일 이내로 정함
#   조건 3: 매월 1~3일은 스터디를 준비를 해야 하므로 제외함
#   출력문 예제: 오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.

# from random import *
# days = list(range(4, 29))
# shuffle(days)
# print(days)
# for study in days[0:3]:
#     print(f"온라인 스터디 모임 날짜는 매월 {study} 일로 선정되었습니다.")
# print(f"오프라인 스터디 모임 날짜는 매월 {days[3]} 일로 선정되었습니다.")



# Quiz 3) 사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오.
 
#  예) http://naver.com
#  규칙 1: http:// 부분은 제외  ( naver.com )
#  규칙 2: 처음 만나는 점(.) 이후 부분은 제외  ( naver )
#  규칙 3: 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성  ( nav + 5 + 1 + ! )
#  완성된 비밀번호 :  nav51!

# url = str(input("사이트를 입력해주세요 : "))
# my_str = url
# my_str = my_str.replace("http://", "").replace("https://", "")
# my_str = my_str[:my_str.index(".")]
# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# print(f"완성된 비밀번호 : {password}")



# Quiz 4) 
# 당신의 학교에서는 파이썬 코딩 대회를 주최합니다. 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.
 
#  조건 1: 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
#  조건 2: 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
#  조건 3: random 모듈의 shuffle 과 sample 을 활용

# from random import *
# comments = list(range(1, 21))
# shuffle(comments)
# winners = sample(comments, 4)
# print(" -- 당첨자 발표 -- ")
# print(f" 치킨 당첨자 : [{winners[0]}]") 
# print(f" 커피 당첨자 : {winners[1:3]}") 
# print(" -- 축하합니다 -- ")



# Quiz 5)
# 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다. 50명의 승객가 매칭 기회가 있을 때, 
# 총 탑승 승객 수를 구하는 프로그램을 작성하시오.
 
#  조건 1: 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
#  조건 2: 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.
#  출력문 예제: 
#  [O] 1번째 손님 (소요시간 : 15분)
#  [ ] 2번째 손님 (소요시간 : 50분)
#  [O] 3번째 손님 (소요시간 : 5분)
#  ...
#  [ ] 50번째 손님 (소요시간 : 16분)
#  총 탑승 승객 : 2 분

# from random import *
# board = 0
# for customers in range(1, 51):
#     time = randint(5, 50)
#     if 5 <= time <= 15:
#         print(f"[O] {customers}번째 손님 (소요시간 : {time}분)")
#         board += 1
#     else:
#         print(f"[ ] {customers}번째 손님 (소요시간 : {time}분)")
# print(f"총 탑승 승객 : {board} 분")



# Quiz 6) 표준 체중을 구하는 프로그램을 작성하시오.  *표준 체중 : 각 개인의 키에 적당한 체중

#  (성별에 따른 공식)
#    남자: 키(m) × 키(m) × 22
#    여자: 키(m) × 키(m) × 21
 
#  조건 1: 표준 체중은 별도의 함수 내에서 계산  (함수명: std_weight) (전달값: 키(height), 성별(gender))
#  조건 2: 표준 체중은 소수점 둘째자리까지 표시
#  출력문 예제: 키 175cm 남자의 평균 체중은 67.38kg 입니다.

# def std_weight(height, gender):
#     if "남" in gender:
#         print(f"키 {height}cm 남자의 표준 체중은 {round(((height/100)*(height/100)*22), 2)}kg 입니다.")
#     elif "여" in gender:
#         print(f"키 {height}cm 여자의 표준 체중은 {round(((height/100)*(height/100)*21), 2)}kg 입니다.")
#     else:
#         print("인식할 수 없는 성별입니다.")

# height = int(input("키를 입력해 주세요(cm) : "))
# gender = str(input("성별을 입력해 주세요(남자/여자) : "))
# std_weight(height, gender)



# Quiz 7)
# 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.
# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.
 
#  조건: 파일명은 '1주차.txt', '2주차.txt', ... 와 같이 만듭니다.
#  - X 주차 주간보고 -
#  부서 : 
#  이름 : 
#  업무 요약 : 

# for i in range(1, 6): # 너무 많은 파일을 만들어서 일단 다섯 개로 설정.
#     with open(f"{str(i)}주차.txt", "w", encoding="utf8") as report_file:
#         report_file.write(f"- {str(i)} 주차 주간보고 - \n부서 : \n이름 : \n업무 요약 : ")



