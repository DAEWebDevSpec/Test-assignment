#dfjsodfjddsdf
def is_prime(num):

    """Check if a number is prime."""

    if num <= 1:

        return False

    for i in range(2, num):

        if num % i == 0:

            return False

    return True
 

def generate_primes(limit):

    """Generate a list of prime numbers up to a given limit."""

    primes = []

    for number in range(2, limit + 1):

        if is_prime(number):

            primes.append(number)

    return primes
 

def main():

  

    upper_limit = int(input("Enter an upper limit to generate prime numbers: "))


    prime_numbers = generate_primes(upper_limit)

    print(f"Prime numbers up to {upper_limit} are: {prime_numbers}")
 

if __name__ == "__main__":

    main()
