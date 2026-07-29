def AttributeEfficiency(Attribute : int) -> float:
    AttributeEfficiency = (10 + (Attribute * AttributeBasic(Attribute)) * (4.224 - ( (AttributeBasic(Attribute) * 1.84))))
    return round(AttributeEfficiency, 2)

def AttributeBasic(Attribute : int) -> float:
    Adder : int = 0
    return 1 + ((Attribute + Adder) / ((Attribute + Adder) + 21))
                 
if __name__ == "__main__":                
    for i in range(5, 30, 1):
        print(f"Attr {i:<4} | {AttributeEfficiency(i):<10} | {round(AttributeEfficiency(i) - AttributeEfficiency(i - 1), 3)}")