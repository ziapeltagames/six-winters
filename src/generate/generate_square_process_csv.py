import random, os, sys

columns = ["name","points","bonus","x1","x2","y1","y2","locregion","locresource","background","iconeffect","texteffect"]

colors=["LL","GG","YY","OO","BB","MM"]
all_colors=["LL","GG","GG","YY","OO","OO","BB","BB","MM"]
em_colors=["MM","OO","GG"]
bd_colors=["GG","BB","YY"]
sl_colors=["LL","OO","BB"]
resources=["xxDIPLOMACY","xxMILITARY","xxSTABILITY","xxTECHNOLOGY","xxSORCERY","xxESPIONAGE"]
numbers=["ONE","TWO","THREE","FOUR","FIVE","SIX"]
regions=["xxEMPIRE","xxBRIGHTDUNE","xxSETTLED"]
region_colors=["EMxxFSQUAREEM","RBxxFSQUARERB","SLxxFSQUARESL"]
bonuses=["BLxxSORCERYBL","OOxxTECHNOLOGYOO","MMxxESPIONAGEMM","LLxxDIPLOMACYLL","GGxxMILITARYGG","YYxxSTABILITYYY"]
skills=["xxRAPPORT","xxDISGUISE","xxCOMMAND","xxLORE","xxSURVIVAL","xxCOMBAT","xxTACTICS","xxTHIEVERY"]

destinations=["Vault","Dungeon","Peak","Crypt","Hall"]
other_effect=["Angry: xxDEFENSExxDEFENSE"]
abilities=["xxDEFENSE","xxOVERCOME","xxMOVE",
           "xxSORCERY xxRIGHT xxASSET","xxMILITARY xxRIGHT xxDIPLOMACY","xxTECHNOLOGY xxRIGHT xxESPIONAGE",
           "xxSTABILITY xxRIGHT xxTECHNOLOGY","xxPSYCHExxPSYCHE","xxBODYxxBODY"]

# Have 60 progress cards (4 * 6 = 24 bonus symbols)
# Put six in each

def random_effect(score):
    score = int(score) + random.randint(1,6)
    score = str(score)
    if random.randint(1,2) < 2:
        icon = ","
        if random.randint(1,6) < 6:
            dest = random.choice(destinations)
            dest = dest + ":" + score + ","
        else:
            dest = random.choice(other_effect) + ","
    else:
        dest=","
        icon = random.choice(abilities) + ","

    return icon+dest
    


def get_region_by_color(color):
    if color == "LL":
        return regions[2]+",SL"+resources[0]+"SL,"+region_colors[2]
    if color == "GG":
        if random.randint(1,2) < 2:
            return regions[0]+",EM"+resources[1]+"EM,"+region_colors[0]
        else:
            return regions[1]+",BD"+resources[1]+"BD,"+region_colors[1]
    if color == "YY":
        return regions[1]+",BD"+resources[2]+"BD,"+region_colors[1]
    if color == "OO":
        if random.randint(1,2) < 2:
            return regions[0]+",EM"+resources[3]+"EM,"+region_colors[0]
        else:
            return regions[2]+",SL"+resources[3]+"SL,"+region_colors[2]
    if color == "BB":
        if random.randint(1,2) < 2:
            return regions[1]+",BD"+resources[4]+"BD,"+region_colors[1]
        else:
            return regions[2]+",SL"+resources[4]+"SL,"+region_colors[2]
    if color == "MM":
        return regions[0]+",EM"+resources[5]+"EM,"+region_colors[0]
        
def get_random_region():
    color = random.choice(all_colors)
    return get_region_by_color(color)

# 20 Color or number
NUM_ONES = 20
def generate_one_pointer(bonus_index):
    
    # Generate color
    if random.randint(1,3) < 3:
        color = random.choice(colors)
        scolor = color+"xxFSQUARE"+color
        squares = scolor+",,,,"
        region = get_region_by_color(color)
    # Generate number
    else:
        num = random.choice(numbers)
        squares = "WWxxFSQUAREWW,,xxW"+num+",,"
        region = get_random_region()

    skill = random.choice(skills)

    return "Placeholder Name,3,"+skill+","+squares+region+","+random_effect(3)

# 15 Number or region
NUM_TWOS=15
def generate_two_pointer(bonus_index):
    if random.randint(1,2) < 2:
        num = random.choice(numbers)
        squares = "WWxxFSQUAREWW,,xxW"+num+",,"
        region = get_random_region()
    else:
        res_region = random.choice(regions)
        squares = "WWxxFSQUAREWW,,"+res_region+",,"
        if res_region == regions[0]:
            region = get_region_by_color(random.choice(em_colors))
        elif res_region == regions[1]:
            region = get_region_by_color(random.choice(bd_colors))
        else:
            region = get_region_by_color(random.choice(sl_colors))
        
    if bonus_index < len(bonuses):
        bonus = bonuses[bonus_index]
    else:
        bonus = random.choice(skills)

    return "Placeholder Name,4,"+bonus+","+squares+region+","+random_effect(4)

# 15 Number and color
NUM_THREES = 13
def generate_three_pointer(bonus_index):
    color = random.choice(colors)
    num = random.choice(numbers)
    squares = "WWxxFSQUAREWW,,"+color+"xx"+num+color+",,"
    region = get_region_by_color(color)

    if bonus_index < len(bonuses):
        bonus = bonuses[bonus_index]
    else:
        bonus = random.choice(skills)

    return "Placeholder Name,5,"+bonus+","+squares+region+","+random_effect(5)

# 10 Random combo of two and two
NUM_FOURS = 6
def generate_four_pointer(bonus_index):

    sel1 = random.randint(1,3)

    if sel1 == 1:
        res_region1 = random.choice(regions)
        sec2 = "WWxxFSQUAREWW,"
        sec5 = ""+res_region1+","
    elif sel1 == 2:
        color1 = random.choice(colors)
        sec2 = ""+color1+"xxFSQUARE"+color1+","
        sec5 = ","
    else:
        num1 = random.choice(numbers)
        sec2 = "WWxxFSQUAREWW,"
        sec5 = "xxW"+num1+","

    sel2 = random.randint(1,3)

    if sel2 == 1:
        res_region2 = random.choice(regions)
        sec3 = "WWxxFSQUAREWW,"
        sec6 = ""+res_region2+","
    elif sel2 == 2:
        color2 = random.choice(colors)
        sec3 = ""+color2+"xxFSQUARE"+color2+","
        sec6 = ","
    else:
        num2 = random.choice(numbers)
        sec3 = "WWxxFSQUAREWW,"
        sec6 = "xxW"+num2+","

    squares = sec2+sec3+sec5+sec6
    
    region = get_random_region()

    score = str(random.randint(6,8))

    if bonus_index < len(bonuses):
        bonus = bonuses[bonus_index]
    else:
        bonus = random.choice(skills)

    return "Placeholder Name,"+score+","+bonus+","+squares+region+","+random_effect(score)

# 10 Random combo of three and two
NUM_FIVES = 6
def generate_five_pointer(bonus_index):

    color1 = random.choice(colors)
    num1 = random.choice(numbers)

    color2 = random.choice(colors)
    num2 = random.choice(numbers)

    squares = "WWxxFSQUAREWW,WWxxFSQUAREWW,"+color1+"xx"+num1+color1+","+color2+"xx"+num2+color2
    
    if random.randint(1,2) < 2:
        region = get_region_by_color(color1)
    else:
        region = get_region_by_color(color2)

    if bonus_index < len(bonuses):
        bonus = bonuses[bonus_index]
    else:
        bonus = random.choice(skills)

    score = str(random.randint(9,10))

    return "Placeholder Name,"+score+","+bonus+","+squares+","+region+","+random_effect(score)

original_stdout = sys.stdout
with open (".\\csv\\square-progress-cards.csv", "w") as csvfile:

    sys.stdout=csvfile

    # Print csv header
    for i in range(len(columns) -1):
        print(columns[i], ',', end='', sep='')
    print(columns[-1])

    print()

    for i in range(NUM_ONES):
        print(generate_one_pointer(i), end='', sep='')
        print()

    for i in range(NUM_TWOS):
        print(generate_two_pointer(i), end='', sep='')
        print()

    for i in range(NUM_THREES):
        print(generate_three_pointer(i), end='', sep='')
        print()

    for i in range(NUM_FOURS):
        print(generate_four_pointer(i), end='', sep='')
        print()

    for i in range(NUM_FIVES):
        print(generate_five_pointer(i), end='', sep='')
        print()

    sys.stdout = original_stdout