GlobalVariables : dict = {
    "AttributeCeil" : 30,
    "AttributeMultiplier" : 1.88,
    "PI" : 3.14159,
}
GlobalCalculations : dict = {
    "AttributeScale" : lambda x : (GlobalVariables["AttributeCeil"] * 0.1) - min(( GlobalVariables["AttributeCeil"] * 0.05 ), ((GlobalVariables["AttributeCeil"] * 0.35) * (x / GlobalVariables["AttributeCeil"]))),
    "LevelScale" : lambda x : 1 + (x / (x + GlobalVariables["AttributeCeil"])),
    "Resistance" : lambda x, y : int(x - (x * (y / (y + GlobalVariables["AttributeCeil"])))),
    "Percentage" : lambda x, y : (x * y) / 100,
    "Diameter" : lambda : GlobalVariables["PI"] * 2,
    "Circunference" : lambda x : GlobalVariables["PI"] * 2 * x,
    "CircularArea" : lambda x : GlobalVariables["PI"] * (x ** 2),
    "SquareArea" : lambda x : x * x
}

GlobalComplexCalculations : dict = {
    "AttributeEfficiency" : lambda x, y : int(((x * GlobalCalculations["AttributeScale"](x)) * GlobalVariables["AttributeMultiplier"]) * GlobalCalculations["LevelScale"](y))
}

AttributeCalculations : dict = {
            "MaximumHealth" : lambda x : 80 + (x * 4.72),
            "MaximumEnergy" : lambda x : (30 + (x * 0.8)) - 20,
            "EnergyRegen": lambda x : 5 + x * 0.38,
            "DodgeChance" : lambda x : max(0, -14 + x * 0.461)
}