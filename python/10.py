import calendar

months = ('January', 'February', 'March', 'April', 'May', 'June',
         'July', 'August', 'September', 'October', 'November', 'December')

def get_days_in_month(month_name):
 

  month_index = months.index(month_name) + 1 
  year = int(input("Enter the year: "))

 
  if month_index == 2:
    return 29 if calendar.isleap(year) else 28
  else:
    return calendar.monthrange(year, month_index)[1]

if __name__ == "__main__":
  month_name = input("Enter the month name: ").capitalize()
  if month_name in months:
    days = get_days_in_month(month_name)
    print(f"{month_name} has {days} days.")
  else:
    print("Invalid month name.")
