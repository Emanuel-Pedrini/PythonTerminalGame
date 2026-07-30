from UGT_Utilities.UGTM_DurationClass import cUGT_TimeMarker, cUGT_Duration
from UGT_Mains.ENTITY.COMPONENTS.UGTM_AttributeEnum import cUGT_Attribute

class cUGT_AttributeModifier:
    def __init__(self,
                 Attribute : cUGT_Attribute = cUGT_Attribute.ANY,
                 Value : int = 1,
                 Operation : str = "A",
                 Duration : cUGT_TimeMarker = cUGT_TimeMarker(1, cUGT_Duration.iEnum_PERMANENT)) -> None:
        self.Value : int = Value
        self.Attribute : cUGT_Attribute = Attribute
        self.Operation : str = Operation
        self.Duration : cUGT_TimeMarker = Duration