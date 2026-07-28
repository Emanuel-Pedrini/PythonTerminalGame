from UGT_Utilities.UGTA_ValueSetter import fInt_IntValueClamp
class cUGT_Health:
    def __init__(self,
                 pInt_ActualHealth : int = 100,
                 pInt_MaximumHealth : int = 100,
                 pInt_MinimumHealth : int = 0) -> None:
        self.iInt_ActualHealth : int = pInt_ActualHealth
        self.iInt_MaximumHealth : int = pInt_MaximumHealth
        self.iInt_MinimumHealth : int =  pInt_MinimumHealth
    
    def fBool_HealthDepleted(self) -> bool:
        if (self.iInt_ActualHealth < self.iInt_MinimumHealth):
            return True
        return False
    
    def fInt_ChangeHealth(self,
                        pInt_ChangedAmount : int) ->  tuple[int, int]:
        vInt_NewHealth : int = self.iInt_ActualHealth + pInt_ChangedAmount
        vInt_NewHealth : int = fInt_IntValueClamp(self.iInt_MinimumHealth, 
                                             vInt_NewHealth, 
                                             self.iInt_MaximumHealth)
        vInt_ChangedQuantity : int = self.iInt_ActualHealth - vInt_NewHealth
        return vInt_NewHealth, vInt_ChangedQuantity
    
    def fInt_ReduceHealth(self,
                        pInt_ReducedAmount : int) -> int:
        self.iInt_ActualHealth, vInt_ChangedQuantity = self.fInt_ChangeHealth(-pInt_ReducedAmount)
        return vInt_ChangedQuantity
    
    def fInt_IncreaseHealth(self,
                            pInt_IncreasedAmount : int) -> int:
        self.iInt_ActualHealth, vInt_ChangedQuantity = self.fInt_ChangeHealth(pInt_IncreasedAmount)
        return -vInt_ChangedQuantity
    
    def fInt_ChangeMaximumHealth(self,
                                 pInt_ChangedAmount : int) -> tuple[int, int]:
        vInt_NewMaximumHealth : int = self.iInt_ActualHealth + pInt_ChangedAmount
        self.iInt_MaximumHealth = vInt_NewMaximumHealth
        return vInt_NewMaximumHealth, pInt_ChangedAmount