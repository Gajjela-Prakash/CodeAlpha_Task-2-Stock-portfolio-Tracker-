128
# Hardcoded stock prices (simulating API data)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 130,
    "AMZN": 140,
    "MSFT": 200
}
portfolio = {}
print("📊 Welcome to Stock Portfolio Tracker!")

while True:
    stock = input("Enter stock symbol (AAPL, TSLA, etc.) or type 'done' to finish: ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("⚠️ Invalid stock symbol. Try again.")
        continue
    try:
        quantity = int(input(f"Enter number of shares for {stock}: "))
        if quantity < 0:
            print("⚠️ Quantity cannot be negative.")
            continue
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("⚠️ Enter a valid number.")
total_value = 0
print("\n📈 Your Portfolio Summary:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_value += value
    print(f"  {stock}: {qty} shares × ₹{price} = ₹{value}")

print(f"\n💰 Total Investment Value: ₹{total_value}")
# Optional: Save portfolio to a text file
save = input("\nDo you want to save your portfolio summary to a file? (yes/no): ").lower()
if save == 'yes':
    with open("portfolio_summary.txt", "w") as file:
        file.write("📈 Stock Portfolio Summary\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            file.write(f"{stock}: {qty} shares × ₹{price} = ₹{value}\n")
        file.write(f"\n💰 Total Investment Value: ₹{total_value}\n")
    print("✅ Portfolio summary saved to 'portfolio_summary.txt'")
