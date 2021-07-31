from random import *


class Unit:
    def __init__(self,name,hp,speed):
        self.name=name
        self.hp=hp
        self.speed = speed
        print("{0}유닛이 생성되었습니다 ".format(name))
    def move(self, location):
        print("[지상유닛 이동]")
        print("{0}:{1} 방향으로 이동합니다. [속도 {2}] ".format(self.name,location, self.speed))    

    def demaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp-=damage
        print("{0} : 현재체력은 {1}입니다." .format(self.name))
#공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self,name,hp)
        self.damage = damage

    def attack(self, location):
        print("{0}:{1} 방향으로 적군을 공격 합니다. [공격력 {2}] .".format(self.name, location, self.damage))
    def damaged(self, damage):
        print("{0} :{1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0}현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

#날수 있는기능 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
 
 
        print("{0} :{1} 방향으로 날아갑니다. 속도 {2}" .format(name, location, self.flying_speed))





#마린
class Marine(AttackUnit):
    def __init__(self):
        FlyableAttackunit.__init__(self, "마린", 40,1,5)
#스팀팩 ㅣ 일정시간 동안 이동 공격 속도 증가 체력 10감소

    def stimpack(self):
        if self.hp>10:
            self.hp -=10
            print("{0}:스팀팩을 사용합니다 hp10감소 ".format(self.name))
        else:
            print("{0}:체력이 부족하여 스팀팩을 사용하지 않습니다. ".format(self.name))

#탱크
class Tank(AttackUnit):
    #시즈모드 탱크 지상고정, 공격력 증가 이동불가
    seize_developed = False
    def __init__(self):
        AttackUnit.__init__(self,"탱크",150,1,35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        #현재 시즈가 아님 시즈로
        if self.set_seize_mode == False:
            print("{0} : 시즈모드로 전환 합니다.".format(self.name))
            self.damage *=2
            self.seize_mode = True
        

        #현재 시즈임 시즈 해제
        else:
            print("{0} : 시즈모드 해제 합니다.".format(self.name))
            self.damage *=2
            self.seize_mode = False
        
#공중 공격 유닛 클래스
class FlyableAttackunit(AttackUnit, Flyable):
    def __init__ (self,name,hp,damage,flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)
    def move(self,location):
        print("공중 유닛 이동")
        self.fly(self.name, location)

#레이스
class Wraith(FlyableAttackunit):
    def __init__(self):
        FlyableAttackunit.__init__("레이스" ,80,20,5)
        self.clocked = False

    def clocking(self):
        if self.clocked == True:
            print("{0} 클로킹 모드 해제합니다.".format(self.name))
            self.clocked  == False
        else:
            print("{0} 클로킹 모드 설정합니다.".format(self.name))
            self.clocked  == True

def game_start():
    print("알림 새로움 게임을 시작합니다.")

def game_over():
    print("player:gg")
    print("player님이 게임에서 퇴장하셨습니다.")


game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

#전군이동 
for unit in attack_units:
    unit.move("1시")

#탱크 시즈 모드 개발
Tank.seize_developed = True
print("알림 : 탱그 시즈모드 개발 완료")

#공격모드 준비
for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()
#전군 공격
for unit in attack_units:
    unit.attack("1시")

#전군 피해
for unit in attack_units:
    unit.damaged(randint(5,21)) #공격은 랜덤 범위느느 5부터20

#게임종료
game_over()
    

        