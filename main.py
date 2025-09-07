# Maryna Hez

amount_of_data_points = int(input("How many data points do you have? ")) #Asking to enter data points
while amount_of_data_points < 2: #At least 2 data points
    print("Must enter at least two data points.") #If less than 2, then print it
    amount_of_data_points = int(input("How many data points do you have? ")) # Asking again to check if amount is still less than 2
else: #What happens if amount of data point => 2
    year = [] #Making an empty list of years
    fertility_rates = [] #Making an empty fertility rates' list

    i = 1 #Initialize the counter for the data points
    while i <= amount_of_data_points: #Counter is between 1 and amount of data points inclusively
        year_input = int(input(f"What is the year of data point {i}? "))  # Asking a data point one by one according to condition i
        fertility_rate_input = float(input(f"What is the fertility rate of data point {i}? "))  # Asking fertility rate according to counter
        i = i+1 #Increase a counter by one

        if year_input in year: #If year is the same as it was previously
            index_of_year = year.index(year_input) #Finding the index of the same year
            fertility_rates[index_of_year] = fertility_rate_input #Changing the fertility rate in a year by index
            i = i - 1 #Decrease a counter as the same year appeared, and we don't want to count it as data point that was used
        else:
            year.append(year_input)  # Adding a year that entered a user in a list of years
            fertility_rates.append(fertility_rate_input)  # Adding a fertility rate of each year to the list with entered fertility rates


start_year = int(input("Which year would you like to start with? ")) #Asking which year they want to start with
if start_year in year: #Checking if start year is in a list
    end_year = int(input("Which year would you like to end with? ")) #Asking a user to enter the end
    if end_year in year: #Check if end year is in a list of years
        if end_year > start_year: #Check if end year is bigger than start year
            start_index_of_year = year.index(start_year) #Finding the index of start year in a list
            end_index_of_year = year.index(end_year) #Finding the index of end year in a list

            start_fertility_rate = fertility_rates[start_index_of_year] #Finding the fertility rate for the start year accordingly to index
            end_fertility_rate = fertility_rates[end_index_of_year] #Finding the fertility rate for the end year accordingly to index

            average_fertility_rate = (start_fertility_rate + end_fertility_rate)/2 #Finding the average fertility rate
            print(f"The average fertility rate of these two years is {average_fertility_rate:.2f}.") #Print the average fertility with up to 2 decimals
            if start_fertility_rate > end_fertility_rate: #If start year is bigger than end rate
                print ("There is a downward trend.") #Print a downward trend
            elif start_fertility_rate < end_fertility_rate: #If start rate is less than end rate
                print ("There is an upward trend.") #Print an upward trent
            else: #If start and end rates are equal
                print("There is a sideways trend.") #Print a  sideways trent


        else: #Otherwise
            print("End year must be after start year.") #Print output

    else: #Otherwise
        print("The end year does not exist.") #Print output

else: #Otherwise
    print("The start year does not exist.") #Print output


#Maryna Hez
#Used only the material from the lectures and tutorials
#Checked multiple times the code in auto-grader