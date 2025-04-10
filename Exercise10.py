#check if the number is odd or even
def is_even_or_odd(number):
#use if function to check an even number
    if number % 2 == 0:
        return f"The {number} is even."
    else:
#if we cannot evenly divide a number thats an odd number
        return f"The  {number} is odd."

#function to produce input and provide result
def main():
#ask the user to input a number
    num = int(input("Enter a number: ")) 
# Check if it's even or odd
    result = is_even_or_odd(num) 
     # Print the result
    print(result)  

#assign to run only the main function
if __name__ == "__main__":
    main()
