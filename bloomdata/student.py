'''
This is a file that has a Student parent class and 
a BloomTechStudent child class.
'''
import random

class Student():
    '''
    This is a class that instantiates students with a name and age.
    '''
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def edit_name(self, edited_name):
        self.name = edited_name
        return self.name

    def edit_age(self):
        self.age += 1
        return self.age

    def __repr__(self):
        return f'{self.name} is a student who is {self.age} years old'

# if __name__ == '__main__':
#     student1 = Student('Chris', 29)
#     print(student1)
#     print(student1.edit_name('Christopher'))
#     print(student1.edit_age())
#     print(student1)

class BloomTechStudent(Student):
    '''
    This is a child class where BloomTechStudent has a particular
    track and sprint status.
    '''
    def __init__(self, name, age, track, sprint):
        super().__init__(name, age)
        self.track = track
        self.sprint = sprint

    def edit_track(self, new_track):
        self.track = new_track
        return f"The new track is {self.track}"

    def edit_sprint(self):
        self.sprint += 1
        return f"{self.name} is now on sprint {self.sprint}"

    def __repr__(self):
        return f'{self.name} is a BloomTech {self.track} student on sprint {self.sprint}'

# if __name__ == '__main__':
#     student1 = BloomTechStudent('Chris', 29, "Data Science", 9)
#     print(student1)
#     print(student1.edit_track('WebDev'))
#     print(student1.edit_sprint())
#     print(student1)


'''
The following are lists for a subsequent function
that will randomly generate BloomTech students
'''
name_list = ['Christopher', 'Chris', 'Carol', 'Sara',
            'Brent', 'Jermaine', 'Bradley', 'Connie',
            'Margerie', 'Gerber']

track_list = ['Data Science', 'BackEnd', 'WebDev']

def student_generator():
    student_list = []

    for i in range(30):
        name = random.choice(name_list)
        age = random.randint(18, 50)
        track = random.choice(track_list)
        sprint = random.randrange(23)

        # Create a new instance of this random student
        studentx = BloomTechStudent(name, age, track, sprint)

        # Add student to list
        student_list.append(studentx)

    return student_list

if __name__ == '__main__':
    print(student_generator())