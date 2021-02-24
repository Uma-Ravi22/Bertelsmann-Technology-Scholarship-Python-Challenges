# Day 64 - Rainfall.
# Write a function, get_rainfall, that tracks rainfall in a number of cities. Users of your program will enter 
# the name of a city; if the city name is blank, then the function prints a report  before exiting. 
# If the city name isn’t blank, then the program should ask the user how much rain has fallen in that
# city (typically measured in millimeters).
# The program repeatedly asks for City name & rainfall until  user enters a blank city name, 
# the program exits—but first, it reports how much total rainfall there was in each city. Thus, if I enter
# Boston 5 
# New York 7 
# Boston 5 [Enter; blank line]
# the program should output : 
# Boston: 10 
# New York: 7 

# Function takes City name & Rainfall in mm, store in a Dictionary.
# If cityname already there, rainfall gets added with the previous value(get() method of will take care of it.)
# Display the Dict values as City : Rainfall format.

def get_rainFall():
    rainfall = dict()
    while True:
        city = input("Enter the City Name:")
        if not city:
            print("No City Name, exiting & printing the report...")
            break
        rain_mm = input("Enter the Rainfall(in Millimeters):")
        rainfall[city] = rainfall.get(city, 0) + float(rain_mm)
    
    # Print the values of rainfall dict.
    print("The Rainfall Report in Various Cities.")
    for key, val in rainfall.items():
        print("{0:10} : {1:5.2f}".format(key, val))
            
# Main
get_rainFall()