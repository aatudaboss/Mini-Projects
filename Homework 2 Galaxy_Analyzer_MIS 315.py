#Aatish Patel MIS 315 Summer 2022 Galaxy Analyzer
# program to analyze area of galaxies


print("Welcome to the Galaxy Analyzer!")
#Using while(true) loop - got from stackoverflow: https://stackoverflow.com/questions/3947055/whats-the-point-of-using-while-true

while (True):
    total_galaxies = int(input("How many galaxies would you like to analyze? "))
    
    # creating a list to store details of the galaxies
    galaxies = [None] * total_galaxies
    
    #defining the variables 
    x = 0
    total_planets = 0
    total_income = 0
    
    
    # LIST FOR THE GALAXIES DETAILS 
    while (x < total_galaxies):
        planets = int(input("How many planets are in the galaxy " + format(x+1) + "? "))
        
        # create a list to store planets details
        galaxies[x] = [None] * planets
        
        y = 0
        
        # read planets details assuming y=0 and its smaller than the input, while loop executes
        while (y < planets):
            income = int(input("What was the planets " + format(y+1) + "'s income last year? "))
            galaxies[x][y] = income
            
            y += 1
            total_income += income
        
        x += 1
        total_planets += planets
    
    # Finding the averages of the incomes and the number of planets. credits: also got some help from professor hours + python101 on format 
    print("Number of planets in the Galactic Quadrant:", total_planets)
    print("Number of planets per galaxy:",  round(total_planets / total_galaxies, 2))
    print("Average planet income:" , round(total_income / total_planets, 2) ,format('(trillions)'))
    print("Average galaxy income:",  round(total_income / total_galaxies, 2) ,format('(trilions)'))
    
    # find income distribution
    twentyk = 0 
    fortyk = 0
    sixtyk = 0
    eightyk = 0
    atleasteightyk = 0
    
    x = 0 
    
    # loop through the list
    for galaxy in galaxies:
        galaxy_income = 0 
        
        # add sum for each galaxy
        for income in galaxy:
            galaxy_income += income 
            
        if (galaxy_income < 20000):
            twentyk += 1 
        elif (galaxy_income >= 20000 and galaxy_income < 40000):
            fortyk += 1
        elif (galaxy_income >= 40000 and galaxy_income < 60000):
            sixtyk += 1
        elif (galaxy_income >= 60000 and galaxy_income < 80000):
            eightyk += 1
        else:
            atleasteightyk += 1
        
    #FOR DISPLAYING INCOME DISTRIBUTION OUTPUTTED
    print("")
    print(" Income distribution:")
    print("")
    print("Less than $20,000:", twentyk, "galaxy(s)")
    print("At least $20,000 but less than $40,000:", fortyk, "galaxy(s)")
    print("At least $40,000 but less than $60,000:", sixtyk, "galaxy(s)")
    print("At least $60,000 but less than $80,000:", eightyk, "galaxy(s)")
    print("At least $80,000:", atleasteightyk, "galaxy(s)")
    
    # asking if the user wants to analyze again
    user_re_analyze = input("Would you like to analyze another galaxy quadrant (yes/no)? ").lower()
    
    # figured out how to break the while loop; it was all about indenting. The loop breaks if the answer is not yes
    if (user_re_analyze != "yes"):
        break
    
print("Thank you for using the Galaxy Analyzer!")
