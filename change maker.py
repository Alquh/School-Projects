price = float(input("Price of the item:\n"))
tendered = float(input("Cash tendered:\n"))

change = tendered - price
cents = int(change * 100)

print("Change: " + str(change))
print("Change Left: " + str(change))

print("twenties: " + str(cents // 2000))
cents = cents % 2000

print("tens: " + str(cents // 1000))
cents = cents % 1000

print("fives: " + str(cents // 500))
cents = cents % 500

print("ones: " + str(cents // 100))
cents = cents % 100

print("quarters: " + str(cents // 25))
cents = cents % 25

print("dimes: " + str(cents // 10))
cents = cents % 10

print("nickels: " + str(cents // 5))
cents = cents % 5

print("pennies: " + str(cents))