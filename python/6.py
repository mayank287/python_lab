def sum_of_digits(num):

  sum = 0
  while num > 0:
    digit = num % 10
    sum += digit
    num //= 10
  return sum

def reverse_number(num):
  
  reverse = 0
  while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
  return reverse

def main():
  num = int(input("Enter a four-digit number: "))

  if 1000 <= num <= 9999:
    sum_digits = sum_of_digits(num)
    reversed_num = reverse_number(num)

    print("Sum of digits:", sum_digits)
    print("Reverse:", reversed_num)
  else:
    print("Invalid input. Please enter a four-digit number.")

if __name__ == "__main__":
  main()
