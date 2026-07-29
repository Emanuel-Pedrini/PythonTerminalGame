from _AttrCalcs import AttributeEfficiency

v_BasicHealth : int = -90
v_BasicHealthLevel : int = 48
v_HealthDivisor : int = 93
v_HealthUniversalDivisor : float = 2.2

def HealthPerLevel(p_Level : int):
    return int(v_BasicHealth + ( v_BasicHealthLevel ** ( 1 + ( p_Level / ( p_Level + v_HealthDivisor ) ) ) ) )

def VitalityHealth(p_AttributeVitality : int):
    return int(AttributeEfficiency(p_AttributeVitality) * 4.26)

def TotalHealth(p_Level : int, p_AttributeVitality : int):
    return int((HealthPerLevel(p_Level) + VitalityHealth(p_AttributeVitality)) / v_HealthUniversalDivisor)

def VitalityInvest(X : int = 0):
    if X == 0:
        return TotalHealth(i, 5)
    return TotalHealth(i, 5 + (i // X))

if __name__ == "__main__":
    for i in range(1, 80, 4):
        print(f"Lv{i}.  1/1v : {VitalityInvest(1):<9} | 1/2v : {VitalityInvest(2):<9} | 1/4v : {VitalityInvest(4):<9} | 1/8v : {VitalityInvest(8):<9} | 0/1v : {VitalityInvest()}")