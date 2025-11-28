def is_quadratic_residue (a, m):
    if a == 0: return True
    if m == 0: return None
    return pow(a, ((m-1)//2), m) == 1


#testing
test_cases = [(0, 2), (1, 2), (2, 3), (1, 3), (2, 5), (4, 5), (10, 13), (6, 13), (123, 101), (50, 97), (0, 5003), (1, 5003), (5002, 5003)]
for test_case in test_cases:
    print(f"is_quadratic_residue{test_case} =", is_quadratic_residue(test_case[0], test_case[1]))

#runtime
a = int(input("Enter number (a): "))
m = int(input("Enter number (m): "))
print("Result =", is_quadratic_residue(a, m))
import timeit
runtime = timeit.timeit("is_quadratic_residue(a, m)", globals=globals(), number = 1000000)
print("Average runtime =", runtime/1000000, "seconds")

#memory usage
import tracemalloc
tracemalloc.start()
is_quadratic_residue(a, m)
peak_memory = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()
print("Peak memory usage =", peak_memory, "Bytes")

#steps counting
def isQuadraticResidue_stepsCounter (a, m):
    steps = 1
    if a == 0:

        steps+=1
        return steps
    
    steps+=1
    if m == 0:

        steps+=1
        return steps
    
    output = pow(a, ((m-1)//2), m) == 1
    steps+=6

    steps+=1
    return steps
print("Number of steps =", isQuadraticResidue_stepsCounter(a, m))