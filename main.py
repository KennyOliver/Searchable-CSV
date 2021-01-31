import csv,time,colorama
from colorama import Fore,Back,Style

def new_section():
  print(Fore.WHITE,Style.BRIGHT,">--------------------<\n",Style.RESET_ALL)

def read_customers ():
  CUSTOMERS = open('database_customers.csv','r')
  reader = csv.reader(CUSTOMERS)

  forename = 0
  surname  = 1
  gender   = 2
  age      = 3
  currentCountry = 4
  vehicle  = 5
  deposit  = 6
  
  searchCategory = str(input("Enter filter to apply\n--> ")).lower()
  if searchCategory == 'forename':
      category = forename
      print(Fore.GREEN,Style.BRIGHT,"Filter category applied.",Style.RESET_ALL)
      time.sleep(1)
      new_section()
  elif searchCategory == 'surname':
      category = surname
      print(Fore.GREEN,Style.BRIGHT,"Filter category applied.",Style.RESET_ALL)
      time.sleep(1)
      new_section()
  elif searchCategory == 'gender':
      category = gender
      print(Fore.GREEN,Style.BRIGHT,"Filter category applied.",Style.RESET_ALL)
      time.sleep(1)
      new_section()
  elif searchCategory == 'age':
      category = age
      print(Fore.GREEN,Style.BRIGHT,"Filter category applied.",Style.RESET_ALL)
      time.sleep(1)
      new_section()
  elif searchCategory == 'country':
      category = currentCountry
      print(Fore.GREEN,Style.BRIGHT,"Filter category applied.",Style.RESET_ALL)
      time.sleep(1)
      new_section()
  elif searchCategory == 'vehicle':
      category = vehicle
      print(Fore.GREEN,Style.BRIGHT,"Filter category applied.",Style.RESET_ALL)
      time.sleep(1)
      new_section()
  elif searchCategory == 'deposit':
      category = deposit
      print(Fore.GREEN,Style.BRIGHT,"Filter category applied.",Style.RESET_ALL)
      time.sleep(1)
      new_section()
  else:
      print(Fore.RED,Style.BRIGHT,"\nNo such filter exists.\n",Style.RESET_ALL)
      time.sleep(1)
      new_section()
      searchCategory = str(input("Enter filter to apply\n--> "))
  
  searchRequest = str(input("Enter the " + searchCategory + "\n--> "))

  for record in reader:
    forename = record[0]
    surname  = record[1]
    gender   = record[2]
    age      = record[3]
    currentCountry = record[4]
    vehicle  = record[5]
    deposit  = record[6]

    RECORD = forename + ' | ' + surname + ' | ' + gender + ' | ' + age + ' | ' + currentCountry + ' | ' + vehicle + ' | ' + '£' + deposit

    #searchRequest = str(input("Enter the " + searchCategory + "\n--> "))

    if searchRequest == forename:
      print(Fore.CYAN,RECORD,Fore.WHITE)
    elif searchRequest == surname:
      print(Fore.CYAN,RECORD,Fore.WHITE)
    elif searchRequest == gender:
      print(Fore.CYAN,RECORD,Fore.WHITE)
    elif searchRequest == age:
      print(Fore.CYAN,RECORD,Fore.WHITE)
    elif searchRequest == currentCountry:
      print(Fore.CYAN,RECORD,Fore.WHITE)
    elif searchRequest == vehicle:
      print(Fore.CYAN,RECORD,Fore.WHITE)
    elif searchRequest == deposit:
      print(Fore.CYAN,RECORD,Fore.WHITE)
    else:
      searchRequest = str(input("Enter the " + searchCategory + "\n--> "))

  '''searchCategory = str(input("Enter filter to apply\n--> ")).lower()
  if searchCategory == 'forename':
      category = forename
      print(Fore.GREEN,Style.BRIGHT,"Filter category applied.",Style.RESET_ALL)
      time.sleep(1)
      new_section()
  elif searchCategory == 'surname':
      category = surname
      print(Fore.GREEN,Style.BRIGHT,"Filter category applied.",Style.RESET_ALL)
      time.sleep(1)
      new_section()
  elif searchCategory == 'gender':
      category = gender
      print(Fore.GREEN,Style.BRIGHT,"Filter category applied.",Style.RESET_ALL)
      time.sleep(1)
      new_section()
  elif searchCategory == 'age':
      category = age
      print(Fore.GREEN,Style.BRIGHT,"Filter category applied.",Style.RESET_ALL)
      time.sleep(1)
      new_section()
  elif searchCategory == 'country':
      category = currentCountry
      print(Fore.GREEN,Style.BRIGHT,"Filter category applied.",Style.RESET_ALL)
      time.sleep(1)
      new_section()
  elif searchCategory == 'vehicle':
      category = vehicle
      print(Fore.GREEN,Style.BRIGHT,"Filter category applied.",Style.RESET_ALL)
      time.sleep(1)
      new_section()
  elif searchCategory == 'deposit':
      category = deposit
      print(Fore.GREEN,Style.BRIGHT,"Filter category applied.",Style.RESET_ALL)
      time.sleep(1)
      new_section()
  else:
      print(Fore.RED,Style.BRIGHT,"\nNo such filter exists.\n",Style.RESET_ALL)
      time.sleep(1)
      new_section()
      searchCategory = str(input("Enter filter to apply\n--> "))
'''

  #searchRequest = str(input("Enter the " + searchCategory + "\n--> "))
  
  '''for row in reader:
    if searchRequest == forename:
      print(Fore.CYAN,RECORD,Fore.WHITE)
    elif searchRequest == surname:
      print(Fore.CYAN,RECORD,Fore.WHITE)
    elif searchRequest == gender:
      print(Fore.CYAN,RECORD,Fore.WHITE)
    elif searchRequest == age:
      print(Fore.CYAN,RECORD,Fore.WHITE)
    elif searchRequest == currentCountry:
      print(Fore.CYAN,RECORD,Fore.WHITE)
    elif searchRequest == vehicle:
      print(Fore.CYAN,RECORD,Fore.WHITE)
    elif searchRequest == deposit:
      print(Fore.CYAN,RECORD,Fore.WHITE)
    else:
      searchRequest = str(input("Enter the " + searchCategory + "\n--> "))
'''
#main program
read_customers()


'''#loop through csv list
for row in csv_file:
    #if current rows 2nd value is equal to input, print that row
    if number == row[1]:
         print(row)'''