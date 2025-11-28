def is_perfect_power (n):
    if n == 1: return True
    if n == 0: return False
    if n == 2: return False
    if n == 3: return False
    a = 2
    while a<=n:
        b = 2
        while True:
            if a**b == n:
                return True
            if a**b > n:
                break
            b+=1
        a+=1
    return False


#testing
for i in [1, 4, 8, 9, 16, 27, 32, 81, 2, 6, 10]:
    print(f"is_perfect_power({i}) =", is_perfect_power(i))


#runtime
n = int(input("Enter number (n): "))
print("Result =", is_perfect_power(n))
import timeit
runtime = timeit.timeit("is_perfect_power(n)", globals=globals(), number = 1000000)
print("Average runtime =", runtime/1000000, "seconds")


#memory usage
import tracemalloc
tracemalloc.start()
is_perfect_power(n)
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