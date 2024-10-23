#exercise 1
user_mood = input("Are you feeling happy, sad, or adventurous today?")
days_weather = input("Is it sunny or rainy today?")
if user_mood == "happy":
    if days_weather == "sunny":
        print("A sunny day and you're feeling happy, sounds like the perfect time for a romantic comedy!!")
    elif days_weather == "rainy":
        print("A rainy day but you're feeling good, chill inside with a nice romance movie.")
elif user_mood == "sad":
    if days_weather == "sunny":
        print("It's sunny outside but you're feeling a bit down, watch a comedy to cheer up a little.")
    elif days_weather == "rainy":
        print("Rainy and feeling down, embrace the day and watch a horror film.")                
elif user_mood == "adventurous":
    if days_weather == "sunny":
        print("A sunny day and an adventure in mind, watch an action-adventure movie!")
    else:
        print("Feeling adventurous but its raining outside, watch a high-fantasy movie and escape to fantastic realms!!")

#exercise 2
day_temp = int(input("What is today's temperature in celcius?"))
event_type = input("Is the event you're attending formal or casual?")
if day_temp < 15:
    if event_type == "formal":
        print("Wear a warm formal suit.")
    elif event_type == "casual":
        print("Wear a cozy sweater and jeans.")
elif day_temp > 15:
    if event_type == "formal":
        print("Wear a light formal suit.")
    else:
        print("Wear a t-shirt and shorts.")

#exercise 3
student_grade = input("What is your current letter grade? (A/B/C/D/F):")
sports_team = input("Are you on one of the school's sports teams? (Yes/No):")
drama_club = input("Are you a member of the shcool's drama club? (Yes/No):")
if student_grade == "A":
    if sports_team == "Yes":
        print("As a student with an A and a memeber of one of the sports teams you get a 20 percent discount.")
    else:
        print("As a student with an A you get a 10 percent discount.")
elif student_grade == "B":
    if drama_club == "Yes":
        print("As a member of the drama club with a B letter grade you get a 15 percent discount.")
    else:
        print("You do not qualify for a discount.")        
else:
    print("You do not qualify for a discount.")             

#exercise 4
user_age = int(input("How old are you?"))
print("You can drive!") if user_age >= 18 else print("Not yet!!")

#exercise 5
meal_type = input("Would you like a vegitarian or non-vegitarian option? (veg/non-veg):")
diet_type = input("Would you prefer a sugar-free or regular meal? (sugar-free/regular):")
if meal_type == "veg":
    if diet_type == "sugar-free":
        print("How about a fruit salad?")
    else:
        print("Try a veg cake.") 
elif meal_type == "non-veg":
    if diet_type == "sugar-free":
        print("Try some sugar-free ice cream.")
    else:
        print("Try a chocolate brownie.")
else:
    print("Try a chocolate brownie!")

