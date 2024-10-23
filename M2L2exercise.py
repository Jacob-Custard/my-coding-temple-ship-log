#exercise 1
traffic_light = input("Is the traffic light red, green, or yellow?")
if traffic_light == "red":
    print("The light is currently red, please come to a complete stop at the intersection.")
elif traffic_light == "green":
    print("The light is currently green please proceed through the intersection.")    
else:
    print("The light is currently yellow please start slowing down and prepare to stop.")    

#exercise 2 
viewer_age = input("How old are you?")
viewer_age = int(viewer_age) #instead of this step you can do viewer_age = int(input("Enter your age"))
movie_rating = input("Is this movie rated G, PG, PG-13, or R?")
if movie_rating == "PG" and viewer_age >= 8:
    print("This movie will be perfect for you and your family.")
elif movie_rating == "PG" and not viewer_age >= 8:
    print("This movie is rated PG, you must be at least 8 years old to see this movie.")    
elif movie_rating == "PG-13" and viewer_age >= 13:
    print("This movie will be perfect for you.") 
elif movie_rating == "PG-13" and not viewer_age >= 13:
    print("This movie is rated PG-13, you must be at least 13 years old to see this movie.") 
elif movie_rating == "R" and viewer_age >= 17:
    print("Enjoy your movie!")
elif movie_rating == "R" and not viewer_age >= 17:
    print("This movie is rated R, you must be at least 17 years old to see this movie.")  
else:
    print("This is a G rated movie, fun for the whole family!!")

#exercise 3
today_temp = int(input("What is the temperature today?"))
if today_temp >= 90:
    print("It's going to be swealtering today, dress in light, cool clothes.")
elif today_temp >= 70 and today_temp < 90:
    print("The temperature should be moderate to hot today, dress in lighter clothes.")
elif today_temp >= 50 and today_temp < 70:
    print("It's going to be a very mild day, dress lightly and bring a light jacket.")
elif today_temp >= 32 and today_temp < 50:
    print("It's going to be cold today, wear heavier clothing and bring a jacket or coat.")
elif today_temp >= 0 and today_temp < 32:
    print("It's going to be below freezing today, bundle up and wear a winter coat.")
else:
    print("It's going to be below zero today, stay inside if possible, if not, wear the heaviest clothing and coat you have, and make sure to cover up as much skin as possible to avoid frostbite.")        

#exercise 4
student_grade = int(input("What grade did the student recieve on the assignment?"))
if student_grade >=90:
    print("The student recieved an A.")
elif student_grade >=80 and student_grade < 90: #dont need the "and" statement only the >= one, because of the order in which the operations are run (top-down)
    print("The student recieved a B.")
elif student_grade >=70 and student_grade < 80:
    print("The student recieved a C.") 
elif student_grade >=60 and student_grade <70:
    print("The student recieved a D. They may need help understanding the concepts or material.") 
else:
    print("The student has recieved a F. This indicates the student doesnt understand even the basic concepts of the material and may need extra help with this material.")    

#exercise 5
exercise_time = input("How many hours a day do you workout or exercise?")
exercise_time = float(exercise_time) #just a reminder you can skip this step by doing exercise_time = float(input("How many hours a day do you workout or excercie?"))
if exercise_time == 0:
    print("That's ok, we all start somewhere. Even 15-30min of exercise a day can have health benefits. Let's try and get up and move just a little bit everyday.")
elif exercise_time <= 1 and exercise_time > 0:
    print("Excellent, keep up the good work!")
elif exercise_time <=3 and exercise_time > 1: 
    print("Woah, that's alot of exercising, make sure you're eating plenty of carbs and protien to fuel your body and help it get stronger.")
else:
    print("That's a ton of exercising. Are you a professional athelete? Make sure you're resting and getting proper nutrients otherwise trainging this extreme can become dangerous and counterproductive.")

#exercie 6
sweet_level = input("Do yo like your coffee sweet or unsweet?")
milk_type = input("What kind of milk do you want in your coffee, whole, half, 2%, skim, or none?")
#i dont know much about coffee, so the recommendations are going to be made up, sorry if they're dont make much sense.
if sweet_level == "sweet" and milk_type == "whole":
    print("We recommend our white chocolate latte.")
elif sweet_level == "unsweet" and milk_type == "whole":
    print("We recommend our latte.")
elif sweet_level == "sweet" and milk_type == "half":
    print("We recommend our cinnamon machiato.")    
elif sweet_level == "unsweet" and milk_type == "half":
    print("We recommend our machiato.")
elif sweet_level == "sweet" and milk_type == "2%":
    print("We recommend our candy bar frappuchino.")
elif sweet_level == "unsweet" and milk_type == "2%":
    print("We recommend our frappuchino.") 
elif sweet_level == "sweet" and milk_type == "skim":
    print("We recommend our caramel light roast coffee.")
elif sweet_level == "sweet" and milk_type == "skim":
    print("We recommend our light roast coffee.")
elif sweet_level == "sweet" and milk_type == "none":
    print("We recommned our dark chocolate dark roast coffee.")
else:
    print("We recommend our dark roast coffee.")

#exercise 7
#didnt undertsnd how to do it so i just watched the example video to understnd. I get it now but don't want to just copy the code that was used in the exmaple so im just skipping this exercise.
