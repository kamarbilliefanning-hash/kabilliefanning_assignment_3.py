# Step 1: Variable Setup
student_name = "YourName"  # Replace with your actual name
current_gpa = 3.2          # Float between 1.0-4.0
study_hours = 25           # Integer (Ex. 25)
social_points = 50         # Integer (Ex. 50)
stress_level = 30          # Integer 0-100

# Display starting stats
print("---------------------------------------")
print(f"Welcome to Semester Simulator, {student_name}!")
print("--- Starting Stats ---")
print(f"GPA: {current_gpa}")
print(f"Study Hours: {study_hours}")
print(f"Social Points: {social_points}")
print(f"Stress Level: {stress_level}")
print("---------------------------------------")

# --- Step 2: Course Planning Decision (if/elif/else and comparison operators) ---

print("\n--- Decision 1: Course Planning ---")
print("Choose your course load:")
print("A) Light (12 credits)")
print("B) Standard (15 credits)")
print("C) Heavy (18 credits)")
choice = input("Your choice: ").upper()

if choice == "A":
    print("Light load chosen: Focus on depth.")
    study_hours += 15
    stress_level -= 10
    # Comparison operators used here
    if current_gpa >= 3.5:
        current_gpa += 0.3
    else:
        current_gpa += 0.5

elif choice == "B":
    print("Standard load chosen: Balanced.")
    study_hours += 10
    stress_level += 5
    # Comparison operator used here
    if current_gpa > 3.0:
        current_gpa += 0.1
    else:
        current_gpa -= 0.1

elif choice == "C":
    print("Heavy load chosen: High intensity.")
    social_points -= 10
    stress_level += 20
    # Comparison operators used here
    if current_gpa >= 3.5:
        current_gpa -= 0.1
    elif current_gpa <= 2.5: # Use <= for variety
        current_gpa -= 0.5
    else:
        current_gpa -= 0.2

else:
    # Handles invalid input
    print("Invalid choice. Defaulting to Standard load.")
    study_hours += 10
    stress_level += 5
    current_gpa += 0.1

# Enforce GPA bounds
current_gpa = max(1.0, min(4.0, current_gpa))

print(f"\nUpdated GPA: {current_gpa:.2f}, Stress: {stress_level}, Study Hours: {study_hours}")

# --- Step 3: Study Strategy Decision (Membership and Logical operators) ---

print("\n--- Decision 2: Study Strategy ---")
print("Where will you focus your study time this week?")
study_options = ["Programming", "Math", "English", "History"]
print(f"Options: {', '.join(study_options)}")
study_focus = input("Your choice: ")

# Membership operator check (in is kept)
if study_focus in study_options:
    print(f"Focusing on {study_focus}.")

    # Logical operators used here (or, not) - 'and' removed by nesting
    if study_focus == "Programming":
        # Replaced 'and' with nesting for dual condition
        if social_points >= 40:
            current_gpa += 0.1
            social_points -= 5
    
    elif study_focus == "Math" or study_focus == "English":
        # 'or' is preserved as requested
        current_gpa += 0.2
        stress_level -= 5
        
    elif study_focus == "History":
        # 'not' is preserved as requested
        if not (stress_level > 80):
            social_points += 10
            
    else:
        pass # Neutral effect for valid choices that didn't meet nested conditions

# Replaced 'elif study_focus not in study_options:' with 'else:'
else:
    # Handles invalid input
    print("Invalid option. You procrastinated.")
    social_points += 20
    study_hours -= 10
    stress_level += 15

# Enforce GPA bounds
current_gpa = max(1.0, min(4.0, current_gpa))

print(f"\nUpdated GPA: {current_gpa:.2f}, Social Points: {social_points}, Study Hours: {study_hours}")

# --- Step 4: Final Semester Assessment (Identity, Nested if, Multiple Endings) ---

print("\n--- Decision 3: Final Semester Assessment ---")
print("Finals week: A) Cram Session or B) Relax?")
final_choice = input("Your choice: ").upper()

# Identity operators used here - using '==' for string literals
if final_choice == "A":
    print("Cram session chosen. High risk, high reward.")
    
    # Nested if statements (min 2 levels)
    if study_hours > 50:
        print("Sufficient prior study helps.")
        current_gpa += 0.2
        
        if social_points is not 0: # Identity operator (is not) still used here
            print("Social life takes a hit, but GPA wins.")
            social_points -= 5
        else:
            print("Pure focus achieved.")
            current_gpa += 0.1
            
    else:
        print("Not enough foundation. Stress rises.")
        current_gpa -= 0.1
        stress_level += 15

elif final_choice == "B":
    print("Relax chosen. Trusting your preparation.")
    if study_hours > 40:
        print("Well-deserved break.")
        social_points += 20
        stress_level -= 30
    else:
        print("Gamble fails.")
        current_gpa -= 0.4
        social_points += 15

else:
    print("Invalid choice. Neutral outcome.")

# Enforce GPA bounds
current_gpa = max(1.0, min(4.0, current_gpa))

# Final Assessment and Endings
print("\n--- Final Semester Assessment ---")
print(f"Final GPA: {current_gpa:.2f}")
print(f"Final Social Points: {social_points}")
print(f"Final Stress Level: {stress_level}")

# Generate 3+ different endings based on accumulated stats (5 endings total)
if current_gpa >= 3.5 and stress_level <= 50:
    print("\nEnding 1: The 'Dean's List Superstar' 🌟")
    print("Perfect balance! High GPA, low stress. You mastered college life.")
elif current_gpa >= 3.0 and social_points >= 60:
    print("\nEnding 2: The 'Well-Rounded Champion' 🤝")
    print("Good GPA and a strong social life. You're set up for success outside of school too.")
elif stress_level > 80:
    print("\nEnding 3: The 'Burnout Blues' 🤕")
    print("Your stress level is critical. You need a long break. Your efforts were unsustainable.")
elif current_gpa < 2.5:
    print("\nEnding 4: The 'Academic Probation' ⚠️")
    print("Your GPA is too low. You have to work on your study habits for next semester.")
else:
    print("\nEnding 5: The 'Just Made It' ✅")
    print("You passed. It wasn't pretty, but you survived the semester. Learn from your choices.")