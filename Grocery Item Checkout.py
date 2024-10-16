# I want to try and write a program that allows you to pick 3 items from a given list,
# then adds up the price of the items and tells you

    # list of steps to be carried out
        #1. create 12 different variables that will act as the items the user can choose and assign each a price
        #2. present the user with a list of available items
        #3. ask user to input items they are purchasing with 3 input questions
        #4. create variable that is the total of the prices of the items the user input
        #5. print mesage to user and total price of selected items
bread, cheese, hamburger, milk, chocolate_milk, eggs = 1.00, 2.00, 5.00, 3.00, 3.50, 0.90
beef_jerkey, ravioli, pepsi, bottled_water, gummy_worms, bacon = 4.25, 4.00, 2.50, 2.00, 1.50, 3.25
print("""Below is the list of items available for purchase, up to 3 items may be purchased at a time.
      You will be prompted to select which items you want one at a time for a total of 3 times. If, after your first item, you
      don't wish to purchase any further item please enter "nothing" in the prompt.
      
        Available items:
        bacon, beef_jerkey, bottled_water, bread
        cheese, chocolate_milk, eggs, gummy_worms
        hamburger, milk, pepsi, ravioli""")
user_item1 = input("what is your first item? Please include any underscores where they are present.")
print(user_item1)
#10/15/24 after getting stuck and looking up what i need to do, i think im too early on to complete this, will come back later in the course to finish it. 