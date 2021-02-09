import csv
import time
import colorama
import random
from colorama import Fore,Style
from search_customers import search_customers
from input_data import input_data
from new_section import new_section


#title/header
print(Fore.LIGHTBLUE_EX,Style.BRIGHT,"\n" + "_" * 30)
print("| 𝙸𝚗𝚜𝚞𝚛𝚊𝚗𝚌𝚎 𝙲𝚘𝚖𝚙𝚊𝚗𝚢 𝙳𝚊𝚝𝚊𝚋𝚊𝚜𝚎 |")
print("¯" * 30 + "\n\n",Style.RESET_ALL)
#====================
def rerun(): #re-runs the program
  new_section()
  search_customers()
#====================

#====================
def choose_task():
  ask = input("Choose:\n[1] Search database\n[2] Enter Data\n--> ")
  if ask == '1':
    search_customers()
  elif ask == '2':
    input_data()
    new_section()
    choose_task()
  else:
    choose_task()

# main program
choose_task()