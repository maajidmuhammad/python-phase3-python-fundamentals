# add functions
def add_numbers(num1, num2):
    return num1 + num2

# even
def is_even(number):
    return number % 2 == 0

# string reversing
def reverse_string(text):
    return text[::-1]

# counting vowels
def count_vowels(text):
    vowels = "aeiou"
    return sum(1 for char in text.lower() if char in vowels)

# calculate_factorial
def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n - 1)
    
# apply_decorator
def decorator_func(func):
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper

def apply_decorator(func):
    decorated_func = decorator_func(func)
    return decorated_func