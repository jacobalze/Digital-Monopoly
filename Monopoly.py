import time
import turtle
gametype = "" #Selecting the game type from user input (Standard or Secret Vault)
#Barcode Ids:
#Box barcodes:
standardid = "195166146355" 
vaultid = "195166190921"
builderid = "195166145440"
#Player Barcodes and names:(DO NOT CHANGE)
playerOne = ""
playerTwo = ""
playerThree = ""
playerFour = ""
playerFive = ""
playerSix = ""

playerOnen = ""
playerTwon = ""
playerThreen = ""
playerFourn = ""
playerFiven = ""
playerSixn = ""

#Vault card barcode: (secret vault only)
vaultcard = "99887766"
vaulttap = "fffb030d900"

#Property Barcodes:
mediterraneanid = "fff5628d900"
balticid = "fff171d900"
orientalid = "fff4e28d900"
vermontid = "fffe626d900"
connecticutid = "fff151d900"
stcharlesid = "fff1c1d900"
statesid = "fffadffd800"
virginiaid = "fffacffd800"
stjamesid = "fff4f28d900"
tennesseeid = "fff5428d900"
newyorkid = "fffe426d900"
kentuckyid = "fff5528d900"
indianaid = "fffe526d900"
illinoisid = "fff5228d900"
atlanticid = "fff131d900"
ventnorid = "fff1d1d900"
marvinid = "fff5328d900"
pacificid = "fff5128d900"
northcarolinaid = "fff141d900"
pennsylvaniaid = "fff161d900"
parkplaceid = "fff1e1d900"
boardwalkid = "fff5028d900"

#Railroad & Utillity Barcodes (standard only):
readingrid = "fff4d28d900"
pennsylvaniarid = "fff1b1d900"
bandorid = "fff181d900"
shortlinerid = "fff52d900"
electricid = "fff1a1d900"
waterworksid = "fff191d900"

#Banker's card barcodes:
buy = "74123698"
auction = "78996332"
payrent = "55633214"
incometax = "65498731"
luxurytax = "99866532"
getoutofjail = "78945612"
passgo = "33266855"
buildahouse = "56956953"
checkbalance = "32568697"
checkvbalance = "96385274"
checkprops = "02365894"
buyproperty = "56977896"
banktoplayer = "74185296"
playertobank = "35795182"
playertoplayer = "99863456"
playertovault = "39586684"
banktovault = "69542656"
endgame = "95569569"
error = "56956985"
recovery = "11256389"

#Settings:
startingAmount = 1500 #Amount you start with

passGoAmount = 200 #Ammount you earn from passing go

#Property amount for buying:
mediterraneanb = 60
balticb = 60
orientalb = 100
vermontb = 100
connecticutb = 120
stcharlesb = 140
statesb = 160
virginiab = 160
stjamesb = 180
tennesseeb = 180
newyorkb = 200
kentuckyb = 220
indianab = 220
illinoisb = 240
atlanticb = 260
ventnorb = 260
marvinb = 280
pacificb = 300
northcarolinab = 300
pennsylvaniab = 320
parkplaceb = 350
boardwalkb = 400

#Railroad and utility (standard only):
railroadb = 200
utilityb = 150

#Rent Values
mediterraneanr = 2
balticr = 4
orientalr = 6
vermontr = 6
connecticutr = 8
stcharlesr = 10
statesr = 10
virginiar = 12
stjamesr = 14
tennesseer = 14
newyorkr = 16
kentuckyr = 18
indianar = 18
illinoisr = 20
atlanticr = 22
ventnorr = 22
marvinr = 24
pacificr = 26
northcarolinar = 26
pennsylvaniar = 28
parkplacer = 35
boardwalkr = 50
railroadr = 25


#House & Hotel buy:
mediterraneanhc = 50
baltichc = 50
orientalhc = 50
vermonthc = 50
connecticuthc = 50

stcharleshc = 100
stateshc = 100
virginiahc = 100
stjameshc = 100
tennesseehc = 100
newyorkhc = 100

kentuckyhc = 150
indianahc = 150
illinoishc = 150
atlantichc = 150
ventnorhc = 150
marvinhc = 150

pacifichc = 200
northcarolinahc = 200
pennsylvaniahc = 200
parkplacehc = 200
boardwalkhc = 200

#Other fees:
payincometax = 200
payluxurytax = 100
paygetoutofjail = 50

#Player Balances:
playerOneb = 0
playerTwob = 0
playerThreeb = 0
playerFourb = 0
playerFiveb = 0
playerSixb = 0

#Vault balance (Secret vault only):
vaultb = 400

#Player Properties:
properties = {
    "playerOnep": [],
    "playerTwop": [],
    "playerThreep": [],
    "playerFourp": [],
    "playerFivep": [],
    "playerSixp": []
}


houses = []
hotels = []

#Color Sets:
colorSets = {
    "Brown": ["Mediterranean", "Baltic"],
    "Light Blue": ["Oriental", "Vermont", "Connecticut"],
    "Pink": ["St. Charles", "States", "Virginia"],
    "Orange": ["St. James", "Tennessee", "New York"],
    "Red": ["Kentucky", "Indiana", "Illinois"],
    "Yellow": ["Atlantic", "Ventnor", "Marvin Gardens"],
    "Green": ["Pacific", "North Carolina", "Pennsylvania"],
    "Dark Blue": ["Park Place", "Boardwalk"],
    "Railroads": ["Reading Railroad", "Pennsylvania Railroad", "B&O Railroad", "Short Line"],
    "Utilities": ["Electric Company", "Water Works"]
}
#Houses and Hotels
houseshotels = {
    "Mediterranean": {"houses": 0, "hotel": False},
    "Baltic": {"houses": 0, "hotel": False},
    "Oriental": {"houses": 0, "hotel": False},
    "Vermont": {"houses": 0, "hotel": False},
    "Connecticut": {"houses": 0, "hotel": False},
    "St. Charles": {"houses": 0, "hotel": False},
    "States": {"houses": 0, "hotel": False},
    "Virginia": {"houses": 0, "hotel": False},
    "St. James": {"houses": 0, "hotel": False},
    "Tennessee": {"houses": 0, "hotel": False},
    "New York": {"houses": 0, "hotel": False},
    "Kentucky": {"houses": 0, "hotel": False},
    "Indiana": {"houses": 0, "hotel": False},
    "Illinois": {"houses": 0, "hotel": False},
    "Atlantic": {"houses": 0, "hotel": False},
    "Ventnor": {"houses": 0, "hotel": False},
    "Marvin Gardens": {"houses": 0, "hotel": False},
    "Pacific": {"houses": 0, "hotel": False},
    "North Carolina": {"houses": 0, "hotel": False},
    "Pennsylvania": {"houses": 0, "hotel": False},
    "Park Place": {"houses": 0, "hotel": False},
    "Boardwalk": {"houses": 0, "hotel": False}
}



propertiesAvalible = []
payamount = 0
currentproperty = ""
currentplayer = ""
utilityamount = 0
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
screen = turtle.Screen()
display = turtle.Turtle()
rrutils = turtle.Turtle()
hide = turtle.Turtle()
statusd = turtle.Turtle()
hide.penup()
statusd.penup()
hide.speed(0)
display.speed(0)
rrutils.speed(0)
statusd.speed(0)
playerColors = ["Green", "Orange", "Purple", "Yellow", "Blue", "Red"]
screen.register_shape("properties.gif")
screen.register_shape("railroads and utlities.gif")
display.penup()
display.goto(400,50)
display.shape("properties.gif")
pen.hideturtle()
hide.hideturtle()
statusd.hideturtle()
statusd.color("red")
hide.goto(645,392)
hide.color("grey")
hide.pendown()
hide.write("v1.2.0", font=("Open Sans", 10, "normal"))
hide.penup()
hide.color("white")

def status(text):
    statusd.clear()
    statusd.color("red")
    statusd.goto(-170,-170)
    statusd.write(text, font=("Open Sans", 20, "normal"))
    
def playerMarker():
    pen.begin_fill()
    for i in range(2):
        pen.forward(47)
        pen.left(90)
        pen.forward(17)
        pen.left(90)
    pen.end_fill()

def hideP():    
    hide.fillcolor("white")
    hide.begin_fill()
    for i in range(2):
        hide.forward(90)
        hide.right(90)
        hide.forward(93)
        hide.right(90)
    hide.end_fill()

def drawDisplay():
    pen.clear()
    pen.goto(-150,280)
    pen.color("red")
    pen.pendown()
    if (gametype == "standard"):
        pen.write("Game Type - Standard", font=("Open Sans", 15, "normal"))
    elif (gametype == "vault"):
        pen.write("Game Type - Secret Vault", font=("Open Sans", 15, "normal"))
    elif (gametype == "builder"):
        pen.write("Game Type - Builder", font=("Open Sans", 15, "normal"))
    pen.penup()
    pen.color("black")
    y = 230
    for i in range(playernum - 1):
        pen.goto(-580,y)
        pen.color(playerColors[i])
        pen.pendown()
        pen.write(balance_labels[i], font=("Open Sans", 20, "normal"))
        pen.penup()
        y -= 75
    if(gametype == "vault"):
        pen.goto(-580,-295)
        pen.color("red")
        pen.pendown()
        pen.write(f"Vault Balance - ${vaultb}", font=("Open Sans", 20, "normal"))
        pen.penup()
    pen.color("black")
    y=300
    if "Mediterranean" in properties["playerOnep"]:  # Mediterranean
        pen.fillcolor("green")
    elif "Mediterranean" in properties["playerTwop"]:
        pen.fillcolor("orange")
    elif "Mediterranean" in properties["playerThreep"]:
        pen.fillcolor("purple")
    elif "Mediterranean" in properties["playerFourp"]:
        pen.fillcolor("yellow")
    elif "Mediterranean" in properties["playerFivep"]:
        pen.fillcolor("blue")
    elif "Mediterranean" in properties["playerSixp"]:
        pen.fillcolor("red")
    else:
        pen.fillcolor("white")
    pen.goto(173, y)
    playerMarker()

    if "Baltic" in properties["playerOnep"]:  # Baltic
        pen.fillcolor("green")
    elif "Baltic" in properties["playerTwop"]:
        pen.fillcolor("orange")
    elif "Baltic" in properties["playerThreep"]:
        pen.fillcolor("purple")
    elif "Baltic" in properties["playerFourp"]:
        pen.fillcolor("yellow")
    elif "Baltic" in properties["playerFivep"]:
        pen.fillcolor("blue")
    elif "Baltic" in properties["playerSixp"]:
        pen.fillcolor("red")
    else:
        pen.fillcolor("white")
    pen.goto(250, y)
    playerMarker()

    if "Oriental" in properties["playerOnep"]:  # Oriental
        pen.fillcolor("green")
    elif "Oriental" in properties["playerTwop"]:
        pen.fillcolor("orange")
    elif "Oriental" in properties["playerThreep"]:
        pen.fillcolor("purple")
    elif "Oriental" in properties["playerFourp"]:
        pen.fillcolor("yellow")
    elif "Oriental" in properties["playerFivep"]:
        pen.fillcolor("blue")
    elif "Oriental" in properties["playerSixp"]:
        pen.fillcolor("red")
    else:
        pen.fillcolor("white")
    pen.goto(348, y)
    playerMarker()

    if "Vermont" in properties["playerOnep"]:  # Vermont
        pen.fillcolor("green")
    elif "Vermont" in properties["playerTwop"]:
        pen.fillcolor("orange")
    elif "Vermont" in properties["playerThreep"]:
        pen.fillcolor("purple")
    elif "Vermont" in properties["playerFourp"]:
        pen.fillcolor("yellow")
    elif "Vermont" in properties["playerFivep"]:
        pen.fillcolor("blue")
    elif "Vermont" in properties["playerSixp"]:
        pen.fillcolor("red")
    else:
        pen.fillcolor("white")
    pen.goto(423, y)
    playerMarker()

    if "Connecticut" in properties["playerOnep"]:  # Connecticut
        pen.fillcolor("green")
    elif "Connecticut" in properties["playerTwop"]:
        pen.fillcolor("orange")
    elif "Connecticut" in properties["playerThreep"]:
        pen.fillcolor("purple")
    elif "Connecticut" in properties["playerFourp"]:
        pen.fillcolor("yellow")
    elif "Connecticut" in properties["playerFivep"]:
        pen.fillcolor("blue")
    elif "Connecticut" in properties["playerSixp"]:
        pen.fillcolor("red")
    else:
        pen.fillcolor("white")
    pen.goto(495, y)
    playerMarker()

    y = 179

    if "St. Charles" in properties["playerOnep"]:  # St. Charles
        pen.fillcolor("green")
    elif "St. Charles" in properties["playerTwop"]:
        pen.fillcolor("orange")
    elif "St. Charles" in properties["playerThreep"]:
        pen.fillcolor("purple")
    elif "St. Charles" in properties["playerFourp"]:
        pen.fillcolor("yellow")
    elif "St. Charles" in properties["playerFivep"]:
        pen.fillcolor("blue")
    elif "St. Charles" in properties["playerSixp"]:
        pen.fillcolor("red")
    else:
        pen.fillcolor("white")
    pen.goto(173, y)
    playerMarker()

    if "States" in properties["playerOnep"]:  # States
        pen.fillcolor("green")
    elif "States" in properties["playerTwop"]:
        pen.fillcolor("orange")
    elif "States" in properties["playerThreep"]:
        pen.fillcolor("purple")
    elif "States" in properties["playerFourp"]:
        pen.fillcolor("yellow")
    elif "States" in properties["playerFivep"]:
        pen.fillcolor("blue")
    elif "States" in properties["playerSixp"]:
        pen.fillcolor("red")
    else:
        pen.fillcolor("white")
    pen.goto(250, y)
    playerMarker()

    if "Virginia" in properties["playerOnep"]:  # Virginia
        pen.fillcolor("green")
    elif "Virginia" in properties["playerTwop"]:
        pen.fillcolor("orange")
    elif "Virginia" in properties["playerThreep"]:
        pen.fillcolor("purple")
    elif "Virginia" in properties["playerFourp"]:
        pen.fillcolor("yellow")
    elif "Virginia" in properties["playerFivep"]:
        pen.fillcolor("blue")
    elif "Virginia" in properties["playerSixp"]:
        pen.fillcolor("red")
    else:
        pen.fillcolor("white")
    pen.goto(320,y)
    playerMarker()
    if "St. James" in properties["playerOnep"]:  # St. James
        pen.fillcolor("green")
    elif "St. James" in properties["playerTwop"]:
        pen.fillcolor("orange")
    elif "St. James" in properties["playerThreep"]:
        pen.fillcolor("purple")
    elif "St. James" in properties["playerFourp"]:
        pen.fillcolor("yellow")
    elif "St. James" in properties["playerFivep"]:
        pen.fillcolor("blue")
    elif "St. James" in properties["playerSixp"]:
        pen.fillcolor("red")
    else:
        pen.fillcolor("white")
    pen.goto(422, y)
    playerMarker()

    if "Tennessee" in properties["playerOnep"]:  # Tennessee
        pen.fillcolor("green")
    elif "Tennessee" in properties["playerTwop"]:
        pen.fillcolor("orange")
    elif "Tennessee" in properties["playerThreep"]:
        pen.fillcolor("purple")
    elif "Tennessee" in properties["playerFourp"]:
        pen.fillcolor("yellow")
    elif "Tennessee" in properties["playerFivep"]:
        pen.fillcolor("blue")
    elif "Tennessee" in properties["playerSixp"]:
        pen.fillcolor("red")
    else:
        pen.fillcolor("white")
    pen.goto(498, y)
    playerMarker()

    if "New York" in properties["playerOnep"]:  # New York
        pen.fillcolor("green")
    elif "New York" in properties["playerTwop"]:
        pen.fillcolor("orange")
    elif "New York" in properties["playerThreep"]:
        pen.fillcolor("purple")
    elif "New York" in properties["playerFourp"]:
        pen.fillcolor("yellow")
    elif "New York" in properties["playerFivep"]:
        pen.fillcolor("blue")
    elif "New York" in properties["playerSixp"]:
        pen.fillcolor("red")
    else:
        pen.fillcolor("white")
    pen.goto(570, y)
    playerMarker()

    y = 49

    if "Kentucky" in properties["playerOnep"]:  # Kentucky
        pen.fillcolor("green")
    elif "Kentucky" in properties["playerTwop"]:
        pen.fillcolor("orange")
    elif "Kentucky" in properties["playerThreep"]:
        pen.fillcolor("purple")
    elif "Kentucky" in properties["playerFourp"]:
        pen.fillcolor("yellow")
    elif "Kentucky" in properties["playerFivep"]:
        pen.fillcolor("blue")
    elif "Kentucky" in properties["playerSixp"]:
        pen.fillcolor("red")
    else:
        pen.fillcolor("white")
    pen.goto(173, y)
    playerMarker()

    if "Indiana" in properties["playerOnep"]:  # Indiana
        pen.fillcolor("green")
    elif "Indiana" in properties["playerTwop"]:
        pen.fillcolor("orange")
    elif "Indiana" in properties["playerThreep"]:
        pen.fillcolor("purple")
    elif "Indiana" in properties["playerFourp"]:
        pen.fillcolor("yellow")
    elif "Indiana" in properties["playerFivep"]:
        pen.fillcolor("blue")
    elif "Indiana" in properties["playerSixp"]:
        pen.fillcolor("red")
    else:
        pen.fillcolor("white")
    pen.goto(250, y)
    playerMarker()

    if "Illinois" in properties["playerOnep"]:  # Illinois
        pen.fillcolor("green")
    elif "Illinois" in properties["playerTwop"]:
        pen.fillcolor("orange")
    elif "Illinois" in properties["playerThreep"]:
        pen.fillcolor("purple")
    elif "Illinois" in properties["playerFourp"]:
        pen.fillcolor("yellow")
    elif "Illinois" in properties["playerFivep"]:
        pen.fillcolor("blue")
    elif "Illinois" in properties["playerSixp"]:
        pen.fillcolor("red")
    else:
        pen.fillcolor("white")

    pen.goto(320,y)
    playerMarker()
    if "Atlantic" in properties["playerOnep"]:  # Atlantic
        pen.fillcolor("green")
    elif "Atlantic" in properties["playerTwop"]:
        pen.fillcolor("orange")
    elif "Atlantic" in properties["playerThreep"]:
        pen.fillcolor("purple")
    elif "Atlantic" in properties["playerFourp"]:
        pen.fillcolor("yellow")
    elif "Atlantic" in properties["playerFivep"]:
        pen.fillcolor("blue")
    elif "Atlantic" in properties["playerSixp"]:
        pen.fillcolor("red")
    else:
        pen.fillcolor("white")
    pen.goto(422, y)
    playerMarker()

    if "Ventnor" in properties["playerOnep"]:  # Ventnor
        pen.fillcolor("green")
    elif "Ventnor" in properties["playerTwop"]:
        pen.fillcolor("orange")
    elif "Ventnor" in properties["playerThreep"]:
        pen.fillcolor("purple")
    elif "Ventnor" in properties["playerFourp"]:
        pen.fillcolor("yellow")
    elif "Ventnor" in properties["playerFivep"]:
        pen.fillcolor("blue")
    elif "Ventnor" in properties["playerSixp"]:
        pen.fillcolor("red")
    else:
        pen.fillcolor("white")
    pen.goto(498, y)
    playerMarker()

    if "Marvin Gardens" in properties["playerOnep"]:  # Marvin Gardens
        pen.fillcolor("green")
    elif "Marvin Gardens" in properties["playerTwop"]:
        pen.fillcolor("orange")
    elif "Marvin Gardens" in properties["playerThreep"]:
        pen.fillcolor("purple")
    elif "Marvin Gardens" in properties["playerFourp"]:
        pen.fillcolor("yellow")
    elif "Marvin Gardens" in properties["playerFivep"]:
        pen.fillcolor("blue")
    elif "Marvin Gardens" in properties["playerSixp"]:
        pen.fillcolor("red")
    else:
        pen.fillcolor("white")
    pen.goto(570, y)
    playerMarker()

    y = -83

    if "Pacific" in properties["playerOnep"]:  # Pacific
        pen.fillcolor("green")
    elif "Pacific" in properties["playerTwop"]:
        pen.fillcolor("orange")
    elif "Pacific" in properties["playerThreep"]:
        pen.fillcolor("purple")
    elif "Pacific" in properties["playerFourp"]:
        pen.fillcolor("yellow")
    elif "Pacific" in properties["playerFivep"]:
        pen.fillcolor("blue")
    elif "Pacific" in properties["playerSixp"]:
        pen.fillcolor("red")
    else:
        pen.fillcolor("white")
    pen.goto(173, y)
    playerMarker()

    if "North Carolina" in properties["playerOnep"]:  # North Carolina
        pen.fillcolor("green")
    elif "North Carolina" in properties["playerTwop"]:
        pen.fillcolor("orange")
    elif "North Carolina" in properties["playerThreep"]:
        pen.fillcolor("purple")
    elif "North Carolina" in properties["playerFourp"]:
        pen.fillcolor("yellow")
    elif "North Carolina" in properties["playerFivep"]:
        pen.fillcolor("blue")
    elif "North Carolina" in properties["playerSixp"]:
        pen.fillcolor("red")
    else:
        pen.fillcolor("white")
    pen.goto(250, y)
    playerMarker()

    if "Pennsylvania" in properties["playerOnep"]:  # Pennsylvania
        pen.fillcolor("green")
    elif "Pennsylvania" in properties["playerTwop"]:
        pen.fillcolor("orange")
    elif "Pennsylvania" in properties["playerThreep"]:
        pen.fillcolor("purple")
    elif "Pennsylvania" in properties["playerFourp"]:
        pen.fillcolor("yellow")
    elif "Pennsylvania" in properties["playerFivep"]:
        pen.fillcolor("blue")
    elif "Pennsylvania" in properties["playerSixp"]:
        pen.fillcolor("red")
    else:
        pen.fillcolor("white")
    pen.goto(320, y)
    playerMarker()

    if "Park Place" in properties["playerOnep"]:  # Park Place
        pen.fillcolor("green")
    elif "Park Place" in properties["playerTwop"]:
        pen.fillcolor("orange")
    elif "Park Place" in properties["playerThreep"]:
        pen.fillcolor("purple")
    elif "Park Place" in properties["playerFourp"]:
        pen.fillcolor("yellow")
    elif "Park Place" in properties["playerFivep"]:
        pen.fillcolor("blue")
    elif "Park Place" in properties["playerSixp"]:
        pen.fillcolor("red")
    else:
        pen.fillcolor("white")
    pen.goto(441, y)
    playerMarker()

    if "Boardwalk" in properties["playerOnep"]:  # Boardwalk
        pen.fillcolor("green")
    elif "Boardwalk" in properties["playerTwop"]:
        pen.fillcolor("orange")
    elif "Boardwalk" in properties["playerThreep"]:
        pen.fillcolor("purple")
    elif "Boardwalk" in properties["playerFourp"]:
        pen.fillcolor("yellow")
    elif "Boardwalk" in properties["playerFivep"]:
        pen.fillcolor("blue")
    elif "Boardwalk" in properties["playerSixp"]:
        pen.fillcolor("red")
    else:
        pen.fillcolor("white")

    pen.goto(519,y)
    playerMarker()
    y=-218
    if "Reading Railroad" in properties["playerOnep"]:  # Reading Railroad
        pen.fillcolor("green")
    elif "Reading Railroad" in properties["playerTwop"]:
        pen.fillcolor("orange")
    elif "Reading Railroad" in properties["playerThreep"]:
        pen.fillcolor("purple")
    elif "Reading Railroad" in properties["playerFourp"]:
        pen.fillcolor("yellow")
    elif "Reading Railroad" in properties["playerFivep"]:
        pen.fillcolor("blue")
    elif "Reading Railroad" in properties["playerSixp"]:
        pen.fillcolor("red")
    else:
        pen.fillcolor("white")
    pen.goto(155,y)
    playerMarker()
    if "Pennsylvania Railroad" in properties["playerOnep"]:  # Pennsylvania Railroad
        pen.fillcolor("green")
    elif "Pennsylvania Railroad" in properties["playerTwop"]:
        pen.fillcolor("orange")
    elif "Pennsylvania Railroad" in properties["playerThreep"]:
        pen.fillcolor("purple")
    elif "Pennsylvania Railroad" in properties["playerFourp"]:
        pen.fillcolor("yellow")
    elif "Pennsylvania Railroad" in properties["playerFivep"]:
        pen.fillcolor("blue")
    elif "Pennsylvania Railroad" in properties["playerSixp"]:
        pen.fillcolor("red")
    else:
        pen.fillcolor("white")
    pen.goto(235,y)
    playerMarker()
    if "B&O Railroad" in properties["playerOnep"]:  # B&O Railroad
        pen.fillcolor("green")
    elif "B&O Railroad" in properties["playerTwop"]:
        pen.fillcolor("orange")
    elif "B&O Railroad" in properties["playerThreep"]:
        pen.fillcolor("purple")
    elif "B&O Railroad" in properties["playerFourp"]:
        pen.fillcolor("yellow")
    elif "B&O Railroad" in properties["playerFivep"]:
        pen.fillcolor("blue")
    elif "B&O Railroad" in properties["playerSixp"]:
        pen.fillcolor("red")
    else:
        pen.fillcolor("white")
    pen.goto(307,y)
    playerMarker()
    if "Short Line" in properties["playerOnep"]:  # Short Line
        pen.fillcolor("green")
    elif "Short Line" in properties["playerTwop"]:
        pen.fillcolor("orange")
    elif "Short Line" in properties["playerThreep"]:
        pen.fillcolor("purple")
    elif "Short Line" in properties["playerFourp"]:
        pen.fillcolor("yellow")
    elif "Short Line" in properties["playerFivep"]:
        pen.fillcolor("blue")
    elif "Short Line" in properties["playerSixp"]:
        pen.fillcolor("red")
    else:
        pen.fillcolor("white")
    pen.goto(382,y)
    playerMarker()
    if "Electric Company" in properties["playerOnep"]:  # Electric Company
        pen.fillcolor("green")
    elif "Electric Company" in properties["playerTwop"]:
        pen.fillcolor("orange")
    elif "Electric Company" in properties["playerThreep"]:
        pen.fillcolor("purple")
    elif "Electric Company" in properties["playerFourp"]:
        pen.fillcolor("yellow")
    elif "Electric Company" in properties["playerFivep"]:
        pen.fillcolor("blue")
    elif "Electric Company" in properties["playerSixp"]:
        pen.fillcolor("red")
    else:
        pen.fillcolor("white")
    pen.goto(572,y)
    playerMarker()
    if "Water Works" in properties["playerOnep"]:  # Water Works
        pen.fillcolor("green")
    elif "Water Works" in properties["playerTwop"]:
        pen.fillcolor("orange")
    elif "Water Works" in properties["playerThreep"]:
        pen.fillcolor("purple")
    elif "Water Works" in properties["playerFourp"]:
        pen.fillcolor("yellow")
    elif "Water Works" in properties["playerFivep"]:
        pen.fillcolor("blue")
    elif "Water Works" in properties["playerSixp"]:
        pen.fillcolor("red")
    else:
        pen.fillcolor("white")
    pen.goto(496,y)
    playerMarker()

def addProperties(code, dataList):
    if(code == mediterraneanid):
        currentproperty = "Mediterranean"
    elif(code == balticid):
        currentproperty = "Baltic"
    elif(code == orientalid):
        currentproperty = "Oriental"
    elif(code == vermontid):
        currentproperty = "Vermont"
    elif(code == connecticutid):
        currentproperty = "Connecticut"
    elif(code == stcharlesid):
        currentproperty = "St. Charles"
    elif(code == statesid):
        currentproperty = "States"
    elif(code == virginiaid):
        currentproperty = "Virginia"
    elif(code == stjamesid):
        currentproperty = "St. James"
    elif(code == tennesseeid):
        currentproperty = "Tennessee"
    elif(code == newyorkid):
        currentproperty = "New York"
    elif(code == kentuckyid):
        currentproperty = "Kentucky"
    elif(code == indianaid):
        currentproperty = "Indiana"
    elif(code == illinoisid):
        currentproperty = "Illinois"
    elif(code == atlanticid):
        currentproperty = "Atlantic"
    elif(code == ventnorid):
        currentproperty = "Ventnor"
    elif(code == marvinid):
        currentproperty = "Marvin Gardens"
    elif(code == pacificid):
        currentproperty = "Pacific"
    elif(code == northcarolinaid):
        currentproperty = "North Carolina"
    elif(code == pennsylvaniaid):
        currentproperty = "Pennsylvania"
    elif(code == parkplaceid):
        currentproperty = "Park Place"
    elif(code == boardwalkid):
        currentproperty = "Boardwalk"
    elif(code == readingrid):
        currentproperty = "Reading Railroad"
    elif(code == pennsylvaniarid):
        currentproperty = "Pennsylvania Railroad"
    elif(code == bandorid):
        currentproperty = "B&O Railroad"
    elif(code == shortlinerid):
        currentproperty = "Short Line"
    elif(code == electricid):
        currentproperty = "Electric Company"
    elif(code == waterworksid):
        currentproperty = "Water Works"
    else:
        print("Invalid Barcode")
        raise ValueError ("Invalid Barcode")

    dataList.append(currentproperty)
    
gameOver = False

print("Welcome to digital Monopoly!") #Welcomes player to game
gameselected = False
status("Select Game")
while(gameselected == False):
    gameid = input("Please scan the UPC Barcode on the side of the box") #requests barcode on front of box
    if gameid == standardid:
        print("Standard game selected!")
        gametype = "standard"
        propertiesAvalible += ["Mediterranean", "Baltic", "Oriental", "Vermont", "Connecticut", "St. Charles", "States", "Virginia", "St. James", "Tennessee", "New York", "Kentucky", "Indiana", "Illinois", "Atlantic", "Ventnor", "Marvin Gardens", "Pacific", "Ventnor", "Marvin Gardens", "Pacific", "North Carolina", "Pennsylvania", "Park Place", "Boardwalk", "Short Line", "Reading Railroad", "Pennsylvania Railroad", "B&O Railroad", "Electric Company", "Water Works"]
        rrutils.penup()
        rrutils.goto(390, -270)
        rrutils.shape("railroads and utlities.gif")
        gameselected = True
    elif gameid == vaultid:
        print("Secret Vault game selected!")
        gametype = "vault"
        #Property Barcodes:
        mediterraneanid = "fff1111d900"
        balticid = "fffcc10d900"
        orientalid = "fffef11d900"
        vermontid = "fff7be6d800"
        connecticutid = "fff4925d900"
        stcharlesid = "fff8610d900"
        statesid = "fffed11d900"
        virginiaid = "ffff011d900"
        stjamesid = "fff4a25d900"
        tennesseeid = "fffca10d900"
        newyorkid = "fffd8fed800"
        kentuckyid = "fffec11d900"
        indianaid = "fffd7fed800"
        illinoisid = "fff4825d900"
        atlanticid = "fffcb10d900"
        ventnorid = "fffdd5d900"
        marvinid = "fffd823d900"
        pacificid = "fffee11d900"
        northcarolinaid = "fffdc5d900"
        pennsylvaniaid = "fff3312d900"
        parkplaceid = "fff9e11d900"
        boardwalkid = "fff4b25d900"
        #Settings:
        startingAmount = 3000 #Amount you start with
        passGoAmount = 400 #Ammount you earn from passing go
        #Property amount for buying:
        mediterraneanb = 120
        balticb = 120
        orientalb = 200
        vermontb = 0
        connecticutb = 240
        stcharlesb = 280
        statesb = 280
        virginiab = 320
        stjamesb = 0
        tennesseeb = 360
        newyorkb = 400
        kentuckyb = 440
        indianab = 440
        illinoisb = 480
        atlanticb = 520
        ventnorb = 0
        marvinb = 500
        pacificb = 600
        northcarolinab = 600
        pennsylvaniab = 640
        parkplaceb = 700
        boardwalkb = 0

        #Rent Value
        mediterraneanr = 20
        balticr = 50
        orientalr = 70
        vermontr = 70
        connecticutr = 80
        stcharlesr = 110
        statesr = 110
        virginiar = 140
        stjamesr = 150
        tennesseer = 150
        newyorkr = 170
        kentuckyr = 200
        indianar = 200
        illinoisr = 230
        atlanticr = 250
        ventnorr = 250
        marvinr = 280
        pacificr = 300
        northcarolinar = 300
        pennsylvaniar = 340
        parkplacer = 390
        boardwalkr = 470

        #Hotel cost (so the player pays nothing to build hotels)
        mediterraneanhc = 0
        baltichc = 0
        orientalhc = 0
        vermonthc = 0
        connecticuthc = 0

        stcharleshc = 0
        stateshc = 0
        virginiahc = 0
        stjameshc = 0
        tennesseehc = 0
        newyorkhc = 0

        kentuckyhc = 0
        indianahc = 0
        illinoishc = 0
        atlantichc = 0
        ventnorhc = 0
        marvinhc = 0

        pacifichc = 0
        northcarolinahc = 0
        pennsylvaniahc = 0
        parkplacehc = 0
        boardwalkhc = 0
        
        #Other fees:
        payincometax = 400
        payluxurytax = 400
        paytoguess = 100
        paygetoutofjail = 100

        propertiesAvalible += ["Mediterranean", "Baltic", "Oriental", "Vermont", "Connecticut", "St. Charles", "States", "Virginia", "St. James", "Tennessee", "New York", "Kentucky", "Indiana", "Illinois", "Atlantic", "Ventnor", "Marvin Gardens", "Pacific", "Ventnor", "Marvin Gardens", "Pacific", "North Carolina", "Pennsylvania", "Park Place", "Boardwalk"]
        #Color Sets:
        colorSets = {
            "Brown": ["Mediterranean", "Baltic"],
            "Light Blue": ["Oriental", "Vermont", "Connecticut"],
            "Pink": ["St. Charles", "States", "Virginia"],
            "Orange": ["St. James", "Tennessee", "New York"],
            "Red": ["Kentucky", "Indiana", "Illinois"],
            "Yellow": ["Atlantic", "Ventnor", "Marvin Gardens"],
            "Green": ["Pacific", "North Carolina", "Pennsylvania"],
            "Dark Blue": ["Park Place", "Boardwalk"],
        }
        rrutils.hideturtle()
        gameselected = True

    elif (gameid == builderid):
        print("Builder game selected!")
        gametype = "builder"
        #Property Barcodes:
        mediterraneanid = "ffff712d900"
        balticid = "fff8611d900"
        orientalid = "fff8711d900"
        vermontid = "fff4111d900"
        stcharlesid = "fff4211d900"
        statesid = "fffcc1ad900"
        stjamesid = "fff526d900"
        tennesseeid = "fff626d900"
        kentuckyid = "fff726d900"
        indianaid = "fffc025d900"
        atlanticid = "fffc125d900"
        ventnorid = "fff1531d900"
        pacificid = "fff3b31d900"
        northcarolinaid = "fffd138d900"
        parkplaceid = "fff5f37d900"
        boardwalkid = "fff6037d900"
        #Settings:
        startingAmount = 900 #Amount you start with
        passGoAmount = 200 #Ammount you earn from passing go
        #Property amount for buying:
        mediterraneanb = 60
        balticb = 60
        orientalb = 100
        vermontb = 100
        stcharlesb = 140
        statesb = 140
        stjamesb = 180
        tennesseeb = 180
        kentuckyb = 220
        indianab = 220
        atlanticb = 260
        ventnorb = 260
        pacificb = 300
        northcarolinab = 300
        parkplaceb = 400
        boardwalkb = 400

        #Rent Value
        mediterraneanr = 30
        balticr = 30
        orientalr = 50
        vermontr = 50
        stcharlesr = 70
        statesr = 70
        stjamesr = 90
        tennesseer = 90
        kentuckyr = 110
        indianar = 110
        atlanticr = 130
        ventnorr = 130
        pacificr = 150
        northcarolinar = 150
        parkplacer = 200
        boardwalkr = 200
        
        #Other fees:
        paygetoutofjail = 50

        propertiesAvalible += ["Mediterranean", "Baltic", "Oriental", "Vermont", "St. Charles", "States", "St. James", "Tennessee", "Kentucky", "Indiana", "Atlantic", "Ventnor", "Pacific", "Ventnor", "Pacific", "North Carolina", "Park Place", "Boardwalk"]
        #Color Sets:
        colorSets = {
        "Brown": ["Mediterranean", "Baltic"],
        "Light Blue": ["Oriental", "Vermont"],
        "Pink": ["St. Charles", "States"],
        "Orange": ["St. James", "Tennessee"],
        "Red": ["Kentucky", "Indiana"],
        "Yellow": ["Atlantic", "Ventnor"],
        "Green": ["Pacific", "North Carolina"],
        "Dark Blue": ["Park Place", "Boardwalk"],
        }
        
        hide.goto(486,295)
        hideP()
        hide.goto(308,173)
        hideP()
        hide.goto(561,174)
        hideP()
        hide.goto(310,42)
        hideP()
        hide.goto(564,43)
        hideP()
        hide.goto(310,-90)
        hideP()
        rrutils.hideturtle()
        
        gameselected = True
        
    else:
        print("Invalid Barcode")
playernum = 1
allplayersjoined = False
print("Now, please scan the barcode on your player card or tap your card to the scanner to join the game, then type 'play' to start game")
while (allplayersjoined == False):
    status(f"Player {playernum}, please join")
    playerid = input(f"Player {playernum}, please join!")
    if(playernum == 1 and playerid != "play"):
        playerOne = playerid
        playerid = ""
        playername = input("Please put in a name to identify yourself(could be your name, a nickname, or the name of the charcter you are using)")
        playerOnen = playername
        playername = ""
        print(f"Welcome, {playerOnen}!")
        playerOneb = startingAmount
        playernum += 1
    elif(playernum == 2 and playerid != "play"):
        playerTwo = playerid
        playerid = ""
        playername = input("Please put in a name to identify yourself(could be your name, a nickname, or the name of the charcter you are using)")
        playerTwon = playername
        playername = ""
        print(f"Welcome, {playerTwon}!")
        playerTwob = startingAmount
        playernum += 1
    elif(playernum == 3 and playerid != "play"):
        playerThree = playerid
        playerid = ""
        playername = input("Please put in a name to identify yourself(could be your name, a nickname, or the name of the charcter you are using)")
        playerThreen = playername
        playername = ""
        print(f"Welcome, {playerThreen}!")
        playerThreeb = startingAmount
        playernum += 1
    elif(playernum == 4 and playerid != "play"):
        playerFour = playerid
        playerid = ""
        playername = input("Please put in a name to identify yourself(could be your name, a nickname, or the name of the charcter you are using)")
        playerFourn = playername
        playername = ""
        print(f"Welcome, {playerFourn}!")
        playerFourb = startingAmount
        playernum += 1
    elif(playernum == 5 and playerid != "play"):
        playerFive = playerid
        playerid = ""
        playername = input("Please put in a name to identify yourself(could be your name, a nickname, or the name of the charcter you are using)")
        playerFiven = playername
        playername = ""
        print(f"Welcome, {playerFiven}!")
        playerFiveb = startingAmount
        playernum += 1
    elif(playernum == 6 and playerid != "play"):
        playerSix = playerid
        playerid == ""
        playername = input("Please put in a name to identify yourself(could be your name, a nickname, or the name of the charcter you are using)")
        playerSixn = playername
        playername = ""
        print(f"Welcome, {playerSixn}!")
        playerSixb = startingAmount
        playernum += 1
        allplayersjoined = True
    elif(playerid == "play"):
        allplayersjoined = True
print("Ok, Let's Play!")


 #---------------------MAIN LOOP---------------------------------
while (gameOver == False):
    try:
        statusd.clear()
        balance_labels = [playerOnen + " - $" + str(playerOneb), playerTwon + " - $" + str(playerTwob), playerThreen + " - $" + str(playerThreeb), playerFourn + " - $" + str(playerFourb), playerFiven + " - $" + str(playerFiveb), playerSixn + " - $" + str(playerSixb)]
        drawDisplay()
        binput = input("Please scan action on banker's card")
        if(binput == buy): #Begins the buying procees
            try:
                status("Scan property")
                buyinput = input("Scan Property to buy")
                if(buyinput == mediterraneanid):
                    payamount = mediterraneanb
                    currentproperty = "Mediterranean"
                elif(buyinput == balticid):
                    payamount = balticb
                    currentproperty = "Baltic"
                elif(buyinput == orientalid):
                    payamount = orientalb
                    currentproperty = "Oriental"
                elif(buyinput == vermontid):
                    payamount = vermontb
                    currentproperty = "Vermont"
                elif(buyinput == connecticutid):
                    payamount = connecticutb
                    currentproperty = "Connecticut"
                elif(buyinput == stcharlesid):
                    payamount = stcharlesb
                    currentproperty = "St. Charles"
                elif(buyinput == statesid):
                    payamount = statesb
                    currentproperty = "States"
                elif(buyinput == virginiaid):
                    payamount = virginiab
                    currentproperty = "Virginia"
                elif(buyinput == stjamesid):
                    payamount = stjamesb
                    currentproperty = "St. James"
                elif(buyinput == tennesseeid):
                    payamount = tennesseeb
                    currentproperty = "Tennessee"
                elif(buyinput == newyorkid):
                    payamount = newyorkb
                    currentproperty = "New York"
                elif(buyinput == kentuckyid):
                    payamount = kentuckyb
                    currentproperty = "Kentucky"
                elif(buyinput == indianaid):
                    payamount = indianab
                    currentproperty = "Indiana"
                elif(buyinput == illinoisid):
                    payamount = illinoisb
                    currentproperty = "Illinois"
                elif(buyinput == atlanticid):
                    payamount = atlanticb
                    currentproperty = "Atlantic"
                elif(buyinput == ventnorid):
                    payamount = ventnorb
                    currentproperty = "Ventnor"
                elif(buyinput == marvinid):
                    payamount = marvinb
                    currentproperty = "Marvin Gardens"
                elif(buyinput == pacificid):
                    payamount = pacificb
                    currentproperty = "Pacific"
                elif(buyinput == northcarolinaid):
                    payamount = northcarolinab
                    currentproperty = "North Carolina"
                elif(buyinput == pennsylvaniaid):
                    payamount = pennsylvaniab
                    currentproperty = "Pennsylvania"
                elif(buyinput == parkplaceid):
                    payamount = parkplaceb
                    currentproperty = "Park Place"
                elif(buyinput == boardwalkid):
                    payamount = boardwalkb
                    currentproperty = "Boardwalk"
                elif(buyinput == readingrid):
                    payamount = railroadb
                    currentproperty = "Reading Railroad"
                elif(buyinput == pennsylvaniarid):
                    payamount = railroadb
                    currentproperty = "Pennsylvania Railroad"
                elif(buyinput == bandorid):
                    payamount = railroadb
                    currentproperty = "B&O Railroad"
                elif(buyinput == shortlinerid):
                    payamount = railroadb
                    currentproperty = "Short Line"
                elif(buyinput == electricid):
                    payamount = utilityb
                    currentproperty = "Electric Company"
                elif(buyinput == waterworksid):
                    payamount = utilityb
                    currentproperty = "Water Works"
                else:
                    print("Invalid Property Barcode")
                    raise ValueError ("Invalid Property Barcode")
                   
            
                status("Scan your card")
                bplayerinput = input("Now scan player card to complete purchace")
                if(bplayerinput == playerOne):
                    if(playerOneb >= payamount):
                        playerOneb -= payamount
                        properties["playerOnep"].append(currentproperty)
                        print(f"{playerOnen} has purchased {currentproperty} for ${payamount}!")
                        propertiesAvalible.remove(currentproperty)
                    else:
                        print("You don't have enough money.")
                elif(bplayerinput == playerTwo):
                    if(playerTwob >= payamount):
                        playerTwob -= payamount
                        properties["playerTwop"].append(currentproperty)
                        print(f"{playerTwon} has purchased {currentproperty} for ${payamount}!")
                        propertiesAvalible.remove(currentproperty)
                    else:
                        print("You don't have enough money.")
                elif(bplayerinput == playerThree):
                    if(playerThreeb >= payamount):
                        playerThreeb -= payamount
                        properties["playerThreep"].append(currentproperty)
                        print(f"{playerThreen} has purchased {currentproperty} for ${payamount}!")
                        propertiesAvalible.remove(currentproperty)
                    else:
                        print("You don't have enough money.")
                elif(bplayerinput == playerFour):
                    if(playerFourb >= payamount):
                        playerFourb -= payamount
                        properties["playerFourp"].append(currentproperty)
                        print(f"{playerFourn} has purchased {currentproperty} for ${payamount}!")
                        propertiesAvalible.remove(currentproperty)
                    else:
                        print("You don't have enough money.")
                elif(bplayerinput == playerFive):
                    if(playerFiveb >= payamount):
                        playerFiveb -= payamount
                        properties["playerFivep"].append(currentproperty)
                        print(f"{playerFiven} has purchased {currentproperty} for ${payamount}!")
                        propertiesAvalible.remove(currentproperty)
                    else:
                        print("You don't have enough money.")
                elif(bplayerinput == playerSix):
                    if(playerSixb >= payamount):
                        playerSixb -= payamount
                        properties["playerSixp"].append(currentproperty)
                        print(f"{playerSixn} has purchased {currentproperty} for ${payamount}!")
                        propertiesAvalible.remove(currentproperty)
                    else:
                        print("You don't have enough money.")
                else:
                    print("Barcode error, please try again")
            except ValueError:
                print("An error has occured. Try Again.")
            currentproperty = ""
            payamount = 0
        elif(binput == payrent): #Pay Rent
            try:
                status("Scan Property")
                rentinput = input("Scan the code of the property that is being payed rent on")    
                if(rentinput == mediterraneanid):
                    payamount = mediterraneanr
                    currentproperty = "Mediterranean"
                elif(rentinput == balticid):
                    payamount = balticr
                    currentproperty = "Baltic"
                elif(rentinput == orientalid):
                    payamount = orientalr
                    currentproperty = "Oriental"
                elif(rentinput == vermontid):
                    payamount = vermontr
                    currentproperty = "Vermont"
                elif(rentinput == connecticutid):
                    payamount = connecticutr
                    currentproperty = "Connecticut"
                elif(rentinput == stcharlesid):
                    payamount = stcharlesr
                    currentproperty = "St. Charles"
                elif(rentinput == statesid):
                    payamount = statesr
                    currentproperty = "States"
                elif(rentinput == virginiaid):
                    payamount = virginiar
                    currentproperty = "Virginia"
                elif(rentinput == stjamesid):
                    payamount = stjamesr
                    currentproperty = "St. James"
                elif(rentinput == tennesseeid):
                    payamount = tennesseer
                    currentproperty = "Tennessee"
                elif(rentinput == newyorkid):
                    payamount = newyorkr
                    currentproperty = "New York"
                elif(rentinput == kentuckyid):
                    payamount = kentuckyr
                    currentproperty = "Kentucky"
                elif(rentinput == indianaid):
                    payamount = indianar
                    currentproperty = "Indiana"
                elif(rentinput == illinoisid):
                    payamount = illinoisr
                    currentproperty = "Illinois"
                elif(rentinput == atlanticid):
                    payamount = atlanticr
                    currentproperty = "Atlantic"
                elif(rentinput == ventnorid):
                    payamount = ventnorr
                    currentproperty = "Ventnor"
                elif(rentinput == marvinid):
                    payamount = marvinr
                    currentproperty = "Marvin Gardens"
                elif(rentinput == pacificid):
                    payamount = pacificr
                    currentproperty = "Pacific"
                elif(rentinput == northcarolinaid):
                    payamount = northcarolinar
                    currentproperty = "North Carolina"
                elif(rentinput == pennsylvaniaid):
                    payamount = pennsylvaniar
                    currentproperty = "Pennsylvania"
                elif(rentinput == parkplaceid):
                    payamount = parkplacer
                    currentproperty = "Park Place"
                elif(rentinput == boardwalkid):
                    payamount = boardwalkr
                    currentproperty = "Boardwalk"
                elif(rentinput == readingrid):
                    payamount = railroadr
                    currentproperty = "Reading Railroad"
                elif(rentinput == pennsylvaniarid):
                    payamount = railroadr
                    currentproperty = "Pennsylvania Railroad"
                elif(rentinput == bandorid):
                    payamount = railroadr
                    currentproperty = "B&O Railroad"
                elif(rentinput == shortlinerid):
                    payamount = railroadr
                    currentproperty = "Short Line"
                elif(rentinput == electricid):
                    payamount = int(input("Roll the dice and enter the number shown:"))
                    currentproperty = "Electric Company"
                elif(rentinput == waterworksid):
                    payamount = int(input("Roll the dice and enter the number shown:"))
                    currentproperty = "Water Works"
                else:
                    print("Invalid Property Barcode")
                    raise ValueError ("Invalid Property Barcode")
                    


                owner = next((name for name, values in properties.items() if currentproperty in values), None)

                rplayeroput = ""
                if (owner == "playerOnep"):
                    rplayeroput = playerOne
                elif (owner == "playerTwop"):
                    rplayeroput = playerTwo
                elif (owner == "playerThreep"):
                    rplayeroput = playerThree
                elif (owner == "playerFourp"):
                    rplayeroput = playerFour
                elif (owner == "playerFivep"):
                    rplayeroput = playerFive
                elif (owner == "playerSixp"):
                    rplayeroput = playerSix
                else:
                    print(f"No one owns {currentproperty}")
                    raise ValueError(f"No one owns {currentproperty}")
                
                playerProperties = properties[owner]
                
                colorSet = next((name for name, values in colorSets.items() if currentproperty in values), None)
                result = ""
                
                if all(item in playerProperties for item in colorSets[colorSet]):
                    if (colorSet == "utilities"):
                        payamount *= 10
                        result = "is one of two utilities owned"
                    elif (colorSet == "railroads"):
                        payamount = 200
                        result = "is one of all four railroads owned by this player"
                    elif (gametype == "standard" and houseshotels[currentproperty]["houses"] > 0): #Houses and Hotels for Standard Game
                        if (houseshotels[currentproperty]["hotel"]): #Hotel
                            if (currentproperty == "Pennsylvania"):
                                payamount = 1400
                            elif (currentproperty == "Connecticut"):
                                payamount = 600
                            elif (currentproperty == "St. James"):
                                payamount = 950
                            elif (currentproperty == "Tennessee"):
                                payamount = 950
                            elif (currentproperty == "New York"):
                                payamount = 1000
                            elif (currentproperty == "Kentucky"):
                                payamount = 1050
                            elif (currentproperty == "Indiana"):
                                payamount = 1050
                            elif (currentproperty == "Park Place"):
                                payamount = 1500
                            elif (currentproperty == "Boardwalk"):
                                payamount = 2000
                            elif (currentproperty == "Atlantic"):
                                payamount = 1150
                            elif (currentproperty == "Ventnor"):
                                payamount = 1150
                            elif (currentproperty == "Marvin Gardens"):
                                payamount = 1200
                            elif (currentproperty == "Virginia"):
                                payamount = 900
                            elif (currentproperty == "Pacific"):
                                payamount = 1275
                            elif (currentproperty == "North Carolina"):
                                payamount = 1275
                            elif (currentproperty == "States"):
                                payamount = 750
                            elif (currentproperty == "St. Charles"):
                                payamount = 750
                            elif (currentproperty == "Vermont"):
                                payamount = 550
                            elif (currentproperty == "Oriental"):
                                payamount = 550
                            elif (currentproperty == "Illinois"):
                                payamount = 1100
                            elif (currentproperty == "Baltic"):
                                payamount = 450
                            elif (currentproperty == "Mediterranean"):
                                payamount = 250
                            result = "has a hotlel"
                        else: #Houses
                            if (houseshotels[currentproperty]["houses"] == 1): # 1 house = 5 times standard rent
                                if (currentproperty == "Pennsylvania"):
                                    payamount = 150
                                elif (currentproperty == "Boardwalk"):
                                    payamount = 200
                                else:
                                    payamount *= 5
                                result = "has 1 house"
                            elif (houseshotels[currentproperty]["houses"] == 2): # 2 houses = 15 times standard rent
                                if (currentproperty == "Pennsylvania"):
                                    payamount = 450
                                elif (currentproperty == "Connecticut"):
                                    payamount = 100
                                elif (currentproperty == "St. James"):
                                    payamount = 200
                                elif (currentproperty == "Tennessee"):
                                    payamount = 200
                                elif (currentproperty == "New York"):
                                    payamount = 220
                                elif (currentproperty == "Kentucky"):
                                    payamount = 250
                                elif (currentproperty == "Indiana"):
                                    payamount = 250
                                elif (currentproperty == "Park Place"):
                                    payamount = 500
                                elif (currentproperty == "Boardwalk"):
                                    payamount = 600
                                else:
                                    payamount *= 15
                                result = "has 2 houses"
                            elif (houseshotels[currentproperty]["houses"] == 3): # 3 houses = 45 times standard rent
                                if (currentproperty == "Pennsylvania"):
                                    payamount = 1000
                                elif (currentproperty == "Connecticut"):
                                    payamount = 300
                                elif (currentproperty == "St. James"):
                                    payamount = 550
                                elif (currentproperty == "Tennessee"):
                                    payamount = 550
                                elif (currentproperty == "New York"):
                                    payamount = 600
                                elif (currentproperty == "Kentucky"):
                                    payamount = 700
                                elif (currentproperty == "Indiana"):
                                    payamount = 750
                                elif (currentproperty == "Park Place"):
                                    payamount = 1100
                                elif (currentproperty == "Boardwalk"):
                                    payamount = 1400
                                elif (currentproperty == "Atlantic"):
                                    payamount = 800
                                elif (currentproperty == "Ventnor"):
                                    payamount = 800
                                elif (currentproperty == "Marvin Gardens"):
                                    payamount = 850
                                elif (currentproperty == "Virginia"):
                                    payamount = 500
                                elif (currentproperty == "Pacific"):
                                    payamount = 900
                                elif (currentproperty == "North Carolina"):
                                    payamount = 900
                                else:
                                    payamount *= 45
                                result = "has 3 houses"
                            elif (houseshotels[currentproperty]["houses"] == 4):  # 4 houses = 80 times standard rent (only 2 follow this rule)
                                if (currentproperty == "Pennsylvania"):
                                    payamount = 1200
                                elif (currentproperty == "Connecticut"):
                                    payamount = 450
                                elif (currentproperty == "St. James"):
                                    payamount = 750
                                elif (currentproperty == "Tennessee"):
                                    payamount = 750
                                elif (currentproperty == "New York"):
                                    payamount = 800
                                elif (currentproperty == "Kentucky"):
                                    payamount = 875
                                elif (currentproperty == "Indiana"):
                                    payamount = 875
                                elif (currentproperty == "Park Place"):
                                    payamount = 1300
                                elif (currentproperty == "Boardwalk"):
                                    payamount = 1700
                                elif (currentproperty == "Atlantic"):
                                    payamount = 975
                                elif (currentproperty == "Ventnor"):
                                    payamount = 975
                                elif (currentproperty == "Marvin Gardens"):
                                    payamount = 1025
                                elif (currentproperty == "Virginia"):
                                    payamount = 700
                                elif (currentproperty == "Pacific"):
                                    payamount = 1100
                                elif (currentproperty == "North Carolina"):
                                    payamount = 1100
                                elif (currentproperty == "States"):
                                    payamount = 625
                                elif (currentproperty == "St. Charles"):
                                    payamount = 625
                                elif (currentproperty == "Vermont"):
                                    payamount = 400
                                elif (currentproperty == "Oriental"):
                                    payamount = 400
                                elif (currentproperty == "Illinois"):
                                    payamount = 925
                                else:
                                    payamount *= 80
                                result = "has 4 houses"
                    elif(gametype == "vault" and houseshotels[currentproperty]["houses"] > 0):# Hotels for Vault Game
                        if (houseshotels[currentproperty]["houses"] == 1): # 1 hotel
                            if (currentproperty == "Pennsylvania"):
                                payamount = 980
                            elif (currentproperty == "Connecticut"):
                                payamount = 460
                            elif (currentproperty == "St. James"):
                                payamount = 600
                            elif (currentproperty == "Tennessee"):
                                payamount = 600
                            elif (currentproperty == "New York"):
                                payamount = 640
                            elif (currentproperty == "Kentucky"):
                                payamount = 700
                            elif (currentproperty == "Indiana"):
                                payamount = 700
                            elif (currentproperty == "Park Place"):
                                payamount = 1080
                            elif (currentproperty == "Boardwalk"):
                                payamount = 1250
                            elif (currentproperty == "Atlantic"):
                                payamount = 800
                            elif (currentproperty == "Ventnor"):
                                payamount = 800
                            elif (currentproperty == "Marvin Gardens"):
                                payamount = 860
                            elif (currentproperty == "Virginia"):
                                payamount = 580
                            elif (currentproperty == "Pacific"):
                                payamount = 900
                            elif (currentproperty == "North Carolina"):
                                payamount = 900
                            elif (currentproperty == "States"):
                                payamount = 520
                            elif (currentproperty == "St. Charles"):
                                payamount = 520
                            elif (currentproperty == "Vermont"):
                                payamount = 440
                            elif (currentproperty == "Oriental"):
                                payamount = 440
                            elif (currentproperty == "Illinois"):
                                payamount = 760
                            elif (currentproperty == "Baltic"):
                                payamount = 400
                            elif (currentproperty == "Mediterranean"):
                                payamount = 340
                            result = "has 1 hotel"
                        elif (houseshotels[currentproperty]["houses"] == 2): #2 Hotels
                            if (currentproperty == "Pennsylvania"):
                                payamount = 1280
                            elif (currentproperty == "Connecticut"):
                                payamount = 760
                            elif (currentproperty == "St. James"):
                                payamount = 900
                            elif (currentproperty == "Tennessee"):
                                payamount = 900
                            elif (currentproperty == "New York"):
                                payamount = 940
                            elif (currentproperty == "Kentucky"):
                                payamount = 1000
                            elif (currentproperty == "Indiana"):
                                payamount = 1000
                            elif (currentproperty == "Park Place"):
                                payamount = 1380
                            elif (currentproperty == "Boardwalk"):
                                payamount = 1550
                            elif (currentproperty == "Atlantic"):
                                payamount = 1100
                            elif (currentproperty == "Ventnor"):
                                payamount = 1100
                            elif (currentproperty == "Marvin Gardens"):
                                payamount = 1160
                            elif (currentproperty == "Virginia"):
                                payamount = 880
                            elif (currentproperty == "Pacific"):
                                payamount = 1200
                            elif (currentproperty == "North Carolina"):
                                payamount = 1200
                            elif (currentproperty == "States"):
                                payamount = 820
                            elif (currentproperty == "St. Charles"):
                                payamount = 820
                            elif (currentproperty == "Vermont"):
                                payamount = 740
                            elif (currentproperty == "Oriental"):
                                payamount = 740
                            elif (currentproperty == "Illinois"):
                                payamount = 1060
                            elif (currentproperty == "Baltic"):
                                payamount = 700
                            elif (currentproperty == "Mediterranean"):
                                payamount = 640
                            result = "has 2 hotels"
                    else: #Just a Color Set = double standard rent
                        if (gametype == "vault" and currentproperty == "Boardwalk"):
                            payamount = 950
                        else:
                            payamount *= 2
                        result = "is part of a full color set owned by this player"
                else: #Normal Rent
                    if (colorSet == "utilities"):
                        payamount *= 4
                        result = "is one utility owned by this player"
                    elif (colorSet == "railroads"):
                        numrr = sum(1 for item in colorSets["railroads"] if item in properties[owner])
                        if (numrr == 2):
                            payamount = 50
                            result = "is one of two railroads owned by this player"
                        elif (numrr == 3):
                            payamount = 100
                            result = "is one of three railroads owned by this player"
                        elif (numrr == 1):
                            result = "is one railroad owned by this player"
                    else:
                        result = "is a standalone property"
                            
                print(f"{currentproperty} {result}, and it's rent value is ${payamount}.")
                status("Scan payer card")
                rplayerput = input("Now scan the card of the player paying to complete purchace")
                if(rplayerput == playerOne):
                    if(playerOneb >= payamount):
                        if(rplayeroput == playerOne):
                            playerOneb += payamount
                            currentplayer = playerOnen
                        elif(rplayeroput == playerTwo):
                            playerTwob += payamount
                            currentplayer = playerTwon
                        elif(rplayeroput == playerThree):
                            playerThreeb += payamount
                            currentplayer = playerThreen
                        elif(rplayeroput == playerFour):
                            playerFourb += payamount
                            currentplayer = playerFourn
                        elif(rplayeroput == playerFive):
                            playerFiveb += payamount
                            currentplayer = playerFive
                        elif(rplayeroput == playerSix):
                            playerSixb += payamount
                            currentplayer = playerSixn  
                        playerOneb -= payamount
                        print(f"{playerOnen} payed {currentplayer} ${payamount}!")
                    else:
                        print("You don't have enough money.")
                elif(rplayerput == playerTwo):
                    if(playerTwob >= payamount):
                        if(rplayeroput == playerOne):
                            playerOneb += payamount
                            currentplayer = playerOnen
                        elif(rplayeroput == playerTwo):
                            playerTwob += payamount
                            currentplayer = playerTwon
                        elif(rplayeroput == playerThree):
                            playerThreeb += payamount
                            currentplayer = playerThreen
                        elif(rplayeroput == playerFour):
                            playerFourb += payamount
                            currentplayer = playerFourn
                        elif(rplayeroput == playerFive):
                            playerFiveb += payamount
                            currentplayer = playerFive
                        elif(rplayeroput == playerSix):
                            playerSixb += payamount
                            currentplayer = playerSixn  
                        playerTwob -= payamount
                        print(f"{playerTwon} payed {currentplayer} ${payamount}!")
                    else:
                        print("You don't have enough money.")
                elif(rplayerput == playerThree):
                    if(playerThreeb >= payamount):
                        if(rplayeroput == playerOne):
                            playerOneb += payamount
                            currentplayer = playerOnen
                        elif(rplayeroput == playerTwo):
                            playerTwob += payamount
                            currentplayer = playerTwon
                        elif(rplayeroput == playerThree):
                            playerThreeb += payamount
                            currentplayer = playerThreen
                        elif(rplayeroput == playerFour):
                            playerFourb += payamount
                            currentplayer = playerFourn
                        elif(rplayeroput == playerFive):
                            playerFiveb += payamount
                            currentplayer = playerFive
                        elif(rplayeroput == playerSix):
                            playerSixb += payamount
                            currentplayer = playerSixn  
                        playerThreeb -= payamount
                        print(f"{playerThreen} payed {currentplayer} ${payamount}!")
                    else:
                        print("You don't have enough money.")
                elif(rplayerput == playerFour):
                    if(playerFourb >= payamount):
                        if(rplayeroput == playerOne):
                            playerOneb += payamount
                            currentplayer = playerOnen
                        elif(rplayeroput == playerTwo):
                            playerTwob += payamount
                            currentplayer = playerTwon
                        elif(rplayeroput == playerThree):
                            playerThreeb += payamount
                            currentplayer = playerThreen
                        elif(rplayeroput == playerFour):
                            playerFourb += payamount
                            currentplayer = playerFourn
                        elif(rplayeroput == playerFive):
                            playerFiveb += payamount
                            currentplayer = playerFive
                        elif(rplayeroput == playerSix):
                            playerSixb += payamount
                            currentplayer = playerSixn  
                        playerFourb -= payamount
                        print(f"{playerFourn} payed {currentplayer} ${payamount}!")
                    else:
                        print("You don't have enough money.")
                elif(rplayerput == playerFive):
                    if(playerFiveb >= payamount):
                        if(rplayeroput == playerOne):
                            playerOneb += payamount
                            currentplayer = playerOnen
                        elif(rplayeroput == playerTwo):
                            playerTwob += payamount
                            currentplayer = playerTwon
                        elif(rplayeroput == playerThree):
                            playerThreeb += payamount
                            currentplayer = playerThreen
                        elif(rplayeroput == playerFour):
                            playerFourb += payamount
                            currentplayer = playerFourn
                        elif(rplayeroput == playerFive):
                            playerFiveb += payamount
                            currentplayer = playerFive
                        elif(rplayeroput == playerSix):
                            playerSixb += payamount
                            currentplayer = playerSixn  
                        playerFiveb -= payamount
                        print(f"{playerFiven} payed {currentplayer} ${payamount}!")
                    else:
                        print("You don't have enough money.")
                elif(rplayerput == playerSix):
                    if(playerSixb >= payamount):
                        if(rplayeroput == playerOne):
                            playerOneb += payamount
                            currentplayer = playerOnen
                        elif(rplayeroput == playerTwo):
                            playerTwob += payamount
                            currentplayer = playerTwon
                        elif(rplayeroput == playerThree):
                            playerThreeb += payamount
                            currentplayer = playerThreen
                        elif(rplayeroput == playerFour):
                            playerFourb += payamount
                            currentplayer = playerFourn
                        elif(rplayeroput == playerFive):
                            playerFiveb += payamount
                            currentplayer = playerFive
                        elif(rplayeroput == playerSix):
                            playerSixb += payamount
                            currentplayer = playerSixn  
                        playerSixb -= payamount
                        print(f"{playerSixn} payed {currentplayer} ${payamount}!")
                    else:
                        print("You don't have enough money.")
                else:
                    print("Barcode error, please try again")
                currentplayer = ""
                payamount = 0
                currentproperty = ""
            except ValueError:
                print("An Error has occured. Please try again")
        elif(binput == auction):  #Auction
            try:
                status("Scan property")
                auctionprop = input("Please scan barcode of property being auctioned off")
                if(auctionprop == mediterraneanid):
                    currentproperty = "Mediterranean"
                elif(auctionprop == balticid):
                    currentproperty = "Baltic"
                elif(auctionprop == orientalid):
                    currentproperty = "Oriental"
                elif(auctionprop == vermontid):
                    currentproperty = "Vermont"
                elif(auctionprop == connecticutid):
                    currentproperty = "Connecticut"
                elif(auctionprop == stcharlesid):
                    currentproperty = "St. Charles"
                elif(auctionprop == statesid):
                    currentproperty = "States"
                elif(auctionprop == virginiaid):
                    currentproperty = "Virginia"
                elif(auctionprop == stjamesid):
                    currentproperty = "St. James"
                elif(auctionprop == tennesseeid):
                    currentproperty = "Tennessee"
                elif(auctionprop == newyorkid):
                    currentproperty = "New York"
                elif(auctionprop == kentuckyid):
                    currentproperty = "Kentucky"
                elif(auctionprop == indianaid):
                    currentproperty = "Indiana"
                elif(auctionprop == illinoisid):
                    currentproperty = "Illinois"
                elif(auctionprop == atlanticid):
                    currentproperty = "Atlantic"
                elif(auctionprop == ventnorid):
                    currentproperty = "Ventnor"
                elif(auctionprop == marvinid):
                    currentproperty = "Marvin Gardens"
                elif(auctionprop == pacificid):
                    currentproperty = "Pacific"
                elif(auctionprop == northcarolinaid):
                    currentproperty = "North Carolina"
                elif(auctionprop == pennsylvaniaid):
                    currentproperty = "Pennsylvania"
                elif(auctionprop == parkplaceid):
                    currentproperty = "Park Place"
                elif(auctionprop == boardwalkid):
                    currentproperty = "Boardwalk"
                elif(auctionprop == readingrid):
                    currentproperty = "Reading Railroad"
                elif(auctionprop == pennsylvaniarid):
                    currentproperty = "Pennsylvania Railroad"
                elif(auctionprop == bandorid):
                    currentproperty = "B&O Railroad"
                elif(auctionprop == shortlinerid):
                    currentproperty = "Short Line"
                elif(auctionprop == electricid):
                    currentproperty = "Electric Company"
                elif(auctionprop == waterworksid):
                    currentproperty = "Water Works"
                else:
                    print("Invalid Barcode")
                    raise ValueError ("Invalid Barcode")
                print(f"{currentproperty} is now being auctioned off. Bidding starts at $10. Scan your player card to bid. When finished, type 'end' to end auction.")
                payamount = 10
                auctionOver = False
                enoughMoney = True
                while(auctionOver == False):
                    status(f"Bidding for ${payamount}.")
                    auctionplay = input(f"Bidding for ${payamount}.")
                    if(auctionplay == playerOne):
                        if(playerOneb >= payamount):
                            currentplayer = playerOnen
                        else:
                            print("You don't have enough money to bid.")
                            enoughMoney = False
                    elif(auctionplay == playerTwo):
                        if(playerTwob >= payamount):
                            currentplayer = playerTwon
                        else:
                            print("You don't have enough money to bid.")
                            enoughMoney = False
                    elif(auctionplay == playerThree):
                        if(playerThreeb >= payamount):
                            currentplayer = playerThreen
                        else:
                            print("You don't have enough money to bid.")
                            enoughMoney = False
                    elif(auctionplay == playerFour):
                        if(playerFourb >= payamount):
                            currentplayer = playerFourn
                        else:
                            print("You don't have enough money to bid.")
                            enoughMoney = False
                    elif(auctionplay == playerFive):
                        if(playerFiveb >= payamount):
                            currentplayer = playerFiven
                        else:
                            print("You don't have enough money to bid.")
                        enoughMoney = False
                    elif(auctionplay == playerSix):
                        if(playerSixb >= payamount):
                            currentplayer = playerSixn
                        else:
                            print("You don't have enough money to bid.")
                            enoughMoney = False
                    elif(auctionplay == "end"):
                        auctionOver = True
                    else:
                        print("Barcode error, please try again")
                        enoughMoney = False
                    if(enoughMoney == True and auctionOver == True):
                        break
                    elif(enoughMoney == True):
                        try:
                            auctiona = int(input("Enter amount you want to bid"))
                            payamount = auctiona
                            if(auctionplay == playerOne):
                                if(playerOneb >= payamount):
                                    print(f"{currentplayer} bidded ${auctiona}!")
                                else:
                                    print("You don't have enough money to bid.")
                                    payamount -= auctiona
                            elif(auctionplay == playerTwo):
                                if(playerTwob >= payamount):
                                    print(f"{currentplayer} bidded ${auctiona}!")
                                else:
                                    print("You don't have enough money to bid.")
                                    payamount -= auctiona
                            elif(auctionplay == playerThree):
                                if(playerThreeb >= payamount):
                                    print(f"{currentplayer} bidded ${auctiona}!")
                                else:
                                    print("You don't have enough money to bid.")
                                    payamount -= auctiona
                            elif(auctionplay == playerFour):
                                if(playerFourb >= payamount):
                                    print(f"{currentplayer} bidded ${auctiona}!")
                                else:
                                    print("You don't have enough money to bid.")
                                    payamount -= auctiona
                            elif(auctionplay == playerFive):
                                if(playerFiveb >= payamount):
                                    print(f"{currentplayer} bidded ${auctiona}!")
                                else:
                                    print("You don't have enough money to bid.")
                                    payamount -= auctiona
                            elif(auctionplay == playerSix):
                                if(playerSixb >= payamount):
                                    print(f"{currentplayer} bidded ${auctiona}!")
                                else:
                                    print("You don't have enough money to bid.")
                                    payamount -= auctiona
                        except ValueError:
                            print("Error. Try Again")
                        enoughMoney = True
                status(f"{currentplayer}, scan your card")
                auctionpay = input(f"The auction is now over. {currentplayer} owes ${payamount}. {currentplayer}, please scan your player card to confirm your purchace of {currentproperty}")
                if(auctionpay == playerOne):
                    playerOneb -= payamount
                    playerOnep.append(currentproperty)
                elif(auctionpay == playerTwo):
                    playerTwob -= payamount
                    playerTwop.append(currentproperty)
                elif(auctionpay == playerThree):
                    playerThreeb -= payamount
                    playerThreep.append(currentproperty)
                elif(auctionpay == playerFour):
                    playerFourb -= payamount
                    playerFourp.append(currentproperty)
                elif(auctionpay == playerFive):
                    playerFiveb -= payamount
                    playerFivep.append(currentproperty)
                elif(auctionpay == playerSix):
                    playerSixb -= payamount
                    playerSixp.append(currentproperty)
                print(f"{currentplayer} has purchaced {currentproperty} for ${payamount}!")
                propertiesAvalible.remove(currentproperty)
                currentproperty = ""
                currentplayer = ""
                payamount =
            except ValueError:
                print("An error has occured. Try again")
        elif(binput == incometax): #Income Tax
            status("Scan payer card")
            intax = input("Scan player card to pay Income Tax")
            payamount = payincometax
            if(gametype == "standard"):
                if(intax == playerOne):
                    if(playerOneb >= payamount):
                        playerOneb -= payamount
                        print(f"{playerOnen} payed Income Tax.")
                    else:
                        print("You don't have enough money to pay.")
                elif(intax == playerTwo):
                     if(playerTwob >= payamount):
                        playerTwob -= payamount
                        print(f"{playerTwon} payed Income Tax.")
                     else:
                        print("You don't have enough money to pay.")
                elif(intax == playerThree):
                    if(playerThreeb >= payamount):
                        playerThreeb -= payamount
                        print(f"{playerThreen} payed Income Tax.")
                    else:
                        print("You don't have enough money to pay.")
                elif(intax == playerFour):
                    if(playerFourb >= payamount):
                        playerFourb -= payamount
                        print(f"{playerFourn} payed Income Tax.")
                    else:
                        print("You don't have enough money to pay.")
                elif(intax == playerFive):
                    if(playerFiveb >= payamount):
                        playerFiveb -= payamount
                        print(f"{playerFiven} payed Income Tax.")
                    else:
                        print("You don't have enough money to pay.")
                elif(intax == playerSix):
                    if(playerSixb >= payamount):
                        playerSixb -= payamount
                        print(f"{playerSixn} payed Income Tax.")
                    else:
                        print("You don't have enough money to pay.")
                else:
                    print("Invalid Player ID. Try Again")
            elif(gametype == "vault"):
                if(intax == playerOne):
                    if(playerOneb >= payamount):
                        playerOneb -= payamount
                        print(f"{playerOnen} payed Income Tax.")
                    else:
                        print("You don't have enough money to pay.")
                elif(intax == playerTwo):
                     if(playerTwob >= payamount):
                        playerTwob -= payamount
                        print(f"{playerTwon} payed Income Tax.")
                     else:
                        print("You don't have enough money to pay.")
                elif(intax == playerThree):
                    if(playerThreeb >= payamount):
                        playerThreeb -= payamount
                        print(f"{playerThreen} payed Income Tax.")
                    else:
                        print("You don't have enough money to pay.")
                elif(intax == playerFour):
                    if(playerFourb >= payamount):
                        playerFourb -= payamount
                        print(f"{playerFourn} payed Income Tax.")
                    else:
                        print("You don't have enough money to pay.")
                elif(intax == playerFive):
                    if(playerFiveb >= payamount):
                        playerFiveb -= payamount
                        print(f"{playerFiven} payed Income Tax.")
                    else:
                        print("You don't have enough money to pay.")
                elif(intax == playerSix):
                    if(playerSixb >= payamount):
                        playerSixb -= payamount
                        print(f"{playerSixn} payed Income Tax.")
                    else:
                        print("You don't have enough money to pay.")
                else:
                    print("Invalid Player ID. Try Again")
                    vaultb -= payamount
                vaultb += payamount
            payamount = 0
        elif(binput == luxurytax): #Luxury Tax
            status("Scan payer card")
            luxtax = input("Scan player card to pay Luxury Tax")
            payamount = payluxurytax
            if(gametype == "standard"):
                if(luxtax == playerOne):
                    if(playerOneb >= payamount):
                        playerOneb -= payamount
                        print(f"{playerOnen} payed Luxury Tax.")
                    else:
                        print("You don't have enough money to pay.")
                elif(luxtax == playerTwo):
                     if(playerTwob >= payamount):
                        playerTwob -= payamount
                        print(f"{playerTwon} payed Luxury Tax.")
                     else:
                        print("You don't have enough money to pay.")
                elif(luxtax == playerThree):
                    if(playerThreeb >= payamount):
                        playerThreeb -= payamount
                        print(f"{playerThreen} payed Luxury Tax.")
                    else:
                        print("You don't have enough money to pay.")
                elif(luxtax == playerFour):
                    if(playerFourb >= payamount):
                        playerFourb -= payamount
                        print(f"{playerFourn} payed Luxury Tax.")
                    else:
                        print("You don't have enough money to pay.")
                elif(luxtax == playerFive):
                    if(playerFiveb >= payamount):
                        playerFiveb -= payamount
                        print(f"{playerFiven} payed Luxury Tax.")
                    else:
                        print("You don't have enough money to pay.")
                elif(luxtax == playerSix):
                    if(playerSixb >= payamount):
                        playerSixb -= payamount
                        print(f"{playerSixn} payed Luxury Tax.")
                    else:
                        print("You don't have enough money to pay.")
                else:
                    print("Invalid Player ID. Try Again")
            elif(gametype == "vault"):
                if(luxtax == playerOne):
                    if(playerOneb >= payamount):
                        playerOneb -= payamount
                        print(f"{playerOnen} payed Luxury Tax.")
                    else:
                        print("You don't have enough money to pay.")
                elif(luxtax == playerTwo):
                     if(playerTwob >= payamount):
                        playerTwob -= payamount
                        print(f"{playerTwon} payed Luxury Tax.")
                     else:
                        print("You don't have enough money to pay.")
                elif(luxtax == playerThree):
                    if(playerThreeb >= payamount):
                        playerThreeb -= payamount
                        print(f"{playerThreen} payed Luxury Tax.")
                    else:
                        print("You don't have enough money to pay.")
                elif(luxtax == playerFour):
                    if(playerFourb >= payamount):
                        playerFourb -= payamount
                        print(f"{playerFourn} payed Luxury Tax.")
                    else:
                        print("You don't have enough money to pay.")
                elif(luxtax == playerFive):
                    if(playerFiveb >= payamount):
                        playerFiveb -= payamount
                        print(f"{playerFiven} payed Luxury Tax.")
                    else:
                        print("You don't have enough money to pay.")
                elif(luxtax == playerSix):
                    if(playerSixb >= payamount):
                        playerSixb -= payamount
                        print(f"{playerSixn} payed Luxury Tax.")
                    else:
                        print("You don't have enough money to pay.")
                else:
                    print("Invalid Player ID. Try Again")
                    vaultb -= payamount
                vaultb += payamount
            payamount = 0
        elif(binput == getoutofjail): #Get Out Of Jail
            status("Scan payer card")
            jailpay = input("Scan Player card to get out of jail")
            payamount = paygetoutofjail
            if(jailpay == playerOne):
                if(playerOneb >= payamount):
                    playerOneb -= payamount
                    print(f"You payed ${payamount}. You're free! Take your turn!")
                else:
                    print("You don't have enough money to pay.")
            elif(jailpay == playerTwo):
                 if(playerTwob >= payamount):
                    playerTwob -= payamount
                    print(f"You payed ${payamount}. You're free! Take your turn!")
                 else:
                    print("You don't have enough money to pay.")
            elif(jailpay == playerThree):
                if(playerThreeb >= payamount):
                    playerThreeb -= payamount
                    print(f"You payed ${payamount}. You're free! Take your turn!")
                else:
                    print("You don't have enough money to pay.")
            elif(jailpay == playerFour):
                if(playerFourb >= payamount):
                    playerFourb -= payamount
                    print(f"You payed ${payamount}. You're free! Take your turn!")
                else:
                    print("You don't have enough money to pay.")
            elif(jailpay == playerFive):
                if(playerFiveb >= payamount):
                    playerFiveb -= payamount
                    print(f"You payed ${payamount}. You're free! Take your turn!")
                else:
                    print("You don't have enough money to pay.")
            elif(jailpay == playerSix):
                if(playerSixb >= payamount):
                    playerSixb -= payamount
                    print(f"You payed ${payamount}. You're free! Take your turn!")
                else:
                    print("You don't have enough money to pay.")
            else:
                print("Invalid Player ID. Try Again")
            payamount = 0
        elif(binput == passgo): #Pass Go
            status("Scan player card")
            passpay = input("Scan Player card to pass go")
            payamount = passGoAmount
            if(passpay == playerOne):
                playerOneb += payamount
                print(f"{playerOnen} got ${payamount} for passing go!")
            elif(passpay == playerTwo):
                playerTwob += payamount
                print(f"{playerTwon} got ${payamount} for passing go!")
            elif(passpay == playerThree):
                playerThreeb += payamount
                print(f"{playerThreen} got ${payamount} for passing go!")
            elif(passpay == playerFour):
                playerFourb += payamount
                print(f"{playerFourn} got ${payamount} for passing go!")
            elif(passpay == playerFive):
                playerFiveb += payamount
                print(f"{playerFiven} got ${payamount} for passing go!")
            elif(passpay == playerSix):
                playerSixb += payamount
                print(f"{playerSixn} got ${payamount} for passing go!")
            else:
                print("Invalid Player ID. Try Again")
            payamount = 0
        elif(binput == buildahouse): #Build a House/Hotel
            try:
                if (gametype == "builder"):
                    print("No houses or hotels can be built in this game mode")
                    raise ValueError("No houses or hotels can be built in this game mode")
                status("Scan property")
                houseprop = input("Please scan property that will be built on")
                if(houseprop == mediterraneanid):
                    payamount = mediterraneanhc
                    currentproperty = "Mediterranean"
                elif(houseprop == balticid):
                    payamount = baltichc
                    currentproperty = "Baltic"
                elif(houseprop == orientalid):
                    payamount = orientalhc
                    currentproperty = "Oriental"
                elif(houseprop == vermontid):
                    payamount = vermonthc
                    currentproperty = "Vermont"
                elif(houseprop == connecticutid):
                    payamount = connecticuthc
                    currentproperty = "Connecticut"
                elif(houseprop == stcharlesid):
                    payamount = stcharleshc
                    currentproperty = "St. Charles"
                elif(houseprop == statesid):
                    payamount = stateshc
                    currentproperty = "States"
                elif(houseprop == virginiaid):
                    payamount = virginiahc
                    currentproperty = "Virginia"
                elif(houseprop == stjamesid):
                    payamount = stjameshc
                    currentproperty = "St. James"
                elif(houseprop == tennesseeid):
                    payamount = tennesseehc
                    currentproperty = "Tennessee"
                elif(houseprop == newyorkid):
                    payamount = newyorkhc
                    currentproperty = "New York"
                elif(houseprop == kentuckyid):
                    payamount = kentuckyhc
                    currentproperty = "Kentucky"
                elif(houseprop == indianaid):
                    payamount = indianahc
                    currentproperty = "Indiana"
                elif(houseprop == illinoisid):
                    payamount = illinoishc
                    currentproperty = "Illinois"
                elif(houseprop == atlanticid):
                    payamount = atlantichc
                    currentproperty = "Atlantic"
                elif(houseprop == ventnorid):
                    payamount = ventnorhc
                    currentproperty = "Ventnor"
                elif(houseprop == marvinid):
                    payamount = marvinhc
                    currentproperty = "Marvin Gardens"
                elif(houseprop == pacificid):
                    payamount = pacifichc
                    currentproperty = "Pacific"
                elif(houseprop == northcarolinaid):
                    payamount = northcarolinahc
                    currentproperty = "North Carolina"
                elif(houseprop == pennsylvaniaid):
                    payamount = pennsylvaniahc
                    currentproperty = "Pennsylvania"
                elif(houseprop == parkplaceid):
                    payamount = parkplacehc
                    currentproperty = "Park Place"
                elif(houseprop == boardwalkid):
                    payamount = boardwalkhc
                    currentproperty = "Boardwalk"
                    
                colorSet = next((name for name, values in colorSets.items() if currentproperty in values), None)
                owner = next((name for name, values in properties.items() if currentproperty in values), None)
                housepput = ""
                if (owner == "playerOnep"):
                    housepput = playerOne
                elif (owner == "playerTwop"):
                    housepput = playerTwo
                elif (owner == "playerThreep"):
                    housepput = playerThree
                elif (owner == "playerFourp"):
                    housepput = playerFour
                elif (owner == "playerFivep"):
                    housepput = playerFive
                elif (owner == "playerSixp"):
                    housepput = playerSix
                else:
                    print(f"No one owns {currentproperty}")
                    raise ValueError(f"No one owns {currentproperty}")
                
                playerProperties = properties[owner]
                
                if (gametype == "standard" and houseshotels[currentproperty]["houses"] == 4 and houseshotels[currentproperty]["hotel"]):
                    print(f"You alreday have the maximum number of houses and hotels on {currentproperty}!")
                    raise ValueError(f"You alreday have the maximum number of houses and hotels on {currentproperty}!")
                elif (gametype == "vault" and houseshotels[currentproperty]["houses"] == 2):
                    print(f"You alreday have the maximum number of hotels on {currentproperty}!")
                    raise ValueError(f"You alreday have the maximum number of hotels on {currentproperty}!")
                elif not(all(item in playerProperties for item in colorSets[colorSet])):
                    print(f"{currentproperty} is not part of a color set!")
                    raise ValueError(f"{currentproperty} is not part of a color set!")
                
                if(housepput == playerOne):
                    if(playerOneb >= payamount):
                        playerOneb -= payamount
                        print(f"Put a house or hotel on {currentproperty}.")
                    else:
                        print("You don't have enough money.")
                elif(housepput == playerTwo):
                    if(playerTwob >= payamount):
                        playerTwob -= payamount
                        print(f"Put a house or hotel on {currentproperty}.")
                    else:
                        print("You don't have enough money.")
                elif(housepput == playerThree):
                    if(playerThreeb >= payamount):
                        playerThreeb -= payamount
                        print(f"Put a house or hotel on {currentproperty}.")
                    else:
                        print("You don't have enough money.")
                elif(housepput == playerFour):
                    if(playerFourb >= payamount):
                        playerFourb -= payamount
                        print(f"Put a house or hotel on {currentproperty}.")
                    else:
                        print("You don't have enough money.")
                elif(housepput == playerFive):
                    if(playerFiveb >= payamount):
                        playerFiveb -= payamount
                        print(f"Put a house or hotel on {currentproperty}.")
                    else:
                        print("You don't have enough money.")
                elif(housepput == playerSix):
                    if(playerSixb >= payamount):
                        playerSixb -= payamount
                        print(f"Put a house or hotel on {currentproperty}.")
                    else:
                        print("You don't have enough money.")
                else:
                    print("Invalid Player ID. Try Again")
                if (gametype == "standard"):
                    if (houseshotels[currentproperty]["houses"] == 4): #If there are 4 houses, add a hotel
                        houseshotels[currentproperty]["hotel"] = True
                    else: #Otherwise, add another house
                        houseshotels[currentproperty]["houses"] += 1
                elif (gametype == "vault"): #Add a hotel
                    houseshotels[currentproperty]["houses"] += 1
            except ValueError:
                print("An Error has Occured. Please Try Again.")
            payamount = 0
            currentproperty = ""
        elif(binput == checkbalance): #Check Balance (Legacy)
            status("Scan player card")
            balancecheck = input("Scan your player card to check balance")
            if(balancecheck == playerOne):
                print(f"{playerOnen} has ${playerOneb}.")
            elif(balancecheck == playerTwo):
                print(f"{playerTwon} has ${playerTwob}.")
            elif(balancecheck == playerThree):
                print(f"{playerThreen} has ${playerThreeb}.")
            elif(balancecheck == playerFour):
                print(f"{playerFourn} has ${playerFourb}.")
            elif(balancecheck == playerFive):
                print(f"{playerFiven} has ${playerFiveb}.")
            elif(balancecheck == playerSix):
                print(f"{playerSixn} has ${playerSixb}.")
            else:
                print("Invalid Player ID. Try Again")
        elif(binput == checkvbalance): # Check Vault Balance (Legacy)
            print(f"The vault has ${vaultb} in it")
        elif(binput == checkprops): #Check Properties (Legacy)
            status("Scan player card")
            propcheck = input("Scan your player card to check your properties")
            if(propcheck == playerOne):
                print(f"{playerOnen} has the following properties:\n{properties['playerOnep']}.")
            elif(propcheck == playerTwo):
                print(f"{playerTwon} has the following properties:\n{properties['playerTwop']}.")
            elif(propcheck == playerThree):
                print(f"{playerThreen} has the following properties:\n{properties['playerThreep']}.")
            elif(propcheck == playerFour):
                print(f"{playerFourn} has the following properties:\n{properties['playerFourp']}.")
            elif(propcheck == playerFive):
                print(f"{playerFiven} has the following properties:\n{properties['playerFivep']}.")
            elif(propcheck == playerSix):
                print(f"{playerSixn} has the following properties:\n{properties['playerSixp']}.")
        elif(binput == buyproperty): #Buy Propery From Player
            try:
                status("Scan property")
                bprop = input("Scan property being purchaced")
                if(bprop == mediterraneanid):
                    currentproperty = "Mediterranean"
                elif(bprop == balticid):
                    currentproperty = "Baltic"
                elif(bprop == orientalid):
                    currentproperty = "Oriental"
                elif(bprop == vermontid):
                    currentproperty = "Vermont"
                elif(bprop == connecticutid):
                    currentproperty = "Connecticut"
                elif(bprop == stcharlesid):
                    currentproperty = "St. Charles"
                elif(bprop == statesid):
                    currentproperty = "States"
                elif(bprop == virginiaid):
                    currentproperty = "Virginia"
                elif(bprop == stjamesid):
                    currentproperty = "St. James"
                elif(bprop == tennesseeid):
                    currentproperty = "Tennessee"
                elif(bprop == newyorkid):
                    currentproperty = "New York"
                elif(bprop == kentuckyid):
                    currentproperty = "Kentucky"
                elif(bprop == indianaid):
                    currentproperty = "Indiana"
                elif(bprop == illinoisid):
                    currentproperty = "Illinois"
                elif(bprop == atlanticid):
                    currentproperty = "Atlantic"
                elif(bprop == ventnorid):
                    currentproperty = "Ventnor"
                elif(bprop == marvinid):
                    currentproperty = "Marvin Gardens"
                elif(bprop == pacificid):
                    currentproperty = "Pacific"
                elif(bprop == northcarolinaid):
                    currentproperty = "North Carolina"
                elif(bprop == pennsylvaniaid):
                    currentproperty = "Pennsylvania"
                elif(bprop == parkplaceid):
                    currentproperty = "Park Place"
                elif(bprop == boardwalkid):
                    currentproperty = "Boardwalk"
                elif(bprop == readingrid):
                    currentproperty = "Reading Railroad"
                elif(bprop == pennsylvaniarid):
                    currentproperty = "Pennsylvania Railroad"
                elif(bprop == bandorid):
                    currentproperty = "B&O Railroad"
                elif(bprop == shortlinerid):
                    currentproperty = "Short Line"
                elif(bprop == electricid):
                    currentproperty = "Electric Company"
                elif(bprop == waterworksid):
                    currentproperty = "Water Works"
                status(f"Scan card of {currentproperty}'s owner")
                bfplayer = input(f"Now scan the card of the person that {currentproperty} belongs to currently.")
                if(bfplayer == playerOne):
                    if(currentproperty not in properties["playerOnep"]):
                        print(f"You don't own {currentproperty}.")
                        raise ValueError (f"You don't own {currentproperty}.")
                    else:
                        print(f"{playerOnen} owns {currentproperty}.")
                elif(bfplayer == playerTwo):
                    if(currentproperty not in properties["playerTwop"]):
                        print(f"You don't own {currentproperty}.")
                        raise ValueError (f"You don't own {currentproperty}.")
                    else:
                        print(f"{playerTwon} owns {currentproperty}.")
                elif(bfplayer == playerThree):
                    if(currentproperty not in properties["playerThreep"]):
                        print(f"You don't own {currentproperty}.")
                        raise ValueError (f"You don't own {currentproperty}.")
                    else:
                        print(f"{playerThreen} owns {currentproperty}.")
                elif(bfplayer == playerFour):
                    if(currentproperty not in properties["playerFourp"]):
                        print(f"You don't own {currentproperty}.")
                        raise ValueError (f"You don't own {currentproperty}.")
                    else:
                        print(f"{playerFourn} owns {currentproperty}.")
                elif(bfplayer == playerFive):
                    if(currentproperty not in properties["playerFivep"]):
                        print(f"You don't own {currentproperty}.")
                        raise ValueError (f"You don't own {currentproperty}.")
                    else:
                        print(f"{playerFiven} owns {currentproperty}.")
                elif(bfplayer == playerSix):
                    if(currentproperty not in properties["playerSixp"]):
                        print(f"You don't own {currentproperty}.")
                        raise ValueError (f"You don't own {currentproperty}.")
                    else:
                        print(f"{playerSixn} owns {currentproperty}.")
                status("Enter price")
                cbuyamount = int(input("Enter amount to be bought for"))
                payamount = cbuyamount
                try:
                    status("Scan payer card")
                    playerbput = input("Now scan the card of the player paying to complete purchace")
                    if(playerbput == playerOne):
                        if(playerOneb >= payamount):
                            if(bfplayer == playerOne):
                                playerOneb += payamount
                                properties["playerOnep"].remove(currentproperty)
                                currentplayer = playerOnen
                            elif(bfplayer == playerTwo):
                                playerTwob += payamount
                                properties["playerTwop"].remove(currentproperty)
                                currentplayer = playerTwon
                            elif(bfplayer== playerThree):
                                playerThreeb += payamount
                                properties["playerThreep"].remove(currentproperty)
                                currentplayer = playerThreen
                            elif(bfplayer == playerFour):
                                playerFourb += payamount
                                properties["playerFourp"].remove(currentproperty)
                                currentplayer = playerFourn
                            elif(bfplayer == playerFive):
                                playerFiveb += payamount
                                properties["playerFivep"].remove(currentproperty)
                                currentplayer = playerFive
                            elif(bfplayer == playerSix):
                                playerSixb += payamount
                                currentplayer = playerSixn  
                            playerOneb -= payamount
                            properties["playerOnep"].append(currentproperty)
                            print(f"{playerOnen} has purchaced {currentproperty} from {currentplayer} for ${payamount}!")
                        else:
                            print("You don't have enough money.")
                    elif(playerbput == playerTwo):
                        if(playerTwob >= payamount):
                            if(bfplayer == playerOne):
                                playerOneb += payamount
                                properties["playerOnep"].remove(currentproperty)
                                currentplayer = playerOnen
                            elif(bfplayer == playerTwo):
                                playerTwob += payamount
                                properties["playerTwop"].remove(currentproperty)
                                currentplayer = playerTwon
                            elif(bfplayer == playerThree):
                                playerThreeb += payamount
                                properties["playerThreep"].remove(currentproperty)
                                currentplayer = playerThreen
                            elif(bfplayer == playerFour):
                                playerFourb += payamount
                                properties["playerFourp"].remove(currentproperty)
                                currentplayer = playerFourn
                            elif(bfplayer == playerFive):
                                playerFiveb += payamount
                                properties["playerFivep"].remove(currentproperty)
                                currentplayer = playerFive
                            elif(bfplayer == playerSix):
                                playerSixb += payamount
                                properties["playerSixp"].remove(currentproperty)
                                currentplayer = playerSixn  
                            playerTwob -= payamount
                            properties["playerTwop"].append(currentproperty)
                            print(f"{playerTwon} has purchaced {currentproperty} from {currentplayer} for ${payamount}!")
                        else:
                            print("You don't have enough money.")
                    elif(playerbput == playerThree):
                        if(playerThreeb >= payamount):
                            if(bfplayer == playerOne):
                                playerOneb += payamount
                                properties["playerOnep"].remove(currentproperty)
                                currentplayer = playerOnen
                            elif(bfplayer == playerTwo):
                                playerTwob += payamount
                                properties["playerTwop"].remove(currentproperty)
                                currentplayer = playerTwon
                            elif(bfplayer == playerThree):
                                playerThreeb += payamount
                                properties["playerThreep"].remove(currentproperty)
                                currentplayer = playerThreen
                            elif(bfplayer == playerFour):
                                playerFourb += payamount
                                properties["playerFourp"].remove(currentproperty)
                                currentplayer = playerFourn
                            elif(bfplayer == playerFive):
                                playerFiveb += payamount
                                properties["playerFivep"].remove(currentproperty)
                                currentplayer = playerFive
                            elif(bfplayer == playerSix):
                                playerSixb += payamount
                                properties["playerSixp"].remove(currentproperty)
                                currentplayer = playerSixn  
                            playerThreeb -= payamount
                            properties["playerThreep"].append(currentproperty)
                            print(f"{playerThreen} has purchaced {currentproperty} from {currentplayer} for ${payamount}!")
                        else:
                            print("You don't have enough money.")
                    elif(playerbput == playerFour):
                        if(playerFourb >= payamount):
                            if(bfplayer == playerOne):
                                playerOneb += payamount
                                properties["playerOnep"].remove(currentproperty)
                                currentplayer = playerOnen
                            elif(bfplayer == playerTwo):
                                playerTwob += payamount
                                properties["playerTwop"].remove(currentproperty)
                                currentplayer = playerTwon
                            elif(bfplayer == playerThree):
                                playerThreeb += payamount
                                properties["playerThreep"].remove(currentproperty)
                                currentplayer = playerThreen
                            elif(bfplayer == playerFour):
                                properties["playerFourp"].remove(currentproperty)
                                playerFourb += payamount
                                currentplayer = playerFourn
                            elif(bfplayer == playerFive):
                                playerFiveb += payamount
                                properties["playerFivep"].remove(currentproperty)
                                currentplayer = playerFive
                            elif(bfplayer == playerSix):
                                playerSixb += payamount
                                properties["playerSixp"].remove(currentproperty)
                                currentplayer = playerSixn  
                            playerFourb -= payamount
                            properties["playerFourp"].append(currentproperty)
                            print(f"{playerFourn} has purchaced {currentproperty} from {currentplayer} for ${payamount}!")
                        else:
                            print("You don't have enough money.")
                    elif(playerbput == playerFive):
                        if(playerFiveb >= payamount):
                            if(bfplayer == playerOne):
                                playerOneb += payamount
                                properties["playerOnep"].remove(currentproperty)
                                currentplayer = playerOnen
                            elif(bfplayer == playerTwo):
                                playerTwob += payamount
                                properties["playerTwop"].remove(currentproperty)
                                currentplayer = playerTwon
                            elif(bfplayer == playerThree):
                                playerThreeb += payamount
                                properties["playerThreep"].remove(currentproperty)
                                currentplayer = playerThreen
                            elif(bfplayer == playerFour):
                                playerFourb += payamount
                                properties["playerFourp"].remove(currentproperty)
                                currentplayer = playerFourn
                            elif(bfplayer == playerFive):
                                playerFiveb += payamount
                                properties["playerFivep"].remove(currentproperty)
                                currentplayer = playerFive
                            elif(bfplayer == playerSix):
                                playerSixb += payamount
                                properties["playerSixp"].remove(currentproperty)
                                currentplayer = playerSixn  
                            playerFiveb -= payamount
                            properties["playerFivep"].append(currentproperty)
                            print(f"{playerFiven} has purchaced {currentproperty} from {currentplayer} for ${payamount}!")
                        else:
                            print("You don't have enough money.")
                    elif(playerbput == playerSix):
                        if(playerSixb >= payamount):
                            if(bfplayer == playerOne):
                                playerOneb += payamount
                                properties["playerOnep"].remove(currentproperty)
                                currentplayer = playerOnen
                            elif(bfplayer == playerTwo):
                                playerTwob += payamount
                                properties["playerTwop"].remove(currentproperty)
                                currentplayer = playerTwon
                            elif(bfplayer == playerThree):
                                playerThreeb += payamount
                                properties["playerThreep"].remove(currentproperty)
                                currentplayer = playerThreen
                            elif(bfplayer == playerFour):
                                playerFourb += payamount
                                properties["playerFourp"].remove(currentproperty)
                                currentplayer = playerFourn
                            elif(bfplayer == playerFive):
                                playerFiveb += payamount
                                properties["playerFivep"].remove(currentproperty)
                                currentplayer = playerFive
                            elif(bfplayer == playerSix):
                                playerSixb += payamount
                                properties["playerSixp"].remove(currentproperty)
                                currentplayer = playerSixn  
                            playerSixb -= payamount
                            properties["playerSixp"].append(currentproperty)
                            print(f"{playerSixn} has purchaced {currentproperty} from {currentplayer} for ${payamount}!")
                        else:
                            print("You don't have enough money.")
                except ValueError:
                    print("Error. Try Again")
                payamount = 0
                currentproperty = ""
                currentplayer = ""
            except ValueError:
                print("Error. Try Again")
        elif(binput == banktoplayer): #Bank To Player
            try:
                status("Scan player card")
                banktop = input("Scan player card of person getting paid")
                status("Enter price")
                banktopa = int(input("Enter amount"))
                payamount = banktopa
                if(banktop == playerOne):
                    playerOneb += payamount
                    print(f"{playerOnen} got paid ${payamount} from the bank!")
                elif(banktop == playerTwo):
                    playerTwob += payamount
                    print(f"{playerTwon} got paid ${payamount} from the bank!")
                elif(banktop == playerThree):
                    playerThreeb += payamount
                    print(f"{playerThreen} got paid ${payamount} from the bank!")
                elif(banktop == playerFour):
                    playerFourb += payamount
                    print(f"{playerFourn} got paid ${payamount} from the bank!")
                elif(banktop == playerFive):
                    playerFiveb += payamount
                    print(f"{playerFiven} got paid ${payamount} from the bank!")
                elif(banktop == playerSix):
                    playerSixb += payamount
                    print(f"{playerSixn} got paid ${payamount} from the bank!")
            except ValueError:
                print("Error. Try Again")
            payamount = 0
        elif(binput == playertobank): #Player to Bank
            try:
                status("Scan payer card")
                ptobank = input("Scan player card of person paying")
                status("Enter price")
                ptobanka = int(input("Enter amount"))
                payamount = ptobanka
                if(ptobank == playerOne):
                    playerOneb -= payamount
                    print(f"{playerOnen} paid ${payamount} to the bank!")
                elif(ptobank == playerTwo):
                    playerTwob -= payamount
                    print(f"{playerTwon} paid ${payamount} to the bank!")
                elif(ptobank == playerThree):
                    playerThreeb -= payamount
                    print(f"{playerThreen} paid ${payamount} to the bank!")
                elif(ptobank == playerFour):
                    playerFourb -= payamount
                    print(f"{playerFourn} paid ${payamount} to the bank!")
                elif(ptobank == playerFive):
                    playerFiveb -= payamount
                    print(f"{playerFiven} paid ${payamount} to the bank!")
                elif(ptobank == playerSix):
                    playerSixb -= payamount
                    print(f"{playerSixn} paid ${payamount} to the bank!")
            except ValueError:
                print("Error. Try Again")
            payamount = 0
        elif(binput == playertoplayer): #Player to Player
            try:
                status("Scan card of player getting payed")
                ptoppaid = input("Scan player card of the person who is getting paid")
                status("Enter price")
                ptopa = int(input("Enter payment amount"))
                payamount = ptopa
                status("Scan payer card")
                ptoppay = input("Now scan the card of the player paying to complete purchace")
                if(ptoppay == playerOne):
                    if(playerOneb >= payamount):
                        if(ptoppaid == playerOne):
                            playerOneb += payamount
                            currentplayer = playerOnen
                        elif(ptoppaid == playerTwo):
                            playerTwob += payamount
                            currentplayer = playerTwon
                        elif(ptoppaid == playerThree):
                            playerThreeb += payamount
                            currentplayer = playerThreen
                        elif(ptoppaid == playerFour):
                            playerFourb += payamount
                            currentplayer = playerFourn
                        elif(ptoppaid == playerFive):
                            playerFiveb += payamount
                            currentplayer = playerFive
                        elif(ptoppaid == playerSix):
                            playerSixb += payamount
                            currentplayer = playerSixn  
                        playerOneb -= payamount
                        print(f"{playerOnen} payed {currentplayer} ${payamount}!")
                    else:
                        print("You don't have enough money.")
                elif(ptoppay == playerTwo):
                    if(playerTwob >= payamount):
                        if(ptoppaid == playerOne):
                            playerOneb += payamount
                            currentplayer = playerOnen
                        elif(ptoppaid == playerTwo):
                            playerTwob += payamount
                            currentplayer = playerTwon
                        elif(ptoppaid == playerThree):
                            playerThreeb += payamount
                            currentplayer = playerThreen
                        elif(ptoppaid == playerFour):
                            playerFourb += payamount
                            currentplayer = playerFourn
                        elif(ptoppaid == playerFive):
                            playerFiveb += payamount
                            currentplayer = playerFive
                        elif(ptoppaid == playerSix):
                            playerSixb += payamount
                            currentplayer = playerSixn  
                        playerTwob -= payamount
                        print(f"{playerTwon} payed {currentplayer} ${payamount}!")
                    else:
                        print("You don't have enough money.")
                elif(ptoppay == playerThree):
                    if(playerThreeb >= payamount):
                        if(ptoppaid == playerOne):
                            playerOneb += payamount
                            currentplayer = playerOnen
                        elif(ptoppaid == playerTwo):
                            playerTwob += payamount
                            currentplayer = playerTwon
                        elif(ptoppaid == playerThree):
                            playerThreeb += payamount
                            currentplayer = playerThreen
                        elif(ptoppaid == playerFour):
                            playerFourb += payamount
                            currentplayer = playerFourn
                        elif(ptoppaid == playerFive):
                            playerFiveb += payamount
                            currentplayer = playerFive
                        elif(ptoppaid == playerSix):
                            playerSixb += payamount
                            currentplayer = playerSixn  
                        playerThreeb -= payamount
                        print(f"{playerThreen} payed {currentplayer} ${payamount}!")
                    else:
                        print("You don't have enough money.")
                elif(ptoppay == playerFour):
                    if(playerFourb >= payamount):
                        if(ptoppaid == playerOne):
                            playerOneb += payamount
                            currentplayer = playerOnen
                        elif(ptoppaid == playerTwo):
                            playerTwob += payamount
                            currentplayer = playerTwon
                        elif(ptoppaid == playerThree):
                            playerThreeb += payamount
                            currentplayer = playerThreen
                        elif(ptoppaid == playerFour):
                            playerFourb += payamount
                            currentplayer = playerFourn
                        elif(ptoppaid == playerFive):
                            playerFiveb += payamount
                            currentplayer = playerFive
                        elif(ptoppaid == playerSix):
                            playerSixb += payamount
                            currentplayer = playerSixn  
                        playerFourb -= payamount
                        print(f"{playerFourn} payed {currentplayer} ${payamount}!")
                    else:
                        print("You don't have enough money.")
                elif(ptoppay == playerFive):
                    if(playerFiveb >= payamount):
                        if(ptoppaid == playerOne):
                            playerOneb += payamount
                            currentplayer = playerOnen
                        elif(ptoppaid == playerTwo):
                            playerTwob += payamount
                            currentplayer = playerTwon
                        elif(ptoppaid == playerThree):
                            playerThreeb += payamount
                            currentplayer = playerThreen
                        elif(ptoppaid == playerFour):
                            playerFourb += payamount
                            currentplayer = playerFourn
                        elif(ptoppaid == playerFive):
                            playerFiveb += payamount
                            currentplayer = playerFive
                        elif(ptoppaid == playerSix):
                            playerSixb += payamount
                            currentplayer = playerSixn  
                        playerFiveb -= payamount
                        print(f"{playerFiven} payed {currentplayer} ${payamount}!")
                    else:
                        print("You don't have enough money.")
                elif(ptoppay == playerSix):
                    if(playerSixb >= payamount):
                        if(ptoppaid == playerOne):
                            playerOneb += payamount
                            currentplayer = playerOnen
                        elif(ptoppaid == playerTwo):
                            playerTwob += payamount
                            currentplayer = playerTwon
                        elif(ptoppaid == playerThree):
                            playerThreeb += payamount
                            currentplayer = playerThreen
                        elif(ptoppaid == playerFour):
                            playerFourb += payamount
                            currentplayer = playerFourn
                        elif(ptoppaid == playerFive):
                            playerFiveb += payamount
                            currentplayer = playerFive
                        elif(ptoppaid == playerSix):
                            playerSixb += payamount
                            currentplayer = playerSixn  
                        playerSixb -= payamount
                        print(f"{playerSixn} payed {currentplayer} ${payamount}!")
                    else:
                        print("You don't have enough money.")
            except ValueError:
                print("Error. Try Again")
            currentplayer = ""
            payamount = 0
        elif(binput == playertovault): #Player to Vault
            try:
                status("Scan payer card")
                ptovault = input("Scan player card of person paying")
                status("Enter price")
                ptovaulta = int(input("Enter amount"))
                payamount = ptovaulta
                if(ptovault == playerOne):
                    playerOneb -= payamount
                    vaultb += payamount
                    print(f"{playerOnen} paid ${payamount} to the vault!")
                elif(ptovault == playerTwo):
                    playerTwob -= payamount
                    vaultb += payamount
                    print(f"{playerTwon} paid ${payamount} to the vault!")
                elif(ptovault == playerThree):
                    playerThreeb -= payamount
                    vaultb += payamount
                    print(f"{playerThreen} paid ${payamount} to the vault!")
                elif(ptovault == playerFour):
                    playerFourb -= payamount
                    vaultb += payamount
                    print(f"{playerFourn} paid ${payamount} to the vault!")
                elif(ptovault == playerFive):
                    playerFiveb -= payamount
                    vaultb += payamount
                    print(f"{playerFiven} paid ${payamount} to the vault!")
                elif(ptovault == playerSix):
                    playerSixb -= payamount
                    vaultb += payamount
                    print(f"{playerSixn} paid ${payamount} to the vault!")
            except ValueError:
                print("Error. Try Again")
            payamount = 0
        elif(binput == banktovault): #Bank to Vault
            try:
                status("Enter price")
                banktvaulta = int(input("Enter amount"))
                vaultb += banktvaulta
                print(f"The bank payed ${banktvaulta} to the vault!")
            except ValueError:
                print("Error. Try Again")
        elif(binput == vaultcard or binput == vaulttap): #Vault Opened
            try:
                status("Scan player card")
                vaulttop = input("Congradulations on opening the vault! Scan your card to collect the rewards inside!")
                payamount = vaultb
                if(vaulttop == playerOne):
                    playerOneb += payamount
                    print(f"{playerOnen} collected ${payamount} from the vault!")
                elif(vaulttop == playerTwo):
                    playerTwob += payamount
                    print(f"{playerTwon} collected ${payamount} from the vault!")
                elif(vaulttop == playerThree):
                    playerThreeb += payamount
                    print(f"{playerThreen} collected ${payamount} from the vault!")
                elif(vaulttop == playerFour):
                    playerFourb += payamount
                    print(f"{playerFourn} collected ${payamount} from the vault!")
                elif(vaulttop == playerFive):
                    playerFiveb += payamount
                    print(f"{playerFiven} collected ${payamount} from the vault!")
                elif(vaulttop == playerSix):
                    playerSixb += payamount
                    print(f"{playerSixn} collected ${payamount} from the vault!")
                else:
                    print("Invalid Player ID.")
                    raise ValueError ("Invalid player ID")
                payamount = 0
                vaultb = 400
            except ValueError:
                print("Error. Try again")
        elif(binput == error): #Error
            print("Error brcode scanned")
        elif(binput == endgame): #End Game
            gameOver = True
            break
        elif(binput == recovery): #Recovery Mode
            print("Starting Recovery Mode...")
            time.sleep(1)
            print("Enter balances and properties for each player when prompted")
            allplayersjoined = False
            for i in range(playernum - 1):
                if (i == 0): #Player 1
                    while True:
                        try:
                            playerOneb = int(input(f"Enter {playerOnen}'s balance:"))
                        except ValueError:
                            print("Error. Try Again")
                        else:
                            break
                    print(f"Now, one by one, scan all of {playerOnen}'s properties, then type 'done' when finished.")
                    while True:
                        try:
                            recovprop = input("Scan Property:")
                            if (recovprop == "done"):
                                break
                            else:
                                addProperties(recovprop, properties["playerOnep"])
                        except ValueError:
                            print("An Error has occured. try again")
#----------------------------------------------------------------------------------------------------------------------------                            
                elif (i == 1): #Player 2
                    while True:
                        try:
                            playerTwob = int(input(f"Enter {playerTwon}'s balance:"))
                        except ValueError:
                            print("Error. Try Again")
                        else:
                            break
                    print(f"Now, one by one, scan all of {playerTwon}'s properties, then type 'done' when finished.")
                    while True:
                        try:
                            recovprop = input("Scan Property:")
                            if (recovprop == "done"):
                                break
                            else:
                                addProperties(recovprop, properties["playerTwop"])
                        except ValueError:
                            print("An Error has occured. try again")
#-----------------------------------------------------------------------------------------------------------------------------                            
                elif (i == 2): #Player 3
                    while True:
                        try:
                            playerThreeb = int(input(f"Enter {playerThreen}'s balance:"))
                        except ValueError:
                            print("Error. Try Again")
                        else:
                            break
                    print(f"Now, one by one, scan all of {playerThreen}'s properties, then type 'done' when finished.")
                    while True:
                        try:
                            recovprop = input("Scan Property:")
                            if (recovprop == "done"):
                                break
                            else:
                                addProperties(recovprop, properties["playerThreep"])
                        except ValueError:
                            print("An Error has occured. try again")
#------------------------------------------------------------------------------------------------------------------------------                            
                elif (i == 3): #Player 4
                    while True:
                        try:
                            playerFourb = int(input(f"Enter {playerFourn}'s balance:"))
                        except ValueError:
                            print("Error. Try Again")
                        else:
                            break
                    print(f"Now, one by one, scan all of {playerFourn}'s properties, then type 'done' when finished.")
                    while True:
                        try:
                            recovprop = input("Scan Property:")
                            if (recovprop == "done"):
                                break
                            else:
                                addProperties(recovprop, properties["playerFourp"])
                        except ValueError:
                            print("An Error has occured. try again")
#---------------------------------------------------------------------------------------------------------------------------
                elif (i == 4): #Player 5
                    while True:
                        try:
                            playerFiveb = int(input(f"Enter {playerFiven}'s balance:"))
                        except ValueError:
                            print("Error. Try Again")
                        else:
                            break
                    print(f"Now, one by one, scan all of {playerFiven}'s properties, then type 'done' when finished.")
                    while True:
                        try:
                            recovprop = input("Scan Property:")
                            if (recovprop == "done"):
                                break
                            else:
                                addProperties(recovprop, properties["playerFivep"])
                        except ValueError:
                            print("An Error has occured. try again")
#------------------------------------------------------------------------------------------------------------------------------                            
                elif (i == 5): #Player 6
                    while True:
                        try:
                            playerSixb = int(input(f"Enter {playerSixn}'s balance:"))
                        except ValueError:
                            print("Error. Try Again")
                        else:
                            break
                    print(f"Now, one by one, scan all of {playerSixn}'s properties, then type 'done' when finished.")
                    while True:
                        try:
                            recovprop = input("Scan Property:")
                            if (recovprop == "done"):
                                break
                            else:
                                addProperties(recovprop, properties["playerSixp"])
                        except ValueError:
                            print("An Error has occured. try again")
            print("Recovery mode has finished. Houses and Hotels must be added back manualy")
            print("Recovery mode closing...")
            time.sleep(1)
    except (SyntaxError, IndentationError, NameError, TypeError, IndexError, KeyError, AttributeError, ValueError, ImportError, ZeroDivisionError) as e:
        print("An error has occurred. Do not repeat this action again. Please report it to the GitHub Page as soon as possible. Include the error details below.")
        print(f"Error Details: {e}")
        
status("Game Over")
print("The game is over! Final totals will be displayed below, please add them with property rent to find out the winner!")
print(f"{playerOnen} - ${playerOneb}")
print(f"{playerTwon} - ${playerTwob}")
print(f"{playerThreen} - ${playerThreeb}")
print(f"{playerFourn} - ${playerFourb}")
print(f"{playerFiven} - ${playerFiveb}")
print(f"{playerSixn} - ${playerSixb}")
print("Thanks for playing!")
time.sleep(300)
