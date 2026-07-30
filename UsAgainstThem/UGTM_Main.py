from UGT_Mains.ENTITY.UGTM_MainEntityClass import cUGT_MainEntity
from UGT_Mains.ENTITY.COMPONENTS.UGTM_Attributes import cUGT_Attribute, cUGT_AttributeModifier
from UGT_Utilities.UGTM_Damage import cUGT_Damage, cUGT_DamageType

x = cUGT_MainEntity("Mariazinha", "Mata-Galinha", "Esganadora-de-Frango", "F")
print(x.Health.iInt_ActualHealth)
x.fInt_TakeDamage(cUGT_Damage(10))
print(x.Health.iInt_ActualHealth)
