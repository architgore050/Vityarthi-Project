def is_mersenne_prime (p):
    n = 2**p - 1
    
    i=2
    is_prime=True
    while i <= n/2:
        if n%i==0:
            is_prime=False
            break
        i+=1
    
    return is_prime

#testing
for i in [2, 3, 5, 7, 11, 13, 17, 19, 23]:
    print(f"is_mersenne_prime({i}) =", is_mersenne_prime(i))

#runtime
n = int(input("Enter number: "))
print("Result =", is_mersenne_prime(n))
import timeit
runtime = timeit.timeit("is_mersenne_prime(n)", globals=globals(), number = 1000000)
print("Runtime =", runtime/1000000, "seconds")

#memory
import tracemalloc
tracemalloc.start()
is_mersenne_prime(n)
max_mem = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()
print("memory usage =", max_mem, "Bytes")

#steps counting
n = 2**n - 1
steps=3

i=2
steps+=1

is_prime=True
steps+=1

steps+=2
while i <= n/2:
    steps+=1

    steps+=2
    if n%i==0:
        steps+=1

        is_prime=False
        steps+=1

        steps+=1
        break
    
    i+=1
    steps+=1

output = is_prime
steps+=1

print("Steps =", steps)