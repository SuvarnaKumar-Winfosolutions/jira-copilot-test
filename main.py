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


def greet():
	"""Print a simple greeting to stdout."""
	print("Hello")



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


def print_primes_1_to_50():
	"""Print prime numbers from 1 to 50 inclusive."""
	def is_prime(n):
		if n < 2:
			return False
		if n == 2:
			return True
		if n % 2 == 0:
			return False
		i = 3
		while i * i <= n:
			if n % i == 0:
				return False
			i += 2
		return True

	primes = [str(n) for n in range(1, 51) if is_prime(n)]
	print("Prime numbers from 1 to 50:", ", ".join(primes))


def print_factors(n: int):
	"""Print factors of n."""
	factors = [str(i) for i in range(1, n + 1) if n % i == 0]
	print(f"Factors of {n}: {', '.join(factors)}")


def main():
	greet()
	print_primes_1_to_50()
	# Per PROJ1-17: print the factors of 50
	print_factors(50)


# Call the main function per ticket PROJ1-16
main()
