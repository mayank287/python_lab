def sum_of_list(numbers):

  return sum(numbers)

def multiply_list_items(numbers):

  product = 1
  for num in numbers:
    product *= num
  return product

def find_largest_number(numbers):
 
  return max(numbers)

def find_smallest_number(numbers):
 
  return min(numbers)


my_list = [2, 5, 1, 8, 3]

print("Sum:", sum_of_list(my_list))
print("Product:", multiply_list_items(my_list))
print("Largest:", find_largest_number(my_list))
print("Smallest:", find_smallest_number(my_list))
