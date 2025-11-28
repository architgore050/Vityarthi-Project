def count_divisors(n):
    divisors = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            if i * i == n:
                divisors += 1
            else:
                divisors += 2
        i += 1
    return divisors

#testing
for i in [1, 2, 3, 4, 5, 10, 20, 50, 100, 1234567890]:
    print(f"count_divisors({i}) =", count_divisors(i))

#runtime
n = int(input("Enter number: "))
print("Result =", count_divisors(n))
import timeit
runtime = timeit.timeit("count_divisors(n)", globals=globals(), number = 1000000)
print("Runtime =", runtime/1000000, "seconds")

#memory
import tracemalloc
tracemalloc.start()
count_divisors(n)
max_mem = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()
print("memory usage =", max_mem, "Bytes")

#steps
divisors = 0
steps=1

i = 1
steps+=1

steps+=2
while i * i <= n:
    steps+=1

    steps+=2
    if n % i == 0:
        steps+=1

        steps+=2
        if i * i == n:
            steps+=1

            divisors += 1
            steps+=2

        else:
            divisors += 2
            steps+=2

    i += 1
    steps+=2

output = divisors
steps+=1

print("Steps =", steps)