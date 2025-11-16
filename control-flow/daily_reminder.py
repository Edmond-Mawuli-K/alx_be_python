# daily_reminder.py

# Prompt for inputs
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Build base reminder text depending on priority
match priority:
    case "high":
        base = f"'{task}' is a high priority task"
    case "medium":
        base = f"'{task}' is a medium priority task"
    case "low":
        base = f"'{task}' is a low priority task"
    case _:
        base = f"'{task}' has an unspecified priority level"

# Append time-sensitivity message and print with "Reminder:" prefix
if time_bound == "yes":
    print("Reminder:", base + " that requires immediate attention today!")
else:
    print("Reminder:", base + ". Consider completing it when you have free time.")
