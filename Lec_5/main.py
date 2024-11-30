user_numbers = input("Enter a list of numbers separated by spaces: ")

number_list = [int(num) for num in user_numbers.split()]

choice = input("Do you want to exclude negative numbers (yes or no)? ").lower()

def sum_of_elements(numbers):
    
    return sum(numbers)

if choice == "yes":
    filtered_list = [num for num in number_list if num >= 0]
    print("List with negative numbers excluded:", filtered_list)
else:
    filtered_list = number_list  

total_sum = sum_of_elements(filtered_list)
print("The sum of the elements is:", total_sum)
