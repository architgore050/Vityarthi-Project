def distinct_prime_factors(n):
    count = 0
    i = 2
    while i * i <= n:
        if n % i == 0:
            count += 1
            while n % i == 0:
                n //= i
        i += 1
    if n > 1:
        count += 1
    return count

#testing
for i in [1, 2, 3, 4, 5, 10, 20, 50, 100, 1234567890]:
    print(f"distinct_prime_factors({i}) =", distinct_prime_factors(i))

#runtime
n = int(input("Enter number: "))
print("Result =", distinct_prime_factors(n))
import timeit
runtime = timeit.timeit("distinct_prime_factors(n)", globals=globals(), number = 1000000)
print("Runtime =", runtime/1000000, "seconds")

#memory
import tracemalloc
tracemalloc.start()
distinct_prime_factors(n)
max_mem = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()
print("memory usage =", max_mem, "Bytes")

#steps
count = 0
steps=1

i = 2
steps+=1

steps+=2
while i * i <= n:
    steps+=1

    steps+=2
    if n % i == 0:
        steps+=1

        count += 1
        steps+=2

        steps+=2
        while n % i == 0:
            steps+=1

            n //= i
            steps+=1

    i += 1
    steps+=2

steps+=1
if n > 1:
    steps+=1

    count += 1
    steps+=2

output = count
steps+=1

print("Steps =", steps)