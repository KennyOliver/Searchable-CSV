import csv,time,colorama,random
from colorama import Fore,Style
#import libraries

#title/header
print(Fore.LIGHTBLUE_EX,Style.BRIGHT,"\n" + "_" * 30)
print("| 𝙸𝚗𝚜𝚞𝚛𝚊𝚗𝚌𝚎 𝙲𝚘𝚖𝚙𝚊𝚗𝚢 𝙳𝚊𝚝𝚊𝚋𝚊𝚜𝚎 |")
print("¯" * 30 + "\n\n",Style.RESET_ALL)

#re-runs the program
def rerun ():
  '''ask = input("\nSearch for more?\nY or N\n--> ").upper()
  if ask == 'Y':
    print("\n")
    time.sleep(1)
    read_customers()
  else:
    None'''
  new_section ()
  read_customers ()

#prints a pattern to make UI split into sections
def new_section ():
  print(Fore.WHITE,Style.BRIGHT,">--------------------<\n",Style.RESET_ALL)

#main program
def read_customers ():
  #opens the CSV file
  CUSTOMERS = open('database_customers.csv','r')
  reader = csv.reader(CUSTOMERS)

  CategoryString = "category"

  #Values set FIRST in order to be used before, having proper values overwritten onto them
  forename = 0
  surname  = 1
  gender   = 2
  age      = 3
  currentCountry = 4
  vehicle  = 5
  deposit  = 6
  
  #FILTER MECHANISM so that individual columns of the CSV are searched
  searchCategory = str(input("Enter filter to apply\n  • Forename\n  • Surname\n  • Gender\n  • Age\n  • Country (ie. Current Country)\n  • Vehicle\n  • Deposit\nCommands\n  • /all\n  • /settings (BROKEN)\n——> ")).lower()
  #Search Categories
  if searchCategory == 'forename':
      category = forename
      print(Fore.GREEN,Style.BRIGHT,"\nFORENAME category applied.",Style.RESET_ALL)
      time.sleep(1)
      new_section()
  elif searchCategory == 'surname':
      category = surname
      print(Fore.GREEN,Style.BRIGHT,"\nSURNAME category applied.",Style.RESET_ALL)
      time.sleep(1)
      new_section()
  elif searchCategory == 'gender':
      category = gender
      print(Fore.GREEN,Style.BRIGHT,"\nGENDER category applied.",Style.RESET_ALL)
      time.sleep(1)
      new_section()
  elif searchCategory == 'age':
      category = age
      print(Fore.GREEN,Style.BRIGHT,"\nAGE category applied.",Style.RESET_ALL)
      time.sleep(1)
      new_section()
  elif searchCategory == 'country':
      category = currentCountry
      print(Fore.GREEN,Style.BRIGHT,"\nCURRENT COUNTRY category applied.",Style.RESET_ALL)
      time.sleep(1)
      new_section()
  elif searchCategory == 'vehicle':
      category = vehicle
      print(Fore.GREEN,Style.BRIGHT,"\nVEHICLE category applied.",Style.RESET_ALL)
      time.sleep(1)
      new_section()
  elif searchCategory == 'deposit':
      category = deposit
      print(Fore.GREEN,Style.BRIGHT,"\nDEPOSIT category applied.",Style.RESET_ALL)
      time.sleep(1)
      new_section()
  elif searchCategory == '/all' or searchCategory == '/ALL':
    category = 'ALL'
    print(Fore.GREEN,Style.BRIGHT,"\nPrinting ALL",Style.RESET_ALL)
    time.sleep(1)
    new_section()
  elif searchCategory == '/settings' or searchCategory == '/SETTINGS':
    category = 'SETTINGS'
    print(Fore.GREEN,Style.BRIGHT,"\nLoading Settings...",Style.RESET_ALL)
    time.sleep(1)
    new_section()
  else:
      print(Fore.RED,Style.BRIGHT,"\nNo such filter exists.\n",Style.RESET_ALL)
      time.sleep(1)
      new_section()
      searchCategory = str(input("Please, enter filter to apply\n——> ")).lower()
  
  if searchCategory == 'age':
    '''searchRequest = str(input("Enter the " + searchCategory + ' ' + CategoryString + "\n——> "))'''
    searchRequest = input("Enter the " + searchCategory + " [10] [20] [30] [40] [50] [60] [70] [80]\n——> ")
  elif searchCategory == 'gender':
    searchRequest = input("Enter the " + searchCategory + " [M] [F] [?]\n——> ")
  elif searchCategory == 'deposit':
    searchRequest = input("Enter the " + searchCategory + " size\n[TINY] [SMALL] [MEDIUM] [LARGE]\n——> ")
  elif searchCategory == '/all' or searchCategory == '/ALL':
    searchRequest = 'PRINT_ALL'
  elif searchCategory == '/settings' or searchCategory == '/SETTINGS':
    searchRequest = 'SETTINGS'
  else:
    searchRequest = str(input("Enter the " + searchCategory + "\n——> "))


  if searchRequest == 'm' or searchRequest == 'male':
    searchRequest = 'M'
  elif searchRequest == 'f' or searchRequest == 'female':
    searchRequest = 'F'
  
  if searchRequest == 'australia':
    searchRequest == 'Australia'
  elif searchRequest == 'canada':
    searchRequest == 'Canada'
  elif searchRequest == 'england':
    searchRequest == 'England'
  elif searchRequest == 'new zealand':
    searchRequest == 'New Zealand'
  
  if searchRequest == 'bicycle':
    searchRequest = 'bike'
  
  if searchRequest == 'tiny' or searchRequest == 't' or searchRequest == 'T':
    searchRequest == 'TINY'
  elif searchRequest == 'small' or searchRequest == 's' or searchRequest == 'S':
    searchRequest == 'SMALL'
  elif searchRequest == 'medium' or searchRequest == 'm' or searchRequest == 'M':
    searchRequest == 'MEDIUM'
  elif searchRequest == 'large' or searchRequest == 'l' or searchRequest == 'L':
    searchRequest == 'LARGE'

  COUNT = 0

  #All the code within the for loop prints out 1 cyan/blue-colored record!
  for record in reader:
    forename = record[0]
    surname  = record[1]
    gender   = record[2]
    age      = record[3]
    currentCountry = record[4]
    vehicle  = record[5]
    deposit  = record[6]
    roundDeposit = int(float(deposit))
    #int() rounds down, round() rounds up & down
    if deposit >= '750':
      DEPOSIT = "LARGE"
    elif deposit >= '500':
      DEPOSIT = "MEDIUM"
    elif deposit >= '250':
      DEPOSIT = "SMALL"
    elif deposit <= '249':
      DEPOSIT = "TINY"
    
    COUNT += 1
    toggleCOUNT = 1
    COUNTstate = True

    RANDOM = random.randint(6,16)/60
    time.sleep(RANDOM)

    RECORD = str(COUNT)+'> '+forename+'|'+surname+'|'+gender+'|' +age+'+'+'|'+currentCountry+'|'+vehicle+'|'+DEPOSIT+':'+str(roundDeposit)+'('+'£'+deposit+')'

    if searchRequest == 'SETTINGS':
      if COUNTstate == True:
        print("COUNT is currently "+Fore.GREEN,Style.BRIGHT,"ON",Style.RESET_ALL)
      elif COUNTstate == False:
        print("COUNT is currently "+Fore.RED,Style.BRIGHT,"OFF",Style.RESET_ALL)

      print("Turn COUNT "+Fore.GREEN,"ON",Style.RESET_ALL+" or "+Fore.RED,"OFF",Style.RESET_ALL)
      toggleCOUNT = bool(input("Enter ON (1) or OFF (0)\n——> "))

      if toggleCOUNT == 'OFF' or '0':
        RECORD = forename+'|'+surname+'|'+gender+'|' +age+'+'+'|'+currentCountry+'|'+vehicle+'|'+DEPOSIT+':'+str(roundDeposit)+'('+'£'+deposit+')'
        COUNTstate = False
      elif toggleCOUNT == 'ON' or '1':
        RECORD = str(COUNT)+'> '+forename+'|'+surname+'|'+gender+'|' +age+'+'+'|'+currentCountry+'|'+vehicle+'|'+DEPOSIT+':'+str(roundDeposit)+'('+'£'+deposit+')'
        COUNTstate = True
      else:
        None

      new_section()
    elif searchRequest == forename:
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
    elif searchRequest == DEPOSIT:
      print(Fore.CYAN,RECORD,Fore.WHITE)
    elif searchRequest == 'PRINT_ALL':
      print(Fore.CYAN,RECORD,Fore.WHITE)
      #if DEPOSIT == searchRequest:
      #  print(Fore.CYAN,RECORD,Fore.WHITE)
    #This continues the program by forcing the user to give a proper value. HOWEVER, for some unknown reason, the program only prints out some/certain records??? A procedure which reruns the program seems to work best!
    '''else:
      searchRequest = str(input("Enter the " + searchCategory + "\n——> "))'''
  rerun()
#main program
read_customers()

#A program that I found from stack exchange (the only code which I copied!!!) that helped me to construct the search mechanism -- I was extremely confused/stuck when my program would only work for the first record. The main fix was that the massive if chains were in the wrong order, and minor shuffling + setting the temporary false values (as commented earlier) helped to make this program function :)
'''#loop through csv list
for row in csv_file:
    #if current rows 2nd value is equal to input, print that row
    if number == row[1]:
         print(row)'''


#This program took a long time to make (about 4/5 hrs even though it looks simple! - Kenny  Oliver Sat 28th March 2020 at 17:58)

# ©Kenny 2020