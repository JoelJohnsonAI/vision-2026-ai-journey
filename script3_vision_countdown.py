# Script 3 — Vision Countdown
# Joel Johnson Sonayon | April 15, 2026

print("=" * 40)
print("VISION 2026-2037 COUNTDOWN")
print("=" * 40)

current_year = 2026
current_phase = 0

milestones = {
    2027: "Depart Nigeria — Begin Master's abroad",
    2029: "Married + PhD enrolled + ₦1B net worth",
    2032: "PhD complete + Global AI Authority",
    2037: "AI Governance Specialist + ₦10B-₦50B net worth"
}

print(f"Current Year : {current_year}")
print(f"Current Phase: Phase {current_phase} — AI Beginner to AI Builder")
print("\nMilestone Countdown:")
print("-" * 40)

for year, milestone in milestones.items():
    years_left = year - current_year
    print(f"{year} ({years_left} years away): {milestone}")

print("-" * 40)
print("\nEvery day of consistency compounds.")
print("Start. Stay. Finish.")
