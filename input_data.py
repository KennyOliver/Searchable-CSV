import csv

def input_data():
  database_file = open("database_customers.csv", 'a')
  reader = csv.reader(database_file)
  
  inputRecord = str(input("Enter record in this format:\nForename, Surname, Gender, Age, Current Country, Vehicle, Deposit\n• Commas must be used! •\n--> "))
  inputRecord.split(", ")
  forename, surname, gender, age, currentCountry, vehicle, deposit = inputRecord[0], inputRecord[1], inputRecord[2], inputRecord[3], inputRecord[4], inputRecord[5], inputRecord[6]
  #database_file.write(forename, surname, gender, age, currentCountry, vehicle, deposit)
  database_file.write("\n" + inputRecord)
  database_file.close()