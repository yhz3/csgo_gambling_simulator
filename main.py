import random
import gamma_case

BLUE = 0.7992
PURPLE = 0.1598
PINK = 0.032
RED = 0.0064
GOLD = 0.0026


def unbox():
    rarity = random.uniform(0,1)
    if rarity <= BLUE:
        gamma_case.gun("mil-spec")
        print("Mil-Spec (Blue)\nProbability: " + str(BLUE*100) + "%")
    elif rarity <= BLUE + PURPLE:
        gamma_case.gun("restricted")
        print("Restricted (Purple)\nProbability: " + str(PURPLE*100) + "%")
    elif rarity <= BLUE + PURPLE + PINK:
        print("Classified (Pink)\nProbability: " + str(PINK*100) + "%")
    elif rarity <= BLUE + PURPLE + PINK + RED:
        print("Covert (Red)\nProbability: " + str(RED*100) + "%")
    else:
        print("Rare Special Item (Gold)\nProbability: " + str(GOLD*100) + "%")

unbox()