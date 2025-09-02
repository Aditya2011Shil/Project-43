# Convert tuple to list
def tuple_to_list(my_tuple):
    return list(my_tuple)

# Convert list to tuple  
def list_to_tuple(my_list):
    return tuple(my_list)

# Example usage
fruits_tuple = ("apple", "banana", "cherry")
numbers_list = [1, 2, 3, 4]

# Convert tuple to list
fruits_list = tuple_to_list(fruits_tuple)
print(f"Tuple to list: {fruits_tuple} → {fruits_list}")

# Convert list to tuple
numbers_tuple = list_to_tuple(numbers_list)  
print(f"List to tuple: {numbers_list} → {numbers_tuple}")