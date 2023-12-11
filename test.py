# Function to check if a number is prime

def is_prime(num):

    """Check if a number is prime."""

    if num <= 1:

        return False

    for i in range(2, num):

        if num % i == 0:

            return False

    return True
 
# Function to generate prime numbers up to a given limit

def generate_primes(limit):

    """Generate a list of prime numbers up to a given limit."""

    primes = []

    for number in range(2, limit + 1):

        if is_prime(number):

            primes.append(number)

    return primes
 
# Main function to demonstrate the functionality

def main():

    # heres a comment

    # User input for the upper limit

    upper_limit = int(input("Enter an upper limit to generate prime numbers: "))

    # Generate and display prime numbers

    prime_numbers = generate_primes(upper_limit)

    print(f"Prime numbers up to {upper_limit} are: {prime_numbers}")
 
# Calling the main function

if __name__ == "__main__":

    main()
