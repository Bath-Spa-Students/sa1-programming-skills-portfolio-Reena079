# List of names containing different strings
list_of_names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Allow the user to input a name to search
search_term = input("Enter the name you want to search for: ")

# Function to search for the specific name in the list
def search_name(list_of_names, search_term):
    if search_term in list_of_names:
       print(f"{search_term} was found in the list!")
    else:
       print(f"{search_term} was not found in the list.")

#Call  the function
search_name(list_of_names,search_term)