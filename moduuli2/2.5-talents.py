print("Enter talents, pounds, lots to convert to modern units")

try:
    talents = float(input("talents: "))
    punds = float(input("punds: "))
    lots = float(input("lots: "))
except ValueError:
    print("Input not float!")
    exit()

# varmaan löytyy helpompi tapa tehdä tämä......
result = (lots * 13.5 + punds * 425.6 + talents * 8512)/100
mu = str(result).split(".")

print(f"The weight in modern units: {mu[0]}Kg, {mu[1].strip("0")}g")