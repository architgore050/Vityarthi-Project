def zeta_approx(s, terms):
    if s<1: return None

    i=1
    output=0
    while i<=terms:
        output += i**(-s)
        i+=1
    return output


#testing
for i in [(2, 1), (2, 5), (2, 100), (3, 5), (3, 50), (4, 5), (4, 100), (1.5, 10), (1.1, 50), (5, 1), (5, 10), (10, 20)]:
    print(f"zeta_approx{i} =", zeta_approx(i[0], i[1]))

#runtime
s = int(input("Enter number (s): "))
terms = int(input("Enter number (terms): "))
print("Result =", zeta_approx(s, terms))
import timeit
runtime = timeit.timeit("zeta_approx(s, terms)", globals=globals(), number = 1000000)
print("Average runtime =", runtime/1000000, "seconds")

#memory usage
import tracemalloc
tracemalloc.start()
zeta_approx(s, terms)
peak_memory = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()
print("Peak memory usage =", peak_memory, "Bytes")

#steps counting
def stepsCounter (s, terms):
    steps=1
    if s<1:

        steps+=1
        return steps

    i=1
    steps+=1

    output=0
    steps+=1

    steps+=1
    while i<=terms:
        steps+=1

        output += i**(-s)
        steps+=4

        i+=1
        steps+=2
    
    steps+=1
    return steps

print("Number of steps =", stepsCounter(s, terms))