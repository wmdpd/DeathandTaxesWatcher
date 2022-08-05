# Importing player log file as an object file
playerlog = open("AppData/LocalLow/Placeholder Gameworks/Death and Taxes/Player.log")

# Defining each of the relevant statistics
Ecology = int(0)
Prosperity = int(0)
Peace = int(0)
Health = int(0)
Loyalty = int(0)
Ecology_Daily = int(0)
Prosperity_Daily = int(0)
Peace_Daily = int(0)
Health_Daily = int(0)


# Resets all Global Variables to 0
def resetStats():
    global Ecology
    global Prosperity
    global Peace
    global Health
    global Loyalty
    global Ecology_Daily
    global Prosperity_Daily
    global Peace_Daily
    global Health_Daily
    Ecology = int(0)
    Prosperity = int(0)
    Peace = int(0)
    Health = int(0)
    Loyalty = int(0)
    Ecology_Daily = int(0)
    Prosperity_Daily = int(0)
    Peace_Daily = int(0)
    Health_Daily = int(0)

# Resets all Daily Global Variables to 0
def resetDailyStats():
    global Ecology_Daily
    global Prosperity_Daily
    global Peace_Daily
    global Health_Daily
    Ecology_Daily = int(0)
    Prosperity_Daily = int(0)
    Peace_Daily = int(0)
    Health_Daily = int(0)

# Finds the value the stat has been changed by
def findStat(line):
    newStat = int(line.partition(" to ")[2])
    return newStat

# Calculations on statistics throughout a game
# Carryover Complete indicates a new NewGame+ save
for line in playerlog:
    if "Carryover complete" in line:
        resetStats()
    if "Getting" in line:
        resetDailyStats()
    if "Modified stat ECOLOGY by" in line:
        Ecology = findStat(line)
    if "Modified stat PROSPERITY by" in line:
        Prosperity = findStat(line)
    if "Modified stat PEACE by" in line:
        Peace = findStat(line)
    if "Modified stat HEALTH by" in line:
        Health = findStat(line)
    if "Modified stat LOYALTY by" in line:
        Loyalty = findStat(line)
    if "Modified stat ECOLOGY_DAILY by" in line:
        Ecology_Daily = findStat(line)
    if "Modified stat PROSPERITY_DAILY by" in line:
        Prosperity_Daily = findStat(line)
    if "Modified stat PEACE_DAILY by" in line:
        Peace_Daily = findStat(line)
    if "Modified stat HEALTH_DAILY by" in line:
        Health_Daily = findStat(line)

# Statistics Dictionaries defined for easier printing
Stats = {
    'Ecology': Ecology,
    'Prosperity': Prosperity,
    'Peace': Peace,
    'Health': Health,
    'Loyalty': Loyalty}
Daily_Stats = {
    'Ecology_Daily': Ecology_Daily,
    'Prosperity_Daily': Prosperity_Daily,
    'Peace_Daily': Peace_Daily,
    'Health_Daily': Health_Daily}

# Calculates the overall average reputation
avgRep = str(int((Ecology + Prosperity + Peace + Health)/4))

# Printing out the statistics & closing the file
print("Total Statistics for Current Run:")
for key, value in Stats.items():
    print(key, ' : ', value)
print("Average Rep: " + avgRep)
print("")
print("Daily Statistics:")
for key, value in Daily_Stats.items():
    print(key, ' : ', value)

playerlog.close()


