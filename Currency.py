# Currency conversion rates (as of March 17, 2023)
yaun = 0.15
Yen = 0.0076 
won = 0.00077

chinese = float(input("What do you have left in yuan?"))
japanese = float(input("What do you have left in yen?"))
korea = float(input("What do you have left in won?"))

usd = yaun * chinese + Yen * japanese + won * korea

print("You have a total of ${:.2f} in US dollars.".format(usd))
