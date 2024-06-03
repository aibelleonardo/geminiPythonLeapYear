def is_leap_year(year):
  """
  Checks if a given year is a leap year.

  Args:
      year: The year to check (integer).

  Returns:
      True if the year is a leap year, False otherwise.
  """

  # A year is a leap year if it is divisible by 4 but not by 100,
  # or if it is divisible by 400.
  return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def main():
  """
  Prompts user for input and checks for leap year.
  """
  while True:
    try:
      year = int(input("Enter a year: "))
      if year < 0:
        print("Year cannot be negative. Please enter a positive year.")
        continue
      leap = is_leap_year(year)
      if leap:
        print(year, "is a leap year.")
      else:
        print(year, "is not a leap year.")
      break  # Exit the loop after a valid year is entered

    except ValueError:
      print("Invalid input. Please enter a number.")

if __name__ == "__main__":
  main()
