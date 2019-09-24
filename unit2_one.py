# by Allison Dixon
# last updated September 24, 2019
# unit two assignment option one
#
# This program has a chatbot interact with the user, asking questions and calculating payment for their dream car.

name = input("What is your name?")
print("I guess it's nice to meet you", name, "! My name is The Banished Prince Zuko of the Fire Nation.")

location = input("Where are you from?")
print("I've heard", location, "is an okay place. Maybe I'll go there once I get my honor back.")

number = int(input("What is your favorite number?"))
print("Your favorite number", number, "is", number/8, "times bigger than my favorite number 8!")

car = input("What is your dream car?")
print("Oh my goodness, I've always wanted a", car, "too, but all I have is a ship.")

cost = float(input("How much does that car cost?"))
print("That's pretty expensive and I'm broke after Uncle spent all our money buying a new lotus tile.")

years = int(input("How many years would you take a loan for to pay for an " + car + "?"))

annual_interest = float(input("What is the annual interest rate (percent) for an " + car + "?"))

# The following lines calculate the monthly payment of the car and the total cost.
monthly_interest = (annual_interest/100) / 12
number_monthly_payments = years * 12
monthly_payment = (monthly_interest * cost) / (1-(1 + monthly_interest) ** -number_monthly_payments)
total_cost = monthly_payment * (12 * years)
print("Your monthly payment for the " + str(car) + " would be $" + str(monthly_payment) +
      " which makes a total of $" + str(total_cost) + " !")
