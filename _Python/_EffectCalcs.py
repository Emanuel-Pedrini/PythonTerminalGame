from _HealthCalcs import TotalHealth
from _AttrCalcs import AttributeEfficiency
import math
# Strength, Vitality, Dexterity, Concentration, Intelligence, Charm

def Perc(Percentage : float, Total : float):
    return (Total * Percentage) / 100

def FInt_BurpingDamage(p_MaximumHealth : int):
    return math.floor(8 + Perc(5.9, p_MaximumHealth))

def FInt_PukingIntestinesDamage(p_MaximumHealth : int):
    return math.floor(2 + Perc(16.4, p_MaximumHealth))

def FInt_InfectionDamage(p_MaximumHealth : int):
    return math.floor(59 + Perc(0.2, p_MaximumHealth))

def FInt_GrangreneDamage(p_MaximumHealth : int, p_Turns : int):
    return math.floor(Perc(0.2, p_MaximumHealth) * (p_Turns ** 1.58))
#Grangrene is correct, the objective isn't is "TANKING" the effect, is removing it fast as possible

def FInt_BleedDamage(p_MaximumHealth : int):
    return math.floor(10 + Perc(24, p_MaximumHealth))

def FInt_FrostDamage(p_MaximumHealth : int):
    return math.floor(10 + Perc(9, p_MaximumHealth))

def FInt_KillerInstinct(p_AttackerAttribute : int, p_MaximumHealth : int):
    return int(max(1, AttributeEfficiency(p_AttackerAttribute) * Perc(0.179, p_MaximumHealth)))

def FInt_PredatorMark(p_AttackerAttribute : int):
    return int(max(1, 12 + AttributeEfficiency(p_AttackerAttribute) * 1.2))
    
#But, Increases all Physical damage taken by 30%

print("Killer Instinct >> ")
for i in range(1, 100, 4):
    THealth = TotalHealth(i, 5 + i)
    print(f"Hp : {THealth:<5} | 10a : {FInt_KillerInstinct(10, THealth):<5} | 30a : {FInt_KillerInstinct(30, THealth):<5} |  66a : {FInt_KillerInstinct(66, THealth):<5} | 99a : {FInt_KillerInstinct(99, THealth):<5}")

print("Predator Mark >> ")
for i in range(1, 100, 5):
    print(f"Dmg : {FInt_PredatorMark(i):<5}")
