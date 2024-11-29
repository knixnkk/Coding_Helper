def countPrimes(n: int) -> int:
    if n <= 2:
        return 0, []
        
    isPrime = [True] * n
    isPrime[0] = isPrime[1] = False
    
    for i in range(2, int(n ** 0.5) + 1):
        if isPrime[i]:
            for j in range(i * i, n, i):
                isPrime[j] = False
    
    primes = [num for num in range(n) if isPrime[num]]
    return len(primes), primes

n = int(input("Enter a number: "))
count, prime_numbers = countPrimes(n)
print(f"Count of prime numbers less than {n} : {count}")
print(f"Prime numbers: {prime_numbers}")
