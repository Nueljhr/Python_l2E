
Name = input("what is your name: ")
Score = int(input("what is your score: "))

if Score >= 90:
    print(f"Excellent, {Name}!")
elif Score >= 70:
    print(f"Very Good, {Name}!")
elif Score >= 50:
    print(f"Pass, {Name}!")
else:
    print(f"Fail, {Name}!")


print("Thanks for checking your results!")
