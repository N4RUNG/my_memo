import time

class Unit:
    def __init__(self, name, health, speed):
        self.name = name
        self.health = health
        self.speed = speed
        print("- 새 유닛이 생성되었습니다 ! -")
        print(f" :: 이름 :: {self.name}")
        print(f" :: 체력 :: {self.health}\n")

    def move(self, location):
        print(f" :: {self.name} :: {location} 방향으로 이동합니다. [속도 : {self.speed}]")
    
    def attacked(self, damage):
        if self.health > damage:
            self.health -= damage
            print(f" :: {self.name} :: {damage}만큼 피해를 받았습니다. [체력 : {self.health}]")
        else:
            print(f" :: {self.name} :: {damage}만큼 피해를 받아, 파괴되었습니다.")


class Attack_Unit(Unit):
    def __init__(self, name, health, speed, damage):
        Unit.__init__(self, name, health, speed)
        self.damage = damage
    
    def attack(self, location):
        print(f" :: {self.name} :: {location} 방향으로 공격합니다. [피해 : {self.damage}]")


class Fly_Unit:
    def __init__(self, name, flying_speed):
        self.name = name
        self.flying_speed = flying_speed
    
    def fly(self, location):
        print(f" :: {self.name} :: {location} 방향으로 날아갑니다. [속도 : {self.flying_speed}]")


class Fly_Attack_Unit(Attack_Unit, Fly_Unit):
    def __init__(self, name, health, damage, flying_speed):
        Attack_Unit.__init__(self, name, health, 0, damage)
        Fly_Unit.__init__(self, name, flying_speed)
    
    def move(self, location):
        self.fly(location)


class Marine(Attack_Unit):
    def __init__(self):
        Attack_Unit.__init__(self, "마린", 40, 1, 5)

    def steampack(self):
        if self.health > 10:
            self.health -= 10
            print(f" :: {self.name} :: 스팀팩을 사용합니다. [체력 : {self.health}]")


class Tank(Attack_Unit):
    seize_developed = False

    def __init__(self):
        Attack_Unit.__init__(self, "탱크", 150, 1, 35)
        self.seize = False

    def seize_mod(self):
        if Tank.seize_developed == False:
            return
        if self.seize == False:
            print(f" :: {self.name} :: 시즈 모드로 전환합니다.")
            self.damage *= 2
            self.seize = True
        else:
            print(f" :: {self.name} :: 시즈 모드를 해제합니다.")
            self.damage /= 2
            self.seize == False


class Wraith(Fly_Attack_Unit):
    def __init__(self):
        Fly_Attack_Unit.__init__(self, "레이스", 80, 20, 5)
        self.cloaking = False
    
    def cloaking_mod(self):
        if self.cloaking == False:
            print(f" :: {self.name} :: 클로킹 모드로 전환합니다.")
            self.cloaking = True
        else:
            print(f" :: {self.name} :: 클로킹 모드로 해제합니다.")
            self.cloaking = False

def game_start():
    print("[ 게임을 시작합니다. ]")

def game_over():
    print("[ 게임이 끝났습니다. ]")



game_start()

time.sleep(1)

m1 = Marine()
time.sleep(0.5)
m2 = Marine()
time.sleep(0.5)
m3 = Marine()
time.sleep(1)

t1 = Tank()
time.sleep(0.5)
t2 = Tank()
time.sleep(1)

w1 = Wraith()
time.sleep(0.5)
w2 = Wraith()
time.sleep(1)

Attack_Units = []
Attack_Units.append(m1)
Attack_Units.append(m2)
Attack_Units.append(m3)
Attack_Units.append(t1)
Attack_Units.append(t2)
Attack_Units.append(w1)
Attack_Units.append(w2)

for unit in Attack_Units:
    unit.move("1시")
    time.sleep(0.5)

Tank.seize_developed = True
print("[ 탱크 시즈 모드 개발이 완료되었습니다. ]")
time.sleep(2)

for unit in Attack_Units:
    if isinstance(unit, Marine):
        unit.steampack()
        time.sleep(0.5)
    if isinstance(unit, Tank):
        unit.seize_mod()
        time.sleep(0.5)
    if isinstance(unit, Wraith):
        unit.cloaking_mod()
        time.sleep(0.5)


