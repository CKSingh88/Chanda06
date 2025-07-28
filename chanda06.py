# STOCK PORTFOLIO TRACKER

# Step 1: Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 258,
    "GOOGL": 135,
    "AMZN": 132
}

# Step 2: Get user input
portfolio = {}
n = int(input("How many different stocks do you own? "))

for _ in range(n):
    name = input("Enter stock name (e.g., AAPL): ").upper()
    qty = int(input(f"Enter quantity of {name}: "))
    portfolio[name] = qty

# Step 3: Calculate total investment
total = 0
print("\nInvestment Details:")
for stock, qty in portfolio.items():
    price = stock_prices.get(stock)
    if price:
        investment = price * qty
        total += investment
        print(f"{stock}: {qty} × ${price} = ${investment}")
    else:
        print(f"{stock}: Price not found, skipped.")

print(f"\nTotal Investment Value: ${total}")

# Step 4: Save to file
save = input("Save to file? (yes/no): ").lower()
if save == 'yes':
    with open("portfolio_summary.txt", "w") as f:
        f.write("Stock Portfolio Summary:\n")
        for stock, qty in portfolio.items():
            price = stock_prices.get(stock, "N/A")
            if price != "N/A":
                f.write(f"{stock}: {qty} × ${price} = ${price * qty}\n")
        f.write(f"\nTotal Investment: ${total}\n")
    print("✅ Summary saved to 'portfolio_summary.txt'")
