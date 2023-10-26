import random
import sys
from time import sleep

import gamma_case

BLUE = 0.7992
PURPLE = 0.1598
PINK = 0.032
RED = 0.0064
GOLD = 0.0026


def unbox():
    rarity = random.uniform(0,1)
    if rarity <= BLUE:
        gamma_case.GammaCase().gun("mil-spec")
        print("Mil-Spec (Blue)\nProbability: " + str(BLUE*100) + "%")
    elif rarity <= BLUE + PURPLE:
        gamma_case.GammaCase().gun("restricted")
        print("Restricted (Purple)\nProbability: " + str(PURPLE*100) + "%")
    elif rarity <= BLUE + PURPLE + PINK:
        gamma_case.GammaCase().gun("classified")
        print("Classified (Pink)\nProbability: " + str(PINK*100) + "%")
    elif rarity <= BLUE + PURPLE + PINK + RED:
        gamma_case.GammaCase().gun("covert")
        print("Covert (Red)\nProbability: " + str(RED*100) + "%")
    else:
        print("Rare Special Item (Gold)\nProbability: " + str(GOLD*100) + "%")


money_spent = 0.00
cases_opened = 0

while input("Open Case\n\n\n\n\n\n\n\n\n\n\n") == "":
    text = "Loading...\n"
    for i in range(3):
        for x in text:
            print(x, end='')
            sys.stdout.flush()
            sleep(0.075)
    input("View Item")
    unbox()
    money_spent = round(money_spent + gamma_case.GammaCase().get_open_price(), 3)
    cases_opened += 1
    print("Cases opened: " + str(cases_opened))
    print("Total Spent: USD " + str(money_spent))
    print("\n\n\n\n\n")
    input("")