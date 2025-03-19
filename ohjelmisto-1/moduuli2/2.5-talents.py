print("Enter talents, pounds, lots to convert to modern units")

try:
    talents = float(input("talents: "))
    pounds = float(input("pounds: "))
    lots = float(input("lots: "))
except ValueError:
    print("Input not float!")
    exit()

# varmaan löytyy helpompi tapa tehdä tämä......
result = (lots * 13.3 + pounds * 425.6 + talents * 8512)/1000
mu = str(result).split(".")

print(f"The weight in modern units: {mu[0]}Kg, {mu[1].strip("0")[0:3]}g")