import csv,time,colorama,random
from colorama import Fore,Style
#import libraries
#import search_customers, input_data
from search_customers import search_customers
from input_data import input_data


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
    search_customers()
  else:
    None'''
  new_section ()
  search_customers ()

#prints a pattern to make UI split into sections
def new_section ():
  print(Fore.WHITE,Style.BRIGHT,">--------------------<\n",Style.RESET_ALL)

#main program
'''search_customers()'''

def choose_task():
  ask = input("Choose:\n[1] Search database\n[2] Enter Data\n--> ")
  if ask == '1':
    search_customers()
  elif ask == '2':
    input_data()
  else:
    None
  choose_task

choose_task()