# %%
name = input("What's your name? ")
age = int(input("How old are you? "))

print("Hello", name + "!")

if age >= 18:
    print("You are an adult.")
else:
    print("You are still a minor.")

print("Next year, you will be", age + 1)

# %%
def budget_manager():
    ## This is an inline comment
    ## to check the github functionality

    ## These lines are added from Gagan Gupta's account

    # This is a comment for merging into staging branch

    name = input("What's your name?") #input name 
    balance = float(input("Enter your balance: ")) #input balance

    print("Hello", name + "!") #print name 
    print("Your initial balance is:", balance) #print initial balance

    pizza= float(input("Amount spent on pizza: "))#input amount spent on pizza
    print("Amount spent on pizza:", pizza) #print amount spent on pizza

    if pizza > balance:
        print("Insufficient Balance", balance) #print insufficient balance if pizza amount is greater than balance
        return 
        
        

    movie = float(input("Amount spent on movie: "))#input amount spent on movie
    print("Amount spent on movie:", movie) #print amount spent on movie

    if movie > ( balance - pizza):
        print("Insufficient Balance", balance) #print insufficient balance if movie amount is greater than balance after pizza
        return 

    icecream = float(input("Amount spent on ice cream: "))#input amount spent on ice cream
    print("Amount spent on ice cream:", icecream) #print amount spent on ice cream

    if icecream > ( balance - pizza - movie):
        print("Insufficient Balance", balance) #print insufficient balance if ice cream amount is greater than balance after pizza and movie
        return

    balance -= (pizza + movie + icecream) #update balance after spending on pizza, movie, and ice cream

    if  balance < 0:
        print("Insufficient Balance", balance) #print insufficient balance if balance is less than 0

    else: 
        print ("Your remaining balance is:",balance)   #print remaining balance if balance is greater than or equal to 0

budget_manager()
        



