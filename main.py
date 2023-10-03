# Алгоритм решето Эратосфена на Python

def eratosthenes(n):
    # Создаем список чисел от 2 до n
    numbers = list(range(2, n+1))
    # Создаем список простых чисел
    primes = []
    while numbers:
        # Берем первое число из списка и добавляем его в список простых чисел
        prime = numbers.pop(0)
        primes.append(prime)
        # Удаляем все числа, кратные данному простому числу
        for number in numbers[:]:
            if number % prime == 0:
                numbers.remove(number)
    return primes