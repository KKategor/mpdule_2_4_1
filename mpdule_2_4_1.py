# Lesson Цикл for. Элементы списка. Полезные функции в цикле

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 11, 12, 13, 14, 15]
primes = []
not_primes = []
n = (len(numbers))
for i in range(n):
    if numbers[i] == 1:
        continue
    is_prime = True
    for j in range(2, numbers[i]):
        if (numbers[i] % j == 0):
            is_prime = False
            break
    if is_prime:
        primes.extend([numbers[i]])
    else:
        not_primes.extend([numbers[i]])
print('numbers = ',numbers)
print('Primes = ', primes)
print('Not_primes = ', not_primes)
