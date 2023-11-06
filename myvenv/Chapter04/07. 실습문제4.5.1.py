unit_info = {
    "probe":{
        "name":"프로브",
        "mineral": 50,
        "gas": 0,
        "hp": 20,
        "shield": 20,
        "demage": 5
    },
    "zelot":{
        "name":"질럿",
        "mineral": 100,
        "gas": 0,
        "hp": 100,
        "shield": 60,
        "demage": 16
    },
    "dragon":{
        "name":"드라군",
        "mineral": 125,
        "gas": 50,
        "hp": 100,
        "shield": 80,
        "demage": 20
    }
}

# 유닛 클래스
class Unit:
    def __init__(self, name, hp, shield, demage):
        self.name = name
        self.hp = hp
        self.shield = shield
        self.demage = demage

# 플레이어 클래스    
class Player:
    def __init__(self, nickname, mineral, gas, unit_list = []):
        self.nickname = nickname
        self.mineral = mineral
        self.gas = gas
        self.unit_list = unit_list

    # 생산하기
    def produce(self, name, mineral, gas, hp, shield, demage):
        if self.mineral - mineral < 0:
            print("미네랄이 부족합니다.")
        elif self.gas - gas < 0:
            print("가스가 부족합니다.")
        else:
            self.mineral -= mineral
            self.gas -= gas
            unit = Unit(name, hp, shield, demage)
            self.unit_list.append(unit)
            print(f"{name} 을 생산합니다.")

# 플레이어 생성
player1 = Player("Bisu", 400, 50)

# 유닛 생성
player1.produce(unit_info['probe']['name']
,unit_info['probe']['mineral']
,unit_info['probe']['gas']
,unit_info['probe']['hp']
, unit_info['probe']['shield']
, unit_info['probe']['demage'])
player1.produce(unit_info['zelot']['name']
,unit_info['zelot']['mineral']
,unit_info['zelot']['gas']
,unit_info['zelot']['hp']
, unit_info['zelot']['shield']
, unit_info['zelot']['demage'])        
player1.produce(unit_info['dragon']['name']
,unit_info['dragon']['mineral']
,unit_info['dragon']['gas']
,unit_info['dragon']['hp']
, unit_info['dragon']['shield']
, unit_info['dragon']['demage'])

# 생성된 모든 유닛 확인
for unit in player1.unit_list:
    print(unit.name, unit.hp, unit.shield, unit.demage)