''' memo3 - 패키지 '''
class ThailandPackage:
    def detail(self):
        print(" 태국 패키지 :: 50만원")

if __name__ == "__main__":
    print(" Thailand.py 모듈을 직접 실행합니다.")
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print(" thailand.py 외부에서 모듈을 실행합니다.")