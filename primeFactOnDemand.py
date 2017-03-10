def prime(n):
    """ Verify if number is prime and display its prime factors
    on demand

    Args: n - Number given to check.
    """

    if (n % 2 == 0):
        while(n > 1):
            ask = input("Do you wish the next number? (y/n) ")
            if (ask == 'y'):
                n = int(n/2)
                print(n)
            elif (ask == 'n'):
                print("Exiting program")
                break
    else:
        print("Number is not prime!")


def main():
    prime(n)

if __name__ == '__main__':
    main()
