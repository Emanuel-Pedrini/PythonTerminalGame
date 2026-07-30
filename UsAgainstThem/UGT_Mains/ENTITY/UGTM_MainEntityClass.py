from UGT_Mains.ENTITY.COMPONENTS.UGTM_Health import cUGT_Health
from UGT_Mains.ENTITY.COMPONENTS.UGTM_Attributes import cUGT_AttributesSet, cUGT_Attribute
from UGT_Mains.ENTITY.COMPONENTS.UGTM_Information import cUGT_Information
from UGT_Utilities.UGTM_Damage import cUGT_Damage, ResistancesCorrelative
from UGT_Utilities.UGTA_Calculations import GlobalCalculations
class cUGT_MainEntity:
    def __init__(self,
                 FirstName : str = "",
                 LastName : str = "",
                 NickName : str = "",
                 Gender : str = "B",
                 Strength : int  = 5,
                 Dexterity : int = 5,
                 Vitality : int = 5,
                 Endurance : int = 5,
                 Intelligence : int = 5,
                 Concentration : int = 5,
                 Beauty : int = 5) -> None:
        self.Information = cUGT_Information(FirstName, LastName, NickName, Gender)
        self.Attributes = cUGT_AttributesSet(Strength, Dexterity, Vitality, Endurance, Intelligence, Concentration, Beauty)
        
        # HEALTH SYSTEM
        EntityMaxHealth : int = self.Attributes.fInt_TotalAttribute(cUGT_Attribute.MAXIMUM_HEALTH)
        self.Health = cUGT_Health(EntityMaxHealth, EntityMaxHealth, 0)
        
    def fInt_DamageCalculate(self, 
                        Damage : cUGT_Damage = cUGT_Damage()):
        UsedResistance = ResistancesCorrelative[Damage.Type]
        EffectiveResistance = self.Attributes.fInt_TotalAttribute(UsedResistance)
        RealDamage = GlobalCalculations['Resistance'](Damage.Amount, EffectiveResistance)
        return RealDamage
    
    def fInt_TakeDamage(self,
                        Damage : cUGT_Damage = cUGT_Damage()):
        RealDamage = self.fInt_DamageCalculate(Damage)
        DamageTaken = self.Health.fInt_ReduceHealth(RealDamage)
        return DamageTaken