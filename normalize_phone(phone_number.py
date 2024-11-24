import re
def normalize_phone(phone_number):
  """
  Sanitizes a given phone number for use in an SMS campaign.

  It takes a string, removes any non-digit characters, and prepends "+38".
  If the string starts with "38", it removes it first.

  Args:
    phone_number (str): The phone number to normalize.

  Returns:
    str: The normalized phone number.

  Raises:
    TypeError: If phone_number is not a string.
  """
  if not isinstance(phone_number, str):
    raise TypeError("Phone number must be a string")
  phone_number = phone_number.strip()
  phone_number = re.sub(r"\D", "", phone_number)
  sanitized_numbers = re.sub(r"^38", "", phone_number)
  return "+38" + sanitized_numbers

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
