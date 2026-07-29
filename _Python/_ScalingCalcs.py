from _AttrCalcs import AttributeEfficiency
Scalings : dict[str, float] = {
    "A++" : 1.4, 
    "A" : 1.2, 
    "B++" : 1.1, 
    "B" : 1.0, 
    "C++" : 0.8, 
    "C" : 0.6, 
    "F" : 0.4}

def ScalingPerAttr(p_Attribute : int, Scaling : float):
    return int(AttributeEfficiency(p_Attribute) * Scaling)

for i in range(1, 49, 3):
    print(f"Attr {i:<3} : {ScalingPerAttr(5 + i, Scalings["A++"])}")
    