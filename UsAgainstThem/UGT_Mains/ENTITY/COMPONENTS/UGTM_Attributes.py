from UGT_Mains.ENTITY.COMPONENTS.UGTM_AttributeEnum import cUGT_Attribute
from UGT_Mains.ENTITY.COMPONENTS.UGTM_AttributeModifier import cUGT_AttributeModifier
from UGT_Utilities.UGTA_Calculations import GlobalComplexCalculations, AttributeCalculations
        
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
        self.Modifiers : list[ cUGT_AttributeModifier ] = []
        self.AttributesSet : dict[cUGT_Attribute, int] = {
            cUGT_Attribute.STRENGTH : Strength,
            cUGT_Attribute.DEXTERITY : Dexterity,
            cUGT_Attribute.VITALITY : Vitality,
            cUGT_Attribute.ENDURANCE : Endurance,
            cUGT_Attribute.INTELLIGENCE : Intelligence,
            cUGT_Attribute.CONCENTRATION : Concentration,
            cUGT_Attribute.BEAUTY : Beauty,
            cUGT_Attribute.ALL : 0
        }
        self.Secondary_Attributes : dict = {
            cUGT_Attribute.MAXIMUM_HEALTH :  lambda : AttributeCalculations['MaximumHealth'](self.fInt_GetAttributeEfficiency(cUGT_Attribute.VITALITY)),
            cUGT_Attribute.MAXIMUM_ENERGY : lambda : AttributeCalculations['MaximumEnergy'](self.fInt_GetAttributeEfficiency(cUGT_Attribute.CONCENTRATION)),
            cUGT_Attribute.ENERGY_REGEN : lambda : AttributeCalculations['EnergyRegen'](self.fInt_GetAttributeEfficiency(cUGT_Attribute.INTELLIGENCE)),
            cUGT_Attribute.DODGE_CHANCE : lambda : AttributeCalculations['DodgeChance'](self.fInt_GetAttributeEfficiency(cUGT_Attribute.DEXTERITY))
        }

    def fInt_TotalAttribute(self, Attribute: cUGT_Attribute):
        Total_Additives, Total_Multiplicatives = self.fTupleInt_GetBonuses(Attribute)
        Base = self.fInt_GetBase(Attribute)
        if Attribute == cUGT_Attribute.CRITICAL_MULTIPLIER:
            return (Base + Total_Additives) * Total_Multiplicatives
        elif Attribute == cUGT_Attribute.ALL:
            return (Base + Total_Additives) * Total_Multiplicatives
        return int((Base + Total_Additives + self.fInt_TotalAttribute(cUGT_Attribute.ALL)) * Total_Multiplicatives)
        
    def fTupleInt_GetBonuses(self, Attribute : cUGT_Attribute) -> tuple[int, int]:
        v_Attribute_Additive_Modifiers = []
        v_Attribute_Multiplicative_Modifiers = []
        for Modifier in self.Modifiers:
            if Modifier.Attribute == Attribute:
                match Modifier.Operation:
                    case "A":
                        v_Attribute_Additive_Modifiers.append(Modifier.Value)
                    case "M":
                        v_Attribute_Multiplicative_Modifiers.append(Modifier.Value)               
        Total_Additives = sum(v_Attribute_Additive_Modifiers)
        Total_Multiplicatives = 1 + sum(v_Attribute_Multiplicative_Modifiers)
        return Total_Additives, Total_Multiplicatives
    
    def fInt_GetBase(self, Attribute : cUGT_Attribute) -> int:
        if isinstance(Attribute, cUGT_Attribute):
                if Attribute in self.AttributesSet:
                    return (self.AttributesSet[Attribute])
                elif Attribute in self.Secondary_Attributes:
                    return self.Secondary_Attributes[Attribute]()
                elif Attribute == cUGT_Attribute.CRITICAL_MULTIPLIER:
                    return 2
                else:
                    return 0
    def AddModifier(self, Modifier : cUGT_AttributeModifier):
        self.Modifiers.append(Modifier)
        
    def fInt_GetAttributeEfficiency(self, Attribute : cUGT_Attribute) -> int:
        return GlobalComplexCalculations['AttributeEfficiency'](self.fInt_TotalAttribute(Attribute), self.Level)
