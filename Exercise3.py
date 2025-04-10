# Enter user input
name=input("Enter your full name:")
hometown=input("Enter your hometown:")

#Check age with validation
while True:
    try:
        age= int(input("Enter your age:")) #Convert it to integer
        break #Exit the loop 
    except ValueError: #Check the case where the input is not the number
        print("Please enter a valid number for age")
    
#Information in a dictionary
user_info= {
    #print the name
    "name":name,
    #print the hometown
    "hometown":hometown,
    #print the age as a value
    "age":age,
}
#Print the values in a single line
print(f"Name:{user_info['name']}\nHometown:{user_info['hometown']}\nAge:{user_info['age']}")