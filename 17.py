def is_prime_power (n):
    # finding primes under n
    p = []
    i=2
    while i<=n:
        k=2
        is_prime=True
        while k <= i/2:
            if i%k==0:
                is_prime=False
                break
            k+=1
        
        if is_prime:
            p.append(i)
        
        i+=1
    
    # finding which prime gives whole number k such that p^k=n where n is input, k is any number, p is selct prime number at the moment
    for num in p:
        k = 2
        while num**k<=n:
            if num**k==n:
                return True
            if num**k>n:
                break
            k+=1
    
    return False

# testing
for i in [0, 1, 2, 3, 4, 5, 9, 10, 25, 27, 49, 50, 100, 121, 1331, 169, 200, 1000]:
    print(f"is_prime_power({i}) =", is_prime_power(i))

#time testing
n = int(input("Enter number: "))
print("Response =", is_prime_power(n))
import timeit
runtime = timeit.timeit("is_prime_power(n)", globals=globals(), number=1000000)
print("Average runtime =", runtime/1000000)

#memory testing
import tracemalloc
tracemalloc.start()
is_prime_power(n)
peak_memory_usage = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()
print("Memory usage =", peak_memory_usage, "Bytes")

#steps
def is_prime_power_stepsCounter (n):
    steps=1
    if n ==0:
        steps+=1
        return steps
    elif n==1:
        steps+=2
        return steps
    elif n<0:
        steps+=2+1
        return steps
    elif n==int(n):
        steps+=3+2
        pass
    else:
        steps+=1+4
        return steps
    
    r = n**0.5
    steps+=1

    steps+=2
    if r!=int(r):
        steps+=1
        return steps        # prime numbers are defined as integers, so decimal numbers can not be prime

    i=2
    steps+=1

    is_prime=True
    steps+=1

    steps+=1
    while i <= r/2:
        steps+=1

        steps+=1
        if r%i==0:
            steps+=1

            is_prime=False
            steps+=1

            steps+=1
            break

        i+=1
        steps+=1
    
    return steps

print("Steps =", is_prime_power_stepsCounter(n))