def calculate_simple_interest(p, r, t):
    return (p * r * t) / 100

def calculate_compound_interest(p, r, t):
    return p * ((1 + r / 100) ** t) - p

print("📊 Interest Calculator")
try:
    principal = float(input("Enter the principal amount (P): ₹ "))
    rate = float(input("Enter the annual interest rate (R%) : "))
    time = float(input("Enter the time in years (T): "))

    # Calculate
    simple = calculate_simple_interest(principal, rate, time)
    compound = calculate_compound_interest(principal, rate, time)

    # Results
    print(f"\n📈 Simple Interest: ₹ {simple:.2f}")
    print(f"📈 Compound Interest: ₹ {compound:.2f}")

except ValueError:
    print("❌ Invalid input! Please enter numeric values only.")
