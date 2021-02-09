import csv

def input_data():
  database_file = open("database_customers.csv", 'a')
  reader = csv.reader(database_file)
  
  inputRecord = str(input("Enter record in this format:\nForename, Surname, Gender, Age, Current Country, Vehicle, Deposit\n• Commas must be used! •\n• Spaces too! •\n--> "))
  inputRecord.split(", ")
  forename =        inputRecord[0] 
  surname =         inputRecord[1] 
  gender =          inputRecord[2] 
  age =             inputRecord[3]
  currentCountry =  inputRecord[4] 
  vehicle =         inputRecord[5] 
  deposit =         inputRecord[6] 
  #database_file.write(forename, surname, gender, age, currentCountry, vehicle, deposit)
  database_file.write(inputRecord + "\n")
  database_file.close()