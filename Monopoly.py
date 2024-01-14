import time

gametype = "" #Selecting the game type from user input (Standard or Secret Vault)
#Barcode Ids:
#Box barcodes:
standardid = "6468475374851" 
vaultid = "7965749577486"

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

#Property Barcodes:
mediterraneanid = "124385"
balticid = "038504"
orientalid = "421503"
vermontid = "847502"
connecticutid = "132712"
stcharlesid = "013857"
statesid = "808327"
virginiaid = "734853"
stjamesid = "405312"
tennesseeid = "381205"
newyorkid = "427808"
kentuckyid = "310837"
indianaid = "053731"
illinoisid = "813412"
atlanticid = "301587"
ventnorid = "841303"
marvinid = "327821"
pacificid = "274831"
northcarolinaid = "639837"
pennsylvaniaid = "143587"
parkplaceid = "738542"
boardwalkid = "504427"

#Railroad & Utillity Barcodes (standard only):
readingrid = "417352"
pennsylvaniarid = "374808"
bandorid = "569845"
shortlinerid = "368742"
electricid = "513817"
waterworksid = "913752"

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
playerOnep = []
playerTwop = []
playerThreep = []
playerFourp = []
playerFivep = []
playerSixp = []

houses = []
hotels = []

#Color Sets:
brown = ["Mediterranean", "Baltic"]
lightblue = ["Oriental", "Vermont", "Connecticut"]
pink = ["St. Charles", "States", "Virginia"]
orange = ["St. James", "Tennessee", "New York"]
red = ["Kentucky", "Indiana", "Illinois"]
yellow = ["Atlantic", "Ventnor", "Marvin Gardens"]
green = ["Pacific", "North Carolina", "Pennsylvania"]
darkblue = ["Park Place", "Boardwalk"]
railroads = ["Reading Railroad", "Pennsylvania Railroad", "B&O Railroad", "Short Line"]
utilities = ["Electic Company", "Water Works"]

propertiesAvalible = []
payamount = 0
currentproperty = ""
currentplayer = ""


utilityamount = 0

gameOver = False

print("Welcome to digital Monopoly!") #Welcomes player to game
gameselected = False
while(gameselected == False):
    gameid = input("Please scan barcode on the front of the box") #requests barcode on front of box
    if gameid == standardid:
        print("Standard game selected!")
        gametype = "standard"
        propertiesAvalible += ["Mediterranean", "Baltic", "Oriental", "Vermont", "Connecticut", "St. Charles", "States", "Virginia", "St. James", "Tennessee", "New York", "Kentucky", "Indiana", "Illinois", "Atlantic", "Ventnor", "Marvin Gardens", "Pacific", "Ventnor", "Marvin Gardens", "Pacific", "North Carolina", "Pennsylvania", "Park Place", "Boardwalk", "Short Line", "Reading Railroad", "Pennsylvania Railroad", "B&O Railroad", "Electric Company", "Water Works"]
        gameselected = True
    elif gameid == vaultid:
        print("Secret Vault game selected!")
        gametype = "vault"
        #Property Barcodes:
        mediterraneanid = "701358"
        balticid = "013737"
        orientalid = "380405"
        vermontid = "281317"
        connecticutid = "828501"
        stcharlesid = "531831"
        statesid = "213587"
        virginiaid = "504504"
        stjamesid = "807803"
        tennesseeid = "896342"
        newyorkid = "373810"
        kentuckyid = "401387"
        indianaid = "837504"
        illinoisid = "307583"
        atlanticid = "014101"
        ventnorid = "183507"
        marvinid = "384537"
        pacificid = "831737"
        northcarolinaid = "735501"
        pennsylvaniaid = "831737"
        parkplaceid = "741387"
        boardwalkid = "801387"
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

        propertiesAvaliable += ["Mediterranean", "Baltic", "Oriental", "Vermont", "Connecticut", "St. Charles", "States", "Virginia", "St. James", "Tennessee", "New York", "Kentucky", "Indiana", "Illinois", "Atlantic", "Ventnor", "Marvin Gardens", "Pacific", "Ventnor", "Marvin Gardens", "Pacific", "North Carolina", "Pennsylvania", "Park Place", "Boardwalk"]
        gameselected = True
        
    else:
        print("Invalid Barcode")
playernum = 1
allplayersjoined = False
print("Now, please scan the barcode on your player card to join the game, then type 'play' to start game")
while (allplayersjoined == False):
    playerid = input(f"Player {playernum}, please join!")
    if(playernum == 1 and playerid != "play"):
        playerOne = playerid
        playerid = ""
        playername = input("Please put in a name to identify yourself(could be your name, a nickname, or the name of the charcter you are using)")
        playerOnen = playername
        playername = ""
        print(f"Welcome, {playerOnen}!")
        playerOneb = startingAmount
    elif(playernum == 2 and playerid != "play"):
        playerTwo = playerid
        playerid = ""
        playername = input("Please put in a name to identify yourself(could be your name, a nickname, or the name of the charcter you are using)")
        playerTwon = playername
        playername = ""
        print(f"Welcome, {playerTwon}!")
        playerTwob = startingAmount
    elif(playernum == 3 and playerid != "play"):
        playerThree = playerid
        playerid = ""
        playername = input("Please put in a name to identify yourself(could be your name, a nickname, or the name of the charcter you are using)")
        playerThreen = playername
        playername = ""
        print(f"Welcome, {playerThreen}!")
        playerThreeb = startingAmount
    elif(playernum == 4 and playerid != "play"):
        playerFour = playerid
        playerid = ""
        playername = input("Please put in a name to identify yourself(could be your name, a nickname, or the name of the charcter you are using)")
        playerFourn = playername
        playername = ""
        print(f"Welcome, {playerFourn}!")
        playerFourb = startingAmount
    elif(playernum == 5 and playerid != "play"):
        playerFive = playerid
        playerid = ""
        playername = input("Please put in a name to identify yourself(could be your name, a nickname, or the name of the charcter you are using)")
        playerFiven = playername
        playername = ""
        print(f"Welcome, {playerFiven}!")
        playerFiveb = startingAmount
    elif(playernum == 6 and playerid != "play"):
        playerSix = playerid
        playerid == ""
        playername = input("Please put in a name to identify yourself(could be your name, a nickname, or the name of the charcter you are using)")
        playerSixn = playername
        playername = ""
        print(f"Welcome, {playerSixn}!")
        playerSixb = startingAmount
    elif(playerid == "play"):
        allplayersjoined = True
    playernum = playernum + 1
print("Ok, Let's Play!")
 #---------------------MAIN LOOP---------------------------------
while (gameOver == False):
    binput = input("Please scan action on banker's card")
    if(binput == buy): #Begins the buying procees
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
            print("Barcode error, scan error barcode to try again, DO NOT SCAN PLAYER BARCODE")
        bplayerinput = input("Now scan player card to complete purchace")
        if(bplayerinput == playerOne):
            if(playerOneb >= payamount):
                playerOneb -= payamount
                playerOnep += currentproperty
                print(f"{playerOnen} has purchased {currentproperty} for ${payamount}!")
                propertiesAvalible.remove(currentproperty)
            else:
                print("You don't have enough money.")
        elif(bplayerinput == playerTwo):
            if(playerTwob >= payamount):
                playerTwob -= payamount
                playerTwop += currentproperty
                print(f"{playerTwon} has purchased {currentproperty} for ${payamount}!")
                propertiesAvalible.remove(currentproperty)
            else:
                print("You don't have enough money.")
        elif(bplayerinput == playerThree):
            if(playerThreeb >= payamount):
                playerThreeb -= payamount
                playerThreep += currentproperty
                print(f"{playerThreen} has purchased {currentproperty} for ${payamount}!")
                propertiesAvalible.remove(currentproperty)
            else:
                print("You don't have enough money.")
        elif(bplayerinput == playerFour):
            if(playerFourb >= payamount):
                playerFourb -= payamount
                playerFourp += currentproperty
                print(f"{playerFourn} has purchased {currentproperty} for ${payamount}!")
                propertiesAvalible.remove(currentproperty)
            else:
                print("You don't have enough money.")
        elif(bplayerinput == playerFive):
            if(playerFiveb >= payamount):
                playerFiveb -= payamount
                playerFivep += currentproperty
                print(f"{playerFiven} has purchased {currentproperty} for ${payamount}!")
                propertiesAvalible.remove(currentproperty)
            else:
                print("You don't have enough money.")
        elif(bplayerinput == playerSix):
            if(playerSixb >= payamount):
                playerSixb -= payamount
                playerSixp += currentproperty
                print(f"{playerSixn} has purchased {currentproperty} for ${payamount}!")
                propertiesAvalible.remove(currentproperty)
            else:
                print("You don't have enough money.")
        else:
            print("Barcode error, please try again")
        currentproperty = ""
        payamount = 0
    elif(binput == payrent): #Pay Rent
        rplayeroput = input("Scan player card of the person who is getting paid")
        rentamount = int(input("Enter rent amount"))
        payamount = rentamount
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
    elif(binput == auction):        
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
            print("Barcode error, scan error barcode to try again, DO NOT SCAN PLAYER BARCODE")
        print(f"{currentproperty} is now being auctioned off. Bidding starts at $10. Scan your player card to bid. When finished, type 'end' to end auction.")
        payamount = 10
        auctionOver = False
        enoughMoney = True
        while(auctionOver == False):
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
                auctiona = int(input("Enter amount you want to bid"))
                payamount += auctiona
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
                        enoughMoney = True 
        auctionpay = input(f"The auction is now over. {currentplayer} owes ${payamount}. {currentplayer}, please scan your player card to complete the purchace of {currentproperty}")
        if(auctionpay == playerOne):
            playerOneb -= payamount
            playerOnep += currentproperty
        elif(auctionpay == playerTwo):
            playerTwob -= payamount
            playerTwop += currentproperty
        elif(auctionpay == playerThree):
            playerThreeb -= payamount
            playerThreep += currentproperty
        elif(auctionpay == playerFour):
            playerFourb -= payamount
            playerFourp += currentproperty
        elif(auctionpay == playerFive):
            playerFiveb -= payamount
            playerFivep += currentproperty
        elif(auctionpay == playerSix):
            playerSixb -= payamount
            playerSixp += currentproperty
        print(f"{currentplayer} has purchaced {currentproperty} for ${payamount}!")
        propertiesAvalible.remove(currentproperty)
        currentproperty = ""
        currentplayer = ""
        payamount = 0
    elif(binput == incometax):
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
            vaultb += payamount
        payamount = 0
    elif(binput == luxurytax):
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
            vaultb += payamount
        payamount = 0
    elif(binput == getoutofjail):
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
        payamount = 0
    elif(binput == passgo):
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
        payamount = 0
    elif(binput == buildahouse):
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
        housepput = input("Now scan card of person paying to compleate purchace")
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
        payamount = 0
        currentproperty = ""
    elif(binput == checkbalance):
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
    elif(binput == checkvbalance):
        print(f"The vault has ${vaultb} in it")
    elif(binput == checkprops):
        propcheck = input("Scan your player card to check your properties")
        if(propcheck == playerOne):
            print(f"{playerOnen} has the following properties:\n{playerOnep}.")
        elif(propcheck == playerTwo):
            print(f"{playerTwon} has the following properties:\n{playerTwop}.")
        elif(propcheck == playerThree):
            print(f"{playerThreen} has the following properties:\n{playerThreep}.")
        elif(propcheck == playerFour):
            print(f"{playerFourn} has the following properties:\n{playerFourp}.")
        elif(propcheck == playerFive):
            print(f"{playerFiven} has the following properties:\n{playerFivep}.")
        elif(propcheck == playerSix):
            print(f"{playerSixn} has the following properties:\n{playerSixp}.")
    elif(binput == buyproperty):
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
        bfplayer = input(f"Now scan the card of the person that {currentproperty} belongs to currently.")
        cbuyamount = int(input("Enter amount to be bought for"))
        payamount = cbuyamount
        playerbput = input("Now scan the card of the player paying to complete purchace")
        if(playerbput == playerOne):
            if(playerOneb >= payamount):
                if(bfplayer == playerOne):
                    playerOneb += payamount
                    playerOnep.remove(currentproperty)
                    currentplayer = playerOnen
                elif(bfplayer == playerTwo):
                    playerTwob += payamount
                    playerTwop.remove(currentproperty)
                    currentplayer = playerTwon
                elif(bfplayer== playerThree):
                    playerThreeb += payamount
                    playerThreep.remove(currentproperty)
                    currentplayer = playerThreen
                elif(bfplayer == playerFour):
                    playerFourb += payamount
                    playerFourp.remove(currentproperty)
                    currentplayer = playerFourn
                elif(bfplayer == playerFive):
                    playerFiveb += payamount
                    playerFivep.remove(currentproperty)
                    currentplayer = playerFive
                elif(bfplayer == playerSix):
                    playerSixb += payamount
                    currentplayer = playerSixn  
                playerOneb -= payamount
                playerOnep += currentproperty
                print(f"{playerOnen} has purchaced {currentproperty} from {currentplayer} for ${payamount}!")
            else:
                print("You don't have enough money.")
        elif(playerbput == playerTwo):
            if(playerTwob >= payamount):
                if(bfplayer == playerOne):
                    playerOneb += payamount
                    playerOnep.remove(currentproperty)
                    currentplayer = playerOnen
                elif(bfplayer == playerTwo):
                    playerTwob += payamount
                    playerTwop.remove(currentproperty)
                    currentplayer = playerTwon
                elif(bfplayer == playerThree):
                    playerThreeb += payamount
                    playerThreep.remove(currentproperty)
                    currentplayer = playerThreen
                elif(bfplayer == playerFour):
                    playerFourb += payamount
                    playerFourp.remove(currentproperty)
                    currentplayer = playerFourn
                elif(bfplayer == playerFive):
                    playerFiveb += payamount
                    playerFivep.remove(currentproperty)
                    currentplayer = playerFive
                elif(bfplayer == playerSix):
                    playerSixb += payamount
                    playerSixp.remove(currentproperty)
                    currentplayer = playerSixn  
                playerTwob -= payamount
                playerTwop += currentproperty
                print(f"{playerTwon} has purchaced {currentproperty} from {currentplayer} for ${payamount}!")
            else:
                print("You don't have enough money.")
        elif(playerbput == playerThree):
            if(playerThreeb >= payamount):
                if(bfplayer == playerOne):
                    playerOneb += payamount
                    playerOnep.remove(currentproperty)
                    currentplayer = playerOnen
                elif(bfplayer == playerTwo):
                    playerTwob += payamount
                    playerTwop.remove(currentproperty)
                    currentplayer = playerTwon
                elif(bfplayer == playerThree):
                    playerThreeb += payamount
                    playerThreep.remove(currentproperty)
                    currentplayer = playerThreen
                elif(bfplayer == playerFour):
                    playerFourb += payamount
                    playerFourp.remove(currentproperty)
                    currentplayer = playerFourn
                elif(bfplayer == playerFive):
                    playerFiveb += payamount
                    playerFivep.remove(currentproperty)
                    currentplayer = playerFive
                elif(bfplayer == playerSix):
                    playerSixb += payamount
                    playerSixp.remove(currentproperty)
                    currentplayer = playerSixn  
                playerThreeb -= payamount
                playerThreep += currentproperty
                print(f"{playerThreen} has purchaced {currentproperty} from {currentplayer} for ${payamount}!")
            else:
                print("You don't have enough money.")
        elif(playerbput == playerFour):
            if(playerFourb >= payamount):
                if(bfplayer == playerOne):
                    playerOneb += payamount
                    playerOnep.remove(currentproperty)
                    currentplayer = playerOnen
                elif(bfplayer == playerTwo):
                    playerTwob += payamount
                    playerTwop.remove(currentproperty)
                    currentplayer = playerTwon
                elif(bfplayer == playerThree):
                    playerThreeb += payamount
                    playerThreep.remove(currentproperty)
                    currentplayer = playerThreen
                elif(bfplayer == playerFour):
                    playerFourp.remove(currentproperty)
                    playerFourb += payamount
                    currentplayer = playerFourn
                elif(bfplayer == playerFive):
                    playerFiveb += payamount
                    playerFivep.remove(currentproperty)
                    currentplayer = playerFive
                elif(bfplayer == playerSix):
                    playerSixb += payamount
                    playerSixp.remove(currentproperty)
                    currentplayer = playerSixn  
                playerFourb -= payamount
                playerFourp += currentproperty
                print(f"{playerFourn} has purchaced {currentproperty} from {currentplayer} for ${payamount}!")
            else:
                print("You don't have enough money.")
        elif(playerbput == playerFive):
            if(playerFiveb >= payamount):
                if(bfplayer == playerOne):
                    playerOneb += payamount
                    playerOnep.remove(currentproperty)
                    currentplayer = playerOnen
                elif(bfplayer == playerTwo):
                    playerTwob += payamount
                    playerTwop.remove(currentproperty)
                    currentplayer = playerTwon
                elif(bfplayer == playerThree):
                    playerThreeb += payamount
                    playerThreep.remove(currentproperty)
                    currentplayer = playerThreen
                elif(bfplayer == playerFour):
                    playerFourb += payamount
                    playerFourp.remove(currentproperty)
                    currentplayer = playerFourn
                elif(bfplayer == playerFive):
                    playerFiveb += payamount
                    playerFivep.remove(currentproperty)
                    currentplayer = playerFive
                elif(bfplayer == playerSix):
                    playerSixb += payamount
                    playerSixp.remove(currentproperty)
                    currentplayer = playerSixn  
                playerFiveb -= payamount
                playerFivep += currentproperty
                print(f"{playerFiven} has purchaced {currentproperty} from {currentplayer} for ${payamount}!")
            else:
                print("You don't have enough money.")
        elif(playerbput == playerSix):
            if(playerSixb >= payamount):
                if(bfplayer == playerOne):
                    playerOneb += payamount
                    playerOnep.remove(currentproperty)
                    currentplayer = playerOnen
                elif(bfplayer == playerTwo):
                    playerTwob += payamount
                    playerTwop.remove(currentproperty)
                    currentplayer = playerTwon
                elif(bfplayer == playerThree):
                    playerThreeb += payamount
                    playerThreep.remove(currentproperty)
                    currentplayer = playerThreen
                elif(bfplayer == playerFour):
                    playerFourb += payamount
                    playerFourp.remove(currentproperty)
                    currentplayer = playerFourn
                elif(bfplayer == playerFive):
                    playerFiveb += payamount
                    playerFivep.remove(currentproperty)
                    currentplayer = playerFive
                elif(bfplayer == playerSix):
                    playerSixb += payamount
                    playerSixp.remove(currentproperty)
                    currentplayer = playerSixn  
                playerSixb -= payamount
                playerSixp += currentproperty
                print(f"{playerSixn} has purchaced {currentproperty} from {currentplayer} for ${payamount}!")
            else:
                print("You don't have enough money.")
            payamount = 0
            currentproperty = ""
            currentplayer = ""
    elif(binput == banktoplayer):
        banktop = input("Scan player card of person getting paid")
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
        payamount = 0
    elif(binput == playertobank):
        ptobank = input("Scan player card of person paying")
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
        payamount = 0
    elif(binput == playertoplayer):
        ptoppaid = input("Scan player card of the person who is getting paid")
        ptopa = int(input("Enter payment amount"))
        payamount = ptopa
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
        currentplayer = ""
        payamount = 0
    elif(binput == playertovault):
        ptovault = input("Scan player card of person paying")
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
        payamount = 0
    elif(binput == banktovault):
        banktvaulta = int(input("Enter amount"))
        vaultb += banktvaulta
    elif(binput == vaultcard):
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
        payamount = 0
        vaultb = 400
    elif(binput == error):
        print("Error brcode scanned")
    elif(binput == endgame):
        gameOver = True
        break
print("The game is over! Final totals will be displayed below, please add them with property rent to find out the winner!")
print(f"{playerOnen} - ${playerOneb}")
print(f"{playerTwon} - ${playerTwob}")
print(f"{playerThreen} - ${playerThreeb}")
print(f"{playerFourn} - ${playerFourb}")
print(f"{playerFiven} - ${playerFiveb}")
print(f"{playerSixn} - ${playerSixb}")
print("Thanks for playing!")
time.sleep(300)
