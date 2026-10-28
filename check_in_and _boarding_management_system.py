from typing import Dict, Optional, List
from dataclasses import dataclass, field
from enum import Enum

# Kotoka International Airport.
"""
1. Check In passenger
2. View Daily Statistics
3. View Flight Summary
4. Clocse check-in """

class TicketClass(Enum):
    FIRST = 1
    BUSINESS = 2
    ECONOMY = 3

@dataclass 
class BaggageInfo:
  count: int
  weights: List[float] 
  total_weight: float = 0.0
  extra_charges: float = 0.0
  requires_inspection: bool = False

@dataclass
class Passemger:
  name: str
  passport_number: str
  nationality: str 
  age: int 
  destination: str
  ticket_class: TicketClass
  baggage: BaggageInfo
  is_eligible: bool = True
  eligibility_reasons: List[str] = field(default_factory=list)
  security_status: str = "Clear"
  boarding_group: str = "Priority 3"



   
class AirportCheckerSystem:
   #Class for business rules
   def __init__(self):
     self.passengers :dict= {}

# Feature 1- Passenger Check-in
   def passenger_check_in(self, passenger_name :str, passport_number : str , nationality :str, age: int, destination :str, number_of_bags :int, ticket_class :int, bags: list ) -> dict:
     passenger :dict = {}
     if not ticket_class:
       print("No ticket class was selected!!")
       ticket_class = None


     economy_limt= 23
     business_limit= 32
     first_class_limit = 40
     #bag weight check
     for i in range(0, len(bags)):
       bags[i]=  int(input(f"Enter weight of Bag {[i+1]}: "))
     for i in bags:
       extra= 0
       total_cost= 0
       tot_weight = 0
       if bags[i] > economy_limt and ticket_class == 3:
         print(f"Bag{i+1} exceeds allowed weight for the Economy Class!")
         extra = bags[i] - economy_limt
         charge= extra * 30
         total_cost += charge
         tot_weight += bags[i]
         print(f"Allowed = {economy_limt}kg \nBag= {bags[i]} \nExtra ={extra} \nCharge= {charge} \nTotal baggage surcharge = {total_cost}")

       elif bags[i] > business_limit and ticket_class == 2:
         print(f"Bag{i+1} exceeds allowed weight for the Business Class!!")
         extra= bags[i] - business_limit
         charge = extra * 30
         tot_weight += bags[i]
         total_cost += charge
         print(f"Allowed = {business_limit}kg \nBag = {bags[i]}  \nExtra = {extra} \nCharge = {charge} \nTotal baggage surcharge = {total_cost}")

       elif bags[i] > first_class_limit and ticket_class == 1:
         print(f"Bag{i+1} exceeds allowed weight for the First Class!!")
         extra =bags[i] - first_class_limit
         charge= extra * 30
         tot_weight += bags[i]
         total_cost += charge
       if bags[i] > 50 :
         inspect =True

       passenger["passenger name"]= passenger_name
       passenger["age"] = age
       passenger["nationality"] = nationality
       passenger["passport number"] = passport_number
       passenger["destination"] = destination
       passenger["ticket class"] = ticket_class
       passenger["number of bags"] = number_of_bags
       passenger["total baggage weight"] = tot_weight
       passenger["extra baggage charges"] = total_cost
       if inspect: passenger["requires_inspection"] = inspect

       self.passengers["passenger"] = passenger
       
       return passenger

   def passenger_eligibility(self) -> None:
     is_eligible= False

     for keys,val in self.passengers.items():
       is_passport_number= False
       is_age_positive = False
       is_destination_present = False
       is_num_of_bags_positive = False

       if val["passport number"] :
         is_passport_number = True
       else:
         reason_1= "Passport number is not present!"

       if val["age"] > 0:
         is_age_positive = True
       else:
         reason_2= "Age is negative! Age must be a positve number(0-70)."

       if val["destination"]:
         is_destination_present = True
       else:
         reason_3= "You have not entered a destination!"

       if val["number of bags"] > 0:
         is_num_of_bags_positive = True
       else:
         reason_4= "Number of bags must be positive(0-20)"

     if is_num_of_bags_positive and is_destination_present and is_age_positive and is_passport_number:
       is_eligible = True

     if not is_eligible:
       print(f"Passenger is NOT eligible for this flight. \nReason:")
       if reason_1: print(reason_1)
       if reason_2: print(reason_2)
       if reason_3: print(reason_3)
       if reason_4: print(reason_4)

     val["eligibility"] = is_eligible
     return

   def security_screening(self) ->None:

     for key,val in self.passengers.items():
       notices= []
       if val["number of bags"] > 5:
         notices = "Security Inspection Required."
       elif val["requires_inspection"]:
         notices = "Manual Security Inspection Required."
       val["security status"] = notices
     return

   def boarding_priority(self) -> None:
     for key,val in self.passenger.items():
       if val["ticket class"] == "1": boarding_group = "Priority 1"
       elif val["ticket class"] == "2": boarding_group = "Priority 2"
       elif val["ticket class"] == "3": boarding_group = "Priority 3"
       val["boarding group"] = boarding_group
     return

   def generate_passenger_summary(self) -> None:
     for key, val in self.passengers.items():
      print("="* 15 + "\nPassenger Succesfully Checked In!\n" + "="*15)
      print(f"""{val["passenger name"]}
                {val["passport number"]}
                {val["destination"]}
                {val["ticket class"]}
                {val["boarding group"]}
                {val["number of bags"]}
                {val["total baggage weight"]}
                {val["extra baggage charges"]}
                {val["security status"]}
                {val["eligibility"]}""")
      return
       
#Feature 2- Daily Statistics
   def daily_statistics(self) -> dict:
    adult_count = 0
    child_count = 0
    economy_passenger_count = 0
    business_passenger_count = 0
    first_class_passenger_count = 0
    security_inspection_count = 0
    total_baggage_charges_collected = 0
    total_bags_processed = 0 
    total_weight = 0


    for key,val in self.passengers.items():
      if val["age"] >= 18:
        adult_count += 1
      elif val["age"] < 18:
        child_count += 1

      if val["ticket class"] == "Economy Class":
        economy_passenger_count += 1
      elif val["ticket class"] == "Business Class":
        business_passenger_count += 1
      elif val["ticket class"] == "First Class":
        first_class_passenger_count += 1

      if val["security status"] == ("Manual Security Inspection Required." or "Security Inspection Required." ):
        security_inspection_count +=1

      if val["extra baggage charges"]: 
        total_baggage_charges_collected += val["extra baggage charges"]

      if val["number of bags"]: 
        total_bags_processed += val["number of bags processed"]

      if val["total baggage weight"]:
        total_weight += val["total baggage weight"]

      all_passengers :int  = adult_count + child_count

    print(f"""Passengers Checked In : {all_passengers}
            adults : {adult_count}
            Children : {child_count}
            Economy Passengers : {economy_passenger_count}
            Business Passengers : {business_passenger_count}
            First Class Passengers : {first_class_passenger_count}
            Passengers Set for Security Inspection : {security_inspection_count}
            Total Baggage Charges Collected : GHC {total_baggage_charges_collected}.00
            Total Number of Bags Processed : {total_bags_processed}""")

    
       
    summary_data= {}
    summary_data["number of adults"] = adult_count 
    summary_data["number of children"] = child_count
    summary_data["all passengers"] = all_passengers
    summary_data["number of bags"] = total_bags_processed 
    summary_data["total_weight"] = total_weight
    summary_data["total baggage charges"] = total_baggage_charges_collected
    
    return summary_data

#Feature 3- Flight summary
   def flight_summary(self,summary_data) -> None:
     all_passengers :int = summary_data["all passengers"]
     children :int  = summary_data["number of children"]
     adults :int = summary_data["number of adults"]
     number_of_bags :int = summary_data["number of bags"]
     total_weight = float(summary_data["total weight"])
     total_charges =summary_data["total baggage charges"]


     average_bags_per_passenger :int = (number_of_bags //all_passengers )
     average_weight_per_passenger :float = total_weight // number_of_bags

     print("="*15 + "END OF DAY REPORT"+"="*15)
     print(f"""Passengers Processed : {all_passengers}
               Children : {children}
               Adults : {adults}
               Total Bags : {number_of_bags}
               Average Bags per Passenger : {average_bags_per_passenger}
               Average Weight per Passenger : {average_weight_per_passenger}
               Total revenue from Baggage : {total_charges}
               Most Popular Ticket Class""")

     
     
     



