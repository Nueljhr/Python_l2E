

Student_name = input("What is your name ?: ")
Student_age = (int(input("What is your age ?: ")))
Student_score = (int(input("What is your score ?: ")))


if Student_score >= 90 and Student_age >= 18:
    print(f"Congratulations, {Student_name}! You qualify for the scholarship.")
elif Student_score >= 90 and Student_age < 18:
    print(f"Excellent score, {Student_name}! You qualify for the junior scholarship.")
else:
    print(f"Sorry, {Student_name}. You do not qualify this time.")

print("Keep working hard!")