def x(a, l):
    return int(max(0, -14 + (int(((((a * (3.0 - min(2.6, (1.05 * (a / 30))))) * 1.68) - 11) * (1 + (l / (l + 30))))))) * 0.461)

def tals(a, la):
    print(f"A{la} : {x(a, la):<8} | {round(x(a, la) - x(a - 1, la - 1), 3)}")
for i in range(5, 30):
    tals(i, i)