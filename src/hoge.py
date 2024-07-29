def is_prime(n: int) -> bool:
    """
    Check if a number is prime.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False

    for divisor in range(2, int(n**0.5) + 1):
        if n % divisor == 0:
            return False

    return True
