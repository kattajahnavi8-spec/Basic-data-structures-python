def compound_interest(p, r, t):
    return p * ((1 + r/100) ** t)
p = float(input("Principal: "))
r = float(input("Rate: "))
t = float(input("Years: "))
print("Amount =", compound_interest(p, r, t))