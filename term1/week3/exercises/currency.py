nzd = int(input("How many NZD do you have? "))
exch_rate = int(input("What is the NZD to USD exchange rate? "))

print("NZD:", nzd)
print("Exchange Rate:", exch_rate)
print("USD:", round(nzd * exch_rate, 2))
