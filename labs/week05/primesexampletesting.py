primes = []
candidate = int(input("Pick a high number: "))
lowchoice = int(input("Pick a low number: "))
for candidate in range(lowchoice, candidate):
    #rang elected by candidate
    #checks if prime
    isPrime = True
    for divisor in range(2, candidate):
        #checks if has remainder = prime
        #if not then isnt prime
        if (candidate % divisor == 0):
            isPrime = False
            break
    if isPrime:
        primes.append(candidate)
    #takes out all numbers in range and puts into primes
print(primes)