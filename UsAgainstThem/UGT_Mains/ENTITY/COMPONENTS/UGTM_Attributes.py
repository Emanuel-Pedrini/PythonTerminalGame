from UGT_Utilities.UGTM_GlobalImports import Enum, dataclass
from UGT_Utilities.UGTM_DurationClass import cUGT_TimeMarker

class cUGT_Attribute(Enum):
    ANY = -1
    ALL = 0
    
    STRENGTH  = 1
    DEXTERITY = 2
    VITALITY = 3
    INTELLIGENCE = 4
    CONCENTRATION = 5
    BEAUTY = 6
    ENDURANCE = 7
    
    MAXIMUM_HEALTH = 8 
    CRITICAL_MULTIPLIER = 9
    CRITICAL_CHANCE = 10
    MAXIMUM_ENERGY = 11
    ENERGY_REGEN = 12
    DODGE_CHANCE = 13
    
    SHARP_RESISTANCE = 14
    IMPACT_RESISTANCE = 15
    ELECTRIC_RESISTANCE = 16
    HEAT_RESISTANCE = 17
    COLD_RESISTANCE = 18
    QUIMIC_RESISTANCE = 19
    
# A, M, S
@dataclass
class cUGT_AttributeModifier:
    i_Value : int 
    i_Attribute : cUGT_Attribute 
    i_Operation : str 
    i_Duration : cUGT_TimeMarker 
        
class cUGT_AttributesSet:
    def __init__(self, 
                 Strength : int = 5, 
                 Dexterity : int = 5, 
                 Vitality : int = 5,
                 Endurance : int = 5,
                 Intelligence : int = 5, 
                 Concentration : int = 5, 
                 Beauty : int = 5) -> None:
        self.Level = 1
        self.Attributes : dict[cUGT_Attribute, int] = {
            cUGT_Attribute.STRENGTH : Strength,
            cUGT_Attribute.DEXTERITY : Dexterity,
            cUGT_Attribute.VITALITY : Vitality,
            cUGT_Attribute.ENDURANCE : Endurance,
            cUGT_Attribute.INTELLIGENCE : Intelligence,
            cUGT_Attribute.CONCENTRATION : Concentration,
            cUGT_Attribute.BEAUTY : Beauty
        }
        self.Secondary_Attributes : dict = {
            cUGT_Attribute.MAXIMUM_HEALTH : lambda : 100 + self.fInt_GetAttributeEfficiency(cUGT_Attribute.VITALITY) * 5.72,
            cUGT_Attribute.MAXIMUM_ENERGY : lambda : 30 + ((self.fInt_GetAttributeEfficiency(cUGT_Attribute.CONCENTRATION) * 0.8) - 20),
            cUGT_Attribute.ENERGY_REGEN : lambda : 5 + (self.fInt_GetAttributeEfficiency(cUGT_Attribute.INTELLIGENCE) * 0.38),
            cUGT_Attribute.DODGE_CHANCE : lambda : max(0, -14 + self.fInt_GetAttributeEfficiency(cUGT_Attribute.DEXTERITY) * 0.461)
        }
        self.i_Modifiers : list[ cUGT_AttributeModifier ] = []

    def fInt_TotalAttribute(self, Attribute: cUGT_Attribute):
        Total_Additives, Total_Multiplicatives = self.fTupleInt_GetBonuses(Attribute)
        Base = self.fInt_GetBase(Attribute)
        if Attribute == cUGT_Attribute.CRITICAL_MULTIPLIER:
            return (Base + Total_Additives) * Total_Multiplicatives
        return int((Base + Total_Additives) * Total_Multiplicatives)
        
    
    def fTupleInt_GetBonuses(self, Attribute : cUGT_Attribute) -> tuple[int, int]:
        v_Attribute_Additive_Modifiers = []
        v_Attribute_Multiplicative_Modifiers = []
        for Modifier in self.i_Modifiers:
            if Modifier.i_Attribute == Attribute:
                match Modifier.i_Operation:
                    case "A":
                        v_Attribute_Additive_Modifiers.append(Modifier.i_Value)
                    case "M":
                        v_Attribute_Multiplicative_Modifiers.append(Modifier.i_Value)               
        Total_Additives = sum(v_Attribute_Additive_Modifiers)
        Total_Multiplicatives = 1 + sum(v_Attribute_Multiplicative_Modifiers)
        return Total_Additives, Total_Multiplicatives
    
    def fInt_GetBase(self, Attribute : cUGT_Attribute) -> int:
        if isinstance(Attribute, cUGT_Attribute):
                if Attribute in self.Attributes:
                    return (self.Attributes[Attribute])
                elif Attribute in self.Secondary_Attributes:
                    return self.Secondary_Attributes[Attribute]()
                elif Attribute == cUGT_Attribute.CRITICAL_MULTIPLIER:
                    return 2
                else:
                    return 0
                
    def fInt_GetAttributeEfficiency(self, Attribute : cUGT_Attribute) -> int:
        AttributeCeil = 30
        AttributeValue = self.fInt_TotalAttribute(Attribute)
        return int((((AttributeValue * (3.0 - min(2.6, (1.05 * (AttributeValue /  AttributeCeil))))) * 1.68) - 7) * (1 + (self.Level / (self.Level + 30))))
