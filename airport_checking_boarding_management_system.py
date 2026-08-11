# Airport check-in and boarding management system

# feature 1 (check-in passenger)
# requirement:
# repeatedly display menu
# record name, passport number, nationality,age, destination, ticket class(economy,business,
#  first-class),number of bags

def generate_boarding_pass(base_number):
   # given a boarding pass number has the format say BP#######
   prefix= base_number[:1] #storing string part as prefix
   next_number += int(base_number[2:]) #incrementing integer part
   return f"{prefix}{next_number:05d}"


while True:
   print("*"*20 +" KOTOKA AIRPORT CHECK-IN SYSTEM "+"="*20)

   print("1. Check In Passenger \n2. View Daily Statistics \n3. View Flight Summary \4. Close Check-in")

   try:
      user_choice=int(input("Enter a number: ").strip())
      if user_choice not in range(1,5):
         print("Number must be between 1 and 4.")
         break
   except ValueError:
      print("Invalid input! You  must enter a number")
      break
   #feature 1:
   if user_choice == 1:
      passenger_name= input("Enter your full name: ").title.strip()
      passport_number= input("Enter your passport number: ").strip()
      nationality= input("What is your nationality? ").strip()
      age= int(input("Enter your age? "))
      destination= input("Enter your destination: ").strip()

      try:
        ticket_class= int(input("Choose a class: 1. Economy  2. Business  3. First Class"))
        if ticket_class not in range(1,4):
           print("Number must be between 1 and 3!")
           break
        if ticket_class ==1:
           ticket_class= "Economy"
        elif ticket_class ==2:
           ticket_class= "Business"
        elif ticket_class ==3:
           ticket_class= "First Class"
      except ValueError:
         print("Invalid! Input must be a number(1-3)")
     #Input check
      try: 
        number_of_bags= int(input("How many bags are you carrying?(0-25) ")) #improvising boundaries to restrict user input

        if number_of_bags <0:
           print("Number must be greater than 0!")
           break
        elif number_of_bags >25:
           print("Number exceeds maximum number of bags! Enter a lower number.")
           break
      
        bag_weights= [] #storing bag weights as a list so each weight can be accessed in order of entry via index
        for i in range(1,number_of_bags):
         weight= int(input(f"Enter weight of Bag{i}: "))
         bag_weights.append(weight)

      except ValueError:
         print("Invalid input! Enter a valid number(0-25).")
      

      #bag checks
      total_bag_price= 0
      if ticket_class == "Economy":
         for i in bag_weights:
            if i > 23:
               print(f"Bag{i} exceeds the allowable limit. ")
               extra= i- 23
               total_bag_price+= (extra *30)
               print(f"Allowed: 25kg \nBag:{i}kg \nExtra: {extra} \nCharge= GHS {extra*30:.2f}")

       # Passenger Eligibility
      if not passport_number:
         is_passport_num= False
         passport_num_requirement= "Passport number not provided"
         eligibility= "NO"
      if age < 0:
         is_age= False
         age_requirement= "Age is below 0 years"
         eligibility= "NO"
      if not destination:
         is_destination= False
         destination_requirement= "No valid destination entered"
         eligibility="NO"
      if number_of_bags<0:
         is_num_of_bags= False
         bag_num_requirement= "Number of bags should be greater than 0"
         eligibility="NO"
      eligibility= "YES"

      #Security Screening
      if number_of_bags > 5:
        security_check="Security Inspection required"
      else:
        security_check= "Security Checks passed."

      for i in bag_weights:
         if i > 50:
            security_status="Manual Security Inspection Required."
         else:
            security_status="Security Checks passed" 
       
      #boarding group
      # using match case for simplicity
      match ticket_class:
         case "First Class":
            boarding_group="Priority 1"
         case "Business":
            boarding_group= "Priority 2"
         case "Economy":
            boarding_group= "Priority 3"
         case _:
            boarding_group= None

      current_pass= "BP201000"

       # passenger summary
      print("=\n"*20+"Passenger Successfully Checked In\n"+"=\n"*20)
      print(f"Name: {passenger_name}")
      print(f"Passport Number: {passport_number}")
      print(f"Destination: {destination}")
      print(f"Ticket Class: {ticket_class} \n Boarding group: {boarding_group}")
      print(f"Boarding Pass Number: {generate_boarding_pass(current_pass)}")
      print(f"Number of Bags: {number_of_bags}")
      print(f"Total Baggage Weight: {sum(bag_weights)}Kg")
      print(f"Extra Baggage Charges: GHS {total_bag_price}")
      print(f"Security Status: {security_status} \n{security_check}")
      print(f"Eligible to Board: {eligibility}")
      print("Reason: ")
      if eligibility=="NO":
        if is_age:
           print(age_requirement)
        if is_destination:
           print(destination_requirement)
        if is_passport_num:
           print(passport_num_requirement)
        if is_num_of_bags:
           print(bag_num_requirement)
      print("="*20)

        
                  


         
      

         


