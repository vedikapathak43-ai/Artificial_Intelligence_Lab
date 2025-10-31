# Career Path Suggestion Based on Two Interests

# Take user inputs
interest1 = input("Enter your first interest: ").strip().title()
interest2 = input("Enter your second interest: ").strip().title()

# Decision logic
if (interest1 == "Maths" and interest2 == "Physics") or (interest1 == "Physics" and interest2 == "Maths"):
    suggestion = "Mechanical Engineering"

elif (interest1 == "Programming" and interest2 == "Maths") or (interest1 == "Maths" and interest2 == "Programming"):
    suggestion = "Computer Engineering"

elif (interest1 == "Biology" and interest2 == "Chemistry") or (interest1 == "Chemistry" and interest2 == "Biology"):
    suggestion = "Biotechnology"

elif (interest1 == "Circuits" and interest2 == "Maths") or (interest1 == "Maths" and interest2 == "Circuits"):
    suggestion = "Electronics Engineering"

elif (interest1 == "Programming" and interest2 == "Statistics") or (interest1 == "Statistics" and interest2 == "Programming"):
    suggestion = "Artificial Intelligence and Data Science"

elif (interest1 == "Programming" and interest2 == "Ai Concepts") or (interest1 == "Ai Concepts" and interest2 == "Programming"):
    suggestion = "Artificial Intelligence and Machine Learning Engineering"

else:
    suggestion = "No specific suggestion available based on your interests."

# Output result
print(f"\nBased on your interests, you should consider: {suggestion}")

