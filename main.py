# class perfaqeson me shume se nje data.
# me classes dhe objects ne krijojme data-type tonen

# mund te krijojme nje student

from Student import Student

student1 = Student()
student1.name = "Jim"
student1.major = "Business"
student1.gpa = 3.1
student1.is_on_probation = False

print (f"{student1.name} \n{student1.major} \n{student1.gpa} \n{student1.is_on_probation}")
