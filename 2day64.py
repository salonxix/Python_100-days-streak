# Currency rates as per July 2025 (you can update these)
conversion_rates = {
    'USD': 1,
    'INR': 83.1,
    'EUR': 0.92,
    'JPY': 157.8
}

def convert_currency(amount, from_currency, to_currency):
    if from_currency not in conversion_rates or to_currency not in conversion_rates:
        return "Invalid currency code"
    
    usd_amount = amount / conversion_rates[from_currency]
    converted = usd_amount * conversion_rates[to_currency]
    return round(converted, 2)

# Example usage:
print("100 INR to USD:", convert_currency(100, 'INR', 'USD'))
print("500 USD to EUR:", convert_currency(500, 'USD', 'EUR'))
print("1000 JPY to INR:", convert_currency(1000, 'JPY', 'INR'))
