def print_even_numbers(n):
    print("Even numbers from 1 to", n, "are:")
    for num in range(1, n + 1):
        if num % 2 != 0:
            print(num)

# Example usage
n = 20
print_even_numbers(n)
