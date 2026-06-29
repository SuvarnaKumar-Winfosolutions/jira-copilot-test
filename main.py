def print_hello_world():
	"""Print 'hello world' to stdout."""
	print("hello world")


print_hello_world()


def print_hello_suvarna():
	"""Print the greeting requested by PRJ-5."""
	print("hello suvarna kumar")


print_hello_suvarna()


from datetime import date

def print_token_based_mcp_configured():
    """Print that token-based MCPs are configured instead of browser-based login."""
    print("Token-based MCPs are configured instead of browser-based login")


# Print the token-based MCP configuration message as requested by PROJ1-27
print_token_based_mcp_configured()


def DateToday():
    """Print today's date."""
    today = date.today()
    print(today.isoformat())


# Print today's date as requested by PROJ1-28
DateToday()


def sum_two_numbers(a, b):
	"""Return the sum of two numbers.

	Args:
		a (int|float): First addend.
		b (int|float): Second addend.

	Returns:
		int|float: The sum of a and b.
	"""
	return a + b


def print_perfect_squares(start=10, end=100):
	"""Print all perfect squares between start and end (inclusive)."""
	n = 1
	# find the first square >= start
	while n * n < start:
		n += 1
	squares = []
	while n * n <= end:
		squares.append(n * n)
		n += 1
	for s in squares:
		print(s)


# print perfect squares between 10 and 100 as requested by PROJ1-20
print_perfect_squares()


def print_is_positive(value=10):
	"""Print whether `value` is a positive number or not."""
	if value > 0:
		print(f"{value} is a positive number")
	elif value < 0:
		print(f"{value} is a negative number")
	else:
		print(f"{value} is zero")


# Print whether 10 is positive as requested by PROJ1-21
print_is_positive(10)

# Print whether -10 is negative as requested by PROJ1-22
print_is_positive(-10)


def print_welcome():
	"""Print a welcome message for PROJ1-24."""
	print("welcome")


# Print welcome as requested by PROJ1-24
print_welcome()


def print_welcome_ai():
	"""Print the welcome message requested by PRJ-25."""
	print("Welcome to AI world")


# Print welcome for PROJ1-25
print_welcome_ai()


def print_25_positive():
	"""Print that 25 is a positive number as requested by PROJ1-29."""
	print("25 is a positive number")


# Print that 25 is positive as requested by PROJ1-29
print_25_positive()

# Import and call thursday function for PRJ-7
from Thursday import say_thursday

say_thursday()
