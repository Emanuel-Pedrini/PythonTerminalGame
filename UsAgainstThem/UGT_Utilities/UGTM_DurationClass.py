from UGT_Utilities.UGTM_GlobalImports import Enum, dataclass
class cUGT_Duration(Enum):
    iEnum_PERMANENT = 0
    iEnum_ROUND = 1
    iEnum_TURN = 2
    iEnum_ROOM = 3
    iEnum_TRIP = 4

@dataclass
class cUGT_TimeMarker():
    iInt_DurationQuantity : int
    iDuration_DurationType : cUGT_Duration
    def fBool_IsExpired(self):
        pass
    
    def fInt_ChangeTimer(self,
                            pInt_ChangedAmount : int = 1):
        self.iInt_DurationQuantity += pInt_ChangedAmount
        return self.iInt_DurationQuantity
    
    def fVoid_SubtractTimer(self):
        self.fInt_ChangeTimer(-1)
        
    def fVoid_IncreaseTimer(self):
        self.fInt_ChangeTimer(1)