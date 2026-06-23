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
