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

def print_week_days():
	"""Print total days in a week and their names."""
	days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
	print(f"Total days in a week: {len(days)}")
	print("Days:", ", ".join(days))


print_week_days()


def sum_two_numbers(a, b):
	"""Return the sum of two numbers.

	Args:
		a (int|float): First addend.
		b (int|float): Second addend.

	Returns:
		int|float: The sum of a and b.
	"""
	return a + b


# Import and call the even/odd checker from OddOrEven.py per PROJ1-15
try:
    from OddOrEven import is_even

    def demonstrate_even_check():
        examples = [2, 3, 0, -1]
        for v in examples:
            print(f"{v} -> {'even' if is_even(v) else 'odd'}")

    demonstrate_even_check()
except Exception:
    # If the module isn't present, skip the demonstration to keep existing behavior
    pass
