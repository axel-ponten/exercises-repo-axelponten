from classroom import Student, Teacher

def main():
    me         = Student("Axel", "Ponten", "Particle Physics")
    instructor = Teacher("Filipe", "lastname", "Advanced Python")
    print(me.get_name_and_subject())
    print(instructor.get_name_and_course())

if __name__== "__main__":
    main()
