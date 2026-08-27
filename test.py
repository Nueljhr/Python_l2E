## TIMES TABLE
 
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f"{i} x {j} = {i * j}")
#     print()  # Print a blank line after each table


# for i in range(12, 20):
#     for j in range(12, 20):
#         print(f"{i} * {j} = {i * j}")
#     print()  # Print a blank line after each table

# def append(my_list, item):
#     my_list.append(item)

# numbers = [1, 2, 3]

# append(numbers, 5)

# print(numbers)

class Student:

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def introduce(self):
        print(f"My name is {self.name}")

    def improve_score(self):
        self.score += 5

        # return self.score
    
    def reset_score(self):
        if self.score >= 100:
            self.score = 0
        return self.score
    
    def get_score(self):
        return self.score

student1 = Student("Kultur", 89)
student2 = Student("Munich", 109)

student1.introduce()
print(student1.improve_score())
student1.improve_score()
print(student1.score)
print(student1.reset_score())

student2.introduce()
print(student2.improve_score())
print(student2.reset_score())
print(student2.get_score())