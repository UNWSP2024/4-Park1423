##
# Code by Parker Jolly
# On 9/25/2025
# Program name: Movie Tix
##

def main():
    #Initialize our ticket variable.
    ticket_total = 0
    
    #Get input and if its not valid, enter a while loop to contine asking for input until it is.
    num_of_movies = input("Input the number of movies you want to see: ")
    while not num_of_movies.isdigit():
        num_of_movies = input("Reinput the number of movies you want to see: ")
        print("Thats not a number.")
    
    #Increase by one for range and convert to int.
    num_of_movies = int(num_of_movies) + 1
    
    #Run through this for loop once per movie
    for iteration in range(1,num_of_movies):
        #Get the name and number of tickets for each movie, doing the same thing we did earlier to check if input is a number.
        userInput = input("Enter the name of movie number " + str(iteration) + ": ")
        userInput = input("Input the number of tickets you want for this movie: ")
        while not userInput.isdigit():
            userInput = input("Reinput the number of tickets you want for this movie: ")
            print("Thats not a number.")
        #Add to total
        ticket_total += int(userInput)
        
    #Once we are ready give the user their total.
    print("You have orded", ticket_total, "tickets.")
    
if __name__ == '__main__':
    main()
