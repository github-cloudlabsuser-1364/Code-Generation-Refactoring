MAX = 100

def get_integer(prompt):
   while True:
      try:
         return int(input(prompt))
      except ValueError:
         print("Invalid input. Please enter a valid integer.")

def main():
   try:
      n = get_integer("Enter the number of elements (1-100): ")
      if not 1 <= n <= MAX:
         print("Invalid input. Please provide a number between 1 and 100.")
         return

      arr = [get_integer(f"Enter integer {_ + 1}/{n}: ") for _ in range(n)]
      total = sum(arr)
      print("Sum of the numbers:", total)

   except KeyboardInterrupt:
      print("\nProgram terminated by user.")

if __name__ == "__main__":
   main()
