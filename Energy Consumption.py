# Define year energy consumption data as lists
year2010 = [17760.7, 15165.4, 2143.3, 6647.5, 534.9]
year2011 = [18059.1, 15716.4, 2278.6, 6494.1, 459.0]
year2012 = [18578.0, 16136.4, 2391.0, 6641.0, 454.3]
year2013 = [18830.1, 16605.6, 2370.0, 6766.4, 350.8]
# Define the number of residents for each year
resident = [3771, 3782, 3818, 3844]

def main():
    while True:
        print("\n1) Total energy consumption of the selected year.")
        print("2) Yearly energy consumption per person")
        print("3) Display the highest energy consumption")
        print("4) Quit")
        choice = int(input("Enter Selection: "))
        if choice == 1:
            TotalEc()  # Call TotalEc function
        if choice == 2:
            AverageEc()
        if choice == 3:
            DisplayEc()
        elif choice == 4:
            print("Exiting the program.")
            break  # Exit the main loop
        else:
            print("Incorrect valid input")

def TotalEc():
    while True:
        print("\n1) The year of 2010 total energy consumptions.")
        print("2) The year of 2011 total energy consumptions.")
        print("3) The year of 2012 total energy consumptions.")
        print("4) The year of 2013 total energy consumptions.")
        print("5) Return to main menu.")  # Option to return
        Input = int(input("Enter Selection: "))

        if Input == 1:
            Total = sum(year2010)
            print(f"The total energy for year 2010 is: {Total:.1f}")
        elif Input == 2:
            Total = sum(year2011)
            print(f"The total energy for year 2011 is: {Total:.1f}")
        elif Input == 3:
            Total = sum(year2012)
            print(f"The total energy for year 2012 is: {Total:.1f}")
        elif Input == 4:
            Total = sum(year2013)
            print(f"The total energy for year 2013 is: {Total:.1f}")
        elif Input == 5:
            return  # Return to the main menu
        else:
            print("Invalid Input")

def AverageEc():
     while True:
        print("\n1) Average of energy per person for year 2010..")
        print("2) Average of energy per person for year 2011.")
        print("3) Average of energy per person for year 2012.")
        print("4) Average of energy per person for year 2013.")
        print("5) Return to main menu.")  # Option to return
        Input = int(input("Enter Selection: "))

        total = 0 

        if Input == 1:
            total = sum(year2010)/resident[0]
            print(f"The average energy per person for year 2010 is: {total:.1f}")
        elif Input == 2:
            total = sum(year2011) / resident[1]
            print(f"The average energy per person for year 2011 is: {total:.1f}")
        elif Input == 3:
            total = sum(year2012) / resident[2]
            print(f"The average energy per person for year 2012 is: {total:.1f}")
        elif Input == 4:
            total = sum(year2013) / resident[3]
            print(f"The average energy per person for year 2013 is: {total:.1f}")
        elif Input == 5:
            return  # Return to the main menu
        else:
            print("Invalid Input")
            
def DisplayEc():
    while True:
        print("\n1) Find the highest consumption for year 2010.")
        print("2) Find the highest consumption for year 2011.")
        print("3) Find the highest consumption for year 2012.")
        print("4) Find the highest consumption for year 2013.")
        print("5) Return to main menu.")  # Option to return

        Input = int(input("Enter Selection: "))

        if Input == 1:
            highest = max(year2010)
            print(f"The highest energy for year 2010 is {highest:.2f}")
        elif Input == 2:
            highest = max(year2011)
            print(f"The highest energy for year 2011 is {highest:.2f}")
        elif Input == 3:
            highest = max(year2012)
            print(f"The highest energy for year 2012 is {highest:.2f}")
        elif Input == 4:
            highest = max(year2013)
            print(f"The highest energy for year 2013 is {highest:.2f}")
        elif Input == 5:
            return  # Return to the main menu
        else:
            print("Invalid Input")

# Main program entry point
if __name__ == "__main__":
    main()
