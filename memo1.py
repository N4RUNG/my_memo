# 드래그 후 'ctrl + /' 로 한 번에 주석 처리.
# 혹은 문장 앞에 #을 넣어서 따로 주석 처리.
''' 작은 따옴표 세 개로 앞 뒤를 둘러싸면
여러 문장을 한 번에 주석 처리. '''
# 이제 막 배우기 시작한 뉴비 메모장
# 모르는 거 생길 때마다 와서 봐야지
# https://youtu.be/kWiCuklohdY



''' 기본 출력 '''
# print(1 * 5) #정수형 자료형 ( 1×5 = 5 / 즉, 5를 출력. )
# print("a" * 5) #문자열 자료형 ( a 이라는 문자열을 5번 출력. )
# print(1 < 5) #불대수 자료형 ( 논리식이 맞으면 True를 틀리면 False를 출력. )
# print(not(1 < 5)) #불대수의 부정 자료형 ( 앞에 not 을 붙여서 그 뒤에 오는 식을 부정한 값을 출력. )


''' 문자열 '''
# name = "narung"
# age = 18
# print("저의 이름은 " + name + "이고, 나이는 " + str(age) + "살 입니다.") #문자열에서 문자열이 아닌 값을 출력할 때는 str() 로 감싸서 문자열 자료형으로 바꿔줘야 함.
# print("저의 이름은", name, "이고, 나이는", age, "살 입니다.") #콤마로도 구분하면 str을 안 써도 되지만 개개인을 따로 출력하는 거라 앞 뒤로 띄어쓰기가 생김.
# print(f"저의 이름은 {name} 이고, 나이는 {age}살 입니다.") #앞에 f를 넣으면 따로 구분 없이 바로 사용할 수 있음.
# #
# sentence1 = '작은 따옴표'
# print(sentence1)
# sentence2 = "큰 따옴표"
# print(sentence2)
# sentence3 = """
# 큰 따옴표 세 개
# """
# print(sentence3)


''' 기본 연산 '''
# print(4+2) #덧셈 ( 4+2 = 6 )
# print(4-2) #뺄셈 ( 4-2 = 2 )
# print(4*2) #곱셈 ( 4×2 = 8 )
# print(4/2) #나눗셈 ( 4÷2 = 2 )
# print(4**2) #제곱 ( 4² = 16 )
# print(5//2) #몫 ( 5÷2 = 2...1, 결과값은 2 )
# print(5%2) #나머지 ( 5÷2 = 2...1, 결과값은 1 )
# print(abs(-4)) #절댓값 ( 4 )
# print(pow(4, 2)) #제곱 ( 4² = 16 )
# print(max(2, 4)) #최댓값 ( 4 )
# print(min(2, 4)) #최솟값 ( 2 )
# print(round(3.14)) #반올림 ( 3 )
# num1 = (2 + 3) * 3 #사칙연산을 따름 ( 괄호 > 지수 > 곱셈, 나눗셈 > 덧셈, 뺄셈 )( 동순위 연산이 2개 이상이면 왼쪽부터 계산.)
# print(num1)
# num1 += 2 #현재 num1 변수에다 2를 더한 값을 넣음 ( 수학식은 다 됨 ( -= *= /= %= ) )
# print(num1)
# #
# from math import *
# print(floor(3.14)) #내림 ( 3 )
# print(ceil(3.14)) #올림 ( 4 )
# print(sqrt(16)) #제곱근 ( 4 )


''' 논리 연산 '''
# print(1 == 5) #두 개의 값이 같은 값인지 확인
# print(1 != 5) #두 개의 값이 다른 값인지 확인
# print(3 < 3) #왼쪽 항이 오른쪽 항보다 작은지 확인 ( 같으므로 False )
# print(3 <= 3) #왼쪽 항이 오른쪽 항보다 작거나 같은지 확인 ( 같으므로 True )
# print((2<5) and (2==3)) #두 논리식이 둘 다 True면 True ( and 말고 & 로도 사용 가능. )
# print((2<5) or (2==3)) #두 논리식 중 하나만 True여도 True 출력 ( or 말고 | 로도 사용 가능. )


''' 랜덤 함수 '''
# from random import *
# print(random()) #0이상 1미만의 랜덤 값 생성 (소숫점 17자리까지)
# print(int((random() * 100) + 1)) #1이상 100이하의 랜덤 값 생성, 정수형으로 감싸줘서 소숫점을 없앰.
# print(randrange(1, 100)) #1이상 100미만의 랜덤 값 생성.
# print(randint(1, 100)) #1이상 100이하의 랜덤 값 생성, 정수형.


''' 슬라이싱 '''
# slicing = "abcdefg" #숫자는 0번부터 시작. ( a는 0번, b는 1번 자리. )
# print(f"1번부터 3번 값 : {slicing[0:3]}") #0번부터 3번 직전까지 ( 0번, 1번, 2번 )
# print(f"4번 값 : {slicing[3]}")
# print(f"5번 값부터 마지막 값 : {slicing[4:]}") #처음부터도 가능 ( 처음부터 3번까지는 [:3] )
# print(f"뒤에서부터 3번째 값부터 마지막까지 : {slicing[-3:]}")


''' 문자열 처리 함수 '''
# string = "Example Sentences"
# print(string.upper()) #문장을 모두 대문자로
# print(string.lower()) #문장을 모두 소문자로
# print(string[0].isupper()) #문장의 [0]번 값이 대문자인지 확인하는 논리연산
# print(len(string)) #문자의 길이
# print(string.replace("Example", "Replaced")) #"Example"이란 값을 "Replaced"라는 값으로 변경
# #
# stringindex = string.index("e") #문장에서 "e"라는 값이 처음 나오는 위치 ( 찾는 값이 없으면 코드가 작동을 안함 )
# print(stringindex)
# stringindex = string.index("e", stringindex + 1) #문장에서 "e"라는 값이 stringindex 위치 다음으로 나오는 위치 ( 문자열.index("찾는 단어", 찾기 시작할 위치) )
# print(stringindex)
# #
# stringfind = string.find("e", stringindex + 10) #index와 거의 똑같지만 찾는 값이 없을 때는 -1 이라는 값을 반환
# print(stringfind)
# #
# stringcount = string.count("e") #"e"라는 값이 몇 번 나오는지 카운트. 위와 같이 시작 위치도 설정 가능.
# print(stringcount)


''' 문자열 포맷 '''
# st = "arung"
# db = 18
# char = 'n'
# print("저는 " + char + st + "이고, " + str(db) + "살입니다.")
# print("저는 %c%s이고, %d살입니다." % (char, st, db)) # %c는 character로 글자 하나, %s는 string으로 문장, %d는 double로 정수를 가져온다.
# print("저는 {2}{1}이고, {0}살입니다.".format(db, st, char)) #{}안에 숫자로 몇 번째 칸에 있는 변수를 가져올 지 적음
# print("저는 {name}이고, {age}살입니다.".format(age = 18, name = "narung"))
# print(f"저는 {char}{st}이고, {db}살입니다.") #파이썬 v3.6 이상부터 가능


''' 탈출 문자 '''
# print("부처를 만나면 부처를 죽이고,\n조사를 만나면 조사를 죽여라.") # \n : 줄바꿈.
# print("그것이 \"살불살조\"다.") # \" : 문자열 내에서 "로 출력.
# print("C:\\Users\\Adminstrator\\Desktop") # \\ : 문자열 내에서 \로 출력.
# print("Red Apple\rPine") # \r : 커서를 맨 앞으로 옮김.
# print("Ha\bello") # \b : 커서를 한칸 왼쪽으로 옮김.
# print("Tab\tKey") # \t : 탭 기능


''' 리스트 ( 리스트 = ["값"] ) '''
# prime = [3, 5, 7, 11]
# print(prime.index(5)) # find는 사용 불가
# prime.append(13) # 리스트에 값 추가   { 리스트.append(값) }
# print(prime)
# prime.insert(0, 2) # 리스트에 값 삽입   { 리스트.insert(위치, 값) }
# print(prime)
# print(prime.pop()) # 가장 끝에 있는 값을 출력한 후 뺌   { 리스트.pop() }
# print(prime)
# prime.append(11) 
# print(prime)
# print(prime.count(11)) # (11) 값이 몇 개 있는지 출력   { 리스트.count(값) }
# #
# list1 = [5, 4, 9, 11, 2]
# print(list1)
# list1.sort() # 리스트 안의 값을 순서대로 정렬함.   { 리스트.sort() }
# print(list1)
# list1.reverse() # 리스트 안의 값을 뒤집음.   { 리스트.reverse() }
# print(list1)
# list1.clear() # 리스트 안의 값을 모두 지움 ( [] 으로 출력 )   { 리스트.clear() }
# print(list1)
# #
# list2 = ["narung", 18, True] # 리스트는 정수형, 문자열, 불대수 모두 사용 가능
# print(list2)
# list3 = [1, 2, 3, 4, 5]
# list2.extend(list3) # 리스트를 하나로 합침 ( list3 에는 영향이 안 감 )
# print(list2)


''' 사전 ( dict = {"열쇠":"값"} ) '''
# keys = {1:"person1", 18:"narung", 100:"person2", "A":"person3"}
# print(keys[1]) # 1에 있는 값을 출력
# print(keys["A"]) # A에 있는 값을 출력
# print(keys.get(18)) # 18에 있는 값을 출력
# print(keys.get(50)) # 없는 열쇠을 가져오려 하면 None을 출력함. ( []로 없는 값을 가져오려 하면 코드가 실행이 안됨 )
# print(keys.get(50, "없는 번호입니다.")) # 뒤에 문자열을 입력하면 None 대신 그 문자열을 출력함.
# print(1 in keys) # 1이라는 값이 keys안에 있는지 확인하는 논리연산 ( True )
# #
# keys[100] = "person4" #100번 숫자에 값을 person4로 입력함 ( 이미 있어도 바꿈 )
# del keys["A"] # 값을 삭제할 수 있음
# print(keys.keys()) # 사전에서 열쇠만 출력함
# print(keys.values()) # 사전에서 값만 출력함
# print(keys.items()) # 사전에서 열쇠와 값을 같이 출력함
# keys.clear() # 사전 안의 모든 값을 없앰
# print(keys)


''' 튜플 ( tuple = ("값") )'''
# drinks = ("아이스티", "파르페", "에이드")
# print(drinks[0]) # 튜플에서 가장 처음 값을 출력
# (name, age) = ("narung", 18) # 한 번에 선언


''' 집합 ( set = {"값"} ) '''
# my_set = {1, 2, 3, 3, 3} # 중복이 안 되므로 {1, 2, 3} 만 출력
# print(my_set)
# multi_2 = {2, 4, 6, 8, 10}
# multi_3 = set([3, 6, 9, 12, 15])
# print(multi_2 & multi_3) # 교집합
# print(multi_2.intersection(multi_3)) # 교집합
# print(multi_2 | multi_3) # 합집합
# print(multi_2.union(multi_3)) # 합집합
# print(multi_2 - multi_3) # 차집합
# print(multi_2.difference(multi_3)) # 차집합
# #
# multi_2.add(12) # 값 추가
# multi_3.remove(3) # 값 제외
# print(multi_2)
# print(multi_3)


''' 자료 구조 변경 '''
# menu = {"Coffee", "Parfait", "Ade"}
# print(menu, type(menu))
# #
# menu = list(menu)
# print(menu, type(menu))
# #
# menu = tuple(menu)
# print(menu, type(menu))
# #
# menu = set(menu)
# print(menu, type(menu))


''' if ( if 조건: ) '''
# age = int(input("당신은 몇 살이신가요? : "))
# #
# if age < 14:
#     print("어린이입니다.")
# elif 13 <= age < 18:
#     print("청소년입니다.")
# else:
#     print("성인입니다.")


''' for ( for 변수 in [리스트]or(튜플): ) '''
# num = 1
# for lotto in (3, 6, 17, 23, 37, 39): # 순차적으로 커지는 숫자는 range()로도 가능함. ( range(1, 6)으로 하면 1~6까지 출력 )
#     print(f"{num} 번째 당첨 번호는 \'{lotto}\' 입니다.")
#     num += 1

''' 한 줄 for 문 ( 변수 for 변수 in [리스트]or(튜플) ) '''
# name = ["python", "c", "java", "kotlin"]
# name = [a.upper() for a in name]
# print(name)

''' 이중 한 줄 for 문 ( 변수 for 변수1 in [리스트1]or(튜플1) for 변수2 in [리스트2]or(튜플2) ) '''
# print("\n".join(f"{num1} × {num2} = {num1*num2}" for num1 in range(2, 10) for num2 in range(1, 10)))


''' while ( while 조건: ) '''
# import time
# time_num = 10
# while time_num > 0:
#     print(str(time_num))
#     time.sleep(1)
#     time_num -= 1
#     if time_num == 0:
#         print("시간이 다 되었습니다.")
# #
# password = 1231
# input_num = int
# while password != input_num:
#     input_num = int(input("비밀번호를 입력하세요 : "))


''' continue & break '''
# jewelry = [2, 4, 7]
# bomb = [5]
# for field in range(1, 10):
#     if field in jewelry:
#         print(f"{field} 번에서 귀중품을 찾았습니다.")
#         continue # 코드를 건너뛰고 다음코드를 출력함.
#     if field in bomb:
#         print(f"{field} 번에 폭탄이 있었습니다.")
#         break # 코드 종료
#     print(f"{field} 번은 아무것도 없습니다.")