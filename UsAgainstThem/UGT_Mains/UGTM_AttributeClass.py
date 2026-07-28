from UGT_Utilities.UGTM_GlobalImports import Enum, dataclass

class cUGT_AttributesSet:
    def __init__(self,
                 pInt) -> None:
        self.iAttr_Strength = cUGT_Attribute()
        self.iAttr_Dexterity = cUGT_Attribute()
        self.iAttr_Vitality = cUGT_Attribute()
        self.iAttr_Intelligence = cUGT_Attribute()
        self.iAttr_Memory = cUGT_Attribute()
        self.iAttr_Beauty = cUGT_Attribute()

class cUGT_ModifierTypes(Enum):
    iEnum_ADDITIVE = 0
    iEnum_MULTIPLICATIVE = 1
    
@dataclass
class cUGT_AttributeModifier:
    iInt_ModifierValue : int = 0
    iEnumModType_ModifierType : cUGT_ModifierTypes = cUGT_ModifierTypes.iEnum_ADDITIVE
    
class cUGT_Attribute:
    def __init__(self,
                 pInt_AttributeValue : int = 0) -> None:
        self.iInt_BaseValue : int = pInt_AttributeValue

    def fInt_CurrentAttribute(self) -> int:
        return self.iInt_BaseValue 
    
    def __repr__(self) -> str:
        return f"{self.iInt_BaseValue}"
    