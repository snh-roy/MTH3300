"Student class"
class Student:
    def __init__(self) -> None:
        self.name = "sneha" 
        self.identity = 2005
        self.enrolled_classes = []

   
 #getter
    def get_name(self):
        return self.name
    
    def get_id(self):
        return self.identity
    
    def get_enrolled_classes(self):
        return self.enrolled_classes
   
   
   
#setter  
    def update_name(self, n:str):
        self.name = n 
        
        
    def update_id(self, id: int):
        self.identity = id 

    def update_enrolled_classes(self, classes:list):
        self.enrolled_classes = classes


sneha: Student = Student()
sneha.update_name("sneha roy")
mario: Student = Student()
mario.update_name("mario gegprifti")
sneha.update_id(3005)

mario.update_enrolled_classes(["wwi","wwii","wwiii"])
print(mario.enrolled_classes)
print(sneha.identity)
print(sneha.name)

print(mario.name)



"Course Class"

class Course:
    def __init__(self) -> None:
        self.course_name = "Evanematics"
        self.course_code = "EF3150"
        self.instructor = "Mario Gegprifti"


#getter
    def get_course_name(self):
        return self.course_name
    
    def get_course_code(self):
        return self.course_code
    
    def get_instructor(self):
        return self.instructor

#setter
    def update_course_name(self, cn:str):
        self.course_name = cn 
    
    def update_course_code(self, cc:str):
        self.course_code = cc

    def update_instructor_name(self, ins:str):
        self.instructor = ins
        # print(math.update_instructor_name)


math: Course = Course()

print(math.get_course_name()) 
print(math.get_course_code())  
print(math.get_instructor())

math.update_course_name("Calculus")
print(math.get_course_name())

math.update_course_code("CS101")
print(math.get_course_code())


math.update_instructor_name("Justin Goluboff")
print(math.get_instructor())  


