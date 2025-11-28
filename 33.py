def collatz_length (n):
    if n < 1: return None
    curr=n
    steps = 0
    while curr != 1:
        if curr % 2 == 0:
            curr = curr / 2
        else:
            curr = 3 * curr + 1
        steps+=1
    return steps

#testing
for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 19, 29]:
    print(f"collatz_lenght({i}) =", collatz_length(i))

#runtime
n = int(input("Enter number (n): "))
print("Result =", collatz_length(n))
import timeit
runtime = timeit.timeit("collatz_length(n)", globals=globals(), number = 1000000)
print("Average runtime =", runtime/1000000, "seconds")

#memory usage
import tracemalloc
tracemalloc.start()
collatz_length(n)
peak_memory = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()
print("Peak memory usage =", peak_memory, "Bytes")

#steps counting
def collatzLength_stepsCounter (n):
    steps_counter=1
    if n < 1:

        steps_counter+=1
        return steps_counter
    
    curr=n
    steps_counter+=1

    steps = 0
    steps_counter+=1

    steps_counter+=1
    while curr != 1:
        steps_counter+=1

        steps_counter+=2
        if curr % 2 == 0:
            steps_counter+=1

            curr = curr / 2
            steps_counter+=2

        else:
            curr = 3 * curr + 1
            steps_counter+=3

        steps+=1
        steps_counter+=2

    steps_counter+=1
    return steps_counter

print("Number of steps =", collatzLength_stepsCounter(n))