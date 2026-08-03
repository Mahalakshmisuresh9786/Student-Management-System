students = []


def add_student():
    name = raw_input("Enter Student Name:")
    students.append(name)
    print("Student Added Successfully")


def view_student():

    if len(students)==0:
        print("No Student Found")
    else:
            print("Student List")
            
    for student in students:
        print(student)


def search_student():
     
    name = raw_input("Enter Your Name:")
    if name in students:
         print("Student Found")
    else:
         print("Student not fonud")

def delete_student():
    name=raw_input("Enter Student Name:")
    if name in students:
        students.remove(name)
        print("Student Name Successfully Deleted")
    else:
        print("Student Not Found")



while True:
    print("////Student Management System/////")
    print("1.add_student")
    print("2.view_student")
    print("3.search_student")
    print("4.delete_student")
    print("5.Exit")

    choice=raw_input("Enter Your Choice:")
    print("choice:")

    if choice=="1":
        add_student()

    elif choice=="2":
        view_student()

    elif choice=="3":
        search_student()
    elif choice=="4":
        delete_student()
    elif choice=="5":
        break
    else:
        print("Invalid Choice")
        
          


        

        
    



        

        
    
