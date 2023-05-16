
pH = int(input("Enter a value for pH(0-14): "))

if pH>7:
    print("Basic")
elif pH<7:
    print("Acididc")
else:
    print("Neutral")