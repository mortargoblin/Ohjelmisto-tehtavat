# Prime number tarkastaja
def main():
    print("Enter integer to check if it's a prime number")
    user_input = int(input("> "))

    if prime_num_check(user_input):
        print("Number is prime number")
    else:
        print("Number is NOT prime number")

def prime_num_check(num):
    for i in range(2, num -1):
        if num % i == 0:
            return False
        else:
            pass
    return True
    
main()