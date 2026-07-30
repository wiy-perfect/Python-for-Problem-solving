# Ask user to create account: an email address, a password.
# ask user to login again with the password they created.
# after logging in successfully, ask user to enter their exam score
# print correct grade letter

# user account creation
print("====================================================================================")
print("Welcome to UG Grade Calculator Portal.\n Please create an account by entering your:")

email_address= input("Your email adress: ").strip()
password= input("Enter a password: ").strip()
print("Your details have been captured.")
print(">>"*15)
print("Your account has been created successfully.")
print()
print()

# user log in
print("_"*12)
print("Please enter the information you provided intially to log in to the system.")
#stretch goal

for i in range(1,4): 
    attempt_email_address= input("Your email: ").strip()
    attempt_password= input("Your password: ").strip() 
    if not (attempt_email_address == email_address and attempt_password == password): 
        print("Your email and password are incorrect!")
        attempts_remaining= 3-i
        print(f"You have {attempts_remaining} attempts remaining!") 
        
    else:
        print("."*15)
        print(f"Logged in succesfully.\nWelcome, {email_address}")
        break
else:
    print("Access Denied!")
    exit()
       



# grade calculation

user_score= int(input("Enter your score (0-100): "))

if (80 <= user_score <=100): # I'm setting upper and lower bounds to enure grades are given only when score between 0 and 100
   grade= "A"
elif (75 <= user_score <= 79):
   grade= "B+"
elif (70 <= user_score <= 74):
   grade= "B"
elif (65 <= user_score <= 69):
   grade= "C+"
elif (60 <= user_score <= 64):
   grade= "C"
elif (55 <= user_score <= 59):
   grade= "D+"
elif (50 <= user_score <= 54):
   grade="D"
elif (45 <= user_score <= 49):
   grade= "E"
elif (0 <= user_score <= 44):
   grade="F"
else:
   print("Invalid input! Score must be between 0-100")
   grade= None # I chose to return None
# grade is stored based on condtion met

if grade is not None:
  print(f"Your grade : {grade}")
  print(">>"*15)






