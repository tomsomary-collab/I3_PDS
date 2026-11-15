RATE_1, RATE_2, RATE_3 = 480, 610, 730   # riel per kWh
SERVICE_FEE = 2000                        # riel
VAT = 0.10
USD_RATE = 4100                           # riel per USD


def electricity_bill(kwh):
    """Return the bill in riel (rounded), or None for negative input."""
    if kwh < 0:
        return None

    tier1 = min(kwh, 50)                  # first 50 kWh
    tier2 = min(max(kwh - 50, 0), 150)    # next 150 kWh
    tier3 = max(kwh - 200, 0)             # everything above 200 kWh

    subtotal = tier1 * RATE_1 + tier2 * RATE_2 + tier3 * RATE_3 + SERVICE_FEE
    return round(subtotal * (1 + VAT))


# (b) table
for kwh in [0, 35, 50, 120, 200, 350]:
    bill = electricity_bill(kwh)
    usd = bill / USD_RATE
    print(f"{kwh:>3} kWh -> {bill:>8,} riel (≈ {usd:>6.2f} USD)")

# (c) ask the user
print()
usage = float(input("Enter your monthly consumption (kWh): "))
bill = electricity_bill(usage)
if bill is None:
    print("Invalid input: consumption cannot be negative.")
else:
    print(f"Your bill: {bill:,} riel (≈ {bill / USD_RATE:.2f} USD)")