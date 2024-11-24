import random

def get_numbers_ticket(min=1, max=1000, values=1):
  """
  Generate a set of unique random numbers within a given range.

  The function returns a list of unique random numbers within a given range
  [min, max], the length of the list is defined by the parameter values.

  Parameters
  ----------
  min : int
    The minimum value of the range.
  max : int
    The maximum value of the range.
  values : int
    The number of values in the list.

  Returns
  -------
  list
    A list of unique random numbers.

  Raises
  ------
  TypeError
    If any of the parameters min, max, values are not integers.
  """
  if not isinstance(min, int) and not isinstance(max, int) and not isinstance(values, int):
    raise TypeError("min, max, values must be an integer")
  if min > max:
    return []
  elif min < 1:
    return []
  elif max > min and max > 1000:
    return []
  elif values < 0:
    return []
  elif values > max:
    return []
  
  ticket  = set()
  while len(ticket) < values:
    number = random.randint(min, max)
    ticket.add(number)
  
  newTicket = list(ticket)
  newTicket.sort()
  return newTicket


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)