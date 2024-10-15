#exercise 1
cakeFlour = 250 #amout in grams of flour each cake requires
totalFlour = 2.5 * 1000 #converting 2.5 kilograms of total flour to grams
totalCakes = totalFlour // cakeFlour
print (totalCakes)

#exercise 2
kingdom = "Pythonland"

#exercise 3
shirt1, shirt2 = 45, 50  #asigning variables
shirtCompare = (shirt1 < shirt2) #comparison statement
print (shirtCompare)

#exercise 4 
rain = True #variable assignment
heavyRain = False #variable assignment
takeUmbrella = rain or heavyRain 
print(takeUmbrella)

#exercise 5
x = 3+5*2-8 #the order of operations would be to multiply first then solve left to right since addition and subtraction are equal in order, so it would be 3+10-8 which equals 5
print(x)

#exercise 6
totalPastries = 10 #variable assignment
totalFriends = 3 #variable assignment
pastriesPerFriend = totalPastries // totalFriends #how many pastries does each friend get if evenly divided
print(pastriesPerFriend)
pastriesLeft = totalPastries % totalFriends #how many pastries are left over after being evenly divided amoung the friends
print(pastriesLeft)

#exercise 7
kingdom += " is wonderful!" #used add and assign to add " is wonderful" to the kingdom variable
print(kingdom)

#exercise 8
knight1, knight2 = 45, 50 #variable assignment
knight1Victor = knight1 > knight2 #function determing if knight1 is stronger than knight2
print(knight1Victor)

#exercise 9
eggs = True #variable assignment
flour = False #variable assignment
makePancakes = eggs and flour #function
print(makePancakes)

#exercise 10
castleHeight = 100 #initial variable assignment
castleMoat = 50 #initial variable assignment
#we want to double the castleHeight and half castleMoat then get the new dimensons
castleHeight *= 2 #variable with new dimensons
castleMoat /= 2 #variable with new dimensons
print(castleHeight)
print(castleMoat)
castleDimensons = castleHeight * castleMoat #calculating the new dimensons of the total castle
print(castleDimensons)
