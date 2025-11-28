def multiplicative_persistence (n):
    if n<10:
        return 0

    digits = str(n)

    prod = 1
    for digit in digits:
        prod*=int(digit)
    
    return 1+multiplicative_persistence(prod)

#testing
for i in [1, 2, 10, 12, 123, 987, 1234, 9876, 123450, 987650]:
        print(f"multiplicative persistence({i}) =", multiplicative_persistence(i))

#runtime
n = int(input("Enter number: "))
import timeit
runtime = timeit.timeit("multiplicative_persistence(n)", globals=globals(), number = 1000000)
print("Average runtime =", runtime/1000000, "seconds")

#memory usage
import tracemalloc
tracemalloc.start()
multiplicative_persistence(n)
peak_memory = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()
print("Peak memory usage =", peak_memory, "Bytes")

#steps counting
def multiplicativePersistence_stepsCounter (n):
    steps = 1
    if n<10:

        steps+=1
        return steps

    digits = str(n)
    steps+=3*len(digits)

    prod = 1
    steps+=1

    for digit in digits:
        steps+=1

        prod*=int(digit)
        steps+=3
    
    return steps+multiplicativePersistence_stepsCounter(prod)

print("Number of steps =", multiplicativePersistence_stepsCounter(n))