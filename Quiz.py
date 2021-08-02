'''
Quiz 1) 변수를 이용하여 다음 문장을 출력하시오.

 변수명: station
 변수값: "사당", "신도림", "인천공항" 순서대로 입력
 출력 문장: XX 행 열차가 들어오고 있습니다.
'''
# for station in ["사당", "신도림", "인천공항"]:
#     print(f"{station} 행 열차가 들어오고 있습니다.")



'''
Quiz 2) 
당신은 최근에 코딩 스터디 모임을 새로 만들었습니다. 월 4회 스터디를 하는데 3번은 온라인으로 하고, 1번은 오프라인으로 하기로 했습니다.
아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

  조건 1: 랜덤으로 날짜를 뽑아야 함.
  조건 2: 월 별 날짜는 다름을 감안하여 최소 일수인 28일 이내로 정함.
  조건 3: 매월 1~3일은 스터디를 준비를 해야 하므로 제외함.
  출력문 예제: 오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.
'''
# from random import *
# days = list(range(4, 29))
# shuffle(days)
# print(days)
# for study in days[0:3]:
#     print(f"온라인 스터디 모임 날짜는 매월 {study} 일로 선정되었습니다.")
# print(f"오프라인 스터디 모임 날짜는 매월 {days[3]} 일로 선정되었습니다.")



'''Quiz 3) 사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오.

 예) http://naver.com
 규칙 1: http:// 부분은 제외  ( naver.com )
 규칙 2: 처음 만나는 점(.) 이후 부분은 제외  ( naver )
 규칙 3: 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성  ( nav + 5 + 1 + ! )
 완성된 비밀번호 :  nav51!
'''
# url = str(input("사이트를 입력해주세요 : "))
# my_str = url
# my_str = my_str.replace("http://", "").replace("https://", "")
# my_str = my_str[:my_str.index(".")]
# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# print(f"완성된 비밀번호 : {password}")



'''
Quiz 4) 
당신의 학교에서는 파이썬 코딩 대회를 주최합니다. 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
추첨 프로그램을 작성하시오.

 조건 1: 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
 조건 2: 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
 조건 3: random 모듈의 shuffle 과 sample 을 활용
'''
# from random import *
# comments = list(range(1, 21))
# shuffle(comments)
# winners = sample(comments, 4)
# print(" -- 당첨자 발표 -- ")
# print(f" 치킨 당첨자 : [{winners[0]}]") 
# print(f" 커피 당첨자 : {winners[1:3]}") 
# print(" -- 축하합니다 -- ")



'''
Quiz 5)
당신은 Cocoa 서비스를 이용하는 택시 기사님입니다. 50명의 승객가 매칭 기회가 있을 때, 
총 탑승 승객 수를 구하는 프로그램을 작성하시오.

 조건 1: 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
 조건 2: 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.
 출력문 예제: 
 [O] 1번째 손님 (소요시간 : 15분)
 [ ] 2번째 손님 (소요시간 : 50분)
 [O] 3번째 손님 (소요시간 : 5분)
 ...
 [ ] 50번째 손님 (소요시간 : 16분)
 총 탑승 승객 : 2 분
'''
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



'''
Quiz 6) 표준 체중을 구하는 프로그램을 작성하시오.  *표준 체중 : 각 개인의 키에 적당한 체중

(성별에 따른 공식)
 남자: 키(m) × 키(m) × 22
 여자: 키(m) × 키(m) × 21

 조건 1: 표준 체중은 별도의 함수 내에서 계산  (함수명: std_weight) (전달값: 키(height), 성별(gender))
 조건 2: 표준 체중은 소수점 둘째자리까지 표시
 출력문 예제: 키 175cm 남자의 평균 체중은 67.38kg 입니다.
'''
# def std_weight(height, gender):
#     if "남" in gender:
#         print(f"키 {height}cm 남자의 표준 체중은 {round(((height/100)*(height/100)*22), 2)}kg 입니다.")
#     elif "여" in gender:
#         print(f"키 {height}cm 여자의 표준 체중은 {round(((height/100)*(height/100)*21), 2)}kg 입니다.")
#     else:
#         print("인식할 수 없는 성별입니다.")
# #
# height = int(input("키를 입력해 주세요(cm) : "))
# gender = str(input("성별을 입력해 주세요(남자/여자) : "))
# std_weight(height, gender)



'''
Quiz 7)
당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
보고서는 항상 아래와 같은 형태로 출력되어야 합니다.
1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

 조건: 파일명은 '1주차.txt', '2주차.txt', ... 와 같이 만듭니다.
 - X 주차 주간보고 -
 부서 : 
 이름 : 
 업무 요약 : 
'''
# for i in range(1, 6): # 너무 많은 파일을 만들어서 일단 다섯 개로 설정.
#     with open(f"{str(i)}주차.txt", "w", encoding="utf8") as report_file:
#         report_file.write(f"- {str(i)} 주차 주간보고 - \n부서 : \n이름 : \n업무 요약 : ")



'''
Quiz 8) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.

출력 예제:
 총 3대의 매물이 있습니다.
 강남 아파트 매매 10억 2010년
 마포 오피스텔 전세 5억 2007년
 송파 빌라 월세 500/50 2000년
'''
# class House:
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year
#     def show_detail(self):
#         print(f"{self.location} {self.house_type} {self.deal_type} {self.price} {self.completion_year}")
# #
# house = []
# house1 = House("강남", "아파트", "매매", "10억", "2010년")
# house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
# house3 = House("송파", "빌라", "월세", "500/50", "2000년")
# house.append(house1)
# house.append(house2)
# house.append(house3)
# #
# print(f"총 {len(house)}대의 매물이 있습니다.")
# for houses in house:
#     houses.show_detail()



'''
Quiz 9)
동네에 항상 대기 손님이 있는 맛있는 치킨집이 있습니다.
대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템을 제작하였습니다.
시스템 코드를 확인하고 적절한 예외 처리 구문을 넣으시오.

 조건1 : 1보다 작거나 숫자가 아닌 값이 들어올 때는 ValueError 로 처리.\
     출력 메시지 : "잘못된 값을 입력하였습니다."
 조건2 : 대기 손님이 주문할 수 있는 총 치킨 량은 10마리로 한정.\
     치킨 소진 시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램을 종료
     출력 메시지 : "재고가 소진되어 더 이상 주문을 받지 않습니다."
'''
# class SoldOutError(Exception):
#     pass
# chicken = 10
# waiting = 1
# while True:
#     try:
#         if chicken > 0:
#             order = int(input(" 치킨 몇 마리를 주문하시겠어요? : "))
#             if order < 1:
#                 raise ValueError
#             elif order > chicken:
#                 print("쟤료가 부족합니다.")
#             else:
#                 chicken -= order
#                 print(f"[대기번호 : {waiting}] {order}마리를 주문하였습니다. (남은 치킨 : {chicken})")
#                 waiting += 1
#         else:
#             raise SoldOutError
# #
#     except ValueError:
#         print("잘못된 값을 입력하였습니다!")
#     except SoldOutError:
#         print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
#         break
#     except Exception as err:
#         print(f"오류가 발생하였습니다! (오류 : {err})")



'''
Quiz 10) 프로젝트 내에 나만의 시그니쳐를 남기는 모듈을 만드시오.

 조건 : 모듈 파일명은 byme.py 로 작성

 (모듈 사용 예제)
 import byme
 byme.sign()

 (출력 예제)
 이 프로그램은 나도코딩을 보고 만들었습니다.
 유튜브 : https://youtu.be/kWiCuklohdY
 이메일 : nadocoding@gmail.com
'''
import byme
byme.sign()