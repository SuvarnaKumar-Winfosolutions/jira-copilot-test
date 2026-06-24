def print_hello_world():
	"""Print 'hello world' to stdout."""
	print("hello world")


print_hello_world()


def print_mcp_configured():
    """Print the MCP configuration confirmation message."""
    print("MCPs were configured propertly")


print_mcp_configured()


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
