def is_palindrome(number):
    # Edge case: Negative numbers are never palindromes
    if number < 0:
        return False

    # Edge case: Single digit numbers (0-9) are always palindromes
    if number < 10:
        return True

    # Store the original number to compare later
    original_number = number
    reversed_number = 0

    # Reverse the digits of the number
    while number > 0:
        digit = number % 10              # Extract the last digit of the number
        reversed_number = reversed_number * 10 + digit  # Append the digit to the reversed number
        number = number // 10            # Remove the last digit from the number

    # Compare the original number with the reversed number
    return original_number == reversed_number

# Take input from the user
user_input = int(input("Enter an integer: "))

# Check if the input is a palindrome
if is_palindrome(user_input):
    print(f"{user_input} is a palindrome.")
else:
    print(f"{user_input} is not a palindrome.")

    """
    Explanation (Multiline Comments):

    1. The `is_palindrome` function takes an integer as input and returns whether the integer is a palindrome.

    2. First, we address edge cases:
       - If the number is negative, we return `False` immediately because negative numbers are not possible palindromes (because of the minus sign).
       - Single-digit numbers (0 to 9) are always palindromes because they remain the same when read from left to right or right to left, so we return `True` in these cases.".

    3. For multi-digit numbers:
       - We keep the original number so we can compare it with the reversed number afterwards.
       - We reverse the number by repeatedly getting the last digit with modulo (`number % 10`), and constructing the reversed number by multiplying the current reversed number by 10 and adding the gotten digit.
    - We take away the last extracted digit from the original number through integer division (`number // 10`).

    4. Finally, we reverse the reversed digits and check with the original number.
       - If they both match, we know that the number is a palindrome and therefore return `True`.
       - Else we return `False`.

    5. Some test case samples:
    - `121` returns `True` because it's a palindrome.
       - `323` returns `True` because it's a palindrome.
       - `321` returns `False` because it's not a palindrome (its reverse is `123`).
       - `-121` returns `False` because negative numbers are never palindromes.
       - `7` returns `True` because all single-digit numbers are palindromes.
    """
