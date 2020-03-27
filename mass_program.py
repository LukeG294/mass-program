#mass program
#convert weight in lbs to mass in kilograms

#while loops, conditional statements, lists and indexes,
#local vs global variables

planetList=["Mercury", "Venus", "Earth", "Mars", "Jupiter",
         "Saturn", "Uranus", "Neptune", "Pluto"]
fgList = [3.7, 8.9, 9.8, 3.7, 24.9, 10.4, 8.9, 11.2, 0.6 ]

weight = int(input("What is the weight(lbs)? ")) #global variable

while True:
    planet = input("What planet do you want to be on? ")
    if planet not in planetList:
        print("Choose a real planet or choose a",
              "planet in the milky way")
        continue
    else:
        
        if planet == planetList[0]:
            mass1 = weight/fgList[0] #answer in slugs // local
            mass2 = round(mass1 * 14.59)  #conversion to kg
            print("The mass of your object (or person) is",
                  mass2, "kg on the planet", planetList[0],".")
        if planet == planetList[1]:
            mass1 = weight/fgList[1] #answer in slugs
            mass2 = round(mass1 * 14.59) #conversion to kg
            print("The mass of your object (or person) is",
                  mass2, "kg on the planet", planetList[1],".")
        if planet == planetList[2]:
            mass1 = weight/fgList[2] #answer in slugs
            mass2 = round(mass1 * 14.59) #conversion to kg
            print("The mass of your object (or person) is",
                  mass2, "kg on the planet", planetList[2],".")
        if planet == planetList[3]:
            mass1 = weight/fgList[3] #answer in slugs
            mass2 = round(mass1 * 14.59)  #conversion to kg
            print("The mass of your object (or person) is",
                  mass2, "kg on the planet", planetList[3],".")
        if planet == planetList[4]:
            mass1 = weight/fgList[4] #answer in slugs
            mass2 = round(mass1 * 14.59) #conversion to kg
            print("The mass of your object (or person) is",
                  mass2, "kg on the planet", planetList[4],".")
        if planet == planetList[5]:
            mass1 = weight/fgList[5] #answer in slugs
            mass2 = round(mass1 * 14.59) #conversion to kg
            print("The mass of your object (or person) is",
                  mass2, "kg on the planet", planetList[5],".")
        if planet == planetList[6]:
            mass1 = weight/fgList[6] #answer in slugs
            mass2 = round(mass1 * 14.59) #conversion to kg
            print("The mass of your object (or person) is",
                  mass2, "kg on the planet", planetList[6],".")
        if planet == planetList[7]:
            mass1 = weight/fgList[7] #answer in slugs
            mass2 = round(mass1 * 14.59) #conversion to kg
            print("The mass of your object (or person) is",
                  mass2, "kg on the planet", planetList[7],".")
        if planet == planetList[8]:
            mass1 = weight/fgList[8] #answer in slugs
            mass2 = round(mass1 * 14.59) #conversion to kg
            print("The mass of your object (or person) is",
                  mass2, "kg on the planet", planetList[8],".")
