print("=======================Scholarship Scholarship Eligibility Checker==================")

print("Please enter your details:")
# user data
user_full_name= input("Enter your full name: ").strip()
user_age= int(input("Enter your age: ").strip())
#bonus
scores=[]
for i in range(0,3):
    user_score= int(input("Enter your score(0-100): ").strip())
    scores.append(user_score)
average_score= sum(scores)/len(scores)

attendence_percentage= int(input(("What is your attendance out of 100? ")).strip())
has_disciplinary_issues= (input("Have you had any disciplinary issues(y or n)? ").lower()).strip()

print("Details recorded---")

# Eligibility checks
age_met= user_age >= 18
score_met= average_score >= 75
attendence_met= attendence_percentage >= 80
discipline_met= has_disciplinary_issues =="n"



age_requirement= "Age requirement met." if age_met else "Age requirement NOT met."
score_requirement= "Score meets requirement." if score_met else "Score does NOT meet requirement."
attendence_requirement= "Attendence meets requirement" if attendence_met else "Attendence below required minimum."
disciplinary_requirement= "No disciplinary issues." if discipline_met else "Has disciplinary issues"


if age_met and score_met and attendence_met and discipline_met:
    status= "ELIGIBLE"
else:
    status= "NOT ELIGIBLE"

# Output
print("=========== Scholarship Result =========")
print(f"Student: {user_full_name}\n")
print(f"Status : {status}\n")
print("Reason:")
print(age_requirement)
print(score_requirement)
print(attendence_requirement)
print(disciplinary_requirement)



    
     

