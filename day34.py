# Object State & Behavioral Rules
# CONDITIONS CAN CONTROL OBJECT BEHAVIOR


# class Score:
#     def __init__(self, score):
#         self.score = score

#     def improve_score(self):
#         self.score += 5

#         if self.score > 100:
#             self.score = 100

# student = Score(98)
# student.improve_score()
# print(student.score)

# # # 98
# #  ↓
# # +5
# #  ↓
# # 103
# #  ↓
# # cap at 100
# #  ↓
# # 100

#TODAYS MISSION

class Student:

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def introduce(self):
        print(f"Hello, my name is {self.name}")

    def improve_score(self):
        self.score += 5

        if self.score > 100:
            self.score = 100

student1 = Student("Kultur", 89)
student1.introduce()
student1.improve_score()
print(student1.score)
print()
student2 = Student("Munich", 98)
student2.introduce()
student2.improve_score()
print(student2.score)
print()
student3 = Student(name="Nuel", score=80)
student3.introduce()
student3.improve_score()
print(student3.score)




