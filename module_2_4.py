print('Задание: "Всё не так уж просто"')
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print('Numbers:', numbers)
primes = []
not_primes = []
is_prime = True
for i in numbers:
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
        else:
            is_prime = True
    if i == 1:
        continue
    elif is_prime == True:
        primes.append(i)
    else:
        not_primes.append(i)
print('Primes:', primes)
print('Not Primes:', not_primes)
print('Задание выполнено')