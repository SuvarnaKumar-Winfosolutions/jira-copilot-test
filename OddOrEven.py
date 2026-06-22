def is_even(n: int) -> bool:
    """Return True if n is even, False if odd."""
    return n % 2 == 0

def main():
    # simple CLI test when run directly
    import sys
    if len(sys.argv) > 1:
        try:
            v = int(sys.argv[1])
        except ValueError:
            print("Please provide an integer")
            return
        print(f"{v} is {'even' if is_even(v) else 'odd'}")

if __name__ == '__main__':
    main()
