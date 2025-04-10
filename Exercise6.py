#Define the correct password
valid_password="12345"

#Set the maximum number of attempts
max_num_of_attempts=5

#Start the loop and start up the number of attempts
attempts=0

#loop to keep asking for the password until it's correct or attempts are over
while attempts <max_num_of_attempts:
        #Ask the user for the password
        entered_password=input("Enter the password:")

        #Check if the  entered password is valid
        if entered_password==valid_password:
                print("Correct password! Access granted.")
                break #Exit the loop when the correct password is entered
        else:
                attempts+=1 #Increase the number of attempts 
                print(f"Incorrect password. You have {max_num_of_attempts-attempts} attempts left.")

#If the loop ends without result or the max number of attempts are over
if attempts==max_num_of_attempts:
        print("Maximum attempts reached. Authorities have been alerted")
            