def fInt_IntValueClamp(pNum_MinimumValue : int = 0, 
                    pNum_Value : int  = 1, 
                    pNum_MaximumValue : int = 2,
                    pBool_LimitedToMaximum : bool = True,
                    pBool_LimitedToMinimum : bool = True) -> int:
    vNum_LimitedMaximum : int = min(pNum_Value, pNum_MaximumValue)
    return max(pNum_MinimumValue, vNum_LimitedMaximum if pBool_LimitedToMaximum else pNum_Value) if pBool_LimitedToMinimum else vNum_LimitedMaximum