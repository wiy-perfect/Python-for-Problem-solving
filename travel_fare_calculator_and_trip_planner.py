# goals:
# calculate cost of journey before purchasing ticket
# operation:
# display menu repeatedly


# variables to store statistics data
total_passengers= 0
total_tickets_sold=0
standard_tickets_sold= 0
vip_tickets_sold= 0
children_served=0
senior_citizen_served=0
total_revenue_collected=0
average_amount_per_booking=0

#generating a ticket number
def generate_next_ticket(current_ticket):
    prefix= current_ticket[0] #stores teh integer part of the current ticket
    next_num= int(current_ticket[1:])+1 #converting integer part into integer data type and incrementing

    return f"{prefix}{next_num:05d}" # new ticket num is returned

ticket_number= "T10300"

while True:
   print("="*10+"SWIFT TRAVELS GHANA Travel Fare Calculator"+"="*10)
   print("---Menu------")
   print("1. Book a Trip \n2. View Today's Statistics \n3. Exit \n")
   user_choice= input("Choose an option: ").lower()

# booking trip
   if user_choice == "1":

      full_name= input("Enter your full name: ").strip()
      user_age= int(input("Enter your age: ")).strip() 
      departure_city= (input("Which city are you departing from?(Accra,Kumasi) ").strip()).lower()
      destination_city= (input("Which city are you heading to?(Takoradi,Kumasi,Tamale) ").strip()).lower()

      # restricting user input to integers to avoid spelling errors
      seat_class=input("Choose a seat class(Enter 1 or 2):  \n1. Standard  \n2. VIP ").split()
      if seat_class == "1": seat_class= "Standard"
      elif seat_class == "2": seat_class= "VIP"
      else: 
        print("Input must be 1 or 2.")
        continue

     # handling negative, zero and non integer inputs.
      try:
        number_of_tickets= int(input("How many tickets do you want to purchase? "))
        if number_of_tickets < 1:
           print("Error: number must be at least 1!")
           continue
      except ValueError:
           print("Error: number of tickets must be a number!")
           continue
      

    #pricing 
      original_price= None

      if seat_class == "Standard": #standard fares
        standard_tickets_sold +=1
        if departure_city== "accra" and destination_city== "kumasi": original_price= 120
        elif departure_city == "accra" and destination_city == "takoradi": original_price= 100
        elif departure_city == "accra" and destination_city == "tamale":  original_price= 220
        elif departure_city == "kumasi" and destination_city == "tamale": original_price=180
        
      elif seat_class == "VIP": # VIP fares
        vip_tickets_sold +=1
        if departure_city== "accra" and destination_city== "kumasi": original_price= 180
        elif departure_city == "accra" and destination_city == "takoradi": original_price= 160
        elif departure_city == "accra" and destination_city == "tamale":  original_price= 300
        elif departure_city == "kumasi" and destination_city == "tamale": original_price=250
      # safety check for cities outside route scope.
      if original_price is None:
        print("Error: We do not operate on a direct route between those two cities!") 
        continue

      current_ticket=generate_next_ticket(ticket_number)

    #discount
      original_group_price= original_price * number_of_tickets 

      age_discount= 0
      if user_age < 12:
        age_discount= 50 # storing percentage discount in a variable to keep if else block calculation free
        children_served += 1
      elif user_age > 60:
        age_discount= 30
        senior_citizen_served +=1

      discounted_price= original_group_price * ((100-age_discount)/100)

    #group discount
      group_discount= 0
      if number_of_tickets >=4:
        group_discount=10
        final_bill= discounted_price * ((100-group_discount)/100)
      else:
         final_bill =discounted_price
        
    # updating statistical info (used later in feature 2)
      total_passengers +=1
      total_tickets_sold +=number_of_tickets
      total_revenue_collected += final_bill

      total_discount= original_group_price- final_bill


    # Trip Summary
      print("="*10+ "\nTRIP CONFIRMATION \n" +"="*10)
      print(f"Passenger Name: {full_name}\n")
      print(f"From {departure_city.title()} to \n{destination_city.title()}\n")
      print(f"Seat Class: {seat_class}\n")
      print(f"Ticket number: {current_ticket}")
      print(f"Number of tickets: {number_of_tickets}\n")
      print(f"Discount applied: GHS {total_discount:.2f}\n")
      print(f"Amount Payable: GHS {final_bill:.2f}\n")
      print("="*32)

   elif user_choice == "2": #display stats

      if total_passengers ==0:
        average_amount_per_booking=0
      else:
        average_amount_per_booking= (total_revenue_collected)/total_passengers
      print("Todays Statistics\n")
      print(f"Total passengers served: {total_passengers} \nTotal tickets sold: {total_tickets_sold}")
      print(f"Standard tickets sold: {standard_tickets_sold} \nVIP tickets sold: {vip_tickets_sold} \nChildren served: {children_served} \nSenior citizens served: {senior_citizen_served}")
      print(f"Total revenue collected: GHS {total_revenue_collected:.2f} \nAverage amount paid per booking: GHS {average_amount_per_booking:.2f}")

   elif user_choice == "3": #exit
      user_decision= input("Are you sure you want to exit (Y/N)? ").strip().upper() # removing whitepace from user input and converting to capital letters
      if user_decision == "Y":
        print("Thank you for using Swift Travel Ghana. Goodbye!")
        break
   else:
      print("Error: Inalid choice. Please enter 1, 2 or 3.")
