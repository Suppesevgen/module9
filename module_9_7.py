def is_prime(func):
    def wrapper(a, b, c):
        result = func(a, b, c)
        count = 0
        for i in range(2, result + 1):
            if result % i == 0:
                count += 1
                print('Составное')
            else:
                print('Простое')
            return result
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)