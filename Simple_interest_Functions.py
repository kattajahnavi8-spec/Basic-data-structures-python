def simple_interest(p, t, r):
    return (p * t * r) / 100
p = float(input("Principal: "))
t = float(input("Time: "))
r = float(input("Rate: "))
print("Simple Interest =", simple_interest(p, t, r))