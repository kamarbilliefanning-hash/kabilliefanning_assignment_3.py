Semester Simulator: A Student Life Text Adventure
This game is a simple text-based adventure that simulates a college student's semester. You make choices that directly change how you're doing in four key areas: GPA, Study Hours, Social Points, and Stress Level. The main goal is to balance these scores to get one of the best possible results at the end of the term.

Branching Concepts Demonstrated
This project shows off different ways Python uses logic (called branching) to decide what happens next in the game:

Step 2: Course Planning Decision

if/elif/else: This structure is used for the three main course load choices (Light, Standard, Heavy) and is also used to catch any invalid answers.

Comparison Operators (>=, >, <=): We use operators like >= (greater than or equal to) to check your current GPA. Based on that check, the game changes your stats differently.

Step 3: Study Strategy Decision

Membership Operator (in): This operator checks if the subject you pick is actually one of the valid options in the study_options list.

Logical Operators (or, not):

or is used to group study subjects ("Math" or "English") so they lead to the same result.

not is used to check for an undesirable state (e.g., if the stress level is not too high).

Nesting for 'and' logic: Instead of using the and operator to check two things at once (like subject and social points), we used a nested if statement (an if inside another if) to show a different way to handle that logic.

Step 4: Final Semester Assessment

Identity Operator (is not): This special operator checks if a variable is exactly the same object as another. Here, we use it to check if your social_points are not zero (is not 0) in a specific part of the final decision.

Nested if Statements: The cram path uses two levels of if statements stacked on top of each other to create detailed outcomes based on both your Study Hours and Social Points.

Multiple Endings: The script wraps up with five different conclusions. Each one is unlocked by your final stat combination.

How to Run the Game
Make sure you have Python 3 installed.

Run the game from your command line using:
python [username]_assignment_3.py

What the Different Endings Mean
The 'Dean's List Superstar' (GPA ≥3.5 and Stress ≤50): High achievement without burning out. Great job!

The 'Well-Rounded Champion' (GPA ≥3.0 and Social Points ≥60): You kept your grades up while still having a good social life.

The 'Burnout Blues' (Stress >80): You pushed yourself too hard. Your health is critical, and the effort was too much.

The 'Academic Probation' (GPA <2.5): Your GPA is too low. You need to focus on studying next semester.

The 'Just Made It' (Default): You passed! Your stats are okay, but you'll need a better strategy next time.

AI Assistance Used During Development
I got some help from Google Gemini when I was organizing the code for Step 3. Specifically, it helped me turn the required and and not in rules into the new types of logic (like nesting) the assignment requested.
