def lucas_sequence (n):
    l = [2, 1]

    i = 2
    while i < n:
        l.append(l[-1]+l[-2])
        i+=1
    l.append(0)
    return l[:n]

#testing
for i in [0, 1, 2, 3, 4, 5, 10, 15, 20]:
    print(f"lucas_sequence({i}) =", lucas_sequence(i))

#runtime
n = int(input("Enter number (n): "))
# print("Result =", lucas_sequence(n))
import timeit
runtime = timeit.timeit("lucas_sequence(n)", globals=globals(), number = 1000000)
print("Average runtime =", runtime/1000000, "seconds")

#memory usage
import tracemalloc
tracemalloc.start()
lucas_sequence(n)
peak_memory = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()
print("Peak memory usage =", peak_memory, "Bytes")

#steps counting
def lucasSequence_stepsCounter (a, n):
    l = [2, 1]
    steps=1

    i = 2
    steps+=1

    steps+=1
    while i < n:
        steps+=1

        l.append(l[-1]+l[-2])
        steps+=4

        i+=1
        steps+=2
    
    l.append(0)
    steps+=1

    output = l[:n]
    steps+=2

    return steps

print("Number of steps =", lucasSequence_stepsCounter(10, n))