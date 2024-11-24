import datetime
import re

def get_days_from_today(date):
  """
  Calculate the number of days between the given date and today.

  Args:
    date (str): The date to calculate the number of days from. Must be in the format YYYY-MM-DD.

  Returns:
    int: The number of days between the given date and today.

  Raises:
    TypeError: If date is not a string.
    ValueError: If date is not in the format YYYY-MM-DD.
  """
  if not isinstance(date, str):
    raise TypeError("Date must be a string")
  if not re.match(r"^\d{4}-\d{2}-\d{2}$", date):
    raise ValueError("Date must be in the format YYYY-MM-DD")
  
  date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
  today = datetime.date.today()
  delta = date - today
  return int(delta.days)


print(get_days_from_today("2023-01-31"))