from datetime import date


def print_hello_world():
	"""Print 'hello world' to stdout."""
	print("hello world")


def print_today_date():
	"""Print today's date in ISO format (YYYY-MM-DD)."""
	today = date.today()
	print(today.isoformat())


print_hello_world()
print_today_date()


def sum_two_numbers(a, b):
	"""Return the sum of two numbers.

	Args:
		a (int|float): First addend.
		b (int|float): Second addend.

	Returns:
		int|float: The sum of a and b.
	"""
	return a + b
