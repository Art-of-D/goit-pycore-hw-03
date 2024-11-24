from datetime import datetime, timedelta

DATE_FORMAT = "%Y.%m.%d"

def get_upcoming_birthdays(users):
  """
  Return a list of upcoming birthdays for the given users.

  The list will only contain birthdays that are in the next week.
  If the birthday is on a Saturday or Sunday, the congratulation date will be
  moved to the following Monday.

  Args:
    users (list): A list of dictionaries. Each dictionary should have the following keys:
      - name (str): The user's name.
      - birthday (str): The user's birthday in the format "YYYY.MM.DD".

  Returns:
    list: A list of dictionaries. Each dictionary will have the following keys:
      - name (str): The user's name.
      - congratulation_date (str): The date when the user should be wished happy birthday.

  Raises:
    TypeError: If users is not a list, or if any of the dictionaries in the list do not contain name and birthday in string format.
  """
  if not isinstance(users, list) and not isinstance(users["name"], str) and not isinstance(users["birthday"], str):
    raise TypeError("Users must be a list, and contain name and birthday in string format")
  
  today = datetime.today().date()
  delta = today + timedelta(days=7)
  
  list = []
  for user in users:
    user_date = check_date(user["birthday"], today)
    
    print(user_date, today, delta)
    if user_date > delta:
      continue

    if user_date.weekday() == 5:
      new_date = date_to_string(user_date, 1)
      list.append({"name": user["name"], "congratulation_date": new_date})
    elif user_date.weekday() == 6:
      new_date = date_to_string(user_date, 2)
      list.append({"name": user["name"], "congratulation_date": new_date})
    else:
      list.append({"name": user["name"], "congratulation_date": user_date.strftime(DATE_FORMAT)})

  return list

def get_date(date):
  """
  Convert a date string from the format "YYYY.MM.DD" to a datetime date

  Args:
    date (str): The date string in the format "YYYY.MM.DD"

  Returns:
    datetime.date: The datetime date object
  """
  date = datetime.strptime(date, DATE_FORMAT).date()
  return date


def check_date(user_date, today):
  """
  Check if user_date is in the current year. If not, move user_date to the current year.
  If user_date is in the past of the current year, move user_date to the next year.

  Args:
    user_date (str): date in "YYYY.MM.DD" format
    today (datetime.date): current date

  Returns:
    datetime.date: user_date in the current year
  """
  date_frmt = get_date(user_date)
  this_year_brithday = date_frmt.replace(year=today.year)
  if this_year_brithday < today:
     return this_year_brithday.replace(year=today.year + 1)
  else:
    return this_year_brithday

def date_to_string(date, plus_day=0, format=DATE_FORMAT):
  """
  Convert a date to a string in the specified format, optionally adding days.

  Args:
    date (datetime.date): The date to convert.
    plus_day (int, optional): The number of days to add to the date. Defaults to 0.
    format (str, optional): The format to use for the string representation of the date. Defaults to DATE_FORMAT.

  Returns:
    str: The date as a formatted string.
  """
  return (date + timedelta(days=plus_day)).strftime(format)

users = [
    {"name": "John Doe", "birthday": "1985.11.27"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
