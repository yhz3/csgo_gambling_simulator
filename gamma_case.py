import random


mil_spec = {0: "Five-SeveN | Violent Daimyo", 1: "P250 | Iron Clad", 2: "Nova | Exo", 3: "Tec-9 | Ice Cap",
            4: "MAC-10| Carnivore", 5: "SG 553 | Aerial", 6: "PP-Bizon | Harvester"}

restricted = {0: "Sawed-Off | Limelight", 1: "P90 | Chopper", 2: "AUG | Aristocrat", 3: "R8 Revolver | Reboot",
              4: "AWP | Phobos"}

classified = {0: "SCAR-20 | Bloodsport", 1: "P2000 | Imperial Dragon", 2: "M4A4 | Desolate Space"}

covert = {0: "Glock-18 | Wasteland Rebel", 1: "M4A1-S | Mecha Industries"}


def gun(rarity: str):
    if rarity == "mil-spec":
        item = random.randint(0,6)
        print(mil_spec[item])
    elif rarity == "restricted":
        item = random.randint(0,4)
        print(restricted[item])
    elif rarity == "classified":
        item = random.randint(0,2)
        print(restricted[item])
    elif rarity == "covert":
        item = random.randint(0,1)
        print(restricted[item])


