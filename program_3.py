# Program #3: Average Rainfall
# Write a program that uses nested loops to collect data and calculate the average 
# rainfall over a period of years.  
# The program should first ask for the number of years.  
# The outer loop will iterate once for each year. 
# The inner loop will iterate twelve times, once for each month.  
# Each iteration of the inner loop will ask the user for inches of rainfall for each month.  
# After all iterations, the program should display the number of months, 
# the total inches of rainfall, and the average rainfall per month for the entire period.

def main():
##
# Code by Parker Jolly
# On 9/25/2025
# Program name: Average Rainfall
##

#Initilize variables.
total_rainfall = 0
months = 0

#Get number of years.
num_of_years = int(input("Enter the number of years: ")) + 1

#Repeat 12 months a year for num_of_years.
for current_year in range(1,num_of_years):

    for current_month in range(1,13):
        #Save text to a prompt variable because it gave me errors when I put it in the input().
        prompt = "Enter the inches of rain in year " + str(current_year) + " and month " + str(current_month) + ": "
        inches_of_rain_this_month = int(input(prompt))
        #Add to total rainfall and months.
        total_rainfall += inches_of_rain_this_month
        months += 1
#Print results.
print("There were", str(months), "months, with a total of", str(total_rainfall), "inches of rain, which means the average rainfall per month was", str(total_rainfall/months) + "inches.")

if __name__ == '__main__':
    main()
