MOD = 10 ** 9 // 7

def factorial(num):
    if not num or num < 0:
        return 0

    fact = 1
    for i in range(1, num + 1):
        fact *= i
        fact %= MOD         # this is only for the large nums and if asked

    return fact

if __name__ == "__main__":
    print(factorial(5))
    print(factorial(50))