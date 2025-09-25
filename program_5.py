# Program #5: Bank Balance
# Write a program that asks the user to enter the amount that he or she has budgeted for a month.
# A loop should then prompt the user to enter each of his or her expenses for the 
# month and keep a running total. (Enter 0 to exit the loop)  
# When the loop finishes, the program should display the amount that the 
# user is over or under budget.

def main():
    ##
    # Code by Parker Jolly
    # On 9/25/2025
    # Program name: Bank Balence
    ##
    
    #Initilize variable.   
    total = 0.0
    
    #Get budget.
    budget = float(input("How much have you budgeted for a month? "))
    
    #Get monthly expenses or exit with 0.
    while True:
        spent = float(input("Enter how much a monthy expense costs, or enter 0 to see results: "))
        total += spent
        if spent == 0:
            break
    
    #Math
    difference = budget - total
    
    #Print results
    if difference < 0:
        print(f"You are ${abs(difference):,.2f} over budget!")
    elif difference == 0:
        print("You have exactly hit your budget.")
    else:
        print(f"Good job! You have ${difference:,.2f} of budget left!")
        
if __name__ == '__main__':
    main()
