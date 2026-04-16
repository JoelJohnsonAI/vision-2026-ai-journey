# Script 2 — Income Calculator
# Joel Johnson Sonayon | April 15, 2026

print("=" * 40)
print("2026 INCOME CALCULATOR")
print("=" * 40)

# Get user input
monthly_income = float(input("Enter your current monthly income (₦): "))
target = 10000000  # ₦10M annual target

# Calculate
remaining = target - monthly_income
monthly_needed = target / 8  # 8 months left in 2026

print(f"\nCurrent monthly income : ₦{monthly_income:,.0f}")
print(f"Annual target          : ₦{target:,.0f}")
print(f"Remaining to hit target: ₦{remaining:,.0f}")
print(f"Monthly avg needed     : ₦{monthly_needed:,.0f}")

if monthly_income >= monthly_needed:
    print("\nYou are ON TRACK. Keep pushing.")
else:
    print("\nYou are behind. Adjust and accelerate.")
