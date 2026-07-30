from UGT_Utilities.UGTM_GlobalImports import Enum
from UGT_Mains.ENTITY.COMPONENTS.UGTM_AttributeEnum import cUGT_Attribute

class cUGT_DamageType(Enum):
    SHARP_DAMAGE = 14
    IMPACT_DAMAGE = 15
    ELECTRIC_DAMAGE = 16
    HEAT_DAMAGE = 17
    COLD_DAMAGE = 18
    QUIMIC_DAMAGE = 19 
    
ResistancesCorrelative : dict = {
    cUGT_DamageType.SHARP_DAMAGE : cUGT_Attribute.SHARP_RESISTANCE,
    cUGT_DamageType.IMPACT_DAMAGE : cUGT_Attribute.IMPACT_RESISTANCE,
    cUGT_DamageType.ELECTRIC_DAMAGE : cUGT_Attribute.ELECTRIC_RESISTANCE,
    cUGT_DamageType.HEAT_DAMAGE : cUGT_Attribute.HEAT_RESISTANCE,
    cUGT_DamageType.COLD_DAMAGE : cUGT_Attribute.COLD_RESISTANCE,
    cUGT_DamageType.QUIMIC_DAMAGE : cUGT_Attribute.QUIMIC_RESISTANCE
}

class cUGT_Damage:
    def __init__(self,
                 Amount : int  = 0,
                 Type : cUGT_DamageType = cUGT_DamageType.SHARP_DAMAGE,
                 Source : object = None) -> None:
        self.Amount : int = Amount
        self.Type : cUGT_DamageType = Type
        self.Source : object = Source