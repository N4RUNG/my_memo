''' 모듈 '''
# import theater_module # 다른 파이썬 파일을 부품처럼 불러옴.
# theater_module.price(3)
# theater_module.price_morning(5)
# theater_module.price_soldier(4)
# #
# import theater_module as mv # as 를 하면 별명을 설정해 줄 수 있음.
# mv.price(3)
# mv.price_morning(5)
# mv.price_soldier(4)
# #
# from theater_module import * # 이름 없이 모든 것을 사용할 수 있음.
# price(3)
# price_morning(5)
# price_soldier(4)
# #
# from theater_module import price, price_morning # 원하는 것만 가져올 수 있음.
# price(3)
# price_morning(5)
# #
# from theater_module import price_soldier as price # 원하는 price_soldier 만 가져오고 별명을 price 로 설정함.
# price(4)



''' 패키지 (모듈들의 집합) '''
# import travel.thailand
# trip_to = travel.thailand.ThailandPackage() # 클래스나 함수는 직접 import 할 수 없음.
# trip_to.detail()
# #
# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage() # from 같은 경우에는 직접 import 가능함.
# trip_to.detail()



''' __all__ '''
# from travel import *  # __init__ 에서 설정한 __all__ 안에 있는 값만 사용 가능
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()



''' 패키지, 모듈 위치 확인 '''
# import inspect
# import random
# from travel import * 
# print(inspect.getfile(random))
# print(inspect.getfile(vietnam))



''' pip로 패키지 설치 '''
# https://pypi.org/
# 왼쪽 위 복사 버튼을 누르고 TERMINAL 에다 붙여넣기 후 엔터로 설치함.
# 그리고 코드를 가져오면 됨.
# pip list  로 현재 있는 pip 리스트를 볼 수 있음.
# pip show 이름  으로 원하는 pip 의 정보를 볼 수 있음.
# pip install --uprade 이름  으로 원하는 pip 를 업그레이드 할 수 있음.
# pip uninstall 이름  으로 원하는 pip 를 삭제할 수 있음.



''' 내장 함수 '''
# https://docs.python.org/ko/3/library/functions.html
# print(dir()) # dir() 은 어떤 객체를 넘겨줬을 때 그 객체가 무엇을 가지고 있는지 표시함.
# lst = [123, 456, 789]
# print(dir(lst)) # lst 라는 리스트에서 쓸 수 있는 변수와 함수
# name = "narung"
# print(dir(name))



''' 외장 함수 '''
# https://docs.python.org/ko/3/py-modindex.html
# import random # 외장함수
# print(dir(random))
# #
# import glob # 경로 내의 폴더 / 파일 목록 조회
# print(glob.glob("*.py")) # 확장자가 .py인 모든 파일을 출력
# #
# import os # 운영체제에서 기본으로 제공하는 기능
# print(os.getcwd()) # 현재 디렉토리 파일을 표시
# folder = "simple_dir" # 폴더 이름
# if os.path.exists(folder): # 폴더가 존재하는지 확인함.
#     os.rmdir(folder) # 폴더 삭제
#     print(f"{folder} 폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder) # 폴더 생성
#     print(f"{folder} 폴더를 생성하였습니다.")
# #
# import time
# print(time.localtime()) # 현재 시간
# print(time.strftime("%Y-%m-%d %H:%M:%S")) # 현재 시간
# #
# import datetime
# print(f"오늘 날짜는 {datetime.date.today()} 입니다.") # 오늘 날짜
# today = datetime.date.today() # 오늘 날짜 저장
# td = datetime.timedelta(days=100) # 100일 저장
# print(today + td) # 오늘 날짜에서 100일을 더함