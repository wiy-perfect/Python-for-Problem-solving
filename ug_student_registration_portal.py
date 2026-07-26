# Input page
print("="*65)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
print("WELCOME TO THE UNIVERSITY OF GHANA STUDENT REGISTRATION PORTAL")
print("="*65)
print("Welcome, User. Enter your details first to register")
first_name= input("Please enter your first name: ")
last_name= input("Please enter your last name: ")
middle_name=input("Please enter your middle name if any: ")

gender= input("What's your gender? \n1. Male  2. Female 3. other \nEnter a number:  ").lower()
if gender =="1":
    gender= "Male"
elif gender== "2":
    gender= "Female"
elif gender=="3":
    gender="Unknown"
else:
    print("Invalid input!")

email_address= input("Enter your email address here: ")
programme_of_study= input("What programme do you study?")
date_of_birth= input("Enter your date of birth(dd/mm/yyyy): ")
phone_number= input("Enter your phone number: ")
password= input("Enter your password: ")
student_id= input("Enter your student ID: ")
location= input("Where do you live? ")
age= input("Enter your age: ")
is_married= (input("Enter T if you are married and F if you are not").lower()).strip()
height= input("Enter your height in  meters: ")
favorite_programming_languge= input("What is your favorite programming language? ")
dream_career= input("Enter your hall of residence: ")
emergency_contact= input("Enter your emergency contact: ")
hobby= input("What is your hobby? ")
nationality= input("What is your nationality? ")
print("."*6)
print("."*3)
print("---Your details have been recorded---")
print()

print("="*100)

# details printed out
print("="*65)
print("You are successfully registered as a student at the University Of Ghana.")
print("-"*12+"\nStudent Details"+"-"*12)
print("Here is the information you entered: ")
print(f"Full Name: {first_name} {middle_name } {last_name}")
print(f"Gender: {gender} ")
print(f"Email Address: {email_address}")
print(f"Programme of Study: {programme_of_study}")
print(f"Date of Birth: {date_of_birth}")
print(f"Phone Number: {phone_number}")
print(f"Password: {password}")
print(f"Student ID: {student_id}")
print(f"Location: {location}")
print(f"Age: {str(age)}")
print(f"Marital Status: {"Married" if is_married== "t" else "Single"}")
print(f"Height: {str(height)} meters")
print()
print(f"Congratulations,{first_name} on your sucessful admission to the University of Ghana.")
print("Quote: *The Heights by great men reached and kept, were not attained by sudden flight. But they, while their companions slept, tioed upwards intothe night. ")